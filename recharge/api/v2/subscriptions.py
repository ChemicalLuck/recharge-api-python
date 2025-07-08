from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.onetime import Onetime
from recharge.model.v2.subscription import (
    Subscription,
    SubscriptionExternalProductId,
    SubscriptionExternalVariantId,
    SubscriptionOrderIntervalUnit,
    SubscriptionProperty,
    SubscriptionStatus,
)


class SubscriptionCreateBodyOptional(TypedDict, total=False):
    customer_id: str
    expire_after_specific_number_of_charges: int
    order_day_of_month: int
    order_day_of_week: int
    plan_id: int
    price: str
    product_title: str
    properties: list[SubscriptionProperty]
    external_product_id: SubscriptionExternalProductId
    status: SubscriptionStatus


class SubscriptionCreateBody(SubscriptionCreateBodyOptional):
    address_id: int
    charge_interval_frequency: int
    next_charge_scheduled_at: str
    order_interval_frequency: int
    quantity: int
    order_interval_unit: SubscriptionOrderIntervalUnit
    external_variant_id: SubscriptionExternalVariantId


class SubscriptionUpdateBody(TypedDict, total=False):
    commit: bool
    force_update: bool
    charge_interval_frequency: int
    expire_after_specific_number_of_charges: int
    external_variant_id: SubscriptionExternalVariantId
    order_day_of_month: str
    order_day_of_week: str
    order_interval_frequency: str
    order_interval_unit: SubscriptionOrderIntervalUnit
    plan_id: int
    price: str
    product_title: str
    properties: list[SubscriptionProperty]
    quantity: str
    sku: str
    sku_override: str
    use_shopify_variant_defaults: bool
    variant_title: str


class SubscriptionDeleteBody(TypedDict):
    send_email: bool


class SubscriptionListQuery(TypedDict, total=False):
    address_id: str
    address_ids: str
    created_at_max: str
    created_at_min: str
    cursor: str
    customer_id: str
    external_variant_id: str
    ids: str
    limit: str
    page: str  # deprecated
    status: SubscriptionStatus
    updated_at_max: str
    updated_at_min: str


class SubscriptionChangeDateBody(TypedDict, total=True):
    date: str


class SubscriptionChangeAddressBodyOptional(TypedDict, total=False):
    next_charge_scheduled_at: str


class SubscriptionChangeAddressBody(SubscriptionChangeAddressBodyOptional):
    address_id: int


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
    object_dict_key = "subscription"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: SubscriptionCreateBody) -> Subscription:
        """Create a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def get(self, subscription_id: str) -> Subscription:
        """Get a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_retrieve
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
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_update
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
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_delete
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
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def list_all(
        self, query: Optional[SubscriptionListQuery] = None
    ) -> list[Subscription]:
        """List all subscriptions.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Subscription(**item) for item in data]

    def change_date(
        self, subscription_id: str, body: SubscriptionChangeDateBody
    ) -> Subscription:
        """Change the date of a queued subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_next_charge
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:subscription_id/set_next_charge_date",
            required_scopes,
        )

        url = f"{self._url}/{subscription_id}/set_next_charge_date"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Subscription(**data)

    def change_address(
        self, subscription_id: str, body: SubscriptionChangeAddressBody
    ) -> Subscription:
        """Change the address of a subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_change_address
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
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_cancel
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

    def activate(self, subscription_id: str) -> Subscription:
        """Activate a cancelled subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/subscriptions_activate
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

    def skip_gift(self, body: SubscriptionSkipGiftBody) -> list[Onetime]:
        """Skip a gift subscription.
        https://developer.rechargepayments.com/2021-11/subscriptions/skip_gift
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}/skip_gift", required_scopes)

        url = f"{self._url}/skip_gift"
        data = self._http_post(url, body, expected=list, response_key="onetimes")
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Onetime(**item) for item in data]
