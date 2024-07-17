from typing import TypedDict, Optional, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class AddressNoteAttributes(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict, total=False):
    code: str
    price: str
    title: str


class AddressCreateBodyOptional(TypedDict, total=False):
    address2: str
    cart_note: str
    company: str
    note_attributes: list[AddressNoteAttributes]
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
    note_attributes: list[AddressNoteAttributes]
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
    recharge_version: RechargeVersion = "2021-01"

    def create(self, customer_id: str, body: AddressCreateBody):
        """Create an address for the customer.
        https://developer.rechargepayments.com/2021-01/addresses/create_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(
            f"POST /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        return self._http_post(url, body)

    def get(self, address_id: str):
        """Get an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/retrieve_address
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/:address_id", required_scopes)

        return self._http_get(f"{self.url}/{address_id}")

    def update(self, address_id: str, body: Optional[AddressUpdateBody] = None):
        """Update an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/update_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"PUT /{self.object_list_key}/:id", required_scopes)

        return self._http_put(f"{self.url}/{address_id}", body)

    def delete(self, address_id: str):
        """Delete an address by ID.
        https://developer.rechargepayments.com/2021-01/addresses/delete_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:address_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{address_id}")

    def list_(self, customer_id: str, query: Optional[AddressListQuery] = None):
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-01/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(
            f"GET /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        return self._http_get(
            f"{self.base_url}/customers/{customer_id}/{self.object_list_key}", query
        )

    def count(self, query: Optional[AddressCountQuery] = None):
        """Retrieve the count of addresses.
        https://developer.rechargepayments.com/2021-01/addresses/count_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)

    def validate(self, body: AddressValidateBody):
        """Validate an address.
        https://developer.rechargepayments.com/2021-01/addresses/validate_address
        """

        return self._http_post(f"{self.url}/validate_address", body)

    def apply_discount(
        self,
        address_id: str,
        body: AddressApplyDiscountBody,
    ):
        """Apply a discount code to an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_apply_address
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:address_id/apply_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{address_id}/apply_discount", body)

    def remove_discount(self, address_id: str):
        """Remove a discount from an address.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_remove_from_address_or_charge
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:address_id/remove_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{address_id}/remove_discount")
