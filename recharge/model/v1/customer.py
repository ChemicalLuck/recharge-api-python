from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

CustomerStatus = Literal["ACTIVE", "INACTIVE"]


class Customer(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    accepts_marketing: Optional[bool] = None
    billing_address1: Optional[str] = None
    billing_address2: Optional[str] = None
    billing_city: Optional[str] = None
    billing_company: Optional[str] = None
    billing_country: Optional[str] = None
    billing_first_name: Optional[str] = None
    billing_last_name: Optional[str] = None
    billing_phone: Optional[str] = None
    billing_province: Optional[str] = None
    billing_zip: Optional[str] = None
    created_at: Optional[str] = None
    email: Optional[str] = None
    first_charge_processed_at: Optional[str] = None
    first_name: Optional[str] = None
    has_card_error_in_dunning: Optional[bool] = None
    has_valid_payment_method: Optional[bool] = None
    hash: Optional[str] = None
    last_name: Optional[str] = None
    number_active_subscriptions: Optional[int] = None
    number_subscriptions: Optional[int] = None
    phone: Optional[str] = None
    processor_type: Optional[str] = None
    reason_payment_method_not_valid: Optional[str] = None
    shopify_customer_id: Optional[str] = None
    status: Optional[CustomerStatus] = None
    updated_at: Optional[str] = None
