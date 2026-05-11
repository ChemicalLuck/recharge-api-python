import json
import logging
import time
from typing import Any, Mapping, Optional, Union

from requests.exceptions import HTTPError, JSONDecodeError, RequestException

from recharge.exceptions import RechargeAPIError, RechargeHTTPError, RechargeRequestException
from recharge.pagination import get_next_page_url
from recharge.retry import ExponentialBackoffRetry, RetryStrategy
from recharge.transport import HttpResponse, HttpTransport, RequestsTransport
from recharge.types import RechargeScope, RechargeVersion

REDACTED_HEADERS = {"X-Recharge-Access-Token", "Cookie"}


class RechargeCustomFormatter(logging.Formatter):
    _standard_attrs = {
        "name", "msg", "args", "levelname", "levelno", "pathname", "filename",
        "module", "exc_info", "exc_text", "stack_info", "lineno", "funcName",
        "created", "msecs", "relativeCreated", "thread", "threadName",
        "processName", "process", "message", "asctime", "taskName",
    }

    def format(self, record: logging.LogRecord) -> str:
        base = super().format(record)
        extra = {k: v for k, v in record.__dict__.items() if k not in self._standard_attrs}
        return f"{base}\n{json.dumps(extra, indent=4)}" if extra else base


def _create_default_logger(level: int) -> logging.Logger:
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            RechargeCustomFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


class RechargeClient:
    base_url = "https://api.rechargeapps.com"

    def __init__(
        self,
        access_token: str,
        transport: Optional[HttpTransport] = None,
        retry_strategy: Optional[RetryStrategy] = None,
        logger: Optional[logging.Logger] = None,
        logging_level: int = logging.DEBUG,
    ) -> None:
        self._base_headers: dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Recharge-Access-Token": access_token,
        }
        self._transport = transport or RequestsTransport()
        self._retry_strategy = retry_strategy or ExponentialBackoffRetry()
        self._logger = logger or _create_default_logger(logging_level)
        self._version: Optional[RechargeVersion] = None

    def set_version(self, version: RechargeVersion) -> "RechargeClient":
        self._version = version
        return self

    def _build_headers(self) -> dict[str, str]:
        headers = dict(self._base_headers)
        if self._version:
            headers["X-Recharge-Version"] = self._version
        return headers

    def _redact(self, headers: dict[str, str]) -> dict[str, str]:
        return {k: ("REDACTED" if k in REDACTED_HEADERS else v) for k, v in headers.items()}

    def _send(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]],
        json_body: Optional[Mapping[str, Any]],
    ) -> HttpResponse:
        headers = self._build_headers()
        attempt = 0

        while True:
            self._logger.debug(
                "Sending request",
                extra={"method": method, "url": url, "headers": self._redact(headers)},
            )
            try:
                response = self._transport.send(method, url, headers, params, json_body)
            except RequestException as exc:
                self._logger.critical("Transport error", extra={"error": str(exc)})
                raise RechargeRequestException("Request failed", cause=exc) from exc

            if self._retry_strategy.should_retry(attempt, response.status_code):
                delay = self._retry_strategy.delay_for(attempt)
                self._logger.warning(
                    "Retrying request",
                    extra={"attempt": attempt, "status_code": response.status_code, "delay": delay},
                )
                time.sleep(delay)
                attempt += 1
                continue

            try:
                response.raise_for_status()
            except HTTPError as exc:
                body = self._extract_body(response)
                self._logger.critical(
                    "HTTP error",
                    extra={"status_code": response.status_code, "body": body},
                )
                raise RechargeHTTPError(
                    f"HTTP {response.status_code}", status_code=response.status_code, body=body
                ) from exc

            self._logger.debug("Request successful", extra={"status_code": response.status_code})
            return response

    def _extract_body(self, response: HttpResponse) -> Any:
        try:
            return response.json()
        except Exception:
            return response.text

    def _extract_data(
        self,
        response: HttpResponse,
        key: Optional[str],
        expected: type[Union[dict, list]],
    ) -> Union[dict, list]:
        body = self._extract_body(response)
        if not isinstance(body, dict):
            self._logger.error("Non-dict response body", extra={"body": body})
            return expected()
        data = body if key is None else body.get(key, body)
        if not isinstance(data, expected):
            self._logger.error(
                "Unexpected data type",
                extra={"expected": expected.__name__, "got": type(data).__name__},
            )
            raise RechargeAPIError(f"Expected {expected.__name__}, got {type(data).__name__}")
        return data

    # ── Public HTTP methods ────────────────────────────────────────────────

    def get(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._send("GET", url, params=query, json_body=None)
        return self._extract_data(response, response_key, expected)

    def post(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._send("POST", url, params=query, json_body=body)
        return self._extract_data(response, response_key, expected)

    def put(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._send("PUT", url, params=query, json_body=body)
        return self._extract_data(response, response_key, expected)

    def delete(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
        expected: type[Union[dict, list]] = dict,
    ) -> Union[dict, list]:
        response = self._send("DELETE", url, params=None, json_body=body)
        return self._extract_data(response, response_key, expected)

    def paginate(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
    ) -> list:
        data: list = []
        page = 0
        current_url: Optional[str] = url
        current_query = query

        while current_url:
            page += 1
            self._logger.debug("Fetching page", extra={"page": page, "url": current_url})
            response = self._send("GET", current_url, params=current_query, json_body=None)
            try:
                body = response.json()
                data.extend(body.get(response_key, []) if response_key else [])
            except Exception:
                self._logger.error("Failed to decode page response")
                break
            current_url = get_next_page_url(response, self._version or "2021-11") or None
            current_query = None

        self._logger.debug("Pagination complete", extra={"pages": page, "records": len(data)})
        return data
