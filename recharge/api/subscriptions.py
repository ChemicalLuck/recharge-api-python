from recharge.api import RechargeResource
from recharge.api.tokens import TokenScope

from typing import TypedDict, Literal, Required

type SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]


class SubscriptionProperty(TypedDict):
    name: str
    value: str


type SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


class SubscriptionCreateBody(TypedDict):
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


class SubscriptionUpdateBody(TypedDict):
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


class SubscriptionListQuery(TypedDict):
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


class SubscriptionCountQuery(TypedDict):
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


class SubscriptionChangeAddressBody(TypedDict):
    address_id: Required[str]
    next_charge_scheduled_at: str


class SubscriptionCancelBody(TypedDict):
    cancellation_reason: Required[str]
    cancellation_reason_comments: str
    send_email: bool


class SubscriptionBulkCreateBody(TypedDict):
    subscriptions: list[SubscriptionCreateBody]


class SubscriptionBulkUpdateBody(TypedDict):
    subscriptions: list[SubscriptionUpdateBody]


class SubscriptionBulkDeleteBodyInner(TypedDict):
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
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("POST /subscriptions", required_scopes)

        return self.http_post(self.url, body)

    def get(self, subscription_id: str):
        """Get a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_retrieve
        """
        required_scopes: list[TokenScope] = ["read_subscriptions"]
        self.check_scopes("GET /subscriptions/:subscription_id", required_scopes)

        return self.http_get(f"{self.url}/{subscription_id}")

    def update(self, subscription_id: str, body: SubscriptionUpdateBody):
        """Update a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_update
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("PUT /subscriptions/:subscription_id", required_scopes)

        return self.http_put(f"{self.url}/{subscription_id}", body)

    def delete(self, subscription_id: str, body: SubscriptionDeleteBody):
        """Delete a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_delete
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("DELETE /subscriptions/:subscription_id", required_scopes)

        return self.http_delete(f"{self.url}/{subscription_id}", body)

    def list(self, query: SubscriptionListQuery):
        """List subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_list
        """
        required_scopes: list[TokenScope] = ["read_subscriptions"]
        self.check_scopes("GET /subscriptions", required_scopes)

        return self.http_get(self.url, query)

    def count(self, query: SubscriptionCountQuery):
        """Count subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_count
        """
        required_scopes: list[TokenScope] = ["read_subscriptions"]
        self.check_scopes("GET /subscriptions/count", required_scopes)

        return self.http_get(f"{self.url}/count", query)

    def change_date(self, subscription_id: str, body: SubscriptionChangeDateBody):
        """Change the date of a queued subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_date
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes(
            "POST /subscriptions/:subscription_id/change_date", required_scopes
        )

        return self.http_post(f"{self.url}/{subscription_id}/change_date", body)

    def change_address(self, subscription_id: str, body: SubscriptionChangeAddressBody):
        """Change the address of a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_change_address
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes(
            "POST /subscriptions/:subscription_id/change_address", required_scopes
        )

        return self.http_post(f"{self.url}/{subscription_id}/change_address", body)

    def cancel(self, subscription_id: str):
        """Cancel a subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_cancel
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes(
            "POST /subscriptions/:subscription_id/cancel", required_scopes
        )

        return self.http_post(f"{self.url}/{subscription_id}/cancel", {})

    def activate(self, subscription_id: str):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_activate
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes(
            "POST /subscriptions/:subscription_id/activate", required_scopes
        )

        return self.http_post(f"{self.url}/{subscription_id}/activate", {})

    def bulk_create(self, body: SubscriptionBulkCreateBody):
        """Bulk create subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_create
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("POST /subscriptions/bulk_create", required_scopes)

        return self.http_post(f"{self.url}/bulk_create", body)

    def bulk_update(self, body: SubscriptionBulkUpdateBody):
        """Bulk update subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_update
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("POST /subscriptions/bulk_update", required_scopes)

        return self.http_post(f"{self.url}/bulk_update", body)

    def bulk_delete(self, body: SubscriptionBulkDeleteBody):
        """Bulk delete subscriptions.
        https://developer.rechargepayments.com/2021-01/subscriptions/subscriptions_bulk_delete
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("POST /subscriptions/bulk_delete", required_scopes)

        return self.http_post(f"{self.url}/bulk_delete", body)
