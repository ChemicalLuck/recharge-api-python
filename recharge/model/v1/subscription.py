from enum import IntEnum
from typing import Literal, TypedDict

SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]


class SubscriptionProperty(TypedDict):
    name: str
    value: str


SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class Subscription(TypedDict):
    id: int
    address_id: IntEnum
    cancellation_reason: str
    cancellation_reason_comment: str
    cancelled_at: str
    charge_interval_frequency: str
    created_at: str
    customer_id: int
    email: str
    expire_after_specific_number_of_charges: int
    has_queued_charges: int
    is_prepaid: bool
    is_skippable: bool
    is_swappable: bool
    max_retries_reached: bool
    next_charge_scheduled_at: str
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: str
    order_interval_unit: SubscriptionOrderIntervalUnit
    price: int
    product_title: str
    properties: list[SubscriptionProperty]
    quantity: int
    recharge_product_id: int
    shopify_product_id: int
    shopify_variant_id: int
    sku: str
    sku_override: bool
    status: SubscriptionStatus
    variant_title: str
