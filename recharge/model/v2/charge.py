from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

ChargeStatus = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]

ChargeType = Literal["CHECKOUT", "RECURRING"]


class ChargeAnalyticsDataUtmParams(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class ChargeAnalyticsData(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    utm_params: Optional[ChargeAnalyticsDataUtmParams] = None


class ChargeBillingAddress(BaseModel):
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


class ChargeClientDetails(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    browser_ip: Optional[str] = None
    user_agent: Optional[str] = None


class ChargeExternalCustomerId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class ChargeCustomer(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[int] = None
    email: Optional[str] = None
    external_customer_id: Optional[ChargeExternalCustomerId] = None
    hash: Optional[str] = None


ChargeDiscountCodeType = Literal["percentage", "fixed_amount"]


class ChargeDiscount(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: Optional[int] = None
    code: Optional[str] = None
    value: Optional[float] = None
    value_type: Optional[ChargeDiscountCodeType] = None


class ChargeExternalOrderId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class ChargeExternalTransactionId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class ChargeLineItemImages(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None
    sort_order: Optional[int] = None


class ChargeLineItemProperty(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class ChargeExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class ChargeExternalVariantId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: Optional[str] = None


class ChargeTaxLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    price: Optional[str] = None
    rate: Optional[str] = None
    title: Optional[str] = None


class ChargeLineItem(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    purchase_item_id: Optional[int] = None
    external_product_id: Optional[ChargeExternalProductId] = None
    external_variant_id: Optional[ChargeExternalVariantId] = None
    grams: Optional[int] = None
    handle: Optional[str] = None
    images: Optional[ChargeLineItemImages] = None
    original_price: Optional[str] = None
    properties: list[ChargeLineItemProperty] = []
    quantity: Optional[int] = None
    sku: Optional[str] = None
    tax_due: Optional[str] = None
    tax_lines: list[ChargeTaxLine] = []
    taxable: Optional[bool] = None
    taxable_amount: Optional[str] = None
    title: Optional[str] = None
    total_price: Optional[str] = None
    unit_price: Optional[str] = None
    unit_price_includes_tax: Optional[bool] = None
    variant_title: Optional[str] = None


class ChargeOrderAttribute(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    value: str


class ChargeShippingAddress(BaseModel):
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


class ChargeShippingLine(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    code: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    taxable: Optional[str] = None
    tax_lines: list[ChargeTaxLine] = []


class Charge(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    address_id: Optional[int] = None
    analytics_data: Optional[ChargeAnalyticsData] = None
    billing_address: Optional[ChargeBillingAddress] = None
    charge_attempts: Optional[int] = None
    client_details: Optional[ChargeClientDetails] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    customer: Optional[ChargeCustomer] = None
    discounts: list[ChargeDiscount] = []
    error: Optional[str] = None
    error_type: Optional[str] = None
    external_order_id: Optional[ChargeExternalOrderId] = None
    external_transaction_id: Optional[ChargeExternalTransactionId] = None
    external_variant_id_not_found: Optional[bool] = None
    has_uncommitted_changes: Optional[bool] = None
    line_items: list[ChargeLineItem] = []
    note: Optional[str] = None
    order_attributes: list[ChargeOrderAttribute] = []
    orders_count: Optional[int] = None
    payment_processor: Optional[str] = None
    processed_at: Optional[str] = None
    retry_date: Optional[str] = None
    scheduled_at: Optional[str] = None
    shipping_address: Optional[ChargeShippingAddress] = None
    shipping_lines: list[ChargeShippingLine] = []
    status: Optional[ChargeStatus] = None
    subtotal_price: Optional[str] = None
    tags: list[str] = []
    tax_lines: list[ChargeTaxLine] = []
    taxable: Optional[bool] = None
    taxes_included: Optional[bool] = None
    total_discounts: Optional[str] = None
    total_line_items_price: Optional[str] = None
    total_price: Optional[str] = None
    total_refunds: Optional[str] = None
    total_tax: Optional[str] = None
    total_weight_grams: Optional[int] = None
    type: Optional[ChargeType] = None
    updated_at: Optional[str] = None
