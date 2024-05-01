from typing import Literal, Required, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope

DiscountProductType: TypeAlias = Literal["ALL", "ONETIME", "SUBSCRIPTION"]

DiscountAppliesToResource: TypeAlias = Literal[
    "shopify_product", "shopify_collection_id"
]


class DiscountChannelSettingsValue:
    can_apply: bool


class DiscountChannelSettings(TypedDict, total=False):
    api: DiscountChannelSettingsValue
    checkout_page: DiscountChannelSettingsValue
    customer_portal: DiscountChannelSettingsValue
    merchant_portal: DiscountChannelSettingsValue


DiscountType: TypeAlias = Literal["percentage", "fixed_amount"]

DiscountFirstTimeCustomerRestriction: TypeAlias = Literal[
    "null", "customer_must_not_exist_in_recharge"
]

DiscountStatus: TypeAlias = Literal["enabled", "disabled", "fully_disabled"]


class DiscountCreateBody(TypedDict, total=False):
    applies_to_id: int
    applies_to_product_type: DiscountProductType
    applies_to_resource: DiscountAppliesToResource
    channel_settings: DiscountChannelSettings
    code: Required[str]
    discount_type: DiscountType
    duration: str
    duration_usage_limit: int
    ends_at: str
    first_time_customer_restriction: DiscountFirstTimeCustomerRestriction
    once_per_customer: bool
    prerequisite_subtotal_min: int
    starts_at: str
    status: DiscountStatus
    usage_limit: int
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

    def create(self, body: DiscountCreateBody):
        """Create a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_create
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, discount_id: str):
        """Get a discount by ID.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self.check_scopes(f"GET /{self.object_list_key}/:discount_id", required_scopes)

        return self._http_get(f"{self.url}/{discount_id}")

    def update(self, discount_id: str, body: DiscountUpdateBody):
        """Update a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_update
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self.check_scopes(f"PUT /{self.object_list_key}/:discount_id", required_scopes)

        return self._http_put(f"{self.url}/{discount_id}", body)

    def delete(self, discount_id: str):
        """Delete a discount.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_delete
        """
        required_scopes: list[RechargeScope] = ["write_discounts"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:discount_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{discount_id}")

    def list(self, query: DiscountListQuery | None = None):
        """List discounts.
        https://developer.rechargepayments.com/2021-01/discounts/discounts_list
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def count(self, query: DiscountCountQuery | None = None):
        """Receive a count of all discounts.
        https://developer.rechargepayments.com/v1#count-discounts
        """
        required_scopes: list[RechargeScope] = ["read_discounts"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)
