from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.metafield import (
    Metafield,
    MetafieldOwnerResource,
    MetafieldValueType,
)


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


class MetafieldCountQueryOptional(TypedDict, total=False):
    namespace: str
    owner_id: str


class MetafieldCountQuery(MetafieldCountQueryOptional):
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
    owner_resource: MetafieldOwnerResource, type_: ScopeType
) -> RechargeScope:
    return MetafieldOwnerResourceScopeMap[owner_resource][type_]


class MetafieldResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/metafields
    """

    object_list_key = "metafields"
    object_dict_key = "metafield"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: MetafieldCreateBody) -> Metafield:
        """Create a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_create
        """
        resource = body["owner_resource"]

        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Metafield(**data)

    def get(self, metafield_id: str, resource: MetafieldOwnerResource) -> Metafield:
        """Get a metafield by ID.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_retrieve
        """
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self._check_scopes(
            f"GET /{self.object_list_key}/:metafield_id", required_scopes
        )

        url = f"{self._url}/{metafield_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Metafield(**data)

    def update(self, metafield_id: str, body: MetafieldUpdateBody) -> Metafield:
        """Update a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_update
        """
        resource = body["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:metafield_id", required_scopes
        )

        url = f"{self._url}/{metafield_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Metafield(**data)

    def delete(self, metafield_id: str, resource: MetafieldOwnerResource) -> dict:
        """Delete a metafield.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_delete
        """
        required_scopes: list[RechargeScope] = [resource_scope(resource, "write")]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:metafield_id", required_scopes
        )

        url = f"{self._url}/{metafield_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: MetafieldListQuery) -> list[Metafield]:
        """List metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_list
        """
        resource = query["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Metafield(**item) for item in data]

    def list_all(self, query: MetafieldListQuery) -> list[Metafield]:
        """List all metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_list
        """
        resource = query["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Metafield(**item) for item in data]

    def count(self, query: MetafieldCountQuery) -> int:
        """Retrieve a count of metafields.
        https://developer.rechargepayments.com/2021-01/metafields/metafields_count
        """
        resource = query["owner_resource"]
        required_scopes: list[RechargeScope] = [resource_scope(resource, "read")]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in response, got {data}")
        return data["count"]
