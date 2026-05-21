from typing import Literal, Optional

from recharge.model.base import RechargeModel

MetafieldOwnerResource = Literal[
    "address", "store", "customer", "subscription", "order", "charge"
]

MetafieldValueType = Literal["string", "json_string", "integer"]


class Metafield(RechargeModel):
    id: int
    created_at: Optional[str] = None
    description: Optional[str] = None
    key: Optional[str] = None
    namespace: Optional[str] = None
    owner_id: Optional[str] = None
    owner_resource: Optional[MetafieldOwnerResource] = None
    updated_at: Optional[str] = None
    value: Optional[str] = None
    value_type: Optional[MetafieldValueType] = None
