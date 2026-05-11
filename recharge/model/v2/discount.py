from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

DiscountAppliesToPurchaseItemType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource = Literal["shopify_product", "shopify_collection_id"]


class DiscountAppliesTo(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ids: Optional[list[str]] = None
    purchase_item_type: Optional[DiscountAppliesToPurchaseItemType] = None
    resource: Optional[DiscountAppliesToResource] = None


DiscountProductType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]


class DiscountChannelSettingsValue(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_apply: bool


class DiscountChannelSettings(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    api: Optional[DiscountChannelSettingsValue] = None
    checkout_page: Optional[DiscountChannelSettingsValue] = None
    customer_portal: Optional[DiscountChannelSettingsValue] = None
    merchant_portal: Optional[DiscountChannelSettingsValue] = None


DiscountValueType = Literal["percentage", "fixed_amount", "shipping"]

DiscountFirstTimeCustomerRestriction = Literal[
    "null", "customer_must_not_exist_in_recharge"
]


class DiscountUsageLimits(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    one_application_per_customer: bool
    first_time_customer_restriction: DiscountFirstTimeCustomerRestriction
    max_subsequent_redemptions: int
    redemptions: int


DiscountStatus = Literal["enabled", "disabled", "fully_disabled"]


class DiscountExternalDiscountId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class Discount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    applies_to: Optional[DiscountAppliesTo] = None
    channel_settings: Optional[DiscountChannelSettings] = None
    code: str
    created_at: str
    ends_at: Optional[str] = None
    external_discount_id: Optional[DiscountExternalDiscountId] = None
    discount_type: Optional[DiscountValueType] = None
    duration: Optional[str] = None
    duration_usage_limit: Optional[int] = None
    once_per_customer: Optional[bool] = None
    prerequisite_subtotal_min: Optional[int] = None
    starts_at: Optional[str] = None
    status: DiscountStatus
    times_used: Optional[int] = None
    updated_at: str
    usage_limits: Optional[DiscountUsageLimits] = None
    value: Optional[str] = None
    value_type: Optional[DiscountValueType] = None
