from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.product import (
    Product,
    ProductExternalProductId,
    ProductImage,
    ProductOption,
    ProductVariant,
)


class ProductCreateBodyOptional(TypedDict, total=False):
    brand: str
    external_created_at: str
    external_updated_at: str
    images: ProductImage
    published_at: str
    requires_shipping: bool


class ProductCreateBody(ProductCreateBodyOptional):
    external_product_id: ProductExternalProductId
    options: list[ProductOption]
    title: str
    variants: list[ProductVariant]
    vendor: str


class ProductUpdateBody(TypedDict, total=False):
    brand: str
    images: ProductImage
    options: list[ProductOption]
    requires_shipping: bool
    title: str
    variants: list[ProductVariant]
    vendor: str


class ProductDeleteBody(TypedDict):
    product_id: str


class ProductListQuery(TypedDict, total=False):
    external_product_ids: str


class ProductResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/products
    """

    object_list_key = "products"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: ProductCreateBody) -> Product:
        """Create a product.
        https://developer.rechargepayments.com/2021-11/products/products_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Product(**data)

    def get(self, product_id: str) -> Product:
        """Get a product.
        https://developer.rechargepayments.com/2021-11/products/products_retrieve
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
        https://developer.rechargepayments.com/2021-11/products/products_update
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
        https://developer.rechargepayments.com/2021-11/products/products_delete
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
        https://developer.rechargepayments.com/2021-11/products/products_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Product(**item) for item in data]

    def list_all(self, query: Optional[ProductListQuery] = None) -> list[Product]:
        """List all products.
        https://developer.rechargepayments.com/2021-11/products/products_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Product(**item) for item in data]
