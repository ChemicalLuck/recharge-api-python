from typing import Literal, TypedDict

CollectionSortOrder = Literal[
    "id-asc", "id-desc", "title-asc", "title-desc", "created-asc", "created-desc"
]


class Collection(TypedDict):
    id: int
    created_at: str
    description: str
    sort_order: CollectionSortOrder
    title: str
    type: Literal["manual"]
    updated_at: str


class CollectionProduct(TypedDict):
    collection_id: int
    created_at: str
    external_product_id: int
    updated_at: str
