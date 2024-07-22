from typing import Optional, TypedDict, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.charge import Charge, ChargeStatus


class ChargeListQuery(TypedDict, total=False):
    address_id: str
    created_at_max: str
    created_at_min: str
    customer_id: str
    date: str
    date_max: str
    date_min: str
    discount_code: str
    discount_id: str
    ids: str
    limit: int
    page: int
    shopify_order_id: str
    status: ChargeStatus
    subscription_id: str
    updated_at_max: str
    updated_at_min: str


class ChargeCountQuery(TypedDict, total=False):
    address_id: str
    customer_id: str
    date: str
    date_max: str
    date_min: str
    discount_id: str
    shopify_order_id: str
    status: ChargeStatus
    subscription_id: str


class ChargeChangeNextChargeDateBody(TypedDict, total=True):
    next_charge_date: str


class ChargeSkipSubscriptionId(TypedDict, total=True):
    subscription_id: str


class ChargeSkipSubscriptionIds(TypedDict, total=True):
    subscription_ids: list[str]


ChargeSkipBody = Union[ChargeSkipSubscriptionId, ChargeSkipSubscriptionIds]


class ChargeRefundBodyOptional(TypedDict, total=False):
    full_refund: bool


class ChargeRefundBody(ChargeRefundBodyOptional):
    amount: str


class ChargeApplyDiscountCodeBody(TypedDict):
    discount_code: str


class ChargeApplyDiscountIdBody(TypedDict):
    discount_id: str


ChargeApplyDiscountBody = Union[ChargeApplyDiscountCodeBody, ChargeApplyDiscountIdBody]


class ChargeResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/charges
    """

    object_list_key = "charges"
    object_dict_key = "charge"
    recharge_version: RechargeVersion = "2021-01"

    def get(self, charge_id: str) -> Charge:
        """Get a charge by id.
        https://developer.rechargepayments.com/2021-01/charges/charge_retrieve
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
        https://developer.rechargepayments.com/2021-01/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Charge(**item) for item in data]

    def list_all(self, query: Optional[ChargeListQuery] = None) -> list[Charge]:
        """List all charges.
        https://developer.rechargepayments.com/2021-01/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Charge(**item) for item in data]

    def count(self, query: Optional[ChargeCountQuery] = None) -> int:
        """Count charges.
        https://developer.rechargepayments.com/2021-01/charges/charge_count
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self._check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        url = f"{self._url}/count"
        data = self._http_get(url, query)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' key in response, got {data}")
        return data["count"]

    def change_next_charge_date(
        self, charge_id: str, body: ChargeChangeNextChargeDateBody
    ) -> Charge:
        """Change the date of a queued charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_change_next_date
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/change_next_charge_date",
            required_scopes,
        )

        url = f"{self._url}/{charge_id}/change_next_charge_date"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def skip(self, charge_id: str, body: ChargeSkipBody) -> Charge:
        """Skip a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_skip
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
        https://developer.rechargepayments.com/2021-01/charges/charge_unskip
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
        https://developer.rechargepayments.com/2021-01/charges/charge_refund
        """
        required_scopes: list[RechargeScope] = ["write_orders", "write_payments"]
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
        https://developer.rechargepayments.com/2021-01/charges/charge_process
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
        https://developer.rechargepayments.com/2021-01/charges/charge_capture
        """
        required_scopes: list[RechargeScope] = [
            "write_orders",
            "write_payments",
            "write_subscriptions",
            "write_customers",
        ]
        self._check_scopes(
            f"POST /{self.object_list_key}/:charge_id/capture", required_scopes
        )

        url = f"{self._url}/{charge_id}/capture"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Charge(**data)

    def apply_discount(self, charge_id: str, body: ChargeApplyDiscountBody) -> Charge:
        """Apply a discount to a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_apply_discount
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
        https://developer.rechargepayments.com/2021-01/charges/charge_remove_discount
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
