from typing import TypedDict


class OnetimeProperty(TypedDict):
    name: str
    value: str


class Onetime(TypedDict):
    id: int
    address_id: int
    add_to_next_charge: bool
    created_at: str
    customer_id: int
    next_charge_scheduled_at: str
    price: int
    product_title: str
    properties: list[OnetimeProperty]
    quantity: int
    recharge_product_id: int
    shopify_product_id: int
    shopify_variant_id: int
    sku: str
    status: str
    updated_at: str
    variant_title: str
