from typing import Any, Mapping, Optional, Protocol, runtime_checkable

from requests import Request, Session
from requests.exceptions import RequestException


@runtime_checkable
class HttpResponse(Protocol):
    @property
    def status_code(self) -> int: ...
    @property
    def text(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def links(self) -> dict: ...
    def json(self) -> Any: ...
    def raise_for_status(self) -> None: ...


@runtime_checkable
class HttpTransport(Protocol):
    def send(
        self,
        method: str,
        url: str,
        headers: dict[str, str],
        params: Optional[Mapping[str, Any]],
        json: Optional[Mapping[str, Any]],
    ) -> HttpResponse: ...


class RequestsTransport:
    def __init__(self, session: Optional[Session] = None) -> None:
        self._session = session or Session()

    def send(
        self,
        method: str,
        url: str,
        headers: dict[str, str],
        params: Optional[Mapping[str, Any]],
        json: Optional[Mapping[str, Any]],
    ) -> HttpResponse:
        request = Request(method, url, headers=headers, params=params, json=json)
        prepared = self._session.prepare_request(request)
        try:
            return self._session.send(prepared)
        except RequestException as exc:
            raise exc
