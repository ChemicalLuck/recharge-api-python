from typing import Literal, TypedDict

from recharge.api import RechargeScope

WebhookTopic = Literal[
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

WebhookIncludedObject = Literal["addresses", "collections", "customer", "metafields"]


class Webhook(TypedDict):
    id: int
    address: str
    included_objects: list[WebhookIncludedObject]
    topic: WebhookTopic
