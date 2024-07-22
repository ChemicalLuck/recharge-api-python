from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.order import (
    Order,
    OrderBillingAddress,
    OrderCustomer,
    OrderExternalOrderId,
    OrderLineItem,
    OrderShippingAddress,
    OrderStatus,
    OrderType,
)


class OrderCloneBody(TypedDict, total=False):
    scheduled_at: str


class OrderUpdateBody(TypedDict, total=False):
    billing_address: OrderBillingAddress
    customer: OrderCustomer
    line_items: list[OrderLineItem]
    external_order_id: OrderExternalOrderId
    scheduled_at: str
    shipping_address: OrderShippingAddress
    status: OrderStatus


class OrderListQuery(TypedDict, total=False):
    address_id: str
    charge_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    external_customer_id: str
    external_order_id: str
    ids: str
    limit: str
    page: str
    scheduled_at_max: str
    scheduled_at_min: str
    has_external_order: str
    status: OrderStatus
    type: OrderType
    purchase_item_id: str
    updated_at_max: str
    updated_at_min: str


class OrderResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/orders
    """

    object_list_key = "orders"
    object_key_dict = "order"
    recharge_version: RechargeVersion = "2021-11"

    def get(self, order_id: str) -> Order:
        """Get an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/:order_id", required_scopes)

        url = f"{self._url}/{order_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def clone(self, order_id: str, body: OrderCloneBody) -> Order:
        """Clone an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_clone
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/clone", required_scopes
        )

        url = f"{self._url}/{order_id}/clone"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def delay(self, order_id: str) -> Order:
        """Delay an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_delay
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/delay", required_scopes
        )

        url = f"{self._url}/{order_id}/delay"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def update(self, order_id: str, body: OrderUpdateBody) -> Order:
        """Update an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_update
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(f"PUT /{self.object_list_key}/:order_id", required_scopes)

        url = f"{self._url}/{order_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def delete(self, order_id: str) -> dict:
        """Delete an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_delete
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(f"DELETE /{self.object_list_key}/:order_id", required_scopes)

        url = f"{self._url}/{order_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[OrderListQuery] = None) -> list[Order]:
        """List orders.
        https://developer.rechargepayments.com/2021-11/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Order(**order) for order in data]

    def list_all(self, query: Optional[OrderListQuery] = None) -> list[Order]:
        """List all orders.
        https://developer.rechargepayments.com/2021-11/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Order(**order) for order in data]
