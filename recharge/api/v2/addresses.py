from typing import TypedDict, Optional

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class AddressOrderAttributes(TypedDict):
    name: str
    value: str


class AddressShippingLinesOverride(TypedDict, total=False):
    code: str
    price: str
    title: str


class AddressDiscounts(TypedDict):
    id: str


class AddressCreateBodyOptional(TypedDict, total=False):
    company: str
    discounts: list[AddressDiscounts]
    order_attributes: list[AddressOrderAttributes]
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
    recharge_version: RechargeVersion = "2021-11"

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

    def update(self, address_id: str, body: AddressUpdateBody):
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

    def list_(self, query: Optional[AddressListQuery] = None):
        """List all addresses for a customer.
        https://developer.rechargepayments.com/2021-11/addresses/list_addresses
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def merge(self, body: AddressMergeBody):
        """Merge two addresses.
        https://developer.rechargepayments.com/2021-11/addresses/merge
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"POST /{self.object_list_key}/merge", required_scopes)

        return self._http_post(f"{self.base_url}/merge", body)

    def skip(self, address_id: str, body: AddressSkipBody):
        """Skip an address.
        https://developer.rechargepayments.com/2021-11/addresses/skip_future_charge
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"POST /{self.object_list_key}/skip", required_scopes)

        return self._http_post(f"{self.base_url}/{address_id}/charges/skip", body)
