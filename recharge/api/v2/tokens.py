from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


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
    https://developer.rechargepayments.com/2021-11/token_information/token_information_object
    """

    object_list_key = "token_information"
    recharge_version: RechargeVersion = "2021-11"

    def get(self) -> TokenInformation:
        """Get token information.
        https://developer.rechargepayments.com/2021-11/token_information/token_information_retrieve
        """
        data = self._http_get(self.url)
        return TokenInformation(**data)
