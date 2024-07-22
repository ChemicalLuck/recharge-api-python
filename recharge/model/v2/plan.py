from typing import Literal, TypedDict


class PlanChannelSettingsApi(TypedDict):
    display: bool


class PlanChannelSettingsCustomerPortal(TypedDict):
    display: bool


class PlanChannelSettingsMerchantPortal(TypedDict):
    display: bool


class PlanChannelSettingsCheckoutPage(TypedDict):
    display: bool


class PlanExternalProductId(TypedDict):
    ecommerce: str


PlanIntervalUnit = Literal["day", "week", "month"]


class PlanSubscriptionPreferences(TypedDict):
    apply_cutoff_date_to_checkout: bool
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    expire_after_specific_number_of_charges: int
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: int
    interval_unit: PlanIntervalUnit


class PlanChannelSettings(TypedDict, total=False):
    api: PlanChannelSettingsApi
    customer_portal: PlanChannelSettingsCustomerPortal
    merchant_portal: PlanChannelSettingsMerchantPortal
    checkout_page: PlanChannelSettingsCheckoutPage


PlanType = Literal["subscription", "prepaid", "onetime"]

PlanDiscountType = Literal["percentage"]


class Plan(TypedDict):
    id: int
    channel_settings: PlanChannelSettings
    created_at: str
    deleted_at: str
    discount_amount: str
    discount_type: PlanDiscountType
    external_plan_group_id: str
    external_plan_id: str
    external_plan_name: str
    external_product_id: PlanExternalProductId
    external_variant_ids: list[str]
    has_variant_restrictions: bool
    sort_order: int
    subscription_preferences: PlanSubscriptionPreferences
    title: str
    updated_at: str


Plan.__annotations__["type"] = PlanType
