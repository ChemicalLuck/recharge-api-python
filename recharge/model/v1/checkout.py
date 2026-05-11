from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict

CheckoutExternalCheckoutSource = Literal["big_commerce", "headless", "shopify"]

CheckoutOrderIntervalUnit = Literal["day", "week", "month"]

CheckoutLineItemType = Literal["SUBSCRIPTION", "ONETIME"]

CheckoutPaymentProcessor = Literal["stripe", "braintree", "mollie", "authorize"]

CheckoutPaymentType = Literal["CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"]


class CheckoutUtmParams(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class CheckoutAnalyticsData(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_params: Optional[list[CheckoutUtmParams]] = None


class CheckoutBillingAddress(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    zip: Optional[str] = None


class CheckoutLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class CheckoutLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    charge_interval_frequency: Optional[int] = None
    cutoff_day_of_month: Optional[int] = None
    cutoff_day_of_week: Optional[int] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    first_recurring_charge_delay: Optional[int] = None
    fulfillment_service: Optional[str] = None
    grams: Optional[int] = None
    image: Optional[str] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: Optional[int] = None
    order_interval_unit: Optional[CheckoutOrderIntervalUnit] = None
    original_price: Optional[str] = None
    price: Optional[str] = None
    product_id: Optional[int] = None
    product_type: Optional[str] = None
    properties: list[CheckoutLineItemProperty] = []
    quantity: Optional[int] = None
    requires_shipping: Optional[bool] = None
    sku: Optional[str] = None
    tax_code: Optional[str] = None
    taxable: Optional[bool] = None
    title: Optional[str] = None
    type: Optional[CheckoutLineItemType] = None
    variant_id: Optional[int] = None
    variant_title: Optional[str] = None


class CheckoutNoteAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class CheckoutShippingAddress(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    company: Optional[str] = None
    country: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    zip: Optional[str] = None


class Checkout(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    analytics_data: Optional[CheckoutAnalyticsData] = None
    billing_address: Optional[CheckoutBillingAddress] = None
    buyer_accepts_marketing: Optional[bool] = None
    currency: Optional[str] = None
    discount_code: Optional[str] = None
    email: Optional[str] = None
    external_checkout_id: Optional[str] = None
    external_checkout_source: Optional[CheckoutExternalCheckoutSource] = None
    external_checkout_customer_id: Optional[str] = None
    line_items: list[CheckoutLineItem] = []
    note: Optional[str] = None
    note_attributes: list[CheckoutNoteAttribute] = []
    phone: Optional[str] = None
    shipping_address: Optional[CheckoutShippingAddress] = None


class CheckoutCharge(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_processor: CheckoutPaymentProcessor
    payment_token: str
    payment_type: CheckoutPaymentType


class CheckoutDetails(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    subtotal_price: Optional[str] = None
    total_price: Optional[str] = None
    total_tax: Optional[str] = None


class CheckoutShippingRate(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    checkout: Optional[CheckoutDetails] = None
    code: str
    delivery_range: Optional[str] = None
    description: Optional[str] = None
    handle: str
    name: str
    phone_required: Optional[bool] = None
    price: str
    tax_lines: list[Any] = []
    title: str
