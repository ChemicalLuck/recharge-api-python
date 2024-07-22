from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.product import (
    Product,
    ProductDiscountType,
    ProductImages,
    ProductOrderIntervalUnit,
    ProductStorefrontPurchaseOptions,
)


class ProductCreateBodyOptional(TypedDict, total=False):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    modifiable_properties: list[str]
    order_day_of_month: int
    order_day_of_week: int
    order_interval_frequency_options: list[int]
    storefront_purchase_options: ProductStorefrontPurchaseOptions


class ProductCreateBody(ProductCreateBodyOptional):
    shopify_product_id: int


class ProductGetQuery(TypedDict, total=False):
    charge_interval_frequency: str
    created_at: str
    cutoff_day_of_month: str
    cutoff_day_of_week: str
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    handle: str
    images: ProductImages
    modifiable_properties: list[str]
    number_charges_until_expiration: str
    order_day_of_month: str
    order_day_of_week: str
    order_interval_frequency: str
    order_interval_unit: ProductOrderIntervalUnit
    shopify_product_id: str
    storefront_purchase_options: ProductStorefrontPurchaseOptions
    title: str
    updated_at: str


class ProductUpdateBodyOptional(TypedDict, total=False):
    charge_interval_frequency: int
    cutoff_day_of_month: int
    cutoff_day_of_week: int
    discount_amount: str
    discount_type: ProductDiscountType
    expire_after_specific_number_of_charges: str
    modifiable_properties: list[str]
    order_day_of_month: int
    order_day_of_week: int
    order_interval_unit: ProductOrderIntervalUnit
    storefront_purchase_options: ProductStorefrontPurchaseOptions


class ProductUpdateBody(ProductCreateBodyOptional):
    shopify_product_id: int


class ProductDeleteBody(TypedDict):
    product_id: str


class ProductListQuery(TypedDict, total=False):
    id: str
    limit: str
    shopify_product_id: int
    page: str


class ProductResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/products
    """

    object_list_key = "products"
    object_dict_key = "product"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: ProductCreateBody) -> Product:
        """Create a product.
        https://developer.rechargepayments.com/2021-01/products/products_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Product(**data)

    def get(self, product_id: str) -> Product:
        """Get a product.
        https://developer.rechargepayments.com/2021-01/products/products_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}/:product_id", required_scopes)

        url = f"{self._url}/{product_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Product(**data)

    def update(self, product_id: str, body: ProductUpdateBody) -> Product:
        """Update a product.
        https://developer.rechargepayments.com/2021-01/products/products_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"PUT /{self.object_list_key}/:product_id", required_scopes)

        url = f"{self._url}/{product_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Product(**data)

    def delete(self, product_id: str) -> dict:
        """Delete a product.
        https://developer.rechargepayments.com/2021-01/products/products_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:product_id", required_scopes
        )

        url = f"{self._url}/{product_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[ProductListQuery] = None) -> list[Product]:
        """List products.
        https://developer.rechargepayments.com/2021-01/products/products_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Product(**item) for item in data]

    def list_all(self, query: Optional[ProductListQuery] = None) -> list[Product]:
        """List all products.
        https://developer.rechargepayments.com/2021-01/products/products_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Product(**item) for item in data]

    def count(self) -> int:
        """Count products.
        https://developer.rechargepayments.com/2021-01/products/products_count
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in response, got {data}")
        return data["count"]
