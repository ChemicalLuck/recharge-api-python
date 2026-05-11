from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

AddressDiscountType = Literal["percentage", "fixed_amount"]


class AddressOrderAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class AddressDiscount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[str] = None
    code: Optional[str] = None
    value: Optional[int] = None
    discount_type: Optional[AddressDiscountType] = None


class AddressNoteAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class AddressShippingLinesOverride(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: Optional[str] = None
    price: Optional[str] = None
    title: Optional[str] = None


class Address(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    payment_method_id: Optional[int] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country_code: Optional[str] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    discounts: list[AddressDiscount] = []
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    order_attributes: list[AddressOrderAttribute] = []
    order_note: Optional[str] = None
    phone: Optional[str] = None
    presentment_currency: Optional[str] = None
    province: Optional[str] = None
    shipping_lines_conserved: list[AddressShippingLinesOverride] = []
    shipping_lines_override: list[AddressShippingLinesOverride] = []
    zip: Optional[str] = None
    updated_at: Optional[str] = None
