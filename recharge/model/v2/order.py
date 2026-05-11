from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict


class OrderBillingAddress(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: Optional[str] = None
    province: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    zip: Optional[str] = None


class OrderShippingAddress(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: Optional[str] = None
    province: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    zip: Optional[str] = None


class OrderCustomer(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class OrderLineItemExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class OrderLineItemExternalVariantId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class OrderLineItemImages(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    original: Optional[str] = None


class OrderLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


OrderLineItemPurchaseItemType = Literal["subscription", "onetime"]


class OrderLineItemTaxLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price: str
    rate: str
    title: str


class OrderLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    purchase_item_id: Optional[int] = None
    external_product_id: Optional[OrderLineItemExternalProductId] = None
    external_variant_id: Optional[OrderLineItemExternalVariantId] = None
    grams: Optional[int] = None
    handle: Optional[str] = None
    images: Optional[OrderLineItemImages] = None
    original_price: Optional[str] = None
    properties: list[OrderLineItemProperty] = []
    purchase_item_type: Optional[OrderLineItemPurchaseItemType] = None
    quantity: Optional[int] = None
    sku: Optional[str] = None
    tax_due: Optional[str] = None
    tax_lines: list[OrderLineItemTaxLine] = []
    taxable: Optional[bool] = None
    taxable_amount: Optional[str] = None
    title: Optional[str] = None
    total_price: Optional[str] = None
    unit_price: Optional[str] = None
    unit_price_includes_tax: Optional[bool] = None
    variant_title: Optional[str] = None


class OrderExternalOrderId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


OrderStatus = Literal["success", "error", "queued", "cancelled"]

OrderType = Literal["checkout", "recurring"]


class OrderExternalTransactionId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class OrderExternalOrderNumber(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class OrderCharge(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    external_transaction_id: Optional[OrderExternalTransactionId] = None


class OrderClientDetails(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    browser_ip: str
    user_agent: str


OrderDiscountValueType = Literal["percentage", "fixed_amount"]


class OrderDiscount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    code: str
    value: float
    value_type: OrderDiscountValueType


class OrderAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class OrderTaxLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price: str
    rate: str
    title: str


class OrderShippingLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str
    price: str
    source: str
    title: str
    taxable: bool
    tax_lines: list[OrderTaxLine] = []


class Order(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    address_id: int
    billing_address: Optional[OrderBillingAddress] = None
    charge: Optional[OrderCharge] = None
    client_details: Optional[OrderClientDetails] = None
    created_at: str
    customer: Optional[OrderCustomer] = None
    discounts: list[OrderDiscount] = []
    external_cart_token: Optional[str] = None
    external_order_id: Optional[OrderExternalOrderId] = None
    external_order_number: Optional[OrderExternalOrderNumber] = None
    is_prepaid: bool
    line_items: list[OrderLineItem] = []
    note: Optional[str] = None
    order_attributes: list[OrderAttribute] = []
    processed_at: Optional[str] = None
    scheduled_at: str
    shipping_address: Optional[OrderShippingAddress] = None
    shipping_lines: list[OrderShippingLine] = []
    status: OrderStatus
    subtotal_price: str
    tags: list[str] = []
    tax_lines: list[OrderTaxLine] = []
    taxable: bool
    total_discounts: str
    total_duties: Optional[str] = None
    total_line_items_price: Optional[int] = None
    total_price: str
    total_tax: str
    total_weight_grams: int
    type: Optional[OrderType] = None
    updated_at: str
