from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

OrderStatus = Literal["SUCCESS", "QUEUED", "ERROR", "REFUNDED", "SKIPPED"]

OrderType = Literal["CHECKOUT", "RECURRING"]


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


class OrderLineItemImages(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None


class OrderLineItemTaxLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price: Optional[str] = None
    rate: Optional[str] = None
    title: Optional[str] = None
    unit_price: Optional[str] = None


class OrderLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class OrderLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_inventory_policy: Optional[str] = None
    gram: Optional[int] = None
    images: Optional[OrderLineItemImages] = None
    original_price: Optional[str] = None
    price: Optional[str] = None
    product_title: Optional[str] = None
    quantity: Optional[int] = None
    shopify_product_id: Optional[int] = None
    shopify_variant_id: Optional[int] = None
    tax_lines: list[OrderLineItemTaxLine] = []
    title: Optional[str] = None
    variant_title: Optional[str] = None
    sku: Optional[str] = None
    properties: list[OrderLineItemProperty] = []


class Order(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    billing_address: Optional[OrderBillingAddress] = None
    currency: Optional[str] = None
    customer: Optional[OrderCustomer] = None
    email: Optional[str] = None
    error: Optional[str] = None
    first_name: Optional[str] = None
    is_prepaid: Optional[bool] = None
    last_name: Optional[str] = None
    line_items: list[OrderLineItem] = []
    payment_processor: Optional[str] = None
    processed_at: Optional[str] = None
    scheduled_at: Optional[str] = None
    shipping_address: Optional[OrderShippingAddress] = None
    shopify_cart_token: Optional[str] = None
    shopify_customer_id: Optional[int] = None
    shopify_order_id: Optional[int] = None
    status: Optional[OrderStatus] = None
    transaction_id: Optional[str] = None
    total_price: Optional[int] = None
    total_duties: Optional[str] = None
    address_id: Optional[int] = None
    charge_id: Optional[int] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    shipping_date: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[OrderType] = None
