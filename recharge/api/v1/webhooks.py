from typing import Literal, Required, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope

WebhookTopic: TypeAlias = Literal[
    "address/created",
    "address/updated",
    "async_batch/processed",
    "bundle_selection/created",
    "bundle_selection/updated",
    "bundle_selection/deleted",
    "customer/activated",
    "customer/created",
    "customer/deactivated",
    "customer/payment_method_updated",
    "customer/updated",
    "customer/deleted",
    "charge/created",
    "charge/failed",
    "charge/max_retries_reached",
    "charge/paid",
    "charge/refunded",
    "charge/uncaptured",
    "charge/upcoming",
    "charge/updated",
    "charge/deleted",
    "checkout/created",
    "checkout/completed",
    "checkout/processed",
    "checkout/updated",
    "onetime/created",
    "onetime/deleted",
    "onetime/updated",
    "order/cancelled",
    "order/created",
    "order/deleted",
    "order/processed",
    "order/payment_captured",
    "order/upcoming",
    "order/updated",
    "order/success",
    "plan/created",
    "plan/deleted",
    "plan/updated",
    "subscription/activated",
    "subscription/cancelled",
    "subscription/created",
    "subscription/deleted",
    "subscription/skipped",
    "subscription/updated",
    "subscription/unskipped",
    "subscription/swapped",
    "subscription/paused",
    "store/updated",
    "recharge/uninstalled",
]

WebhookTopicMap: dict[str, RechargeScope] = {
    "address": "read_customers",
    "async_batch": "read_batches",
    "bundle_selection": "read_subscriptions",
    "customer": "read_customers",
    "charge": "read_orders",
    "checkout": "read_checkouts",
    "onetime": "read_subscriptions",
    "order": "read_orders",
    "product": "read_products",
    "subscription": "read_subscriptions",
    "shop": "store_info",
    "recharge": "store_info",
}

WebhookIncludedObject: TypeAlias = Literal[
    "addresses", "collections", "customer", "metafields"
]


class WebhookCreateBody(TypedDict, total=False):
    address: Required[str]
    inclded_objects: list[WebhookIncludedObject]
    topic: Required[WebhookTopic]


class WebhookResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_object
    """

    object_list_key = "webhooks"

    def create(self, body: WebhookCreateBody):
        """Create a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_create
        """
        resource = body["topic"].split("/")[0]
        required_scopes: list[RechargeScope] = [WebhookTopicMap[resource]]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, webhook_id: str):
        """Get a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_retrieve
        """
        return self._http_get(f"{self.url}/{webhook_id}")

    def update(self, webhook_id: str):
        """Update a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_update
        """
        return self._http_delete(f"{self.url}/{webhook_id}")

    def list(self):
        """List webhooks.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_list
        """
        return self._http_get(self.url)

    def test(self, webhook_id: str):
        """Test a webhook.
        https://developer.rechargepayments.com/2021-01/webhooks_endpoints/webhooks_test
        """
        return self._http_post(f"{self.url}/{webhook_id}/test")
