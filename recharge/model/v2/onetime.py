from typing import Optional, TypedDict


class OnetimeExternalProductId(TypedDict):
    ecommerce: str


class OnetimeExternalVariantId(TypedDict):
    ecommerce: str


class OnetimeProperty(TypedDict):
    name: str
    value: str


class Onetime(TypedDict):
    id: int
    address_id: int
    created_at: str
    customer_id: int
    external_product_id: OnetimeExternalProductId
    external_variant_id: OnetimeExternalVariantId
    is_cancelled: bool
    next_charge_scheduled_at: str
    price: Optional[int]
    product_title: str
    properties: list[OnetimeProperty]
    quantity: int
    sku: str
    sku_override: bool
    updated_at: str
    variant_title: str
