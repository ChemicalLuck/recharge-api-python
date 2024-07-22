from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.discount import (
    Discount,
    DiscountAppliesToResource,
    DiscountChannelSettings,
    DiscountFirstTimeCustomerRestriction,
    DiscountProductType,
    DiscountStatus,
    DiscountType,
)


class DiscountCreateBodyOptional(TypedDict, total=False):
    applies_to_id: int
    duration: str
    duration_usage_limit: int
    ends_at: str
    once_per_customer: bool
    prerequisite_subtotal_min: int
    usage_limit: int


class DiscountCreateBody(DiscountCreateBodyOptional):
    applies_to_product_type: DiscountProductType
    applies_to_resource: DiscountAppliesToResource
    channel_settings: DiscountChannelSettings
    code: str
    discount_type: DiscountType
    first_time_customer_restriction: DiscountFirstTimeCustomerRestriction
    starts_at: str
    status: DiscountStatus
    value: str


class DiscountUpdateBody(TypedDict, total=False):
    channel_settings: DiscountChannelSettings
    ends_at: str
    starts_at: str
    status: DiscountStatus
    usage_limit: int


class DiscountDeleteBody(TypedDict):
    discount_id: str


class DiscountListQuery(TypedDict, total=False):
    created_at_max: str
    created_at_min: str
    discount_code: str
    discount_type: DiscountType
    ids: str
    limit: str
    page: str
    status: DiscountStatus
    updated_at_max: str
    updated_at_min: str


class DiscountCountQuery(TypedDict, total=False):
    created_at_max: str
    created_at_min: str
    discount_type: DiscountType
    status: DiscountStatus
    updated_at_max: str
    updated_at_min: str


class DiscountResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/discounts
    """

    object_list_key = "discounts"
    object_dict_key = "discount"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: DiscountCreateBody) -> Discount:
        """Create a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_create
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Discount(**data)

    def get(self, discount_id: str) -> Discount:
        """Get a discount by ID.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self._check_scopes(f"GET /{self.object_list_key}/:discount_id", required_scopes)

        url = f"{self._url}/{discount_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Discount(**data)

    def update(self, discount_id: str, body: DiscountUpdateBody) -> Discount:
        """Update a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_update
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self._check_scopes(f"PUT /{self.object_list_key}/:discount_id", required_scopes)

        url = f"{self._url}/{discount_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Discount(**data)

    def delete(self, discount_id: str) -> dict:
        """Delete a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_delete
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:discount_id", required_scopes
        )

        url = f"{self._url}/{discount_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self, query: Optional[DiscountListQuery] = None) -> list[Discount]:
        """List discounts.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_list
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Discount(**item) for item in data]

    def list_all(self, query: Optional[DiscountListQuery] = None) -> list[Discount]:
        """List all discounts.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_list
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Discount(**item) for item in data]

    def count(self, query: Optional[DiscountCountQuery] = None) -> int:
        """Receive a count of all discounts.
        https://developer.rechargepayments.com/v1#count-discounts
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in response, got {data}")
        return data["count"]
