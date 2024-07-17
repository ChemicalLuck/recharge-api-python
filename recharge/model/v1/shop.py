from typing import TypedDict


class Store(TypedDict):
    id: int
    created_at: str
    currency: str
    domain: str
    iana_timezone: str
    my_shopify_domain: str
    name: str
    shop_phone: str
    shop_email: str
    timezone: str
    updated_at: str


class ShippingCountryProvince(TypedDict):
    id: int
    code: str
    name: str


class ShippingCountry(TypedDict):
    id: int
    code: str
    country_id: str
    name: str
    provinces: list[ShippingCountryProvince]
