from typing import Literal, Optional, TypedDict

DiscountAppliesToPurchaseItemType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource = Literal["shopify_product", "shopify_collection_id"]


class DiscountAppliesTo(TypedDict, total=False):
    ids: list[str]
    purchase_item_type: DiscountAppliesToPurchaseItemType
    resource: DiscountAppliesToResource


DiscountProductType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]


class DiscountChannelSettingsValue:
    can_apply: bool


class DiscountChannelSettings(TypedDict, total=False):
    api: DiscountChannelSettingsValue
    checkout_page: DiscountChannelSettingsValue
    customer_portal: DiscountChannelSettingsValue
    merchant_portal: DiscountChannelSettingsValue


DiscountValueType = Literal["percentage", "fixed_amount", "shipping"]

DiscountFirstTimeCustomerRestriction = Literal[
    "null", "customer_must_not_exist_in_recharge"
]


class DiscountUsageLimits(TypedDict):
    one_application_per_customer: bool
    first_time_customer_restriction: DiscountFirstTimeCustomerRestriction
    max_subsequent_redemptions: int
    redemptions: int


DiscountStatus = Literal["enabled", "disabled", "fully_disabled"]


class DiscountExternalDiscountId(TypedDict):
    ecommerce: str


class Discount(TypedDict):
    id: int
    applies_to: DiscountAppliesTo
    channel_settings: DiscountChannelSettings
    code: str
    created_at: str
    ends_at: Optional[str]
    external_discount_id: DiscountExternalDiscountId
    discount_type: DiscountValueType
    duration: str
    duration_usage_limit: int
    once_per_customer: bool
    prerequisite_subtotal_min: int
    starts_at: str
    status: DiscountStatus
    times_used: int
    updated_at: str
    usage_limits: DiscountUsageLimits
    value: str
    value_type: DiscountValueType
