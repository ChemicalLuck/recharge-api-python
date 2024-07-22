from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.customer import Customer, CustomerStatus


class CustomerCreateBodyOptional(TypedDict, total=False):
    accepts_marketing: bool
    billing_address2: str
    billing_company: str
    billing_phone: str
    phone: str
    processor_type: str
    shopify_customer_id: str


class CustomerCreateBody(CustomerCreateBodyOptional):
    billing_address1: str
    billing_city: str
    billing_country: str
    billing_first_name: str
    billing_last_name: str
    billing_province: str
    billing_zip: str
    email: str
    first_name: str
    last_name: str


class CustomerUpdateBody(TypedDict, total=False):
    accepts_marketing: bool
    billing_address1: str
    billing_address2: str
    billing_city: str
    billing_company: str
    billing_country: str
    billing_first_name: str
    billing_last_name: str
    billing_phone: str
    billing_province: str
    billing_zip: str
    email: str
    first_name: str
    last_name: str
    phone: str
    shopify_customer_id: str


class CustomerListQuery(TypedDict, total=False):
    email: str
    created_at_max: str
    created_at_min: str
    hash: str
    ids: str
    limit: str
    page: str
    shopify_customer_id: str
    status: CustomerStatus
    updated_at_max: str
    updated_at_min: str


class CustomerCountQuery(TypedDict, total=False):
    created_at_max: str
    created_at_min: str
    status: CustomerStatus
    updated_at_max: str
    updated_at_min: str


class CustomerResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/customers
    """

    object_list_key = "customers"
    object_dict_key = "customer"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: CustomerCreateBody) -> Customer:
        """Create a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_create
        """
        required_scopes: list[RechargeScope] = ["write_customers", "write_payments"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Customer(**data)

    def get(self, customer_id: str) -> Customer:
        """Get a customer by ID.
        https://developer.rechargepayments.com/2021-01/customers/customers_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}/:customer_id", required_scopes)

        url = f"{self._url}/{customer_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Customer(**data)

    def update(self, customer_id: str, body: CustomerUpdateBody) -> Customer:
        """Update a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_update
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(f"PUT /{self.object_list_key}/:customer_id", required_scopes)

        url = f"{self._url}/{customer_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Customer(**data)

    def delete(self, customer_id: str) -> dict:
        """Delete a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_delete
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:customer_id", required_scopes
        )

        url = f"{self._url}/{customer_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[CustomerListQuery] = None) -> list[Customer]:
        """List customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        print(query)
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Customer(**item) for item in data]

    def list_all(self, query: Optional[CustomerListQuery] = None) -> list[Customer]:
        """List all customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Customer(**item) for item in data]

    def count(self, query: Optional[CustomerCountQuery] = None) -> int:
        """Retrieve a count of customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_count
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
