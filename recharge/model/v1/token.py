from typing import Optional

from recharge.model.base import RechargeModel


class TokenClient(RechargeModel):
    name: Optional[str] = None
    email: Optional[str] = None


class TokenInformation(RechargeModel):
    client: Optional[TokenClient] = None
    contact_email: Optional[str] = None
    name: Optional[str] = None
    scopes: list[str] = []
