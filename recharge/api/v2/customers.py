from typing import Literal, Required, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class CustomerCreateExternalCustomerId(TypedDict, total=False):
    ecommerce: str


class CustomerCreateBody(TypedDict, total=False):
    email: Required[str]
    external_customer_id: CustomerCreateExternalCustomerId
    first_name: Required[str]
    last_name: Required[str]
    phone: str
    tax_exempt: bool


class CustomerUpdateBody(TypedDict, total=False):
    apply_credit_to_next_recurring_charge: bool
    email: str
    external_customer_id: CustomerCreateExternalCustomerId
    first_name: str
    last_name: str
    phone: str
    tax_exempt: bool


CustomerStatus: TypeAlias = Literal["ACTIVE", "INACTIVE"]


class CustomerListQuery(TypedDict, total=False):
    email: str
    created_at_max: str
    created_at_min: str
    hash: str
    ids: str
    limit: str
    page: str
    external_customer_id: str
    updated_at_max: str
    updated_at_min: str


class CustomerGetDeliveryScheduleQuery(TypedDict, total=False):
    delivery_count_future: int
    future_interval: int
    date_max: str


class CustomerResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/customers
    """

    object_list_key = "customers"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: CustomerCreateBody):
        """Create a customer.
        https://developer.rechargepayments.com/2021-11/customers/customers_create
        """
        required_scopes: list[RechargeScope] = [
            "write_customers",
            "write_payment_methods",
        ]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, customer_id: str):
        """Get a customer by ID.
        https://developer.rechargepayments.com/2021-11/customers/customers_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}/:customer_id", required_scopes)

        return self._http_get(f"{self.url}/{customer_id}")

    def update(self, customer_id: str, body: CustomerUpdateBody):
        """Update a customer.
        https://developer.rechargepayments.com/2021-11/customers/customers_update
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(f"PUT /{self.object_list_key}/:customer_id", required_scopes)

        return self._http_put(f"{self.url}/{customer_id}", body)

    def delete(self, customer_id: str):
        """Delete a customer.
        https://developer.rechargepayments.com/2021-11/customers/customers_delete
        """
        required_scopes: list[RechargeScope] = ["write_customers"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:customer_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{customer_id}")

    def list(self, query: CustomerListQuery | None = None):
        """List customers.
        https://developer.rechargepayments.com/2021-11/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def get_delivery_schedule(
        self, customer_id: str, query: CustomerGetDeliveryScheduleQuery | None = None
    ):
        """Get a customer's delivery schedule.
        https://developer.rechargepayments.com/2021-11/customers/customer_delivery_schedule
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:customer_id/delivery_schedule",
            required_scopes,
        )

        return self._http_get(f"{self.url}/{customer_id}/delivery_schedule", query)

    def get_credit_summary(self, customer_id: str):
        """Get a customer's credit summary.
        https://developer.rechargepayments.com/2021-11/customers/customer_credit_summary
        """
        required_scopes: list[RechargeScope] = ["read_credit_summary"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:customer_id/credit_summary", required_scopes
        )

        return self._http_get(f"{self.url}/{customer_id}/credit_summary")
