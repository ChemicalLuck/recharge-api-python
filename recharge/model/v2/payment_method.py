from typing import Literal, Optional, TypedDict

PaymentMethodType = Literal[
    "CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY", "SEPA_DEBIT"
]

PaymentMethodProcessorName = Literal[
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


class PaymentMethodDetails(TypedDict):
    brand: str
    exp_month: str
    exp_year: str
    last4: str
    paypal_email: Optional[str]
    paypal_payer_id: Optional[str]
    wallet_type: Optional[str]
    funding_type: Optional[str]


PaymentMethodStatus = Literal["unvalidated", "valid", "invalid", "empty"]


class PaymentMethod(TypedDict):
    id: int
    customer_id: int
    created_at: str
    default: bool
    payment_details: PaymentMethodDetails
    payment_type: PaymentMethodType
    processor_customer_token: str
    processor_name: PaymentMethodProcessorName
    processor_payment_method_token: str
    status: PaymentMethodStatus
    status_reason: str
    updated_at: str
