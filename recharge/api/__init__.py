from typing import Any, Mapping, Optional, Union

from recharge.client import RechargeClient
from recharge.exceptions import RechargeAPIError
from recharge.types import RechargeScope, RechargeVersion

# Re-exported so resource files can continue `from recharge.api import RechargeScope, RechargeVersion`
__all__ = ["RechargeResource", "RechargeScope", "RechargeVersion"]


class RechargeResource:
    """
    Base class for all Recharge API resources.

    Subclasses must define:
      - object_list_key: str   (used in URLs and as list response key)
      - object_dict_key: str   (used as single-item response key)
    """

    base_url = "https://api.rechargeapps.com"
    object_list_key: str
    object_dict_key: str
    recharge_version: RechargeVersion = "2021-11"
    _abstract = False

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "_abstract", False):
            if not getattr(cls, "object_list_key", None):
                raise TypeError(f"{cls.__name__} must define a non-empty object_list_key")
            if not getattr(cls, "object_dict_key", None):
                raise TypeError(f"{cls.__name__} must define a non-empty object_dict_key")

    def __init__(
        self,
        client: RechargeClient,
        scopes: list[RechargeScope] = [],
    ) -> None:
        self._client = client
        self._scopes = scopes
        self._allowed_endpoints: set[str] = set()

    @property
    def _url(self) -> str:
        return f"{self.base_url}/{self.object_list_key}"

    def _check_scopes(self, endpoint: str, required: list[RechargeScope]) -> None:
        if endpoint in self._allowed_endpoints:
            return
        if not self._scopes:
            raise RechargeAPIError("No scopes found for token.")
        missing = [s for s in required if s not in self._scopes]
        if missing:
            raise RechargeAPIError(
                f"Endpoint '{endpoint}' requires scopes {missing}. "
                f"Token has: {self._scopes}"
            )
        self._allowed_endpoints.add(endpoint)

    def _get_response_key(self, expected: type[Union[dict, list]]) -> Optional[str]:
        if expected is dict:
            return self.object_dict_key
        if expected is list:
            return self.object_list_key
        return None

    def _http_get(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        key = response_key if response_key is not None else self._get_response_key(expected)
        return self._client.get(url, query, key, expected)

    def _paginate(
        self,
        url: str,
        query: Optional[Mapping[str, Any]] = None,
        response_key: Optional[str] = None,
    ) -> list:
        self._client.set_version(self.recharge_version)
        key = response_key if response_key is not None else self.object_list_key
        return self._client.paginate(url, query, key)

    def _http_post(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        key = response_key if response_key is not None else self._get_response_key(expected)
        return self._client.post(url, body, query, key, expected)

    def _http_put(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        query: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        key = response_key if response_key is not None else self._get_response_key(expected)
        return self._client.put(url, body, query, key, expected)

    def _http_delete(
        self,
        url: str,
        body: Optional[Mapping[str, Any]] = None,
        expected: type[Union[dict, list]] = dict,
        response_key: Optional[str] = None,
    ) -> Union[dict, list]:
        self._client.set_version(self.recharge_version)
        key = response_key if response_key is not None else self._get_response_key(expected)
        return self._client.delete(url, body, key, expected)
