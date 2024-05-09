from typing import Required, TypedDict, TypeAlias, Literal

from recharge.api import RechargeResource, RechargeScope

CollectionCreateSortOrder: TypeAlias = Literal[
    "id-asc", "id-desc", "title-asc", "title-desc", "created-asc", "created-desc"
]


class CollectionCreateBody(TypedDict, total=False):
    description: Required[str]
    sort_order: CollectionCreateSortOrder
    titel: Required[str]


class CollectionUpdateBody(TypedDict, total=False):
    description: str
    sort_order: CollectionCreateSortOrder
    title: str


class CollectionListQuery(TypedDict, total=False):
    title: str


class CollectionListProductsQuery(TypedDict, total=False):
    collection_id: int


class CollectionProduct(TypedDict):
    external_product_id: str


class CollectionAddProductsBody(TypedDict):
    collection_products: list[CollectionProduct]


class CollectionDeleteProductsBody(TypedDict):
    collection_products: list[CollectionProduct]


class CollectionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/collections
    """

    object_list_key = "collections"

    def create(self, body: CollectionCreateBody):
        """Create a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, collection_id: str):
        """Get a collection by ID.
        https://developer.rechargepayments.com/2021-11/collections/collections_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_get(f"{self.url}/{collection_id}")

    def update(self, collection_id: str, body: CollectionUpdateBody):
        """Update a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_put(f"{self.url}/{collection_id}", body)

    def delete(self, collection_id: str):
        """Delete a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{collection_id}")

    def list(self, query: CollectionListQuery | None = None):
        """List collections.
        https://developer.rechargepayments.com/2021-11/collections/collections_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def list_products(self, query: CollectionListProductsQuery | None = None):
        """List products in a collection.
        https://developer.rechargepayments.com/2021-11/collections/collection_products
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self.check_scopes("GET /collection_products", required_scopes)

        return self._http_get(f"{self.base_url}/collection_products", query)

    def add_products(self, collection_id: str, body: CollectionAddProductsBody):
        """Add products to a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_add
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        return self._http_post(f"{self.url}/{collection_id}/products", body)

    def delete_products(self, collection_id: str, body: CollectionDeleteProductsBody):
        """Delete products from a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        return self._http_delete(
            f"{self.url}/{collection_id}/collection_products-bulk", body
        )
