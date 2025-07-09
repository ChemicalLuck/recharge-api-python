from typing import Literal, Optional, TypedDict, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.charge import Charge, ChargeStatus

ChargeListSortBy = Literal[
    "id-asc",
    "id-desc",
    "updated_at-asc",
    "updated_at-desc",
    "scheduled_at-asc",
    "scheduled_at-desc",
]


class ChargeListQuery(TypedDict, total=False):
    address_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    discount_code: str
    discount_id: str
    external_order_id: str
    ids: str
    limit: str
    page: str
    purchase_item_id: str
    purchase_item_ids: str
    scheduled_at: str
    scheduled_at_max: str
    scheduled_at_min: str
    sort_by: ChargeListSortBy
    status: ChargeStatus
    updated_at_max: str
    updated_at_min: str
    processed_at_min: str
    processed_at_max: str


class ChargeDiscountApplyDiscountCode(TypedDict):
    discount_code: str


class ChargeDiscountApplyDiscountId(TypedDict):
    discount_id: str


ChargeDiscountApplyBody = Union[
    ChargeDiscountApplyDiscountCode, ChargeDiscountApplyDiscountId
]


class ChargeSkipSubscriptionId(TypedDict, total=True):
    purchase_item_id: str


class ChargeSkipSubscriptionIds(TypedDict, total=True):
    purchase_item_ids: list[str]


ChargeSkipBody = Union[ChargeSkipSubscriptionId, ChargeSkipSubscriptionIds]


class ChargeRefundBodyOptional(TypedDict, total=False):
    full_refund: bool
    retry: bool
    error: str
    error_type: str


class ChargeRefundBody(ChargeRefundBodyOptional):
    amount: str


class ChargeResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/charges
    """

    object_list_key = "charges"
    object_dict_key = "charge"
    recharge_version: RechargeVersion = "2021-11"

    def get(self, charge_id: str) -> Charge:
        """Get a charge by id.
        https://developer.rechargepayments.com/2021-11/charges/charge_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/:charge_id", required_scopes)

        url = f"{self._url}/{charge_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def list_(self, query: Optional[ChargeListQuery] = None) -> list[Charge]:
        """List charges.
        https://developer.rechargepayments.com/2021-11/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Charge(**item) for item in data]

    def list_all(self, query: Optional[ChargeListQuery] = None) -> list[Charge]:
        """List all charges.
        https://developer.rechargepayments.com/2021-11/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Charge(**item) for item in data]

    def apply_discount(self, charge_id: str, body: ChargeDiscountApplyBody) -> Charge:
        """Apply a discount to a charge.
        https://developer.rechargepayments.com/2021-11/charges/apply_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/apply_discount", required_scopes
        )

        url = f"{self._url}/{charge_id}/apply_discount"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def remove_discount(self, charge_id: str) -> Charge:
        """Remove a discount from a charge.
        https://developer.rechargepayments.com/2021-11/charges/remove_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/remove_discount", required_scopes
        )

        url = f"{self._url}/{charge_id}/remove_discount"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def skip(self, charge_id: str, body: ChargeSkipBody) -> Charge:
        """Skip a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_skip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/skip", required_scopes
        )

        url = f"{self._url}/{charge_id}/skip"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def unskip(self, charge_id: str, body: ChargeSkipBody) -> Charge:
        """Unskip a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_unskip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/unskip", required_scopes
        )

        url = f"{self._url}/{charge_id}/unskip"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def refund(self, charge_id: str, body: ChargeRefundBody) -> Charge:
        """Refund a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_refund
        """
        required_scopes: list[RechargeScope] = ["write_orders", "write_payment_methods"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/refund", required_scopes
        )

        url = f"{self._url}/{charge_id}/refund"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def process(self, charge_id: str) -> Charge:
        """Process a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_process
        """
        required_scopes: list[RechargeScope] = ["write_payments"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/process", required_scopes
        )

        url = f"{self._url}/{charge_id}/process"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def capture(self, charge_id: str) -> Charge:
        """Capture a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_capture
        """
        required_scopes: list[RechargeScope] = [
            "write_orders",
            "write_payment_methods",
            "write_subscriptions",
            "write_customers",
        ]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/capture", required_scopes
        )

        url = f"{self._url}/{charge_id}/capture_payment"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)
