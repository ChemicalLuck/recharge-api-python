from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

DiscountProductType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource = Literal["shopify_product", "shopify_collection_id"]

DiscountType = Literal["percentage", "fixed_amount"]

DiscountFirstTimeCustomerRestriction = Literal[
    "null", "customer_must_not_exist_in_recharge"
]

DiscountStatus = Literal["enabled", "disabled", "fully_disabled"]


class DiscountChannelSettingsValue(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    can_apply: Optional[bool] = None


class DiscountChannelSettings(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    api: Optional[DiscountChannelSettingsValue] = None
    checkout_page: Optional[DiscountChannelSettingsValue] = None
    customer_portal: Optional[DiscountChannelSettingsValue] = None
    merchant_portal: Optional[DiscountChannelSettingsValue] = None


class Discount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    applies_to_id: Optional[int] = None
    applies_to_product_type: Optional[DiscountProductType] = None
    applies_to_resource: Optional[DiscountAppliesToResource] = None
    channel_settings: Optional[DiscountChannelSettings] = None
    code: Optional[str] = None
    created_at: Optional[str] = None
    discount_type: Optional[DiscountType] = None
    duration: Optional[str] = None
    duration_usage_limit: Optional[int] = None
    ends_at: Optional[str] = None
    first_time_customer_restriction: Optional[DiscountFirstTimeCustomerRestriction] = None
    once_per_customer: Optional[bool] = None
    prerequisite_subtotal_min: Optional[int] = None
    starts_at: Optional[str] = None
    status: Optional[DiscountStatus] = None
    times_used: Optional[int] = None
    updated_at: Optional[str] = None
    usage_limit: Optional[int] = None
    value: Optional[str] = None
