import logging
import time
import json
from enum import Enum
from typing import Any, Literal, Mapping, Optional, Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from requests import Request, Response, Session
from requests.exceptions import HTTPError, RequestException, JSONDecodeError
from requests.models import PreparedRequest

from recharge.exceptions import (
    RechargeHTTPError,
    RechargeAPIError,
    RechargeRequestException,
)

RechargeVersion = Literal["2021-01", "2021-11"]

RechargeScope = Literal[
    "write_orders",
    "read_orders",
    "read_discounts",
    "write_discounts",
    "write_subscriptions",
    "read_subscriptions",
    "write_payments",
    "read_payments",
    "write_payment_methods",
    "read_payment_methods",
    "write_customers",
    "read_customers",
    "write_products",
    "read_products",
    "store_info",
    "write_batches",
    "read_batches",
    "read_accounts",
    "write_checkouts",
    "read_checkouts",
    "write_notifications",
    "read_events",
    "write_retention_strategies",
    "read_gift_purchases",
    "write_gift_purchases",
    "read_gift_purchases",
    "write_gift_purchases",
    "read_bundle_products",
    "read_credit_summary",
]

REDACTED_HEADERS = ["Cookie", "X-Recharge-Access-Token"]

class RequestMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class RechargeCustomFormatter(logging.Formatter):
    # List of standard log record attributes
    standard_attributes = {
        'name', 'msg', 'args', 'levelname', 'levelno', 'pathname', 'filename', 'module', 
        'exc_info', 'exc_text', 'stack_info', 'lineno', 'funcName', 'created', 'msecs', 
        'relativeCreated', 'thread', 'threadName', 'processName', 'process', 'message', 
        'asctime'
    }

    def format(self, record):
        # Start with the base message
        base_message = super().format(record)
        
        # Get the extra fields
        extra_fields = {key: value for key, value in record.__dict__.items() if key not in self.standard_attributes}
        
        # Combine base message with extra fields
        if extra_fields:
            extra_message = json.dumps(extra_fields, indent=4)
            return f'{base_message}\n{extra_message}'
        else:
            return base_message


class RechargeClient:
    def __init__(
        self,
        access_token: str,
        max_retries: int = 3,
        retry_delay: int = 10,
        session: Optional[Session] = None,
        logger: Optional[logging.Logger] = None,
        logging_level: int = logging.DEBUG,
    ):
        self._max_retries = max_retries
        self._retry_delay = retry_delay
        self._retries = 0
        self._logger = logger or logging.getLogger(__name__)
        if logger is None:
            self._default_logging_setup(logging_level)

        self._session = session or Session()
        self._session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Recharge-Access-Token": access_token,
            }
        )

    def _default_logging_setup(self, logging_level: int = logging.DEBUG):
        handler = logging.StreamHandler()
        formatter = RechargeCustomFormatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging_level)

    def _redact_auth(self, request: PreparedRequest) -> PreparedRequest:
        """Redacts the Authorization header from a request."""

        temp_request = request.copy()
        for header in REDACTED_HEADERS:
            if header in temp_request.headers:
                temp_request.headers[header] = "REDACTED"
        return temp_request

    def _retry(self, request: PreparedRequest) -> Response:
        """Retries a request."""
        redacted_request = self._redact_auth(request)
        if self._retries >= self._max_retries:
            self._logger.error(
                "Max retries reached",
                extra={
                    "retries": self._retries,
                    "max_retries": self._max_retries,
                    "url": redacted_request.url,
                    "body": redacted_request.body,
                    "headers": dict(redacted_request.headers),
                },
            )
            raise RechargeAPIError("Max retries reached")

        self._retries += 1
        self._logger.info(
            "Retrying",
            extra={
                "retries": self._retries,
                "max_retries": self._max_retries,
                "delay": self._retry_delay,
                "url": redacted_request.url,
                "body": redacted_request.body,
                "headers": dict(redacted_request.headers),
            },
        )
        time.sleep(self._retry_delay)
        return self._send(request)

    def _extract_error_message(self, response: Response):
        """Extracts an error message from a response."""

        try:
            error_response = response.json()
            return error_response
        except JSONDecodeError:
            self._logger.error(
                "Failed to decode JSON response", extra={"response": response.text}
            )
            return response.text

    def _send(self, request: PreparedRequest) -> Response:
        """Sends a request and handles retries and errors."""
        redacted_request = self._redact_auth(request)

        self._logger.debug(
            "Sending request",
            extra={
                "url": redacted_request.url,
                "body": redacted_request.body,
                "headers": dict(redacted_request.headers)
            },
        )
        try:
            response = self._session.send(request)

            if response.status_code == 429:
                self._logger.warning("Rate limited, retrying...")
                return self._retry(request)

            if response.status_code >= 500:
                self._logger.error(
                    "Server error, retrying...",
                    extra={
                        "response": response.text,
                        "status_code": response.status_code,
                    },
                )
                return self._retry(request)

            self._retries = 0
            response.raise_for_status()

            self._logger.debug("Request successful", extra={"response": response.text})
            return response

        except HTTPError as http_error:
            self._logger.critical(
                "HTTP error",
                extra={
                    "error": http_error.response.text,
                    "request": http_error.request,
                },
            )
            raise RechargeHTTPError(
                self._extract_error_message(http_error.response)
            ) from http_error
        except RequestException as request_error:
            self._logger.critical(
                "Request failed",
                extra={
                    "error": "An ambiguous error occured",
                    "request": request_error.request,
                },
            )
            raise RechargeRequestException("Request failed") from request_error

    def _extract_data(
        self,
        response: Response,
        key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        try:
            response_json = response.json()
        except JSONDecodeError:
            self._logger.error(
                "Failed to decode JSON response, expect missing data",
                extra={"response": response.text},
            )
            return expected()

        if key is None:
            return response_json

        data = response_json.get(key, response_json)

        if not isinstance(data, expected):
            self._logger.error(
                "Invalid data type",
                extra={
                    "expected": expected.__name__,
                    "got": type(data).__name__,
                    "response": response.text,
                },
            )
            raise ValueError(
                f"Expected data to be of type {expected.__name__}, got {type(data).__name__}"
            )

        return data

    def _request(
        self,
        method: RequestMethod,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        json: Optional[Mapping[str, Any]] = None,
    ) -> Response:
        request = Request(method.value, url, params=query, json=json)
        prepared_request = self._session.prepare_request(request)
        return self._send(prepared_request)

    def _get_next_page_url(self, response: Response) -> Optional[str]:
        version = self._session.headers.get("X-Recharge-Version")

        if version == "2021-01":
            return response.links.get("next", {}).get("url")
        
        if version == "2021-11":
            try:
                data = response.json()
                cursor = data.get("next_cursor")
                if cursor:
                    parsed_url = urlparse(response.url)
                    query_params = parse_qs(parsed_url.query)
                    query_params["cursor"] = [cursor]
                    query_params = {k: v for k, v in query_params.items() if k in ["cursor", "limit"]}
                    new_query_string = urlencode(query_params, doseq=True)
                    return urlunparse(parsed_url._replace(query=new_query_string))
            except JSONDecodeError:
                self._logger.error(
                    "Failed to decode JSON response, expect missing data",
                    extra={"response": response.text},
                )

        return None

    def set_version(self, version: RechargeVersion):
        self._session.headers.update({"X-Recharge-Version": version})
        return self

    def paginate(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None
    ) -> list:
        pages = 0
        data = []
        while True:
            pages += 1
            self._logger.debug("Fetching page", extra={"page": pages, "url": url, "query": query})
            response = self._request(RequestMethod.GET, url, query)
            if not isinstance(response, Response):
                return data
            
            try:
                response_data = response.json()
            except JSONDecodeError:
                self._logger.error(
                    "Failed to decode JSON response, expect missing data",
                    extra={
                        "response_key": response_key,
                        "response": response.text
                    },
                )
                break
            data.extend(response_data.get(response_key, []))

            new_url = self._get_next_page_url(response)
            if new_url is None:
                break
            query = None
            url = new_url

        self._logger.debug(
            "Fetched all pages",
            extra={
                "pages": pages,
                "records": len(data)
            },
        )

        return data

    def delete(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._request(RequestMethod.DELETE, url, json=body)
        return self._extract_data(response, response_key, expected)

    def get(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._request(RequestMethod.GET, url, query)
        return self._extract_data(response, response_key, expected)

    def put(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._request(RequestMethod.PUT, url, query, body)
        return self._extract_data(response, response_key, expected)

    def post(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._request(RequestMethod.POST, url, query, body)
        return self._extract_data(response, response_key, expected)
