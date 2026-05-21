from typing import Optional

from recharge.model.base import RechargeModel


class Account(RechargeModel):
    id: int
    user_id: int
    created_at: str
    invited_at: Optional[str] = None
    is_owner: bool
