from typing import Literal, Optional

from recharge.model.base import RechargeModel


class PlanChannelSettingsApi(RechargeModel):
    display: bool


class PlanChannelSettingsCustomerPortal(RechargeModel):
    display: bool


class PlanChannelSettingsMerchantPortal(RechargeModel):
    display: bool


class PlanChannelSettingsCheckoutPage(RechargeModel):
    display: bool


class PlanExternalProductId(RechargeModel):
    ecommerce: str


PlanIntervalUnit = Literal["day", "week", "month"]


class PlanSubscriptionPreferences(RechargeModel):
    apply_cutoff_date_to_checkout: Optional[bool] = None
    charge_interval_frequency: Optional[int] = None
    cutoff_day_of_month: Optional[int] = None
    cutoff_day_of_week: Optional[int] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: Optional[int] = None
    interval_unit: Optional[PlanIntervalUnit] = None


class PlanChannelSettings(RechargeModel):
    api: Optional[PlanChannelSettingsApi] = None
    customer_portal: Optional[PlanChannelSettingsCustomerPortal] = None
    merchant_portal: Optional[PlanChannelSettingsMerchantPortal] = None
    checkout_page: Optional[PlanChannelSettingsCheckoutPage] = None


PlanType = Literal["subscription", "prepaid", "onetime"]

PlanDiscountType = Literal["percentage"]


class Plan(RechargeModel):
    id: int
    channel_settings: Optional[PlanChannelSettings] = None
    created_at: Optional[str] = None
    deleted_at: Optional[str] = None
    discount_amount: Optional[str] = None
    discount_type: Optional[PlanDiscountType] = None
    external_plan_group_id: Optional[str] = None
    external_plan_id: Optional[str] = None
    external_plan_name: Optional[str] = None
    external_product_id: Optional[PlanExternalProductId] = None
    external_variant_ids: list[str] = []
    has_variant_restrictions: Optional[bool] = None
    sort_order: Optional[int] = None
    subscription_preferences: Optional[PlanSubscriptionPreferences] = None
    title: Optional[str] = None
    type: Optional[PlanType] = None
    updated_at: Optional[str] = None
