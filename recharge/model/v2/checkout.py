from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict


class CheckoutExternalCustomerId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


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
    country_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    province: Optional[str] = None
    zip: Optional[str] = None


CheckoutExternalCheckoutSource = Literal["big_commerce", "headless", "shopify"]

CheckoutOrderIntervalUnit = Literal["day", "week", "month"]


class CheckoutLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


CheckoutLineItemType = Literal["SUBSCRIPTION", "ONETIME"]


class CheckoutLineItemExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class CheckoutLineItemExternalVariantId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class CheckoutLineItemImages(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    original: Optional[str] = None


CheckoutLineItemPurchaseItemType = Literal["subscription", "onetime"]


class CheckoutLineItemSubscriptionPreferences(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    charge_interval_frequency: int
    cutoff_day_of_month: Optional[int] = None
    cutoff_day_of_week: Optional[int] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency: int
    interval_unit: CheckoutOrderIntervalUnit


class CheckoutLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    external_product_id: Optional[CheckoutLineItemExternalProductId] = None
    external_variant_id: Optional[CheckoutLineItemExternalVariantId] = None
    handle: Optional[str] = None
    images: Optional[CheckoutLineItemImages] = None
    properties: list[CheckoutLineItemProperty] = []
    purchase_item_type: Optional[CheckoutLineItemPurchaseItemType] = None
    quantity: Optional[int] = None
    sku: Optional[str] = None
    subscription_preferences: Optional[CheckoutLineItemSubscriptionPreferences] = None
    title: Optional[str] = None
    unit_price: Optional[str] = None
    variant_title: Optional[str] = None
    weight: Optional[int] = None


class CheckoutOrderAttribute(BaseModel):
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


CheckoutDiscountValueType = Literal["fixed_amount", "percentage"]


class CheckoutAppliedDiscount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    amount: Optional[str] = None
    applicable: Optional[bool] = None
    discount_code: str
    non_redeemable_reason: Optional[str] = None
    value: Optional[str] = None
    value_type: Optional[CheckoutDiscountValueType] = None


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
    phone_required: Optional[str] = None
    price: str
    title: str


class CheckoutCustomShippingRateOption(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str
    price: str
    title: str
    handle: str


class CheckoutExternalTransactionId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    payment_processor: str


class CheckoutAppliedShippingLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: str
    price: str
    source: str
    title: str
    taxable: bool


class CheckoutShippingLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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


class CheckoutTaxLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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


class CheckoutNotificationPreferencesConsentDetail(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    last_opt_in_at: Optional[str] = None
    last_opt_in_source: Optional[CheckoutNotificationPreferencesConsentSource] = None
    last_opt_out_at: Optional[str] = None
    last_opt_out_source: Optional[CheckoutNotificationPreferencesConsentSource] = None
    status: CheckoutNotificationPreferencesConsentStatus


class CheckoutNotificationPreferencesDetail(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    promotional: Optional[CheckoutNotificationPreferencesConsentDetail] = None
    replenishment: Optional[CheckoutNotificationPreferencesConsentDetail] = None
    transactional: Optional[CheckoutNotificationPreferencesConsentDetail] = None


class CheckoutNotificationPreferences(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    email: Optional[CheckoutNotificationPreferencesDetail] = None
    sms: Optional[CheckoutNotificationPreferencesDetail] = None


class Checkout(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    charge_id: Optional[int] = None
    analytics_data: Optional[CheckoutAnalyticsData] = None
    applied_discounts: list[CheckoutAppliedDiscount] = []
    applied_shipping_rate: Optional[CheckoutShippingRate] = None
    available_shipping_rates: list[CheckoutShippingRate] = []
    billing_address: Optional[CheckoutBillingAddress] = None
    completed_at: Optional[str] = None
    created_at: str
    currency: Optional[str] = None
    email: Optional[str] = None
    external_checkout_id: Optional[str] = None
    external_checkout_source: Optional[CheckoutExternalCheckoutSource] = None
    external_customer_id: Optional[CheckoutExternalCustomerId] = None
    external_transaction_id: Optional[CheckoutExternalTransactionId] = None
    line_items: list[CheckoutLineItem] = []
    note: Optional[str] = None
    notification_preferences: Optional[CheckoutNotificationPreferences] = None
    order_attributes: list[CheckoutOrderAttribute] = []
    payment_processor: Optional[str] = None
    requires_shipping: Optional[bool] = None
    shipping_address: Optional[CheckoutShippingAddress] = None
    shipping_lines: list[CheckoutShippingLine] = []
    subtotal_price: Optional[str] = None
    tax_lines: list[CheckoutTaxLine] = []
    taxable: Optional[bool] = None
    taxes_included: Optional[bool] = None
    token: str
    total_price: Optional[str] = None
    total_tax: Optional[str] = None
    updated_at: str


CheckoutPaymentProcessor = Literal["stripe", "braintree", "mollie", "authorize"]

CheckoutPaymentType = Literal["CREDIT_CARD", "PAYPAL", "APPLE_PAY", "GOOGLE_PAY"]


class CheckoutCharge(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    autorization_token: Optional[str] = None
    charge_id: int
    free: bool
    payment_processor: CheckoutPaymentProcessor
    processor_customer_token: str
    processor_payment_method_token: str
    payment_processor_transaction_id: str
    payment_token: str
    payment_type: CheckoutPaymentType
    status: str
