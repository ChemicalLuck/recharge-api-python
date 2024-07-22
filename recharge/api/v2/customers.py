from typing import Literal, Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.customer import (
    Customer,
    CustomerCreditSummary,
    CustomerDeliverySchedule,
)


class CustomerCreateExternalCustomerId(TypedDict, total=False):
    ecommerce: str


class CustomerCreateBodyOptional(TypedDict, total=False):
    external_customer_id: CustomerCreateExternalCustomerId
    phone: str
    tax_exempt: bool


class CustomerCreateBody(CustomerCreateBodyOptional):
    email: str
    first_name: str
    last_name: str


class CustomerUpdateBody(TypedDict, total=False):
    apply_credit_to_next_recurring_charge: bool
    email: str
    external_customer_id: CustomerCreateExternalCustomerId
    first_name: str
    last_name: str
    phone: str
    tax_exempt: bool


CustomerStatus = Literal["ACTIVE", "INACTIVE"]


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
    object_dict_key = "customer"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: CustomerCreateBody) -> Customer:
        """Create a customer.
        https://developer.rechargepayments.com/2021-11/customers/customers_create
        """
        required_scopes: list[RechargeScope] = [
            "write_customers",
            "write_payment_methods",
        ]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Customer(**data)

    def get(self, customer_id: str) -> Customer:
        """Get a customer by ID.
        https://developer.rechargepayments.com/2021-11/customers/customers_retrieve
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
        https://developer.rechargepayments.com/2021-11/customers/customers_update
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
        https://developer.rechargepayments.com/2021-11/customers/customers_delete
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
        https://developer.rechargepayments.com/2021-11/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Customer(**item) for item in data]

    def list_all(self, query: Optional[CustomerListQuery] = None) -> list[Customer]:
        """List all customers.
        https://developer.rechargepayments.com/2021-11/customers/customers_list
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Customer(**item) for item in data]

    def get_delivery_schedule(
        self, customer_id: str, query: Optional[CustomerGetDeliveryScheduleQuery] = None
    ) -> CustomerDeliverySchedule:
        """Get a customer's delivery schedule.
        https://developer.rechargepayments.com/2021-11/customers/customer_delivery_schedule
        """
        required_scopes: list[RechargeScope] = ["read_customers"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:customer_id/delivery_schedule",
            required_scopes,
        )

        url = f"{self._url}/{customer_id}/delivery_schedule"
        data = self._http_get(url, query, response_key="deliverySchedule")
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return CustomerDeliverySchedule(**data)

    def get_credit_summary(self, customer_id: str) -> CustomerCreditSummary:
        """Get a customer's credit summary.
        https://developer.rechargepayments.com/2021-11/customers/customer_credit_summary
        """
        required_scopes: list[RechargeScope] = ["read_credit_summary"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:customer_id/credit_summary", required_scopes
        )

        url = f"{self._url}/{customer_id}/credit_summary"
        data = self._http_get(url, response_key="credit_summary")
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return CustomerCreditSummary(**data)
