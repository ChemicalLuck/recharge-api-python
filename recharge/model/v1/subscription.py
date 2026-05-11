from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]

SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class SubscriptionProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class Subscription(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    address_id: Optional[int] = None
    cancellation_reason: Optional[str] = None
    cancellation_reason_comment: Optional[str] = None
    cancelled_at: Optional[str] = None
    charge_interval_frequency: Optional[str] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    email: Optional[str] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    has_queued_charges: Optional[int] = None
    is_prepaid: Optional[bool] = None
    is_skippable: Optional[bool] = None
    is_swappable: Optional[bool] = None
    max_retries_reached: Optional[bool] = None
    next_charge_scheduled_at: Optional[str] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: Optional[str] = None
    order_interval_unit: Optional[SubscriptionOrderIntervalUnit] = None
    price: Optional[int] = None
    product_title: Optional[str] = None
    properties: list[SubscriptionProperty] = []
    quantity: Optional[int] = None
    recharge_product_id: Optional[int] = None
    shopify_product_id: Optional[int] = None
    shopify_variant_id: Optional[int] = None
    sku: Optional[str] = None
    sku_override: Optional[bool] = None
    status: Optional[SubscriptionStatus] = None
    variant_title: Optional[str] = None
