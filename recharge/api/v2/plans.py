from typing import Literal, Required, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class PlanChannelSettingsApi(TypedDict):
    display: bool


class PlanChannelSettingsCustomerPortal(TypedDict):
    display: bool


class PlanChannelSettingsMerchantPortal(TypedDict):
    display: bool


class PlanChannelSettingsCheckoutPage(TypedDict):
    display: bool


PlanDiscountType: TypeAlias = Literal["percentage", "fixed_amount"]


class PlanExternalProductId(TypedDict):
    ecommerce: str


PlanIntervalUnit: TypeAlias = Literal["day", "week", "month"]


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


PlanType: TypeAlias = Literal["subscription", "prepaid", "onetime"]


class PlanCreateBody(TypedDict, total=False):
    channel_settings: PlanChannelSettings
    discount_amount: str
    discount_type: PlanDiscountType
    external_product_id: Required[PlanExternalProductId]
    sort_order: int
    subscription_preferences: Required[PlanSubscriptionPreferences]
    title: Required[str]
    type: Required[PlanType]


class PlanUpdateBody(TypedDict, total=False):
    channel_settings: PlanChannelSettings
    discount_amount: str
    discount_type: PlanDiscountType
    external_product_id: PlanExternalProductId
    sort_order: int
    subscription_preferences: PlanSubscriptionPreferences
    title: str


class PlanListQuery(TypedDict, total=False):
    limit: str
    page: str
    external_product_id: str
    ids: str
    updated_at_min: str
    updated_at_max: str
    type: PlanType


class PlanBulkCreateBody(TypedDict):
    plans: list[PlanCreateBody]


class PlanBulkUpdateBody(TypedDict):
    plans: list[PlanUpdateBody]


class PlanDeleteBody(TypedDict):
    id: str


class PlanBulkDeleteBody(TypedDict):
    plan_ids: list[PlanDeleteBody]


class PlanResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/plans
    """

    object_list_key = "plans"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: PlanCreateBody):
        """Create a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def update(self, plan_id: int, body: PlanUpdateBody):
        """Update a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"PUT /{self.object_list_key}/:plan_id", required_scopes)

        return self._http_put(f"{self.url}/{plan_id}", body)

    def delete(self, plan_id: int):
        """Delete a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"DELETE /{self.object_list_key}/:plan_id", required_scopes)

        return self._http_delete(f"{self.url}/{plan_id}")

    def list(self, query: PlanListQuery | None = None):
        """List plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def bulk_create(self, external_product_id: str, body: PlanBulkCreateBody):
        """Bulk create plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            "POST /products/:external_product_id/plans-bulk", required_scopes
        )

        return self._http_post(
            f"{self.base_url}/products/{external_product_id}/plans-bulk", body
        )

    def bulk_update(self, external_product_id: str, body: PlanBulkUpdateBody):
        """Bulk update plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            "PUT /products/:external_product_id/plans-bulk", required_scopes
        )

        return self._http_put(
            f"{self.base_url}/products/{external_product_id}/plans-bulk", body
        )

    def bulk_delete(self, external_product_id: str, body: PlanBulkDeleteBody):
        """Bulk delete plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            "DELETE /products/:external_product_id/plans-bulk", required_scopes
        )

        return self._http_delete(
            f"{self.base_url}/products/{external_product_id}/plans-bulk", body
        )
