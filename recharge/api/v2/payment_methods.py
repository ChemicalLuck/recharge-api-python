from typing import TypeAlias, TypedDict, Literal, Required
from recharge.api import RechargeResource, RechargeScope

PaymentMethodType: TypeAlias = Literal[
    "CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY", "SEPA_DEBIT"
]

PaymentMethodProcessorName: TypeAlias = Literal[
    "stripe", "braintree", "authorize", "shopify_payments", "mollie"
]


class PaymentMethodBillingAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class PaymentMethodCreateBody(TypedDict, total=False):
    customer_id: Required[int]
    default: bool
    payment_type: Required[PaymentMethodType]
    processor_customer_token: Required[str]
    processor_name: Required[PaymentMethodProcessorName]
    processor_payment_method_token: str
    billing_address: PaymentMethodBillingAddress
    retry_charges: bool


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

    def create(self, body: PaymentMethodCreateBody):
        """Create a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_create
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, payment_method_id: int):
        """Get a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_get
        """
        required_scopes: list[RechargeScope] = ["read_payment_methods"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:payment_method_id", required_scopes
        )

        return self._http_get(f"/{self.url}/{payment_method_id}")

    def update(self, payment_method_id: int, body: PaymentMethodUpdateBody):
        """Update a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_update
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:payment_method_id", required_scopes
        )

        return self._http_put(f"{self.url}/{payment_method_id}", body)

    def delete(self, payment_method_id: int):
        """Delete a payment method.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_delete
        """
        required_scopes: list[RechargeScope] = ["write_payment_methods"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:payment_method_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{payment_method_id}")

    def list(self, query: PaymentMethodListQuery | None = None):
        """List payment methods.
        https://developer.rechargepayments.com/2021-11/payment_methods/payment_methods_list
        """
        required_scopes: list[RechargeScope] = ["read_payment_methods"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
