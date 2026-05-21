from typing import Literal, Optional

from recharge.model.base import RechargeModel


class ProductExternalProductId(RechargeModel):
    ecommerce: str


class ProductImage(RechargeModel):
    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None
    sort_order: Optional[int] = None


class ProductOptionValue(RechargeModel):
    label: str
    position: str


class ProductOption(RechargeModel):
    name: str
    position: str
    values: list[ProductOptionValue]


class ProductVariantDimensions(RechargeModel):
    weight: int
    weight_unit: str


class ProductVariantOptionValue(RechargeModel):
    label: str


class ProductVariantPrices(RechargeModel):
    compare_at_price: str
    unit_price: str


class ProductVariant(RechargeModel):
    dimensions: Optional[ProductVariantDimensions] = None
    external_variant_id: str
    image: Optional[ProductImage] = None
    option_values: list[ProductVariantOptionValue] = []
    prices: Optional[ProductVariantPrices] = None
    requires_shipping: bool
    sku: Optional[str] = None
    tax_code: Optional[str] = None
    taxable: bool
    title: str


ProductDiscountType = Literal["percentage"]

ProductStorefrontPurchaseOptions = Literal[
    "subscription_only", "subscription_and_onetime"
]

ProductOrderIntervalUnit = Literal["day", "week", "month"]


class Product(RechargeModel):
    external_product_id: str
    brand: Optional[str] = None
    external_created_at: Optional[str] = None
    external_updated_at: Optional[str] = None
    images: list[ProductImage] = []
    options: list[ProductOption] = []
    published_at: Optional[str] = None
    requires_shipping: Optional[bool] = None
    title: str
    variants: list[ProductVariant] = []
    vendor: Optional[str] = None
