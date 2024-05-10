from typing import Literal, Required, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope


SubscriptionOrderIntervalUnit: TypeAlias = Literal["day", "week", "month"]


class SubscriptionProperty(TypedDict):
    name: str
    value: str


SubscriptionStatus: TypeAlias = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class SubscriptionCreateBody(TypedDict, total=False):
    address_id: Required[int]
    charge_interval_frequency: Required[int]
    customer_id: str
    expire_after_specific_number_of_charges: str
    next_charge_scheduled_at: Required[str]
    order_day_of_month: str
    order_day_of_week: str
    order_interval_frequency: Required[str]
    order_interval_unit: Required[SubscriptionOrderIntervalUnit]
    price: str
    properties: list[SubscriptionProperty]
    product_title: str
    quantity: Required[str]
    shopify_product_id: Required[str]
    shopify_variant_id: Required[str]
    status: SubscriptionStatus


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


class SubscriptionChangeAddressBody(TypedDict, total=False):
    address_id: Required[str]
    next_charge_scheduled_at: str


class SubscriptionCancelBody(TypedDict, total=False):
    cancellation_reason: Required[str]
    cancellation_reason_comments: str
    send_email: bool


class SubscriptionBulkCreateBody(TypedDict):
    subscriptions: list[SubscriptionCreateBody]


class SubscriptionBulkUpdateBody(TypedDict):
    subscriptions: list[SubscriptionUpdateBody]


class SubscriptionBulkDeleteBodyInner(TypedDict, total=False):
    id: Required[str]
    send_email: bool


class SubscriptionBulkDeleteBody(TypedDict):
    subscriptions: list[SubscriptionBulkDeleteBodyInner]


class SubscriptionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/subscriptions
    """

    object_list_key = "subscriptions"

    def create(self, body: SubscriptionCreateBody):
        """Create a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, subscription_id: str):
        """Get a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_get(f"{self.url}/{subscription_id}")

    def update(self, subscription_id: str, body: SubscriptionUpdateBody):
        """Update a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_put(f"{self.url}/{subscription_id}", body)

    def delete(self, subscription_id: str, body: SubscriptionDeleteBody):
        """Delete a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{subscription_id}", body)

    def list(self, query: SubscriptionListQuery):
        """List subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def count(self, query: SubscriptionCountQuery):
        """Count subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)

    def change_date(self, subscription_id: str, body: SubscriptionChangeDateBody):
        """Change the date of a queued subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_date
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/change_date",
            required_scopes,
        )

        return self._http_post(f"{self.url}/{subscription_id}/change_date", body)

    def change_address(self, subscription_id: str, body: SubscriptionChangeAddressBody):
        """Change the address of a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_address
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/change_address",
            required_scopes,
        )

        return self._http_post(f"{self.url}/{subscription_id}/change_address", body)

    def cancel(self, subscription_id: str):
        """Cancel a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_cancel
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/cancel", required_scopes
        )

        return self._http_post(f"{self.url}/{subscription_id}/cancel", {})

    def activate(self, subscription_id: str):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_activate
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/activate", required_scopes
        )

        return self._http_post(f"{self.url}/{subscription_id}/activate", {})

    def bulk_create(self, body: SubscriptionBulkCreateBody):
        """Bulk create subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}/bulk_create", required_scopes)

        return self._http_post(f"{self.url}/bulk_create", body)

    def bulk_update(self, body: SubscriptionBulkUpdateBody):
        """Bulk update subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}/bulk_update", required_scopes)

        return self._http_post(f"{self.url}/bulk_update", body)

    def bulk_delete(self, body: SubscriptionBulkDeleteBody):
        """Bulk delete subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}/bulk_delete", required_scopes)

        return self._http_post(f"{self.url}/bulk_delete", body)
