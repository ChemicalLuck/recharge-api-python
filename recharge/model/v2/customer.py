from typing import Literal, Optional, TypedDict

CustomerStatus = Literal["ACTIVE", "INACTIVE"]


class CustomerAnalyticsDataUtmParams(TypedDict, total=False):
    utm_campaign: str
    utm_content: str
    utm_data_source: str
    utm_source: str
    utm_medium: str
    utm_term: str
    utm_timestamp: str


class CustomerAnalyticsData(TypedDict, total=False):
    utm_params: list[CustomerAnalyticsDataUtmParams]


class CustomerExternalCustomerId(TypedDict, total=False):
    ecommerce: str


class Customer(TypedDict):
    id: int
    analytics_data: CustomerAnalyticsData
    apply_credit_to_next_recurring_charge: bool
    created_at: str
    email: str
    external_customer_id: CustomerExternalCustomerId
    first_charge_processed_at: Optional[str]
    first_name: str
    has_payment_method_in_dunning: bool
    has_valid_payment_method: bool
    hash: str
    last_name: str
    phone: str
    subscriptions_active_count: int
    subscriptions_total_count: int
    tax_exempt: bool
    updated_at: str


class CustomerCreditSummary(TypedDict):
    customer_id: int
    total_available_balance: str
    currency_code: str


class CustomerDeliveryOrderLineItemExternalProductId(TypedDict):
    ecommerce: str


class CustomerDeliveryOrderLineItemExternalVariantId(TypedDict):
    ecommerce: str


class CustomerDeliveryOrderLineItemImage(TypedDict, total=False):
    large: str
    medium: str
    small: str
    original: str
    sort_order: int


CustomerDeliveryOrderLineItemPlanType = Literal["subscription", "onetime"]


class CustomerDeliveryOrderLineItemProperty(TypedDict):
    name: str
    value: str


class CustomerDeliveryOrderLineItem(TypedDict):
    subscription_id: int
    external_product_id: CustomerDeliveryOrderLineItemExternalProductId
    external_variant_id: CustomerDeliveryOrderLineItemExternalVariantId
    images: list[CustomerDeliveryOrderLineItemImage]
    is_prepaid: bool
    is_skippable: bool
    is_skipped: bool
    original_price: str
    plan_type: CustomerDeliveryOrderLineItemPlanType
    product_title: str
    properties: list[CustomerDeliveryOrderLineItemProperty]
    quantity: int
    subtotal_price: str
    unit_price: str
    variant_title: str


class CustomerPaymentDetails(TypedDict, total=False):
    brand: str
    exp_month: int
    exp_year: int
    last4: str
    paypal_email: str
    paypal_payer_id: str
    wallet_type: str
    funding_type: str


class CustomerBillingAddress(TypedDict, total=False):
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


class CustomerDeliveryOrderPaymentMethod(TypedDict):
    id: int
    billing_address: CustomerBillingAddress
    payment_details: CustomerPaymentDetails


class CustomerDeliveryOrderShippingAddress(TypedDict, total=False):
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


class CustomerDeliveryOrder(TypedDict):
    id: Optional[int]
    address_id: int
    charge_id: int
    line_items: list[CustomerDeliveryOrderLineItem]
    order_subtotal: str
    payment_method: CustomerDeliveryOrderPaymentMethod
    shipping_address: CustomerDeliveryOrderShippingAddress


class CustomerDeliveryScheduleDelivery(TypedDict):
    date: str
    orders: list[CustomerDeliveryOrder]


class CustomerDeliveryScheduleCustomer(TypedDict):
    id: int
    email: str
    first_name: str
    last_name: str


class CustomerDeliverySchedule(TypedDict):
    customer: CustomerDeliveryScheduleCustomer
    delvieries: list[CustomerDeliveryScheduleDelivery]
