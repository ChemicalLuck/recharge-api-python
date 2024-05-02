from typing import Literal, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope


class OrderBillingAddress(TypedDict, total=False):
    address1: str
    province: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    zip: str


class OrderShippingAddress(TypedDict, total=False):
    address1: str
    province: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    zip: str


class OrderCustomer(TypedDict, total=False):
    first_name: str
    last_name: str
    email: str


class OrderUpdateBody(TypedDict, total=False):
    billing_address: OrderBillingAddress
    shipping_address: OrderShippingAddress
    customer: OrderCustomer


OrderStatus: TypeAlias = Literal["SUCCESS", "QUEUED", "ERROR", "REFUNDED", "SKIPPED"]


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

    def get(self, order_id: str):
        """Get an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/:order_id", required_scopes)

        return self._http_get(f"{self.url}/{order_id}")

    def update(self, order_id: str, body: OrderUpdateBody):
        """Update an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_update
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(f"PUT /{self.object_list_key}/:order_id", required_scopes)

        return self._http_put(f"{self.url}/{order_id}", body)

    def delete(self, order_id: str):
        """Delete an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delete
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(f"DELETE /{self.object_list_key}/:order_id", required_scopes)

        return self._http_delete(f"{self.url}/{order_id}")

    def list(self, query: OrderListQuery):
        """List orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def count(self, query: OrderCountQuery):
        """Count orders.
        https://developer.rechargepayments.com/2021-01/orders/orders_count
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)

    def change_date(self, order_id: str, body: OrderChangeDateBody):
        """Change the date of a queued order.
        https://developer.rechargepayments.com/2021-01/orders/orders_change_date
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:order_id/change_date", required_scopes
        )

        return self._http_post(
            f"{self.url}/{order_id}/change_date",
            body,
        )

    def change_variant(
        self, order_id: str, old_variant_id: str, body: OrderChangeVariantBody
    ):
        """Change an order variant.
        https://developer.rechargepayments.com/v1#change-an-order-variant
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:order_id/update_shopify_variant/:old_variant_id",
            required_scopes,
        )

        return self._http_put(
            f"{self.url}/{order_id}/update_shopify_variant/{old_variant_id}", body
        )

    def clone(self, order_id: str, charge_id: str, body: OrderCloneBody):
        """Clone an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_clone
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:order_id/clone", required_scopes
        )

        return self._http_post(
            f"{self.url}/clone_order_on_success_charge/{order_id}/charge/{charge_id}",
            body,
        )

    def delay(self, order_id: str):
        """Delay an order.
        https://developer.rechargepayments.com/2021-01/orders/orders_delay
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:order_id/delay", required_scopes
        )

        return self._http_post(f"{self.url}/{order_id}/delay", None)
