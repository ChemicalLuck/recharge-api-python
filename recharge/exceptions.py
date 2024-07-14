from requests.exceptions import HTTPError, RequestException


class RechargeRequestException(RequestException):
    """Recharge request exception."""

    pass


class RechargeHTTPError(HTTPError):
    """Recharge HTTP error."""

    pass


class RechargeAPIError(Exception):
    """Recharge API error."""

    pass
