from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

CustomerStatus = Literal["ACTIVE", "INACTIVE"]


class CustomerAnalyticsDataUtmParams(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class CustomerAnalyticsData(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_params: Optional[list[CustomerAnalyticsDataUtmParams]] = None


class CustomerExternalCustomerId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class Customer(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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
    subscriptions_active_count: int
    subscriptions_total_count: int
    tax_exempt: bool
    updated_at: str


class CustomerCreditSummary(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer_id: int
    total_available_balance: str
    currency_code: str


class CustomerDeliveryOrderLineItemExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class CustomerDeliveryOrderLineItemExternalVariantId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class CustomerDeliveryOrderLineItemImage(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    small: Optional[str] = None
    original: Optional[str] = None
    sort_order: Optional[int] = None


CustomerDeliveryOrderLineItemPlanType = Literal["subscription", "onetime"]


class CustomerDeliveryOrderLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class CustomerDeliveryOrderLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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


class CustomerPaymentDetails(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    brand: Optional[str] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None
    last4: Optional[str] = None
    paypal_email: Optional[str] = None
    paypal_payer_id: Optional[str] = None
    wallet_type: Optional[str] = None
    funding_type: Optional[str] = None


class CustomerBillingAddress(BaseModel):
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


class CustomerDeliveryOrderPaymentMethod(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    billing_address: CustomerBillingAddress
    payment_details: CustomerPaymentDetails


class CustomerDeliveryOrderShippingAddress(BaseModel):
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


class CustomerDeliveryOrder(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[int] = None
    address_id: int
    charge_id: int
    line_items: list[CustomerDeliveryOrderLineItem]
    order_subtotal: str
    payment_method: CustomerDeliveryOrderPaymentMethod
    shipping_address: CustomerDeliveryOrderShippingAddress


class CustomerDeliveryScheduleDelivery(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    date: str
    orders: list[CustomerDeliveryOrder]


class CustomerDeliveryScheduleCustomer(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    email: str
    first_name: str
    last_name: str


class CustomerDeliverySchedule(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    customer: CustomerDeliveryScheduleCustomer
    deliveries: list[CustomerDeliveryScheduleDelivery]  # fixed: was 'delvieries'
