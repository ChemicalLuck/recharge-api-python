from typing import TypedDict, Literal, Optional

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

CollectionCreateSortOrder = Literal[
    "id-asc", "id-desc", "title-asc", "title-desc", "created-asc", "created-desc"
]


class CollectionCreateBodyOptional(TypedDict, total=False):
    sort_order: CollectionCreateSortOrder


class CollectionCreateBody(CollectionCreateBodyOptional):
    description: str
    titel: str


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
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: CollectionCreateBody):
        """Create a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self._url, body)

    def get(self, collection_id: str):
        """Get a collection by ID.
        https://developer.rechargepayments.com/2021-11/collections/collections_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_get(f"{self._url}/{collection_id}")

    def update(self, collection_id: str, body: CollectionUpdateBody):
        """Update a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_put(f"{self._url}/{collection_id}", body)

    def delete(self, collection_id: str):
        """Delete a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id", required_scopes
        )

        return self._http_delete(f"{self._url}/{collection_id}")

    def list_(self, query: Optional[CollectionListQuery] = None):
        """List collections.
        https://developer.rechargepayments.com/2021-11/collections/collections_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self._url, query)

    def list_products(self, query: Optional[CollectionListProductsQuery] = None):
        """List products in a collection.
        https://developer.rechargepayments.com/2021-11/collections/collection_products
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes("GET /collection_products", required_scopes)

        return self._http_get(f"{self.base_url}/collection_products", query)

    def add_products(self, collection_id: str, body: CollectionAddProductsBody):
        """Add products to a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_add
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        return self._http_post(f"{self._url}/{collection_id}/products", body)

    def delete_products(self, collection_id: str, body: CollectionDeleteProductsBody):
        """Delete products from a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        return self._http_delete(
            f"{self._url}/{collection_id}/collection_products-bulk", body
        )
