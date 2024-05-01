from recharge.api.tokens import TokenScope
from . import RechargeResource

from typing import TypedDict, Required


class OnetimeProperty(TypedDict):
    name: str
    value: str


class OnetimeCreateBody(TypedDict):
    add_to_next_charge: bool
    next_charge_scheduled_at: Required[str]
    price: int
    product_title: str
    properties: list[OnetimeProperty]
    quantity: Required[int]
    shopify_product_id: int
    shopify_variant_id: Required[int]


class OnetimeUpdateBody(TypedDict):
    next_charge_scheduled_at: str
    price: int
    product_title: str
    properties: list[OnetimeProperty]
    quantity: int
    shopify_product_id: int
    sku: str
    shopify_variant_id: int


class OnetimeListQuery(TypedDict):
    address_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    limit: str
    page: str
    shopify_customer_id: str
    updated_at_max: str
    updated_at_min: str


class OnetimeResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/onetimes
    """

    object_list_key = "onetimes"

    def create(self, body: OnetimeCreateBody):
        """Create a Onetime
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_create
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("POST /onetimes", required_scopes)

        return self.http_post(self.url, body)

    def get(self, onetime_id: str):
        """Get a Onetime
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_retrieve
        """
        required_scopes: list[TokenScope] = ["read_subscriptions"]
        self.check_scopes("GET /onetimes/:onetime_id", required_scopes)

        return self.http_get(f"{self.url}/{onetime_id}")

    def update(self, onetime_id: str, body: OnetimeUpdateBody):
        """Update a Onetime
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_update
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("PUT /onetimes/:onetime_id", required_scopes)

        return self.http_put(f"{self.url}/{onetime_id}", body)

    def delete(self, onetime_id: str):
        """Delete a Onetime.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_delete
        """
        required_scopes: list[TokenScope] = ["write_subscriptions"]
        self.check_scopes("DELETE /onetimes/:onetime_id", required_scopes)

        return self.http_delete(f"{self.url}/{onetime_id}")

    def list(self, query: OnetimeListQuery):
        """List Onetimes.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list
        """
        required_scopes: list[TokenScope] = ["read_subscriptions"]
        self.check_scopes("GET /onetimes", required_scopes)

        return self.http_get(self.url, query)
