from typing import Optional

from pydantic import BaseModel, ConfigDict


class OnetimeExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class OnetimeExternalVariantId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class OnetimeProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class Onetime(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    address_id: Optional[int] = None
    created_at: Optional[str] = None
    customer_id: Optional[int] = None
    external_product_id: Optional[OnetimeExternalProductId] = None
    external_variant_id: Optional[OnetimeExternalVariantId] = None
    is_cancelled: Optional[bool] = None
    next_charge_scheduled_at: Optional[str] = None
    price: Optional[int] = None
    product_title: Optional[str] = None
    properties: list[OnetimeProperty] = []
    quantity: Optional[int] = None
    sku: Optional[str] = None
    sku_override: Optional[bool] = None
    updated_at: Optional[str] = None
    variant_title: Optional[str] = None
