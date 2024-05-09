from typing import Literal, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope


class OrderCloneBody(TypedDict, total=False):
    scheduled_at: str


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


class OrderLineItemExternalProductId(TypedDict, total=False):
    ecommerce: str


class OrderLineItemExternalVariantId(TypedDict, total=False):
    ecommerce: str


class OrderLineItemImages(TypedDict, total=False):
    large: str
    medium: str
    small: str
    original: str


class OrderLineItemProperty(TypedDict):
    name: str
    value: str


OrderLineItemPurchaseItemType: TypeAlias = Literal["subscription", "onetime"]


class OrderLineItemTaxLine(TypedDict):
    price: str
    rate: str
    title: str


class OrderLineItem(TypedDict, total=False):
    purchase_item_id: int
    external_product_id: OrderLineItemExternalProductId
    external_variant_id: OrderLineItemExternalVariantId
    grams: int
    handle: str
    images: OrderLineItemImages
    original_price: str
    properties: list[OrderLineItemProperty]
    purchase_item_type: OrderLineItemPurchaseItemType
    quantity: int
    sku: str
    tax_due: str
    tax_lines: list[OrderLineItemTaxLine]
    taxable: bool
    taxable_amount: str
    title: str
    total_price: str
    unit_price: str
    unit_price_includes_tax: bool
    variant_title: str


class OrderExternalOrderId(TypedDict, total=False):
    ecommerce: str


OrderStatus: TypeAlias = Literal["success", "error", "queued", "cancelled"]


class OrderUpdateBody(TypedDict, total=False):
    billing_address: OrderBillingAddress
    customer: OrderCustomer
    line_items: list[OrderLineItem]
    external_order_id: OrderExternalOrderId
    scheduled_at: str
    shipping_address: OrderShippingAddress
    status: OrderStatus


OrderType: TypeAlias = Literal["checkout", "recurring"]


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

    def get(self, order_id: str):
        """Get an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/:order_id", required_scopes)

        return self._http_get(f"{self.url}/{order_id}")

    def clone(self, order_id: str, body: OrderCloneBody):
        """Clone an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_clone
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:order_id/clone", required_scopes
        )

        return self._http_post(f"{self.url}/{order_id}/clone", body)

    def delay(self, order_id: str):
        """Delay an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_delay
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:order_id/delay", required_scopes
        )

        return self._http_post(f"{self.url}/{order_id}/delay")

    def update(self, order_id: str, body: OrderUpdateBody):
        """Update an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_update
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(f"PUT /{self.object_list_key}/:order_id", required_scopes)

        return self._http_put(f"{self.url}/{order_id}", body)

    def delete(self, order_id: str):
        """Delete an order.
        https://developer.rechargepayments.com/2021-11/orders/orders_delete
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(f"DELETE /{self.object_list_key}/:order_id", required_scopes)

        return self._http_delete(f"{self.url}/{order_id}")

    def list(self, query: OrderListQuery | None = None):
        """List orders.
        https://developer.rechargepayments.com/2021-11/orders/orders_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
