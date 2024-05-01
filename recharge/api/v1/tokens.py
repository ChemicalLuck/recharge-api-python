from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope


class TokenClient(TypedDict):
    name: str
    email: str


class TokenInformation(TypedDict):
    client: TokenClient
    contact_email: str
    name: str
    scopes: list[RechargeScope]


class TokenResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/token_information/token_information_object
    """

    object_list_key = "token_information"

    def get(self) -> TokenInformation:
        """Get token information.
        https://developer.rechargepayments.com/2021-01/token_information/token_information_retrieve
        """
        return self._http_get(f"{self.url}")
