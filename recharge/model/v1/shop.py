from typing import Optional

from pydantic import BaseModel, ConfigDict


class Store(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    created_at: Optional[str] = None
    currency: Optional[str] = None
    domain: Optional[str] = None
    iana_timezone: Optional[str] = None
    my_shopify_domain: Optional[str] = None
    name: Optional[str] = None
    shop_phone: Optional[str] = None
    shop_email: Optional[str] = None
    timezone: Optional[str] = None
    updated_at: Optional[str] = None


class ShippingCountryProvince(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    code: Optional[str] = None
    name: Optional[str] = None


class ShippingCountry(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    code: Optional[str] = None
    country_id: Optional[str] = None
    name: Optional[str] = None
    provinces: list[ShippingCountryProvince] = []
