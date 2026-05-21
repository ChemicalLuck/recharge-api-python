from typing import Literal, Optional

from recharge.model.base import RechargeModel

CollectionSortOrder = Literal[
    "id-asc", "id-desc", "title-asc", "title-desc", "created-asc", "created-desc"
]


class Collection(RechargeModel):
    id: int
    created_at: Optional[str] = None
    description: Optional[str] = None
    sort_order: Optional[CollectionSortOrder] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None


class CollectionProduct(RechargeModel):
    collection_id: Optional[int] = None
    created_at: Optional[str] = None
    external_product_id: Optional[int] = None
    updated_at: Optional[str] = None
