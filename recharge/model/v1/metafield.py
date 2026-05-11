from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

MetafieldOwnerResource = Literal[
    "address", "store", "customer", "subscription", "order", "charge"
]

MetafieldValueType = Literal["string", "json_string", "integer"]


class Metafield(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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
