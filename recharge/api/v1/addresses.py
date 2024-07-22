from typing import Optional, TypedDict, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.address import (
    Address,
    AddressNoteAttribute,
    AddressShippingLinesOverride,
)


class AddressCreateBodyOptional(TypedDict, total=False):
    address2: str
    cart_note: str
    company: str
    note_attributes: list[AddressNoteAttribute]
    presentment_currency: str
    shipping_lines_override: list[AddressShippingLinesOverride]


class AddressCreateBody(AddressCreateBodyOptional):
    address1: str
    city: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class AddressUpdateBody(TypedDict, total=False):
    address1: str
    address2: str
    cart_note: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    note_attributes: list[AddressNoteAttribute]
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
    limit: int
    page: int
    updated_at_max: str
    updated_at_min: str


class AddressCountQuery(TypedDict, total=False):
    created_at_max: str
    created_at_min: str
    discount_code: str
    discount_id: str
    updated_at_max: str
    updated_at_min: str


class AddressValidateBody(TypedDict, total=False):
    address1: str
    city: str
    state: str
    zipcode: str


class AddressValidateResponse(TypedDict):
    city: str
    errors: dict
    state: str
    state_name: str
    zipcode: str


class AddressApplyDiscountCodeBody(TypedDict):
    discount_code: str


class AddressApplyDiscountIdBody(TypedDict):
    discount_id: str


AddressApplyDiscountBody = Union[
    AddressApplyDiscountCodeBody, AddressApplyDiscountIdBody
]

AddressRemoveDiscountBody = AddressApplyDiscountBody


class AddressResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/addresses
    """

    object_list_key = "addresses"
    object_dict_key = "address"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, customer_id: str, body: AddressCreateBody) -> Address:
        """Create an address for the customer.
        https://developer.rechargepayments.com/2021-01/addresses/create_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(
            f"POST /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def get(self, address_id: str) -> Address:
        """Get an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/retrieve_address
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}/:address_id", required_scopes)

        url = f"{self._url}/{address_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def update(
        self, address_id: str, body: Optional[AddressUpdateBody] = None
    ) -> Address:
        """Update an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/update_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"PUT /{self.object_list_key}/:id", required_scopes)

        url = f"{self._url}/{address_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def delete(self, address_id: str) -> dict:
        """Delete an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/delete_address
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

    def list_(
        self, customer_id: str, query: Optional[AddressListQuery] = None
    ) -> list[Address]:
        """List addresses for a customer.
        https://developer.rechargepayments.com/2021-01/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(
            f"GET /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        data = self._http_get(url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Address(**item) for item in data]

    def list_all(
        self, customer_id: str, query: Optional[AddressListQuery] = None
    ) -> list[Address]:
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-01/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(
            f"GET /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        data = self._paginate(url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Address(**item) for item in data]

    def count(self, query: Optional[AddressCountQuery] = None) -> int:
        """Retrieve the count of addresses.
        https://developer.rechargepayments.com/2021-01/addresses/count_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected key 'count' in response, got {data}")
        return data["count"]

    def validate(self, body: AddressValidateBody) -> AddressValidateResponse:
        """Validate an address.
        https://developer.rechargepayments.com/2021-01/addresses/validate_address
        """

        url = f"{self._url}/validate_address"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return AddressValidateResponse(**data)

    def apply_discount(
        self,
        address_id: str,
        body: AddressApplyDiscountBody,
    ) -> Address:
        """Apply a discount code to an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_apply_address
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:address_id/apply_discount", required_scopes
        )

        url = f"{self._url}/{address_id}/apply_discount"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)

    def remove_discount(self, address_id: str) -> Address:
        """Remove a discount from an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_remove_from_address_or_charge
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:address_id/remove_discount", required_scopes
        )

        url = f"{self._url}/{address_id}/remove_discount"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Address(**data)
