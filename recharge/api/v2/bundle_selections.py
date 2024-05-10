from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

BundleSelectionListSortBy = Literal[
    "id-asc", "id-desc", "updated_at-asc", "updated_at-desc"
]


class BundleSelectionListQuery(TypedDict, total=False):
    purchase_item_ids: str
    bundle_variant_ids: str
    item_external_variant_ids: str
    item_external_product_ids: str
    limit: str
    page: str
    sort_by: BundleSelectionListSortBy
    active_purchase_items: bool


class BundleSelectionCreateItem(TypedDict, total=False):
    collection_id: str
    collection_source: str
    external_product_id: str
    external_variant_id: str
    quantity: int


class BundleSelectionCreateBody(TypedDict):
    purchase_item_id: int
    items: list[BundleSelectionCreateItem]


class BundleSelectionUpdateBody(TypedDict, total=False):
    purchase_item_id: int
    items: list[BundleSelectionCreateItem]


class BundleSelectionResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/bundle_selections
    """

    object_list_key = "bundle_selections"
    recharge_version: RechargeVersion = "2021-11"

    def list(self, query: BundleSelectionListQuery | None = None):
        """List bundle selections.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def get(self, bundle_selection_id: str):
        """Get a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        return self._http_get(f"{self.url}/{bundle_selection_id}")

    def create(self, body: BundleSelectionCreateBody):
        """Create a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def update(self, bundle_selection_id: str, body: BundleSelectionUpdateBody):
        """Update a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        return self._http_put(f"{self.url}/{bundle_selection_id}", body)

    def delete(self, bundle_selection_id: str):
        """Delete a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{bundle_selection_id}")
