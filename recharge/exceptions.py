from typing import Any


class RechargeAPIError(Exception):
    """Raised for logical API errors (bad scopes, max retries, unexpected response shape)."""


class RechargeHTTPError(Exception):
    """Raised when the API returns a non-2xx status code after all retries."""

    def __init__(self, message: str, status_code: int, body: Any) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.body = body


class RechargeRequestException(Exception):
    """Raised when the HTTP transport fails at the network level."""

    def __init__(self, message: str, cause: Exception) -> None:
        super().__init__(message)
        self.cause = cause
