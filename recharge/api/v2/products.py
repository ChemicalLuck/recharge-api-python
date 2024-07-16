from typing import Literal, TypedDict, TypeAlias

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

ProductDiscountType: TypeAlias = Literal["percentage"]


class ProductExternalProductId(TypedDict):
    ecommerce: str


class ProductImages(TypedDict, total=False):
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
    image: ProductImages
    option_values: list[ProductVariantOptionValue]
    prices: ProductVariantPrices
    requires_shipping: bool
    sku: str
    tax_code: str
    taxable: bool
    title: str

class ProductCreateBodyOptional(TypedDict, total=False):
    brand: str
    external_created_at: str
    external_updated_at: str
    images: ProductImages
    published_at: str
    requires_shipping: bool

class ProductCreateBody(ProductCreateBodyOptional):
    external_product_id: ProductExternalProductId
    options: list[ProductOption]
    title: str
    variants: list[ProductVariant]
    vendor: str


ProductOrderIntervalUnit: TypeAlias = Literal["day", "week", "month"]


class ProductUpdateBody(TypedDict, total=False):
    brand: str
    images: ProductImages
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

    def create(self, body: ProductCreateBody):
        """Create a product.
        https://developer.rechargepayments.com/2021-11/products/products_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, product_id: str):
        """Get a product.
        https://developer.rechargepayments.com/2021-11/products/products_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes(f"GET /{self.object_list_key}/:product_id", required_scopes)

        return self._http_get(f"{self.url}/{product_id}")

    def update(self, product_id: str, body: ProductUpdateBody):
        """Update a product.
        https://developer.rechargepayments.com/2021-11/products/products_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"PUT /{self.object_list_key}/:product_id", required_scopes)

        return self._http_put(f"{self.url}/{product_id}", body)

    def delete(self, product_id: str):
        """Delete a product.
        https://developer.rechargepayments.com/2021-11/products/products_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:product_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{product_id}")

    def list_(self, query: ProductListQuery | None = None):
        """List products.
        https://developer.rechargepayments.com/2021-11/products/products_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
