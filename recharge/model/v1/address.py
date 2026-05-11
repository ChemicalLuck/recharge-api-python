from typing import Optional

from pydantic import BaseModel, ConfigDict


class AddressNoteAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class AddressShippingLinesOverride(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str
    price: str
    title: str


class Address(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    address1: Optional[str] = None
    address2: Optional[str] = None
    cart_note: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    customer_id: Optional[int] = None
    discount_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    note_attributes: list[AddressNoteAttribute] = []
    phone: Optional[str] = None
    presentment_currency: Optional[str] = None
    province: Optional[str] = None
    shipping_lines_override: list[AddressShippingLinesOverride] = []
    zip: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
