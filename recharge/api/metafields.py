from recharge.api import RechargeResource
from recharge.api.tokens import TokenScope

from typing import TypedDict, Required, Literal

type MetafieldOwnerResource = Literal[
    "address", "store", "customer", "subscription", "order", "charge"
]

type MetafieldValueType = Literal["string", "json_string", "integer"]


class MetafieldCreateBody(TypedDict):
    description: str
    key: Required[str]
    namespace: Required[str]
    owner_id: Required[int]
    owner_resource: Required[MetafieldOwnerResource]
    value: Required[str]
    value_type: Required[MetafieldValueType]


class MetafieldUpdateBody(TypedDict):
    description: str
    owner_id: str
    owner_resource: MetafieldOwnerResource
    value: str
    value_type: MetafieldValueType


class MetafieldListQuery(TypedDict):
    limit: str
    namespace: str
    owner_id: str
    owner_resource: MetafieldOwnerResource
    page: str


class MetafieldCountQuery(TypedDict):
    namespace: str
    owner_id: str
    owner_resource: MetafieldOwnerResource


MetafieldOwnerResourceScopeMap: dict[str, dict[str, TokenScope]] = {
    "address": {
        "read": "read_customers",
        "write": "write_customers",
    },
    "store": {
        "read": "store_info",
    },
    "customer": {
        "read": "read_customers",
        "write": "write_customers",
    },
    "subscription": {
        "read": "read_subscriptions",
        "write": "write_subscriptions",
    },
    "order": {
        "read": "read_orders",
        "write": "write_orders",
    },
    "charge": {
        "read": "read_orders",
        "write": "write_orders",
    },
}

type ScopeType = Literal["read", "write"]


def resource_scope(
    owner_resource: MetafieldOwnerResource, type: ScopeType
) -> TokenScope:
    return MetafieldOwnerResourceScopeMap[owner_resource][type]


class MetafieldResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/metafields
    """

    object_list_key = "metafields"

    def create(self, body: MetafieldCreateBody):
        """Create a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_create
        """
        resource = body["owner_resource"]

        required_scopes: list[TokenScope] = [resource_scope(resource, "write")]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self.http_post(self.url, body)

    def get(self, metafield_id: str, resource: MetafieldOwnerResource):
        """Get a metafield by ID.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_retrieve
        """
        required_scopes: list[TokenScope] = [resource_scope(resource, "read")]
        self.check_scopes(f"GET /{self.object_list_key}/:metafield_id", required_scopes)

        return self.http_get(f"{self.url}/{metafield_id}")

    def update(self, metafield_id: str, body: MetafieldUpdateBody):
        """Update a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_update
        """
        resource = body["owner_resource"]
        required_scopes: list[TokenScope] = [resource_scope(resource, "write")]
        self.check_scopes(f"PUT /{self.object_list_key}/:metafield_id", required_scopes)

        return self.http_put(f"{self.url}/{metafield_id}", body)

    def delete(self, metafield_id: str, resource: MetafieldOwnerResource):
        """Delete a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_delete
        """
        required_scopes: list[TokenScope] = [resource_scope(resource, "write")]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:metafield_id", required_scopes
        )

        return self.http_delete(f"{self.url}/{metafield_id}")

    def list(self, query: MetafieldListQuery):
        """List metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_list
        """
        resource = query["owner_resource"]
        required_scopes: list[TokenScope] = [resource_scope(resource, "read")]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self.http_get(self.url, query)

    def count(self, query: MetafieldCountQuery):
        """Retrieve a count of metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_count
        """
        resource = query["owner_resource"]
        required_scopes: list[TokenScope] = [resource_scope(resource, "read")]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self.http_get(f"{self.url}/count", query)
