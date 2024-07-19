from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.payment_method import (
    PaymentMethod,
    PaymentMethodBillingAddress,
    PaymentMethodProcessorName,
    PaymentMethodType,
)


class PaymentMethodCreateBodyOptional(TypedDict, total=False):
    default: bool
    processor_payment_method_token: str
    billing_address: PaymentMethodBillingAddress
    retry_charges: bool


class PaymentMethodCreateBody(PaymentMethodCreateBodyOptional):
    customer_id: int
    payment_type: PaymentMethodType
    processor_customer_token: str
    processor_name: PaymentMethodProcessorName


class PaymentMethodUpdateBody(TypedDict, total=False):
    default: bool
    processor_name: PaymentMethodProcessorName
    billing_address: PaymentMethodBillingAddress


class PaymentMethodListQuery(TypedDict, total=False):
    customer_id: int


class PaymentMethodResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/payment_methods
    """

    object_list_key = "payment_methods"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: PaymentMethodCreateBody) -> PaymentMethod:
        """Create a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_create
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return PaymentMethod(**data)

    def get(self, payment_method_id: int) -> PaymentMethod:
        """Get a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_get
        """
        required_scopes: list[RechargeScope] = ["read_payment_methods"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:payment_method_id", required_scopes
        )

        url = f"{self._url}/{payment_method_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return PaymentMethod(**data)

    def update(
        self, payment_method_id: int, body: PaymentMethodUpdateBody
    ) -> PaymentMethod:
        """Update a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_update
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:payment_method_id", required_scopes
        )

        url = f"{self._url}/{payment_method_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return PaymentMethod(**data)

    def delete(self, payment_method_id: int) -> dict:
        """Delete a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_delete
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:payment_method_id", required_scopes
        )

        url = f"{self._url}/{payment_method_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(
        self, query: Optional[PaymentMethodListQuery] = None
    ) -> list[PaymentMethod]:
        """List payment methods.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_list
        """
        required_scopes: list[RechargeScope] = ["read_payment_methods"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [PaymentMethod(**item) for item in data]

    def list_all(
        self, query: Optional[PaymentMethodListQuery] = None
    ) -> list[PaymentMethod]:
        """List all payment methods.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_list
        """
        required_scopes: list[RechargeScope] = ["read_payment_methods"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [PaymentMethod(**item) for item in data]
