from typing import Any, Literal, Optional

from pydantic import field_validator

from recharge.model.base import RechargeModel

SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]


class SubscriptionProperty(RechargeModel):
    name: str
    value: str


SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class SubscriptionAnalyticsDataUtmParams(RechargeModel):
    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class SubscriptionAnalyticsData(RechargeModel):
    utm_params: list[SubscriptionAnalyticsDataUtmParams] = []


class SubscriptionExternalProductId(RechargeModel):
    ecommerce: str


class SubscriptionExternalVariantId(RechargeModel):
    ecommerce: str


class Subscription(RechargeModel):
    @field_validator("status", mode="before")
    @classmethod
    def uppercase_status(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.upper()
        return v

    id: int
    address_id: int
    customer_id: int
    analytics_data: Optional[SubscriptionAnalyticsData] = None
    plan_id: Optional[int] = None
    cancellation_reason: Optional[str] = None
    cancellation_reason_comment: Optional[str] = None
    cancelled_at: Optional[str] = None
    charge_interval_frequency: int
    created_at: str
    expire_after_specific_number_of_charges: Optional[int] = None
    external_product_id: Optional[SubscriptionExternalProductId] = None
    external_variant_id: Optional[SubscriptionExternalVariantId] = None
    has_queued_charges: bool
    is_prepaid: bool
    is_skippable: bool
    is_swappable: bool
    max_retries_reached: bool
    next_charge_scheduled_at: Optional[str]
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: int
    order_interval_unit: SubscriptionOrderIntervalUnit
    presentment_currency: Optional[str] = None
    price: str
    product_title: str
    properties: list[SubscriptionProperty] = []
    quantity: int
    sku: Optional[str] = None
    sku_override: bool
    status: SubscriptionStatus
    updated_at: str
    variant_title: Optional[str] = None
