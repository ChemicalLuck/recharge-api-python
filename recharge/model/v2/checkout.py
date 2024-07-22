from typing import Literal, Optional, TypedDict


class CheckoutExternalCustomerId(TypedDict):
    ecommerce: str


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


class CheckoutBillingAddress(TypedDict):
    address1: str
    address2: str
    city: str
    company: Optional[str]
    country_code: str
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


class CheckoutLineItemExternalProductId(TypedDict, total=False):
    ecommerce: str


class CheckoutLineItemExternalVariantId(TypedDict):
    ecommerce: str


class CheckoutLineItemImages(TypedDict, total=False):
    large: str
    medium: str
    small: str
    original: str


CheckoutLineItemPurchaseItemType = Literal["subscription", "onetime"]


class CheckoutLineItemSubscriptionPreferences(TypedDict):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    expire_after_specific_number_of_charges: int
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency: int
    interval_unit: CheckoutOrderIntervalUnit


class CheckoutLineItem(TypedDict, total=False):
    external_product_id: CheckoutLineItemExternalProductId
    external_variant_id: CheckoutLineItemExternalVariantId
    handle: str
    images: CheckoutLineItemImages
    properties: list[CheckoutLineItemProperty]
    purchase_item_type: CheckoutLineItemPurchaseItemType
    quantity: int
    sku: str
    subscription_preferences: CheckoutLineItemSubscriptionPreferences
    title: str
    unit_price: str
    variant_title: str
    weight: int


class CheckoutOrderAttribute(TypedDict):
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


CheckoutDiscountValueType = Literal["fixed_amount", "percentage"]


class CheckoutAppliedDiscount(TypedDict):
    amount: str
    applicable: bool
    discount_code: str
    non_redeemable_reason: Optional[str]
    value: str
    value_type: CheckoutDiscountValueType


class CheckoutDetails(TypedDict):
    subtotal_price: Optional[str]
    total_price: Optional[str]
    total_tax: Optional[str]


class CheckoutShippingRate(TypedDict):
    checkout: CheckoutDetails
    code: str
    delivery_range: Optional[str]
    description: Optional[str]
    handle: str
    name: str
    phone_required: Optional[str]
    price: str
    title: str


class CheckoutCustomShippingRateOption(TypedDict):
    code: str
    price: str
    title: str
    handle: str


class CheckoutExternalTransactionId(TypedDict):
    payment_processor: str


class CheckoutAppliedShippingLine(TypedDict):
    code: str
    price: str
    source: str
    title: str
    taxable: bool


class CheckoutShippingLine(TypedDict):
    address1: str
    address2: Optional[str]
    city: str
    company: str
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class CheckoutTaxLine(TypedDict):
    price: str
    rate: str
    title: str


CheckoutNotificationPreferencesConsentSource = Literal[
    "sms_reminder",
    "store_opt_in_widget",
    "replenishment_checkout",
    "script",
    "rechargesms_app",
    "customer_sms",
    "subscription_checkout_extension",
    "recharge_checkout",
    "sci_cart",
]

CheckoutNotificationPreferencesConsentStatus = Literal[
    "unspecified", "accepted", "declined"
]


class CheckoutNotificationPreferencesConsentDetail(TypedDict):
    last_opt_in_at: Optional[str]
    last_opt_in_source: CheckoutNotificationPreferencesConsentSource
    last_opt_out_at: Optional[str]
    last_opt_out_source: CheckoutNotificationPreferencesConsentSource
    status: CheckoutNotificationPreferencesConsentStatus


class CheckoutNotificationPreferencesDetail(TypedDict):
    promotional: CheckoutNotificationPreferencesConsentDetail
    replenishment: CheckoutNotificationPreferencesConsentDetail
    transactional: CheckoutNotificationPreferencesConsentDetail


class CheckoutNotificationPreferences(TypedDict):
    email: CheckoutNotificationPreferencesDetail
    sms: CheckoutNotificationPreferencesDetail


class Checkout(TypedDict):
    charge_id: Optional[int]
    analytics_data: CheckoutAnalyticsData
    applied_discounts: list[CheckoutAppliedDiscount]
    applied_shipping_rate: CheckoutShippingRate
    available_shipping_rates: list[CheckoutShippingRate]
    billing_address: CheckoutBillingAddress
    completed_at: str
    created_at: str
    currency: str
    email: str
    external_checkout_id: str
    external_checkout_source: CheckoutExternalCheckoutSource
    external_customer_id: CheckoutExternalCustomerId
    external_transaction_id: CheckoutExternalTransactionId
    line_items: list[CheckoutLineItem]
    note: str
    notification_preferences: CheckoutNotificationPreferences
    order_attributes: list[CheckoutOrderAttribute]
    payment_processor: str
    requires_shipping: bool
    shipping_address: CheckoutShippingAddress
    shipping_lines: list[CheckoutShippingLine]
    subtotal_price: str
    tax_lines: list[CheckoutTaxLine]
    taxable: bool
    taxes_included: bool
    token: str
    total_price: str
    total_tax: str
    updated_at: str


CheckoutPaymentProcessor = Literal["stripe", "braintree", "mollie", "authorize"]

CheckoutPaymentType = Literal["CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"]


class CheckoutCharge(TypedDict):
    autorization_token: Optional[str]
    charge_id: int
    free: bool
    payment_processor: CheckoutPaymentProcessor
    processor_customer_token: str
    processor_payment_method_token: str
    payment_processor_transaction_id: str
    payment_token: str
    payment_type: CheckoutPaymentType
    status: str
