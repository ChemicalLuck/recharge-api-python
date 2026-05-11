from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

CollectionSortOrder = Literal[
    "id-asc", "id-desc", "title-asc", "title-desc", "created-asc", "created-desc"
]


class Collection(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    created_at: Optional[str] = None
    description: Optional[str] = None
    sort_order: Optional[CollectionSortOrder] = None
    title: Optional[str] = None
    type: Optional[Literal["manual"]] = None
    updated_at: Optional[str] = None


class CollectionProduct(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    collection_id: Optional[int] = None
    created_at: Optional[str] = None
    external_product_id: Optional[int] = None
    updated_at: Optional[str] = None
