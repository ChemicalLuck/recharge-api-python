from typing import Any, Literal, Optional, Union

from pydantic import field_validator

from recharge.model.base import RechargeModel


class OrderBillingAddress(RechargeModel):
    address1: Optional[str] = None
    province: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    zip: Optional[str] = None


class OrderShippingAddress(RechargeModel):
    address1: Optional[str] = None
    province: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    zip: Optional[str] = None


class OrderCustomer(RechargeModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class OrderLineItemExternalProductId(RechargeModel):
    ecommerce: Optional[str] = None


class OrderLineItemExternalVariantId(RechargeModel):
    ecommerce: Optional[str] = None


class OrderLineItemImages(RechargeModel):
    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    original: Optional[str] = None


class OrderLineItemProperty(RechargeModel):
    name: str
    value: str


OrderLineItemPurchaseItemType = Literal["subscription", "onetime"]


class OrderLineItemTaxLine(RechargeModel):
    price: str
    rate: Union[str, float]
    title: str


class OrderLineItem(RechargeModel):
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


class OrderExternalOrderId(RechargeModel):
    ecommerce: Optional[str] = None


OrderStatus = Literal["success", "error", "queued", "cancelled"]

OrderType = Literal["checkout", "recurring"]


class OrderExternalTransactionId(RechargeModel):
    payment_processor: Optional[str] = None


class OrderExternalOrderNumber(RechargeModel):
    ecommerce: str


class OrderCharge(RechargeModel):
    id: int
    external_transaction_id: Optional[OrderExternalTransactionId] = None


class OrderClientDetails(RechargeModel):
    browser_ip: Optional[str] = None
    user_agent: Optional[str] = None


OrderDiscountValueType = Literal["percentage", "fixed_amount", "shipping"]


class OrderDiscount(RechargeModel):
    id: int
    code: str
    value: float
    value_type: OrderDiscountValueType


class OrderAttribute(RechargeModel):
    name: str
    value: Optional[str] = None


class OrderTaxLine(RechargeModel):
    price: str
    rate: Union[str, float]
    title: str


class OrderShippingLine(RechargeModel):
    code: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    taxable: Optional[Union[str, bool]] = None
    tax_lines: list[OrderTaxLine] = []


class Order(RechargeModel):
    @field_validator("tags", mode="before")
    @classmethod
    def parse_tags(cls, v: Any) -> Any:
        if isinstance(v, str):
            return [t.strip() for t in v.split(",") if t.strip()]
        return v

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
    total_line_items_price: Optional[str] = None
    total_price: str
    total_tax: str
    total_weight_grams: int
    type: Optional[OrderType] = None
    updated_at: str
