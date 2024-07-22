from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.onetime import Onetime, OnetimeProperty


class OnetimeCreateBodyOptional(TypedDict, total=False):
    add_to_next_charge: bool
    price: int
    product_title: str
    properties: list[OnetimeProperty]
    shopify_product_id: int


class OnetimeCreateBody(OnetimeCreateBodyOptional):
    next_charge_scheduled_at: str
    quantity: int
    shopify_variant_id: int


class OnetimeUpdateBody(TypedDict, total=False):
    next_charge_scheduled_at: str
    price: int
    product_title: str
    properties: list[OnetimeProperty]
    quantity: int
    shopify_product_id: int
    sku: str
    shopify_variant_id: int


class OnetimeDeleteBody(TypedDict):
    onetime_id: str


class OnetimeListQuery(TypedDict, total=False):
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
    object_dict_key = "onetime"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: OnetimeCreateBody) -> Onetime:
        """Create a Onetime
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Onetime(**data)

    def get(self, onetime_id: str) -> Onetime:
        """Get a Onetime
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_retrieve
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
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_update
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
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_delete
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
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Onetime(**item) for item in data]

    def list_all(self, query: Optional[OnetimeListQuery] = None) -> list[Onetime]:
        """List all Onetimes.
        https://developer.rechargepayments.com/2021-01/onetimes/onetimes_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Onetime(**item) for item in data]
