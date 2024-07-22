from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.address import (
    Address,
    AddressDiscount,
    AddressOrderAttribute,
    AddressShippingLinesOverride,
)


class AddressCreateBodyOptional(TypedDict, total=False):
    company: str
    discounts: list[AddressDiscount]
    order_attributes: list[AddressOrderAttribute]
    order_note: str
    payment_method_id: int
    presentment_currency: str
    shipping_lines_override: list[AddressShippingLinesOverride]


class AddressCreateBody(AddressCreateBodyOptional):
    customer_id: str
    address1: str
    address2: str
    city: str
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class AddressUpdateBody(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country_code: str
    discounts: list[AddressDiscount]
    first_name: str
    last_name: str
    order_attributes: list[AddressOrderAttribute]
    order_note: str
    payment_method_id: int
    phone: str
    province: str
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: str


class AddressListQuery(TypedDict, total=False):
    created_at_max: str
    created_at_min: str
    customer_id: str
    discount_code: str
    discount_id: str
    ids: str
    limit: str
    page: str
    updated_at_max: str
    updated_at_min: str
    is_active: bool


class AddressMergeTargetAddress(TypedDict):
    id: str


class AddressMergeBodyOptional(TypedDict, total=False):
    delete_source_address: bool
    next_charge_date: str


class AddressMergeBody(AddressMergeBodyOptional):
    target_address: AddressMergeTargetAddress
    source_addresses: list[str]


class AddressSkipBody(TypedDict):
    date: str
    subscription_ids: list[str]


class AddressResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/addresses
    """

    object_list_key = "addresses"
    object_dict_key = "address"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: AddressCreateBody) -> Address:
        """Create an address for the customer.
        https://developer.rechargepayments.com/2021-11/addresses/create_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def get(self, address_id: str) -> Address:
        """Get an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/retrieve_address
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}/:address_id", required_scopes)

        url = f"{self._url}/{address_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def update(self, address_id: str, body: AddressUpdateBody) -> Address:
        """Update an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/update_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"PUT /{self.object_list_key}/:address_id", required_scopes)

        url = f"{self._url}/{address_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def delete(self, address_id: str) -> dict:
        """Delete an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/delete_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:address_id", required_scopes
        )

        url = f"{self._url}/{address_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[AddressListQuery] = None) -> list[Address]:
        """List addresses for a customer.
        https://developer.rechargepayments.com/2021-11/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Address(**address) for address in data]

    def list_all(self, query: Optional[AddressListQuery] = None) -> list[Address]:
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-11/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Address(**address) for address in data]

    def merge(self, body: AddressMergeBody) -> Address:
        """Merge two addresses.
        https://developer.rechargepayments.com/2021-11/addresses/merge
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"POST /{self.object_list_key}/merge", required_scopes)

        url = f"{self.base_url}/merge"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def skip(self, address_id: str, body: AddressSkipBody) -> Address:
        """Skip an address.
        https://developer.rechargepayments.com/2021-11/addresses/skip_future_charge
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"POST /{self.object_list_key}/skip", required_scopes)

        url = f"{self.base_url}/{address_id}/charges/skip"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)
