from typing import Literal, Optional

from recharge.model.base import RechargeModel

ChargeStatus = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]

ChargeDiscountCodeType = Literal["percentage", "fixed_amount"]


class ChargeAnalyticsDataUtmParams(RechargeModel):
    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class ChargeAnalyticsData(RechargeModel):
    utm_params: Optional[ChargeAnalyticsDataUtmParams] = None


class ChargeBillingAddress(RechargeModel):
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


class ChargeClientDetails(RechargeModel):
    browser_ip: Optional[str] = None
    user_agent: Optional[str] = None


class ChargeDiscountCode(RechargeModel):
    recharge_discount_id: Optional[int] = None
    code: Optional[str] = None
    value: Optional[float] = None
    type: Optional[ChargeDiscountCodeType] = None


class ChargeLineItemImages(RechargeModel):
    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None


class ChargeLineItemProperty(RechargeModel):
    name: str
    value: str


class ChargeLineItem(RechargeModel):
    gram: Optional[int] = None
    images: Optional[ChargeLineItemImages] = None
    original_price: Optional[str] = None
    price: Optional[str] = None
    properties: list[ChargeLineItemProperty] = []
    quantity: Optional[int] = None
    shopify_product_id: Optional[int] = None
    shopify_variant_id: Optional[int] = None
    sku: Optional[str] = None
    title: Optional[str] = None
    variant_title: Optional[str] = None
    subscription_id: Optional[int] = None


class ChargeNoteAttribute(RechargeModel):
    name: str
    value: str


class ChargeShippingAddress(RechargeModel):
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


class ChargeShippingLine(RechargeModel):
    code: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    taxable: Optional[str] = None


class ChargeTaxLine(RechargeModel):
    code: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    taxable: Optional[str] = None


class Charge(RechargeModel):
    id: int
    address_id: Optional[int] = None
    analytics_data: Optional[ChargeAnalyticsData] = None
    billing_address: Optional[ChargeBillingAddress] = None
    client_details: Optional[ChargeClientDetails] = None
    created_at: Optional[str] = None
    customer_hash: Optional[str] = None
    customer_id: Optional[str] = None
    discount_codes: list[ChargeDiscountCode] = []
    email: Optional[str] = None
    first_name: Optional[str] = None
    has_uncommitted_changes: Optional[bool] = None
    last_name: Optional[str] = None
    line_items: list[ChargeLineItem] = []
    note: Optional[str] = None
    note_attributes: list[ChargeNoteAttribute] = []
    processor_name: Optional[str] = None
    processed_at: Optional[str] = None
    scheduled_at: Optional[str] = None
    shipments_count: Optional[int] = None
    shipping_address: Optional[ChargeShippingAddress] = None
    shipping_lines: list[ChargeShippingLine] = []
    shopify_order_id: Optional[int] = None
    status: Optional[ChargeStatus] = None
    subtotal_price: Optional[str] = None
    tags: list[str] = []
    tax_lines: list[ChargeTaxLine] = []
    total_discounts: Optional[str] = None
    total_line_items_price: Optional[str] = None
    total_price: Optional[str] = None
    total_refunds: Optional[str] = None
    total_weight: Optional[str] = None
    transaction_id: Optional[str] = None
    updated_at: Optional[str] = None
    error: Optional[str] = None
    error_type: Optional[str] = None
    last_charge_attempt_date: Optional[str] = None
    number_times_tried: Optional[int] = None
    retry_date: Optional[str] = None
    shopify_variant_id_not_found: Optional[int] = None
    type: Optional[str] = None
