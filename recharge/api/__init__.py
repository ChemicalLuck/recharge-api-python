from typing import Any, Mapping, Optional, Union

from recharge.client import RechargeClient, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError


class RechargeResource:
    """
    Resource from the Recharge API. This class handles
    logging, sending requests, parsing JSON, and rate
    limiting.

    Refer to the API docs to see the expected responses.
    https://developer.rechargepayments.com/
    """

    base_url = "https://api.rechargeapps.com"
    object_list_key = None
    object_dict_key = None
    recharge_version: RechargeVersion = "2021-11"

    def __init__(
        self,
        client: RechargeClient,
        scopes: list[RechargeScope] = [],
    ):
        self._client = client
        self._scopes = scopes
        self._allowed_endpoints = []

    @property
    def _url(self) -> str:
        return f"{self.base_url}/{self.object_list_key}"

    def _check_scopes(self, endpoint: str, scopes: list[RechargeScope]):
        if endpoint in self._allowed_endpoints:
            return

        if not self._scopes:
            raise RechargeAPIError("No scopes found for token.")

        missing_scopes = []

        for scope in scopes:
            if scope not in self._scopes:
                missing_scopes.append(scope)

        if missing_scopes:
            raise RechargeAPIError(
                f"Endpoint {endpoint} missing scopes: {missing_scopes}"
            )
        else:
            self._allowed_endpoints.append(endpoint)

    def _get_response_key(self, expected: type[Union[dict, list]]) -> Optional[str]:
        if expected is dict:
            return self.object_dict_key
        elif expected is list:
            return self.object_list_key
        else:
            return None

    def _http_get(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        response_key = response_key or self._get_response_key(expected)
        return self._client.get(url, query, response_key, expected)

    def _paginate(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
    ) -> list:
        self._client.set_version(self.recharge_version)
        response_key = response_key or self.object_list_key
        return self._client.paginate(url, query, response_key)

    def _http_post(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        response_key = response_key or self._get_response_key(expected)
        return self._client.post(url, body, query, response_key, expected)

    def _http_put(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        response_key = response_key or self._get_response_key(expected)
        return self._client.put(url, body, query, response_key, expected)

    def _http_delete(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        response_key = response_key or self._get_response_key(expected)
        return self._client.delete(url, body, response_key, expected)
