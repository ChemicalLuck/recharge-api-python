from pydantic import BaseModel, ConfigDict


class StoreTimezone(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    iana_name: str
    name: str


class Store(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    checkout_logo_url: str
    checkout_platform: str
    created_at: str
    currency: str
    customer_portal_base_url: str
    default_api_version: str
    email: str
    enabled_presentment_currencies: list[str]
    enabled_presentment_currencies_symbols: list[str]
    disabled_currencies_historical: list[str]
    external_platform: str
    identifier: str
    merchant_portal_base_url: str
    name: str
    phone: str
    timezone: StoreTimezone
    updated_at: str
    weight_unit: str
