from typing import Literal, TypedDict


class ProductExternalProductId(TypedDict):
    ecommerce: str


class ProductImage(TypedDict, total=False):
    large: str
    medium: str
    original: str
    small: str
    sort_order: int


class ProductOptionValue(TypedDict):
    label: str
    position: str


class ProductOption(TypedDict):
    name: str
    position: str
    values: list[ProductOptionValue]


class ProductVariantDimensions(TypedDict):
    weight: int
    weight_unit: str


class ProductVariantOptionValue(TypedDict):
    label: str


class ProductVariantPrices(TypedDict):
    compare_at_price: str
    unit_price: str


class ProductVariant(TypedDict):
    dimensions: ProductVariantDimensions
    external_variant_id: str
    image: ProductImage
    option_values: list[ProductVariantOptionValue]
    prices: ProductVariantPrices
    requires_shipping: bool
    sku: str
    tax_code: str
    taxable: bool
    title: str


ProductDiscountType = Literal["percentage"]

ProductStorefrontPurchaseOptions = Literal[
    "subscription_only", "subscription_and_onetime"
]


ProductOrderIntervalUnit = Literal["day", "week", "month"]


class Product(TypedDict):
    external_product_id: str
    brand: str
    external_created_at: str
    external_updated_at: str
    images: list[ProductImage]
    options: list[ProductOption]
    published_at: str
    requires_shipping: bool
    title: str
    variants: list[ProductVariant]
    vendor: str
