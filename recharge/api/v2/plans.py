from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.plan import (
    Plan,
    PlanChannelSettings,
    PlanDiscountType,
    PlanExternalProductId,
    PlanSubscriptionPreferences,
    PlanType,
)


class PlanCreateBodyOptional(TypedDict, total=False):
    channel_settings: PlanChannelSettings
    discount_amount: str
    discount_type: PlanDiscountType
    sort_order: int


class PlanCreateBody(PlanCreateBodyOptional):
    external_product_id: PlanExternalProductId
    subscription_preferences: PlanSubscriptionPreferences
    title: str
    type: PlanType


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
    object_key_dict = "plan"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: PlanCreateBody) -> Plan:
        """Create a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Plan(**data)

    def update(self, plan_id: int, body: PlanUpdateBody) -> Plan:
        """Update a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"PUT /{self.object_list_key}/:plan_id", required_scopes)

        url = f"{self._url}/{plan_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Plan(**data)

    def delete(self, plan_id: int) -> dict:
        """Delete a plan.
        https://developer.rechargepayments.com/2021-11/plans/plans_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"DELETE /{self.object_list_key}/:plan_id", required_scopes)

        url = f"{self._url}/{plan_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[PlanListQuery] = None) -> list[Plan]:
        """List plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Plan(**item) for item in data]

    def list_all(self, query: Optional[PlanListQuery] = None) -> list[Plan]:
        """List all plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Plan(**item) for item in data]

    def bulk_create(
        self, external_product_id: str, body: PlanBulkCreateBody
    ) -> list[Plan]:
        """Bulk create plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            "POST /products/:external_product_id/plans-bulk", required_scopes
        )

        url = f"{self.base_url}/products/{external_product_id}/plans-bulk"
        data = self._http_post(url, body, expected=list)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return [Plan(**item) for item in data]

    def bulk_update(
        self, external_product_id: str, body: PlanBulkUpdateBody
    ) -> list[Plan]:
        """Bulk update plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            "PUT /products/:external_product_id/plans-bulk", required_scopes
        )

        url = f"{self.base_url}/products/{external_product_id}/plans-bulk"
        data = self._http_put(url, body, expected=list)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return [Plan(**item) for item in data]

    def bulk_delete(self, external_product_id: str, body: PlanBulkDeleteBody) -> dict:
        """Bulk delete plans.
        https://developer.rechargepayments.com/2021-11/plans/plans_bulk_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            "DELETE /products/:external_product_id/plans-bulk", required_scopes
        )

        url = f"{self.base_url}/products/{external_product_id}/plans-bulk"
        data = self._http_delete(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data
