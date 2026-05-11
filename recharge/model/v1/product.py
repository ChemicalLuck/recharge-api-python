from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

ProductDiscountType = Literal["percentage"]

ProductStorefrontPurchaseOptions = Literal[
    "subscription_only", "subscription_and_onetime"
]

ProductOrderIntervalUnit = Literal["day", "week", "month"]


class ProductImages(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    large: Optional[str] = None
    medium: Optional[str] = None
    original: Optional[str] = None
    small: Optional[str] = None


class Product(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    charge_interval_frequency: Optional[int] = None
    created_at: Optional[str] = None
    cutoff_day_of_month: Optional[int] = None
    cutoff_day_of_week: Optional[int] = None
    discount_amount: Optional[int] = None
    discount_type: Optional[ProductDiscountType] = None
    expire_after_specific_number_of_charges: Optional[int] = None
    handle: Optional[str] = None
    images: Optional[ProductImages] = None
    modifiable_properties: list[str] = []
    number_charges_until_expiration: Optional[int] = None
    order_day_of_month: Optional[int] = None
    order_day_of_week: Optional[int] = None
    order_interval_frequency_options: Optional[str] = None
    order_interval_unit: Optional[ProductOrderIntervalUnit] = None
    shopify_product_id: Optional[int] = None
    storefront_purchase_options: Optional[ProductStorefrontPurchaseOptions] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
