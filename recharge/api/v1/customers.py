from typing import Literal, Required, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope


class CustomerCreateBody(TypedDict, total=False):
    accepts_marketing: bool
    billing_address1: Required[str]
    billing_address2: str
    billing_city: Required[str]
    billing_company: str
    billing_country: Required[str]
    billing_first_name: Required[str]
    billing_last_name: Required[str]
    billing_phone: str
    billing_province: Required[str]
    billing_zip: Required[str]
    email: Required[str]
    first_name: Required[str]
    last_name: Required[str]
    phone: str
    processor_type: str
    shopify_customer_id: str


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


CustomerStatus: TypeAlias = Literal["ACTIVE", "INACTIVE"]


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

    def create(self, body: CustomerCreateBody):
        """Create a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_create
        """
        required_scopes: list[RechargeScope] = ["write_customers", "write_payments"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, customer_id: str):
        """Get a customer by ID.
        https://developer.rechargepayments.com/2021-01/customers/customers_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/:customer_id", required_scopes)

        return self._http_get(f"{self.url}/{customer_id}")

    def update(self, customer_id: str, body: CustomerUpdateBody):
        """Update a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_update
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"PUT /{self.object_list_key}/:customer_id", required_scopes)

        return self._http_put(f"{self.url}/{customer_id}", body)

    def delete(self, customer_id: str):
        """Delete a customer.
        https://developer.rechargepayments.com/2021-01/customers/customers_delete
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:customer_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{customer_id}")

    def list(self, query: CustomerListQuery | None = None):
        """List customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def count(self, query: CustomerCountQuery | None = None):
        """Retrieve a count of customers.
        https://developer.rechargepayments.com/2021-01/customers/customers_count
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)
