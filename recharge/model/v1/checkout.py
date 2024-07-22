from typing import Literal, TypedDict


class CheckoutUtmParams(TypedDict, total=False):
    utm_campaign: str
    utm_content: str
    utm_data_source: str
    utm_source: str
    utm_medium: str
    utm_term: str
    utm_timestamp: str


class CheckoutAnalyticsData(TypedDict, total=False):
    utm_params: list[CheckoutUtmParams]


class CheckoutBillingAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


CheckoutExternalCheckoutSource = Literal["big_commerce", "headless", "shopify"]

CheckoutOrderIntervalUnit = Literal["day", "week", "month"]


class CheckoutLineItemProperty(TypedDict):
    name: str
    value: str


CheckoutLineItemType = Literal["SUBSCRIPTION", "ONETIME"]


class CheckoutLineItem(TypedDict, total=False):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    expire_after_specific_number_of_charges: int
    first_recurring_charge_delay: int
    fulfillment_service: str
    grams: int
    image: str
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: int
    order_interval_unit: CheckoutOrderIntervalUnit
    original_price: str
    price: str
    product_id: int
    product_type: str
    properties: list[CheckoutLineItemProperty]
    quantity: int
    requires_shipping: bool
    sku: str
    tax_code: str
    taxable: bool
    title: str
    type: CheckoutLineItemType
    variant_id: int
    variant_title: str


class CheckoutNoteAttribute(TypedDict):
    name: str
    value: str


class CheckoutShippingAddress(TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class Checkout(TypedDict):
    analytics_data: CheckoutAnalyticsData
    billing_address: CheckoutBillingAddress
    buyer_accepts_marketing: bool
    currency: str
    discount_code: str
    email: str
    external_checkout_id: str
    external_checkout_source: CheckoutExternalCheckoutSource
    external_checkout_customer_id: str
    line_items: list[CheckoutLineItem]
    note: str
    note_attributes: list[CheckoutNoteAttribute]
    phone: str
    shipping_address: CheckoutShippingAddress


CheckoutPaymentProcessor = Literal["stripe", "braintree", "mollie", "authorize"]

CheckoutPaymentType = Literal["CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"]


class CheckoutCharge(TypedDict):
    payment_processor: CheckoutPaymentProcessor
    payment_token: str
    payment_type: CheckoutPaymentType


class CheckoutDetails(TypedDict):
    subtotal_price: str
    total_price: str
    total_tax: str


class CheckoutShippingRate(TypedDict):
    checkout: CheckoutDetails
    code: str
    delivery_range: str
    description: str
    handle: str
    name: str
    phone_required: bool
    price: str
    tax_lines: list
    title: str
