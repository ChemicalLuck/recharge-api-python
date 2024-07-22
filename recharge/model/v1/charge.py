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
    company: str
    country: str
    first_name: str
    last_name: str
    phone: str
    province: str
    zip: str


class ChargeClientDetails(TypedDict):
    browser_ip: str
    user_agent: str


class ChargeDiscountCode(TypedDict):
    recharge_discount_id: int
    code: str
    value: float


ChargeDiscountCodeType = Literal["percentage", "fixed_amount"]

ChargeDiscountCode.__annotations__["type"] = ChargeDiscountCodeType


class ChargeLineItemImages(TypedDict):
    large: str
    medium: str
    original: str
    small: str


class ChargeLineItemProperty(TypedDict):
    name: str
    value: str


class ChargeLineItem(TypedDict):
    gram: int
    images: ChargeLineItemImages
    original_price: str
    price: str
    properties: list[ChargeLineItemProperty]
    quantity: int
    shopify_product_id: int
    shopify_variant_id: int
    sku: str
    title: str
    variant_title: str
    subscription_id: int


class ChargeNoteAttribute(TypedDict):
    name: str
    value: str


class ChargeShippingAddress(TypedDict):
    address1: str
    address2: Optional[str]
    city: str
    company: str
    country: str
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


class ChargeTaxLine(TypedDict):
    code: str
    price: str
    source: str
    title: str
    taxable: str


class Charge(TypedDict):
    id: int
    address_id: int
    analytics_data: ChargeAnalyticsData
    billing_address: ChargeBillingAddress
    client_details: ChargeClientDetails
    created_at: str
    customer_hash: str
    customer_id: str
    discount_codes: list[ChargeDiscountCode]
    email: str
    first_name: str
    has_uncommitted_changes: bool
    last_name: str
    line_items: list[ChargeLineItem]
    note: str
    note_attributes: list[ChargeNoteAttribute]
    processor_name: str
    processed_at: Optional[str]
    scheduled_at: str
    shipments_count: Optional[int]
    shipping_address: ChargeShippingAddress
    shipping_lines: list[ChargeShippingLine]
    shopify_order_id: int
    status: ChargeStatus
    subtotal_price: str
    tags: list[str]
    tax_lines: list[ChargeTaxLine]
    total_discounts: str
    total_line_items_price: str
    total_price: str
    total_refunds: str
    total_weight: str
    transaction_id: str
    updated_at: str
    error: str
    error_type: str
    last_charge_attempt_date: str
    number_times_tried: int
    retry_date: Optional[str]
    shopify_variant_id_not_found: int


Charge.__annotations__["type"] = str
