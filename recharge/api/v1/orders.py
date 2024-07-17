from typing import TypedDict, Optional

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.model.v1.order import (
    OrderStatus,
    OrderBillingAddress,
    OrderShippingAddress,
    OrderCustomer,
)


class OrderUpdateBody(TypedDict, total=False):
    billing_address: OrderBillingAddress
    shipping_address: OrderShippingAddress
    customer: OrderCustomer


class OrderListQuery(TypedDict, total=False):
    address_id: str
    charge_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    ids: str
    limit: str
    page: str
    scheduled_at_max: str
    scheduled_at_min: str
    shipping_date: str
    shopify_order_id: str
    has_external_id: str
    status: OrderStatus
    subscription_id: str
    updated_at_max: str
    updated_at_min: str


class OrderCountQuery(TypedDict, total=False):
    address_id: str
    charge_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    scheduled_at_max: str
    scheduled_at_min: str
    shopify_customer_id: str
    status: OrderStatus
    subscription_id: str
    updated_at_max: str
    updated_at_min: str


class OrderChangeDateBody(TypedDict):
    scheduled_at: str


class OrderChangeVariantBody(TypedDict):
    new_shopify_variant_id: str


class OrderCloneBody(TypedDict):
    scheduled_at: str


class OrderResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/orders
    """

    object_list_key = "orders"
    object_dict_key = "order"
    recharge_version: RechargeVersion = "2021-01"

    def get(self, order_id: str):
        """Get an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/:order_id", required_scopes)

        return self._http_get(f"{self._url}/{order_id}")

    def update(self, order_id: str, body: OrderUpdateBody):
        """Update an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_update
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(f"PUT /{self.object_list_key}/:order_id", required_scopes)

        return self._http_put(f"{self._url}/{order_id}", body)

    def delete(self, order_id: str):
        """Delete an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delete
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(f"DELETE /{self.object_list_key}/:order_id", required_scopes)

        return self._http_delete(f"{self._url}/{order_id}")

    def list_(self, query: Optional[OrderListQuery] = None):
        """List orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self._url, query)

    def count(self, query: Optional[OrderCountQuery] = None):
        """Count orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_count
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self._url}/count", query)

    def change_date(self, order_id: str, body: OrderChangeDateBody):
        """Change the date of a queued order.
        https://developer.rechargepayments.com/2021-01/orders/orders_change_date
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/change_date", required_scopes
        )

        return self._http_post(
            f"{self._url}/{order_id}/change_date",
            body,
        )

    def change_variant(
        self, order_id: str, old_variant_id: str, body: OrderChangeVariantBody
    ):
        """Change an order variant.
        https://developer.rechargepayments.com/v1#change-an-order-variant
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:order_id/update_shopify_variant/:old_variant_id",
            required_scopes,
        )

        return self._http_put(
            f"{self._url}/{order_id}/update_shopify_variant/{old_variant_id}", body
        )

    def clone(self, order_id: str, charge_id: str, body: OrderCloneBody):
        """Clone an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_clone
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/clone", required_scopes
        )

        return self._http_post(
            f"{self._url}/clone_order_on_success_charge/{order_id}/charge/{charge_id}",
            body,
        )

    def delay(self, order_id: str):
        """Delay an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delay
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/delay", required_scopes
        )

        return self._http_post(f"{self._url}/{order_id}/delay", None)
