from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict


class ProductExternalProductId(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    ecommerce: str


class ProductImage(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None
    sort_order: Optional[int] = None


class ProductOptionValue(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str
    position: str


class ProductOption(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    name: str
    position: str
    values: list[ProductOptionValue]


class ProductVariantDimensions(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    weight: int
    weight_unit: str


class ProductVariantOptionValue(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    label: str


class ProductVariantPrices(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    compare_at_price: str
    unit_price: str


class ProductVariant(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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


class Product(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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
