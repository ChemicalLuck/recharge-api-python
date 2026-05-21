from typing import Literal, Optional

from recharge.model.base import RechargeModel

CustomerStatus = Literal["ACTIVE", "INACTIVE"]


class CustomerAnalyticsDataUtmParams(RechargeModel):
    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class CustomerAnalyticsData(RechargeModel):
    utm_params: Optional[list[CustomerAnalyticsDataUtmParams]] = None


class CustomerExternalCustomerId(RechargeModel):
    ecommerce: Optional[str] = None


class Customer(RechargeModel):
    id: int
    analytics_data: Optional[CustomerAnalyticsData] = None
    apply_credit_to_next_recurring_charge: bool
    created_at: str
    email: str
    external_customer_id: Optional[CustomerExternalCustomerId] = None
    first_charge_processed_at: Optional[str] = None
    first_name: str
    has_payment_method_in_dunning: bool
    has_valid_payment_method: bool
    hash: str
    last_name: str
    phone: Optional[str] = None
    status: Optional[CustomerStatus] = None
    subscriptions_active_count: int
    subscriptions_total_count: int
    tax_exempt: bool
    updated_at: str


class CustomerCreditSummary(RechargeModel):
    customer_id: int
    total_available_balance: str
    currency_code: str


class CustomerDeliveryOrderLineItemExternalProductId(RechargeModel):
    ecommerce: str


class CustomerDeliveryOrderLineItemExternalVariantId(RechargeModel):
    ecommerce: str


class CustomerDeliveryOrderLineItemImage(RechargeModel):
    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    original: Optional[str] = None
    sort_order: Optional[int] = None


CustomerDeliveryOrderLineItemPlanType = Literal["subscription", "onetime"]


class CustomerDeliveryOrderLineItemProperty(RechargeModel):
    name: str
    value: str


class CustomerDeliveryOrderLineItem(RechargeModel):
    subscription_id: int
    external_product_id: CustomerDeliveryOrderLineItemExternalProductId
    external_variant_id: CustomerDeliveryOrderLineItemExternalVariantId
    images: Optional[CustomerDeliveryOrderLineItemImage] = None
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


class CustomerPaymentDetails(RechargeModel):
    brand: Optional[str] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    last4: Optional[str] = None
    paypal_email: Optional[str] = None
    paypal_payer_id: Optional[str] = None
    wallet_type: Optional[str] = None
    funding_type: Optional[str] = None


class CustomerBillingAddress(RechargeModel):
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


class CustomerDeliveryOrderPaymentMethod(RechargeModel):
    id: int
    billing_address: CustomerBillingAddress
    payment_details: CustomerPaymentDetails


class CustomerDeliveryOrderShippingAddress(RechargeModel):
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


class CustomerDeliveryOrder(RechargeModel):
    id: Optional[int] = None
    address_id: int
    charge_id: Optional[int] = None
    line_items: list[CustomerDeliveryOrderLineItem]
    order_subtotal: str
    payment_method: CustomerDeliveryOrderPaymentMethod
    shipping_address: CustomerDeliveryOrderShippingAddress


class CustomerDeliveryScheduleDelivery(RechargeModel):
    date: str
    orders: list[CustomerDeliveryOrder]


class CustomerDeliveryScheduleCustomer(RechargeModel):
    id: int
    email: str
    first_name: str
    last_name: str


class CustomerDeliverySchedule(RechargeModel):
    customer: CustomerDeliveryScheduleCustomer
    deliveries: list[CustomerDeliveryScheduleDelivery]  # fixed: was 'delvieries'
