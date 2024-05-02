from typing import Required, TypedDict

from recharge.api import RechargeResource, RechargeScope


class AddressOrderAttributes(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict, total=False):
    code: str
    price: str
    title: str


class AddressDiscounts(TypedDict):
    id: str


class AddressCreateBody(TypedDict, total=False):
    customer_id: Required[str]
    address1: Required[str]
    address2: Required[str]
    city: Required[str]
    company: str
    country_code: Required[str]
    discounts: list[AddressDiscounts]
    first_name: Required[str]
    last_name: Required[str]
    order_attributes: list[AddressOrderAttributes]
    order_note: str
    payment_method_id: int
    phone: Required[str]
    presentment_currency: str
    province: Required[str]
    shipping_lines_override: list[AddressShippingLinesOverride]
    zip: Required[str]


class AddressUpdateBody(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country_code: str
    discounts: list[AddressDiscounts]
    first_name: str
    last_name: str
    order_attributes: list[AddressOrderAttributes]
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


class AddressMergeBody(TypedDict, total=False):
    delete_source_address: bool
    next_charge_date: str
    target_address: Required[AddressMergeTargetAddress]
    source_addresses: Required[list[str]]


class AddressSkipBody(TypedDict):
    date: str
    subscription_ids: list[str]


class AddressResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/addresses
    """

    object_list_key = "addresses"

    def create(self, body: AddressCreateBody):
        """Create an address for the customer.
        https://developer.rechargepayments.com/2021-11/addresses/create_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, address_id: str):
        """Get an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/retrieve_address
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/:address_id", required_scopes)

        return self._http_get(f"{self.url}/{address_id}")

    def update(self, address_id: str, body: AddressUpdateBody | None = None):
        """Update an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/update_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"PUT /{self.object_list_key}/:address_id", required_scopes)

        return self._http_put(f"{self.url}/{address_id}", body)

    def delete(self, address_id: str):
        """Delete an address by ID.
        https://developer.rechargepayments.com/2021-11/addresses/delete_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:address_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{address_id}")

    def list(self, query: AddressListQuery | None = None):
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-11/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def merge(self, body: AddressMergeBody):
        """Merge two addresses.
        https://developer.rechargepayments.com/2021-11/addresses/merge_addresses
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"POST /{self.object_list_key}/merge", required_scopes)

        return self._http_post(f"{self.base_url}/merge", body)

    def skip(self, address_id: str, body: AddressSkipBody):
        """Skip an address.
        https://developer.rechargepayments.com/2021-11/addresses/skip_address
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"POST /{self.object_list_key}/skip", required_scopes)

        return self._http_post(f"{self.base_url}/{address_id}/charges/skip", body)
