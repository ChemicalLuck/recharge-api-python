from typing import Literal, Optional, TypedDict

DiscountProductType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource = Literal["shopify_product", "shopify_collection_id"]


class DiscountChannelSettingsValue:
    can_apply: bool


class DiscountChannelSettings(TypedDict, total=False):
    api: DiscountChannelSettingsValue
    checkout_page: DiscountChannelSettingsValue
    customer_portal: DiscountChannelSettingsValue
    merchant_portal: DiscountChannelSettingsValue


DiscountType = Literal["percentage", "fixed_amount"]

DiscountFirstTimeCustomerRestriction = Literal[
    "null", "customer_must_not_exist_in_recharge"
]

DiscountStatus = Literal["enabled", "disabled", "fully_disabled"]


class Discount(TypedDict):
    id: int
    applies_to_id: int
    applies_to_product_type: DiscountProductType
    applies_to_resource: DiscountAppliesToResource
    channel_settings: DiscountChannelSettings
    code: str
    created_at: str
    discount_type: DiscountType
    duration: str
    duration_usage_limit: int
    ends_at: Optional[str]
    first_time_customer_restriction: DiscountFirstTimeCustomerRestriction
    once_per_customer: bool
    prerequisite_subtotal_min: int
    starts_at: str
    status: DiscountStatus
    times_used: int
    updated_at: str
    usage_limit: int
    value: str
