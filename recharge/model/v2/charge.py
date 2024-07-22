from typing import Literal, Optional, TypedDict

ChargeStatus = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]


class ChargeAnalyticsDataUtmParams(TypedDict):
    utm_campaign: str
    utm_content: str
    utm_data_source: str
    utm_source: str
    utm_medium: str
    utm_term: str
    utm_timestamp: str


class ChargeAnalyticsData(TypedDict):
    utm_params: ChargeAnalyticsDataUtmParams


class ChargeBillingAddress(TypedDict):
    address1: str
    address2: Optional[str]
    city: str
    company: Optional[str]
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class ChargeClientDetails(TypedDict):
    browser_ip: str
    user_agent: str


class ChargeExternalCustomerId(TypedDict):
    ecommerce: str


class ChargeCustomer(TypedDict):
    id: int
    email: str
    external_customer_id: ChargeExternalCustomerId
    hash: str


ChargeDiscountCodeType = Literal["percentage", "fixed_amount"]


class ChargeDiscount(TypedDict):
    id: int
    code: str
    value: float
    value_type: ChargeDiscountCodeType


class ChargeExternalOrderId(TypedDict):
    ecommerce: str


class ChargeExternalTransactionId(TypedDict):
    ecommerce: str


class ChargeLineItemImages(TypedDict):
    large: str
    medium: str
    original: str
    small: str
    sort_order: int


class ChargeLineItemProperty(TypedDict):
    name: str
    value: str


class ChargeExternalProductId(TypedDict):
    ecommerce: str


class ChargeExternalVariantId(TypedDict):
    ecommerce: str


class ChargeTaxLine(TypedDict):
    price: str
    rate: str
    title: str


class ChargeLineItem(TypedDict):
    purchase_item_id: int
    external_product_id: ChargeExternalProductId
    external_variant_id: ChargeExternalVariantId
    grams: int
    handle: str
    images: ChargeLineItemImages
    original_price: str
    properties: list[ChargeLineItemProperty]
    quantity: int
    sku: str
    tax_due: str
    tax_lines: list[ChargeTaxLine]
    taxable: bool
    taxable_amount: str
    title: str
    total_price: str
    unit_price: str
    unit_price_includes_tax: bool
    variant_title: str


class ChargeOrderAttribute(TypedDict):
    name: str
    value: str


class ChargeShippingAddress(TypedDict):
    address1: str
    address2: Optional[str]
    city: str
    company: Optional[str]
    country_code: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class ChargeShippingLine(TypedDict):
    code: str
    price: str
    source: str
    title: str
    taxable: str
    tax_lines: list[ChargeTaxLine]


class Charge(TypedDict):
    id: int
    address_id: int
    analytics_data: ChargeAnalyticsData
    billing_address: ChargeBillingAddress
    charge_attempts: Optional[int]
    client_details: ChargeClientDetails
    created_at: str
    currency: str
    customer: ChargeCustomer
    discounts: list[ChargeDiscount]
    error: Optional[str]
    error_type: Optional[str]
    external_order_id: ChargeExternalOrderId
    external_transaction_id: ChargeExternalTransactionId
    external_variant_id_not_found: Optional[bool]
    has_uncommitted_changes: bool
    line_items: list[ChargeLineItem]
    note: str
    order_attributes: list[ChargeOrderAttribute]
    orders_count: int
    payment_processor: str
    processed_at: Optional[str]
    retry_date: Optional[str]
    scheduled_at: str
    shipping_address: ChargeShippingAddress
    shipping_lines: list[ChargeShippingLine]
    status: ChargeStatus
    subtotal_price: str
    tags: list[str]
    tax_lines: list[ChargeTaxLine]
    taxable: bool
    taxes_included: bool
    total_discounts: str
    total_line_items_price: str
    total_price: str
    total_refunds: Optional[str]
    total_tax: str
    total_weight_grams: int
    updated_at: str


ChargeType = Literal["checkout", "recurring"]

Charge.__annotations__["type"] = ChargeType
