from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict


class PlanChannelSettingsApi(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display: bool


class PlanChannelSettingsCustomerPortal(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display: bool


class PlanChannelSettingsMerchantPortal(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display: bool


class PlanChannelSettingsCheckoutPage(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    display: bool


class PlanExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


PlanIntervalUnit = Literal["day", "week", "month"]


class PlanSubscriptionPreferences(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    apply_cutoff_date_to_checkout: Optional[bool] = None
    charge_interval_frequency: int
    cutoff_day_of_month: Optional[int] = None
    cutoff_day_of_week: Optional[int] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: int
    interval_unit: PlanIntervalUnit


class PlanChannelSettings(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    api: Optional[PlanChannelSettingsApi] = None
    customer_portal: Optional[PlanChannelSettingsCustomerPortal] = None
    merchant_portal: Optional[PlanChannelSettingsMerchantPortal] = None
    checkout_page: Optional[PlanChannelSettingsCheckoutPage] = None


PlanType = Literal["subscription", "prepaid", "onetime"]

PlanDiscountType = Literal["percentage"]


class Plan(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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
