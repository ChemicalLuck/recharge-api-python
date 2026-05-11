from pydantic import BaseModel, ConfigDict

from recharge.types import RechargeScope


class TokenClient(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    contact_email: str


class TokenInformation(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    client: TokenClient
    contact_email: str
    name: str
    scopes: list[RechargeScope]
