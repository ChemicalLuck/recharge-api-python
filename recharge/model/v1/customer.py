from typing import Literal, TypedDict

CustomerStatus = Literal["ACTIVE", "INACTIVE"]


class Customer(TypedDict):
    id: int
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
    created_at: str
    email: str
    first_charge_processed_at: str
    first_name: str
    has_card_error_in_dunning: bool
    has_valid_payment_method: bool
    hash: str
    last_name: str
    number_active_subscriptions: int
    number_subscriptions: int
    phone: str
    processor_type: str
    reason_payment_method_not_valid: str
    shopify_customer_id: str
    status: CustomerStatus
    updated_at: str
