from typing import Optional

from recharge.model.base import RechargeModel


class OnetimeExternalProductId(RechargeModel):
    ecommerce: Optional[str] = None


class OnetimeExternalVariantId(RechargeModel):
    ecommerce: Optional[str] = None


class OnetimeProperty(RechargeModel):
    name: str
    value: str


class Onetime(RechargeModel):
    id: int
    address_id: Optional[int] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    external_product_id: Optional[OnetimeExternalProductId] = None
    external_variant_id: Optional[OnetimeExternalVariantId] = None
    is_cancelled: Optional[bool] = None
    next_charge_scheduled_at: Optional[str] = None
    price: Optional[str] = None
    product_title: Optional[str] = None
    properties: list[OnetimeProperty] = []
    quantity: Optional[int] = None
    sku: Optional[str] = None
    sku_override: Optional[bool] = None
    updated_at: Optional[str] = None
    variant_title: Optional[str] = None
