from recharge.model.base import RechargeModel


class TokenClient(RechargeModel):
    name: str
    contact_email: str


class TokenInformation(RechargeModel):
    client: TokenClient
    contact_email: str
    name: str
    scopes: list[str]
