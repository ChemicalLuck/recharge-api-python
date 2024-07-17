from typing import TypedDict

from recharge.api import RechargeScope


class TokenClient(TypedDict):
    name: str
    email: str


class TokenInformation(TypedDict):
    client: TokenClient
    contact_email: str
    name: str
    scopes: list[RechargeScope]
