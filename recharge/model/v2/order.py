from typing import Literal, Optional, TypedDict


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


OrderLineItemPurchaseItemType = Literal["subscription", "onetime"]


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


OrderStatus = Literal["success", "error", "queued", "cancelled"]

OrderType = Literal["checkout", "recurring"]


class OrderExternalTransactionId(TypedDict):
    ecommerce: str


class OrderExternalOrderNumber(TypedDict):
    ecommerce: str


class OrderCharge(TypedDict):
    id: int
    external_transaction_id: OrderExternalTransactionId


class OrderClientDetails(TypedDict):
    browser_ip: str
    user_agent: str


OrderDiscountValueType = Literal["percentage", "fixed_amount"]


class OrderDiscount(TypedDict):
    id: int
    code: str
    value: float
    value_type: OrderDiscountValueType


class OrderAttribute(TypedDict):
    name: str
    value: str


class OrderTaxLine(TypedDict):
    price: str
    rate: str
    title: str


class OrderShippingLine(TypedDict):
    code: str
    price: str
    source: str
    title: str
    taxable: bool
    tax_lines: list[OrderTaxLine]


class Order(TypedDict):
    id: int
    address_id: int
    billing_address: OrderBillingAddress
    charge: OrderCharge
    client_details: OrderClientDetails
    created_at: str
    customer: OrderCustomer
    discounts: list[OrderDiscount]
    external_cart_token: str
    external_order_id: OrderExternalOrderId
    external_order_number: OrderExternalOrderNumber
    is_prepaid: bool
    line_items: list[OrderLineItem]
    note: str
    order_attributes: list[OrderAttribute]
    processed_at: Optional[str]
    scheduled_at: str
    shipping_address: OrderShippingAddress
    shipping_lines: list[OrderShippingLine]
    status: OrderStatus
    subtotal_price: str
    tags: list[str]
    tax_lines: list[OrderTaxLine]
    taxable: bool
    total_discounts: str
    total_duties: str
    total_line_items_price: int
    total_price: str
    total_tax: str
    total_weight_grams: int
    updated_at: str


Order.__annotations__["type"] = OrderType
