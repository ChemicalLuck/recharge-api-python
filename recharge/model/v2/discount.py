from typing import Any, Literal, Optional, Union

from recharge.model.base import RechargeModel

DiscountAppliesToPurchaseItemType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource = Literal["shopify_product", "shopify_collection_id"]


class DiscountAppliesTo(RechargeModel):
    ids: Optional[list[Union[str, int]]] = None
    purchase_item_type: Optional[DiscountAppliesToPurchaseItemType] = None
    resource: Optional[DiscountAppliesToResource] = None


DiscountProductType = Literal["ALL", "ONETIME", "SUBSCRIPTION"]


class DiscountChannelSettingsValue(RechargeModel):
    can_apply: Optional[bool] = None


class DiscountChannelSettings(RechargeModel):
    api: Optional[DiscountChannelSettingsValue] = None
    checkout_page: Optional[DiscountChannelSettingsValue] = None
    customer_portal: Optional[DiscountChannelSettingsValue] = None
    merchant_portal: Optional[DiscountChannelSettingsValue] = None


DiscountValueType = Literal["percentage", "fixed_amount", "shipping"]

DiscountFirstTimeCustomerRestriction = Literal[
    "null", "customer_must_not_exist_in_recharge"
]


class DiscountUsageLimits(RechargeModel):
    one_application_per_customer: bool
    first_time_customer_restriction: Optional[Any] = None
    max_subsequent_redemptions: Optional[int] = None
    redemptions: Optional[int] = None


DiscountStatus = Literal["enabled", "disabled", "fully_disabled"]


class DiscountExternalDiscountId(RechargeModel):
    ecommerce: Optional[str] = None


class Discount(RechargeModel):
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
