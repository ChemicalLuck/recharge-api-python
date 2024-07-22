from typing import Optional, TypedDict


class AddressNoteAttribute(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict):
    code: str
    price: str
    title: str


class Address(TypedDict):
    id: int
    address1: str
    address2: str
    cart_note: Optional[str]
    city: str
    company: str
    country: str
    country_code: str
    customer_id: int
    discount_id: int
    first_name: str
    last_name: str
    note_attributes: list[AddressNoteAttribute]
    phone: str
    presentment_currency: str
    province: str
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: str
    created_at: str
    updated_at: str
