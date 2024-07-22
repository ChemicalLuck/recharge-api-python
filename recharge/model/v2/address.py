from typing import Literal, Optional, TypedDict


class AddressOrderAttribute(TypedDict):
    name: str
    value: str


AddressDiscountType = Literal["percentage", "fixed_amount"]


class AddressDiscount(TypedDict):
    id: str
    code: str
    value: int
    discount_type: AddressDiscountType


class AddressNoteAttribute(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict):
    code: str
    price: str
    title: str


class Address(TypedDict):
    id: int
    payment_method_id: int
    address1: str
    address2: Optional[str]
    city: str
    company: str
    country_code: str
    created_at: str
    customer_id: int
    discounts: list[AddressDiscount]
    first_name: str
    last_name: str
    order_attributes: list[AddressOrderAttribute]
    order_note: str
    phone: str
    presentment_currency: str
    province: str
    shipping_lines_conserved: list[AddressShippingLinesOverride]
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: str
    updated_at: str
