from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

MetafieldOwnerResource = Literal[
    "address", "store", "customer", "subscription", "order", "charge"
]

MetafieldValueType = Literal["string", "json_string", "integer"]


class MetafieldCreateBodyOptional(TypedDict, total=False):
    description: str


class MetafieldCreateBody(MetafieldCreateBodyOptional):
    key: str
    namespace: str
    owner_id: int
    owner_resource: MetafieldOwnerResource
    value: str
    value_type: MetafieldValueType


class MetafieldUpdateBodyOptional(TypedDict, total=False):
    description: str
    owner_id: int
    value: str
    value_type: MetafieldValueType


class MetafieldUpdateBody(MetafieldUpdateBodyOptional):
    owner_resource: MetafieldOwnerResource


class MetafieldListQueryOptional(TypedDict, total=False):
    limit: str
    namespace: str
    owner_id: str
    page: str


class MetafieldListQuery(MetafieldListQueryOptional):
    owner_resource: MetafieldOwnerResource


MetafieldOwnerResourceScopeMap: dict[str, dict[str, RechargeScope]] = {
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

ScopeType = Literal["read", "write"]


def resource_scope(
    owner_resource: MetafieldOwnerResource, type: ScopeType
) -> RechargeScope:
    return MetafieldOwnerResourceScopeMap[owner_resource][type]


class MetafieldResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/metafields
    """

    object_list_key = "metafields"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: MetafieldCreateBody):
        """Create a metafield.
        https://developer.rechargepayments.com/2021-11/metafields/metafields_create
        """
        resource = body["owner_resource"]

        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, metafield_id: str, resource: MetafieldOwnerResource):
        """Get a metafield by ID.
        https://developer.rechargepayments.com/2021-11/metafields/metafields_retrieve
        """
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self.check_scopes(f"GET /{self.object_list_key}/:metafield_id", required_scopes)

        return self._http_get(f"{self.url}/{metafield_id}")

    def update(self, metafield_id: str, body: MetafieldUpdateBody):
        """Update a metafield.
        https://developer.rechargepayments.com/2021-11/metafields/metafields_update
        """
        resource = body["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self.check_scopes(f"PUT /{self.object_list_key}/:metafield_id", required_scopes)

        return self._http_put(f"{self.url}/{metafield_id}", body)

    def delete(self, metafield_id: str, resource: MetafieldOwnerResource):
        """Delete a metafield.
        https://developer.rechargepayments.com/2021-11/metafields/metafields_delete
        """
        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:metafield_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{metafield_id}")

    def list_(self, query: MetafieldListQuery):
        """List metafields.
        https://developer.rechargepayments.com/2021-11/metafields/metafields_list
        """
        resource = query["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
