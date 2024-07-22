from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.collection import (
    Collection,
    CollectionProduct,
    CollectionSortOrder,
)


class CollectionCreateBodyOptional(TypedDict, total=False):
    sort_order: CollectionSortOrder


class CollectionCreateBody(CollectionCreateBodyOptional):
    description: str
    titel: str


class CollectionUpdateBody(TypedDict, total=False):
    description: str
    sort_order: CollectionSortOrder
    title: str


class CollectionListQuery(TypedDict, total=False):
    title: str


class CollectionListProductsQuery(TypedDict, total=False):
    collection_id: int


class CollectionBodyProduct(TypedDict):
    external_product_id: str


class CollectionAddProductsBody(TypedDict):
    collection_products: list[CollectionBodyProduct]


class CollectionDeleteProductsBody(TypedDict):
    collection_products: list[CollectionBodyProduct]


class CollectionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/collections
    """

    object_list_key = "collections"
    object_dict_key = "collection"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: CollectionCreateBody) -> Collection:
        """Create a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_create
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Collection(**data)

    def get(self, collection_id: str) -> Collection:
        """Get a collection by ID.
        https://developer.rechargepayments.com/2021-11/collections/collections_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:collection_id", required_scopes
        )

        url = f"{self._url}/{collection_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Collection(**data)

    def update(self, collection_id: str, body: CollectionUpdateBody) -> Collection:
        """Update a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_update
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:collection_id", required_scopes
        )

        url = f"{self._url}/{collection_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Collection(**data)

    def delete(self, collection_id: str) -> dict:
        """Delete a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id", required_scopes
        )

        url = f"{self._url}/{collection_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[CollectionListQuery] = None) -> list[Collection]:
        """List collections.
        https://developer.rechargepayments.com/2021-11/collections/collections_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Collection(**item) for item in data]

    def list_all(self, query: Optional[CollectionListQuery] = None) -> list[Collection]:
        """List all collections.
        https://developer.rechargepayments.com/2021-11/collections/collections_list
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Collection(**item) for item in data]

    def list_products(
        self, query: Optional[CollectionListProductsQuery] = None
    ) -> list[CollectionProduct]:
        """List products in a collection.
        https://developer.rechargepayments.com/2021-11/collections/collection_products
        """
        required_scopes: list[RechargeScope] = ["read_products"]
        self._check_scopes("GET /collection_products", required_scopes)

        url = f"{self.base_url}/collection_products"
        data = self._http_get(url, query, list, response_key="collection_products")
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [CollectionProduct(**item) for item in data]

    def add_products(
        self, collection_id: str, body: CollectionAddProductsBody
    ) -> list[CollectionProduct]:
        """Add products to a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_add
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        url = f"{self._url}/{collection_id}/products"
        data = self._http_post(
            url, body, expected=list, response_key="collection_products"
        )
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [CollectionProduct(**item) for item in data]

    def delete_products(
        self, collection_id: str, body: CollectionDeleteProductsBody
    ) -> dict:
        """Delete products from a collection.
        https://developer.rechargepayments.com/2021-11/collections/collections_products_delete
        """
        required_scopes: list[RechargeScope] = ["write_products"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:collection_id/collection_products-bulk",
            required_scopes,
        )

        url = f"{self._url}/{collection_id}/products"
        data = self._http_delete(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data
