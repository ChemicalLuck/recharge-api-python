from typing import Any, Literal, Optional

from pydantic import field_validator

from recharge.model.base import RechargeModel

PaymentMethodType = Literal[
    "CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY", "SEPA_DEBIT"
]

PaymentMethodProcessorName = Literal[
    "stripe", "braintree", "authorize", "shopify_payments", "mollie"
]


class PaymentMethodBillingAddress(RechargeModel):
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    zip: Optional[str] = None


class PaymentMethodDetails(RechargeModel):
    brand: Optional[str] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    last4: Optional[str] = None
    paypal_email: Optional[str] = None
    paypal_payer_id: Optional[str] = None
    wallet_type: Optional[str] = None
    funding_type: Optional[str] = None


PaymentMethodStatus = Literal["unvalidated", "valid", "invalid", "empty"]


class PaymentMethod(RechargeModel):
    @field_validator("payment_type", mode="before")
    @classmethod
    def uppercase_payment_type(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.upper()
        return v

    id: int
    customer_id: int
    billing_address: Optional[PaymentMethodBillingAddress] = None
    created_at: str
    default: bool
    payment_details: Optional[PaymentMethodDetails] = None
    payment_type: PaymentMethodType
    processor_customer_token: str
    processor_name: PaymentMethodProcessorName
    processor_payment_method_token: Optional[str] = None
    status: PaymentMethodStatus
    status_reason: Optional[str] = None
    updated_at: str
