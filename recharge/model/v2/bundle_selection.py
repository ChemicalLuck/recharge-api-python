from typing import TypedDict


class BundleSelectionItem(TypedDict):
    id: int
    collection_id: str
    collection_source: str
    created_at: str
    external_product_id: str
    external_variant_id: str
    quantity: int
    updated_at: str


class BundleSelection(TypedDict):
    id: int
    bundle_variant_id: int
    purchase_item_id: int
    created_at: str
    external_product_id: str
    external_variant_id: str
    items: list[BundleSelectionItem]
    updated_at: str
