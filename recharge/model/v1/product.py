from typing import Literal, TypedDict

ProductDiscountType = Literal["percentage"]

ProductStorefrontPurchaseOptions = Literal[
    "subscription_only", "subscription_and_onetime"
]


ProductOrderIntervalUnit = Literal["day", "week", "month"]


class ProductImages(TypedDict, total=False):
    large: str
    medium: str
    original: str
    small: str


class Product(TypedDict):
    id: int
    charge_interval_frequency: int
    created_at: str
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    discount_amount: int
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: int
    handle: str
    images: ProductImages
    modifiable_properties: list[str]
    number_charges_until_expiration: int
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency_options: str
    order_interval_unit: ProductOrderIntervalUnit
    shopify_product_id: int
    storefront_purchase_options: ProductStorefrontPurchaseOptions
    title: str
    updated_at: str
