from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.order import (
    Order,
    OrderBillingAddress,
    OrderCustomer,
    OrderShippingAddress,
    OrderStatus,
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

    def get(self, order_id: str) -> Order:
        """Get an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/:order_id", required_scopes)

        url = f"{self._url}/{order_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def update(self, order_id: str, body: OrderUpdateBody) -> Order:
        """Update an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_update
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
        https://developer.rechargepayments.com/2021-01/orders/orders_delete
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
        https://developer.rechargepayments.com/2021-01/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Order(**item) for item in data]

    def list_all(self, query: Optional[OrderListQuery] = None) -> list[Order]:
        """List all orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Order(**item) for item in data]

    def count(self, query: Optional[OrderCountQuery] = None) -> int:
        """Count orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_count
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in response, got {data}")
        return data["count"]

    def change_date(self, order_id: str, body: OrderChangeDateBody) -> Order:
        """Change the date of a queued order.
        https://developer.rechargepayments.com/2021-01/orders/orders_change_date
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:order_id/change_date", required_scopes
        )

        url = f"{self._url}/{order_id}/change_date"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def change_variant(
        self, order_id: str, old_variant_id: str, body: OrderChangeVariantBody
    ) -> Order:
        """Change an order variant.
        https://developer.rechargepayments.com/v1#change-an-order-variant
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:order_id/update_shopify_variant/:old_variant_id",
            required_scopes,
        )

        url = f"{self._url}/{order_id}/update_shopify_variant/{old_variant_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def clone(self, order_id: str, charge_id: str, body: OrderCloneBody) -> Order:
        """Clone an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_clone
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/clone_order_on_success_charge/:order_id/charge/:charge_id",
            required_scopes,
        )

        url = f"{self._url}/clone_order_on_success_charge/{order_id}/charge/{charge_id}"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Order(**data)

    def delay(self, order_id: str) -> Order:
        """Delay an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delay
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
