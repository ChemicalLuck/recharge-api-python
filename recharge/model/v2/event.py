from typing import Any, Optional

from recharge.model.base import RechargeModel


class EventSource(RechargeModel):
    account_id: Optional[Any] = None
    api_token_id: Optional[Any] = None
    api_token_name: Optional[str] = None
    account_email: Optional[str] = None
    origin: Optional[str] = None
    user_type: Optional[str] = None


class Event(RechargeModel):
    id: int
    object_id: int
    customer_id: int
    created_at: str
    object_type: str
    verb: str
    description: str
    updated_attributes: Any = None
    source: Optional[EventSource] = None
    custom_attributes: Any = None
