from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.subscription import (
    Subscription,
    SubscriptionOrderIntervalUnit,
    SubscriptionProperty,
    SubscriptionStatus,
)


class SubscriptionCreateBodyOptional(TypedDict, total=False):
    customer_id: str
    expire_after_specific_number_of_charges: str
    order_day_of_month: str
    order_day_of_week: str
    price: str
    properties: list[SubscriptionProperty]
    product_title: str
    status: SubscriptionStatus


class SubscriptionCreateBody(SubscriptionCreateBodyOptional):
    address_id: int
    charge_interval_frequency: int
    next_charge_scheduled_at: str
    order_interval_frequency: str
    order_interval_unit: SubscriptionOrderIntervalUnit
    quantity: str
    shopify_product_id: str
    shopify_variant_id: str


class SubscriptionUpdateBody(TypedDict, total=False):
    charge_interval_frequency: str
    commit_update: bool
    expire_after_specific_number_of_charges: str
    order_day_of_month: str
    order_day_of_week: str
    order_interval_frequency: str
    order_interval_unit: SubscriptionOrderIntervalUnit
    override: str
    price: str
    product_title: str
    properties: list[SubscriptionProperty]
    quantity: str
    shopify_variant_id: str
    sku: str
    sku_override: str
    use_shopify_variant_defaults: bool
    variant_title: str


class SubscriptionDeleteBody(TypedDict):
    send_email: bool


class SubscriptionListQuery(TypedDict, total=False):
    address_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    ids: str
    include_onetimes: str
    limit: str
    page: str
    shopify_customer_id: str
    shopify_variant_id: str
    status: SubscriptionStatus
    updated_at_max: str
    updated_at_min: str


class SubscriptionCountQuery(TypedDict, total=False):
    address_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    shopify_customer_id: str
    shopify_variant_id: str
    status: SubscriptionStatus
    updated_at_max: str
    updated_at_min: str


class SubscriptionChangeDateBody(TypedDict, total=True):
    date: str


class SubscriptionChangeAddressBodyOptional(TypedDict, total=False):
    next_charge_scheduled_at: str


class SubscriptionChangeAddressBody(SubscriptionChangeAddressBodyOptional):
    address_id: str


class SubscriptionCancelBodyOptional(TypedDict, total=False):
    cancellation_reason_comments: str
    send_email: bool


class SubscriptionCancelBody(SubscriptionCancelBodyOptional):
    cancellation_reason: str


class SubscriptionBulkCreateBody(TypedDict):
    subscriptions: list[SubscriptionCreateBody]


class SubscriptionBulkUpdateBody(TypedDict):
    subscriptions: list[SubscriptionUpdateBody]


class SubscriptionBulkDeleteBodyInnerOptional(TypedDict, total=False):
    send_email: bool


class SubscriptionBulkDeleteBodyInner(SubscriptionBulkDeleteBodyInnerOptional):
    id: str


class SubscriptionBulkDeleteBody(TypedDict):
    subscriptions: list[SubscriptionBulkDeleteBodyInner]


class SubscriptionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/subscriptions
    """

    object_list_key = "subscriptions"
    object_dict_key = "subscription"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: SubscriptionCreateBody) -> Subscription:
        """Create a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def get(self, subscription_id: str) -> Subscription:
        """Get a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:subscription_id", required_scopes
        )

        url = f"{self._url}/{subscription_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def update(
        self, subscription_id: str, body: SubscriptionUpdateBody
    ) -> Subscription:
        """Update a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:subscription_id", required_scopes
        )

        url = f"{self._url}/{subscription_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def delete(self, subscription_id: str, body: SubscriptionDeleteBody) -> dict:
        """Delete a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:subscription_id", required_scopes
        )

        url = f"{self._url}/{subscription_id}"
        data = self._http_delete(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(
        self, query: Optional[SubscriptionListQuery] = None
    ) -> list[Subscription]:
        """List subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def list_all(
        self, query: Optional[SubscriptionListQuery] = None
    ) -> list[Subscription]:
        """List all subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def count(self, query: Optional[SubscriptionCountQuery] = None) -> int:
        """Count subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in dict, got {data}")
        return data["count"]

    def change_date(
        self, subscription_id: str, body: SubscriptionChangeDateBody
    ) -> Subscription:
        """Change the date of a queued subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_date
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/change_date",
            required_scopes,
        )

        url = f"{self._url}/{subscription_id}/change_date"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def change_address(
        self, subscription_id: str, body: SubscriptionChangeAddressBody
    ) -> Subscription:
        """Change the address of a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_address
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/change_address",
            required_scopes,
        )

        url = f"{self._url}/{subscription_id}/change_address"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def cancel(
        self, subscription_id: str, body: SubscriptionCancelBody
    ) -> Subscription:
        """Cancel a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_cancel
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/cancel", required_scopes
        )

        url = f"{self._url}/{subscription_id}/cancel"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def activate(self, subscription_id: str):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_activate
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/activate", required_scopes
        )

        url = f"{self._url}/{subscription_id}/activate"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def bulk_create(self, body: SubscriptionBulkCreateBody) -> list[Subscription]:
        """Bulk create subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}/bulk_create", required_scopes)

        url = f"{self._url}/bulk_create"
        data = self._http_post(url, body, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def bulk_update(self, body: SubscriptionBulkUpdateBody) -> list[Subscription]:
        """Bulk update subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}/bulk_update", required_scopes)

        url = f"{self._url}/bulk_update"
        data = self._http_post(url, body, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def bulk_delete(self, body: SubscriptionBulkDeleteBody) -> list[Subscription]:
        """Bulk delete subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}/bulk_delete", required_scopes)

        url = f"{self._url}/bulk_delete"
        data = self._http_post(url, body, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]
