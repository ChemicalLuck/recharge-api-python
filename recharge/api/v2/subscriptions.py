from typing import Literal, Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


SubscriptionOrderIntervalUnit = Literal["day", "week", "month"]


class SubscriptionProperty(TypedDict):
    name: str
    value: str


SubscriptionStatus = Literal["ACTIVE", "CANCELLED", "EXPIRED"]


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


class SubscriptionSkipGiftRecipientAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str
    email: str


class SubscriptionSkipGiftBody(TypedDict):
    purchase_item_ids: list[int]
    recipient_address: SubscriptionSkipGiftRecipientAddress


class SubscriptionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/subscriptions
    """

    object_list_key = "subscriptions"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: SubscriptionCreateBody):
        """Create a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self._url, body)

    def get(self, subscription_id: str):
        """Get a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_get(f"{self._url}/{subscription_id}")

    def update(self, subscription_id: str, body: SubscriptionUpdateBody):
        """Update a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_put(f"{self._url}/{subscription_id}", body)

    def delete(self, subscription_id: str, body: SubscriptionDeleteBody):
        """Delete a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:subscription_id", required_scopes
        )

        return self._http_delete(f"{self._url}/{subscription_id}", body)

    def list_(self, query: Optional[SubscriptionListQuery] = None):
        """List subscriptions.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self._url, query)

    def change_date(self, subscription_id: str, body: SubscriptionChangeDateBody):
        """Change the date of a queued subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_next_charge
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/set_next_change_date",
            required_scopes,
        )

        return self._http_post(
            f"{self._url}/{subscription_id}/set_next_change_date", body
        )

    def change_address(self, subscription_id: str, body: SubscriptionChangeAddressBody):
        """Change the address of a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_address
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/change_address",
            required_scopes,
        )

        return self._http_post(f"{self._url}/{subscription_id}/change_address", body)

    def cancel(self, subscription_id: str):
        """Cancel a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_cancel
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/cancel", required_scopes
        )

        return self._http_post(f"{self._url}/{subscription_id}/cancel", {})

    def activate(self, subscription_id: str):
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_activate
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/activate", required_scopes
        )

        return self._http_post(f"{self._url}/{subscription_id}/activate", {})

    def skip_gift(self, body: SubscriptionSkipGiftBody):
        """Skip a gift subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/skip_gift
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}/skip_gift", required_scopes)

        return self._http_post(f"{self._url}/skip_gift", body)
