from typing import Literal, Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.bundle_selection import BundleSelection

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
    object_dict_key = "bundle_selection"
    recharge_version: RechargeVersion = "2021-11"

    def list_(
        self, query: Optional[BundleSelectionListQuery] = None
    ) -> list[BundleSelection]:
        """List bundle selections.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [BundleSelection(**item) for item in data]

    def list_all(self) -> list[BundleSelection]:
        """List all bundle selections.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [BundleSelection(**item) for item in data]

    def get(self, bundle_selection_id: str) -> BundleSelection:
        """Get a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        url = f"{self._url}/{bundle_selection_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return BundleSelection(**data)

    def create(self, body: BundleSelectionCreateBody) -> BundleSelection:
        """Create a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_create
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return BundleSelection(**data)

    def update(
        self, bundle_selection_id: str, body: BundleSelectionUpdateBody
    ) -> BundleSelection:
        """Update a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_update
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        url = f"{self._url}/{bundle_selection_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return BundleSelection(**data)

    def delete(self, bundle_selection_id: str) -> dict:
        """Delete a bundle selection.
        https://developer.rechargepayments.com/2021-11/bundle_selections/bundle_selections_delete
        """
        required_scopes: list[RechargeScope] = ["write_subscriptions"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:bundle_selection_id", required_scopes
        )

        url = f"{self._url}/{bundle_selection_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data
