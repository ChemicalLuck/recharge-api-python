from typing import Literal, TypedDict


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


OrderStatus = Literal["SUCCESS", "QUEUED", "ERROR", "REFUNDED", "SKIPPED"]


class OrderLineItemImages(TypedDict):
    large: str
    medium: str
    original: str
    small: str


class OrderLineItemTaxLine(TypedDict):
    price: str
    rate: str
    title: str
    unit_price: str


class OrderLineItemProperty(TypedDict):
    name: str
    value: str


class OrderLineItem(TypedDict):
    external_inventory_policy: str
    gram: int
    images: OrderLineItemImages
    original_price: str
    price: str
    product_title: str
    quantity: int
    shopify_product_id: int
    shopify_variant_id: int
    tax_lines: list[OrderLineItemTaxLine]
    title: str
    variant_title: str
    sku: str
    properties: list[OrderLineItemProperty]


class Order(TypedDict):
    id: int
    billing_address: OrderBillingAddress
    currency: str
    customer: OrderCustomer
    email: str
    error: str
    first_name: str
    is_prepaid: bool
    last_name: str
    line_items: list[OrderLineItem]
    payment_processor: str
    processed_at: str
    scheduled_at: str
    shipping_address: OrderShippingAddress
    shopify_cart_token: str
    shopify_customer_id: int
    shopify_order_id: int
    status: OrderStatus
    transaction_id: str
    total_price: int
    total_duties: str
    address_id: int
    charge_id: int
    created_at: str
    customer_id: int
    shipping_date: str
    updated_at: str


OrderType = Literal["CHECKOUT", "RECURRING"]


Order.__annotations__["type"] = OrderType
