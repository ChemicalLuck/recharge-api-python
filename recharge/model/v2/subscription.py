from typing import Literal, Optional, TypedDict

SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]


class SubscriptionProperty(TypedDict):
    name: str
    value: str


SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class SubscriptionAnalyticsDataUtmParams(TypedDict, total=False):
    utm_campaign: str
    utm_content: str
    utm_data_source: str
    utm_source: str
    utm_medium: str
    utm_term: str
    utm_timestamp: str


class SubscriptionAnalyticsData(TypedDict):
    utm_params: list[SubscriptionAnalyticsDataUtmParams]


class SubscriptionExternalProductId(TypedDict):
    ecommerce: str


class SubscriptionExternalVariantId(TypedDict):
    ecommerce: str


class Subscription(TypedDict):
    id: int
    address_id: int
    customer_id: int
    analytics_data: SubscriptionAnalyticsData
    cancellation_reason: Optional[str]
    cancellation_reason_comment: Optional[str]
    cancelled_at: Optional[str]
    charge_interval_frequency: int
    created_at: str
    expire_after_specific_number_of_charges: Optional[int]
    external_product_id: SubscriptionExternalProductId
    external_variant_id: SubscriptionExternalVariantId
    has_queued_charges: bool
    is_prepaid: bool
    is_skippable: bool
    is_swappable: bool
    max_retries_reached: bool
    next_charge_scheduled_at: str
    order_day_of_month: Optional[int]
    order_day_of_week: Optional[int]
    order_interval_frequency: int
    order_interval_unit: SubscriptionOrderIntervalUnit
    presentment_currency: str
    price: str
    product_title: str
    properties: list[SubscriptionProperty]
    quantity: int
    sku: Optional[str]
    sku_override: bool
    status: SubscriptionStatus
    updated_at: str
    variant_title: str
