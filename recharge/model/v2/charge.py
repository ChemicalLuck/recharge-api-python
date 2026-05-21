from typing import Any, Literal, Optional, Union

from pydantic import field_validator

from recharge.model.base import RechargeModel

ChargeStatus = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]

ChargeType = Literal["CHECKOUT", "RECURRING"]


class ChargeAnalyticsDataUtmParams(RechargeModel):
    utm_campaign: Optional[str] = None
    utm_content: Optional[str] = None
    utm_data_source: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    utm_term: Optional[str] = None
    utm_timestamp: Optional[str] = None


class ChargeAnalyticsData(RechargeModel):
    utm_params: Optional[list[ChargeAnalyticsDataUtmParams]] = None


class ChargeBillingAddress(RechargeModel):
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


class ChargeClientDetails(RechargeModel):
    browser_ip: Optional[str] = None
    user_agent: Optional[str] = None


class ChargeExternalCustomerId(RechargeModel):
    ecommerce: Optional[str] = None


class ChargeCustomer(RechargeModel):
    id: Optional[int] = None
    email: Optional[str] = None
    external_customer_id: Optional[ChargeExternalCustomerId] = None
    hash: Optional[str] = None


ChargeDiscountCodeType = Literal["percentage", "fixed_amount"]


class ChargeDiscount(RechargeModel):
    id: Optional[int] = None
    code: Optional[str] = None
    value: Optional[float] = None
    value_type: Optional[ChargeDiscountCodeType] = None


class ChargeExternalOrderId(RechargeModel):
    ecommerce: Optional[str] = None


class ChargeExternalTransactionId(RechargeModel):
    payment_processor: Optional[str] = None


class ChargeLineItemImages(RechargeModel):
    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None
    sort_order: Optional[int] = None


class ChargeLineItemProperty(RechargeModel):
    name: str
    value: str


class ChargeExternalProductId(RechargeModel):
    ecommerce: Optional[str] = None


class ChargeExternalVariantId(RechargeModel):
    ecommerce: Optional[str] = None


class ChargeTaxLine(RechargeModel):
    price: Optional[str] = None
    rate: Optional[Union[str, float]] = None
    title: Optional[str] = None
    unit_price: Optional[str] = None


ChargeLineItemPurchaseItemType = Literal["subscription", "onetime"]


class ChargeLineItem(RechargeModel):
    purchase_item_id: Optional[int] = None
    external_product_id: Optional[ChargeExternalProductId] = None
    external_variant_id: Optional[ChargeExternalVariantId] = None
    grams: Optional[int] = None
    handle: Optional[str] = None
    images: Optional[ChargeLineItemImages] = None
    original_price: Optional[str] = None
    properties: list[ChargeLineItemProperty] = []
    purchase_item_type: Optional[ChargeLineItemPurchaseItemType] = None
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


class ChargeOrderAttribute(RechargeModel):
    name: str
    value: Optional[str] = None


class ChargeShippingAddress(RechargeModel):
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


class ChargeShippingLine(RechargeModel):
    code: Optional[str] = None
    price: Optional[str] = None
    source: Optional[str] = None
    title: Optional[str] = None
    taxable: Optional[Union[str, bool]] = None
    tax_lines: list[ChargeTaxLine] = []


class Charge(RechargeModel):
    @field_validator("status", "type", mode="before")
    @classmethod
    def uppercase_literals(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.upper()
        return v

    @field_validator("tags", mode="before")
    @classmethod
    def coerce_tags(cls, v: Any) -> Any:
        if isinstance(v, str):
            return [t.strip() for t in v.split(",") if t.strip()]
        return v

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
