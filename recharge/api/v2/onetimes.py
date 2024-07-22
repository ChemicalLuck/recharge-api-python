from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.onetime import (
    Onetime,
    OnetimeExternalProductId,
    OnetimeExternalVariantId,
    OnetimeProperty,
)


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
    object_dict_key = "onetime"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: OnetimeCreateBody) -> Onetime:
        """Create a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Onetime(**data)

    def get(self, onetime_id: str) -> Onetime:
        """Get a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}/:onetime_id", required_scopes)

        url = f"{self._url}/{onetime_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Onetime(**data)

    def update(self, onetime_id: str, body: OnetimeUpdateBody) -> Onetime:
        """Update a Onetime
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"PUT /{self.object_list_key}/:onetime_id", required_scopes)

        url = f"{self._url}/{onetime_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Onetime(**data)

    def delete(self, onetime_id: str) -> dict:
        """Delete a Onetime.
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:onetime_id", required_scopes
        )

        url = f"{self._url}/{onetime_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[OnetimeListQuery] = None) -> list[Onetime]:
        """List Onetimes.
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Onetime(**item) for item in data]

    def list_all(self, query: Optional[OnetimeListQuery] = None) -> list[Onetime]:
        """List all onetimes.
        https://developer.rechargepayments.com/2021-11/onetimes/onetimes_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Onetime(**item) for item in data]
