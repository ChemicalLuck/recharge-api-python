from typing import Optional

from pydantic import BaseModel, ConfigDict

from recharge.types import RechargeScope


class TokenClient(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: Optional[str] = None
    email: Optional[str] = None


class TokenInformation(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    client: Optional[TokenClient] = None
    contact_email: Optional[str] = None
    name: Optional[str] = None
    scopes: list[RechargeScope] = []
