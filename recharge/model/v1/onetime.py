from typing import Optional

from recharge.model.base import RechargeModel


class OnetimeProperty(RechargeModel):
    name: str
    value: str


class Onetime(RechargeModel):
    id: int
    address_id: Optional[int] = None
    add_to_next_charge: Optional[bool] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    next_charge_scheduled_at: Optional[str] = None
    price: Optional[int] = None
    product_title: Optional[str] = None
    properties: list[OnetimeProperty] = []
    quantity: Optional[int] = None
    recharge_product_id: Optional[int] = None
    shopify_product_id: Optional[int] = None
    shopify_variant_id: Optional[int] = None
    sku: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[str] = None
    variant_title: Optional[str] = None
