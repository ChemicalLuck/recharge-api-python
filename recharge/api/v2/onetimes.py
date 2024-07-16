from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class OnetimeProperty(TypedDict):
    name: str
    value: str


class OnetimeExternalProductId(TypedDict):
    ecommerce: str


class OnetimeExternalVariantId(TypedDict):
    ecommerce: str

class OnetimeCreateBodyOptional(TypedDict, total=False):
    add_to_next_charge: bool
    external_product_id: OnetimeExternalProductId
    price: str
    properties: list[OnetimeProperty]
    sku: str

class OnetimeCreateBody(OnetimeCreateBodyOptional):
    address_id: int
    external_variant_id: OnetimeExternalVariantId
    next_charge_scheduled_at: str
    product_title: str
    quantity: int


class OnetimeUpdateBody(TypedDict, total=False):
    address_id: int
    next_charge_scheduled_at: str
    price: str
    product_title: str
    properties: list[OnetimeProperty]
    quantity: int
    external_variant_id: OnetimeExternalVariantId
    sku: str
    variant_title: str


class OnetimeDeleteBody(TypedDict):
    onetime_id: str


class OnetimeListQuery(TypedDict, total=False):
    address_id: str
    address_ids: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    include_cancelled: bool
    limit: str
    page: str
    external_variant_id: str
    updated_at_max: str
    updated_at_min: str
    ids: str


class OnetimeResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/onetimes
    """

    object_list_key = "onetimes"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: OnetimeCreateBody):
        """Create a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, onetime_id: str):
        """Get a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}/:onetime_id", required_scopes)

        return self._http_get(f"{self.url}/{onetime_id}")

    def update(self, onetime_id: str, body: OnetimeUpdateBody):
        """Update a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"PUT /{self.object_list_key}/:onetime_id", required_scopes)

        return self._http_put(f"{self.url}/{onetime_id}", body)

    def delete(self, onetime_id: str):
        """Delete a Onetime.
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:onetime_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{onetime_id}")

    def list_(self, query: OnetimeListQuery | None = None):
        """List Onetimes.
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
