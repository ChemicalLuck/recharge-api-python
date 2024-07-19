from typing import Literal, TypedDict

MetafieldOwnerResource = Literal[
    "address", "store", "customer", "subscription", "order", "charge"
]

MetafieldValueType = Literal["string", "json_string", "integer"]


class Metafield(TypedDict):
    id: int
    created_at: str
    description: str
    key: str
    namespace: str
    owner_id: str
    owner_resource: MetafieldOwnerResource
    updated_at: str
    value: str
    value_type: MetafieldValueType
