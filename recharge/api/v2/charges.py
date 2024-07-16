from typing import Literal, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


ChargeStatus: TypeAlias = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]

ChargeListSortBy: TypeAlias = Literal[
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


ChargeDiscountApplyBody: TypeAlias = (
    ChargeDiscountApplyDiscountCode | ChargeDiscountApplyDiscountId
)


class ChargeSkipSubscriptionId(TypedDict, total=True):
    subscription_id: str


class ChargeSkupSubscriptionIds(TypedDict, total=True):
    subscription_ids: list[str]


ChargeSkipBody: TypeAlias = ChargeSkipSubscriptionId | ChargeSkupSubscriptionIds

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
    recharge_version: RechargeVersion = "2021-11"

    def get(self, charge_id: str):
        """Get a charge by id.
        https://developer.rechargepayments.com/2021-11/charges/charge_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/:charge_id", required_scopes)

        return self._http_get(f"{self.url}/{charge_id}")

    def list_(self, query: ChargeListQuery | None = None):
        """List charges.
        https://developer.rechargepayments.com/2021-11/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def apply_discount(self, charge_id: str, body: ChargeDiscountApplyBody):
        """Apply a discount to a charge.
        https://developer.rechargepayments.com/2021-11/charges/apply_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/apply_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/apply_discount", body)

    def remove_discount(self, charge_id: str):
        """Remove a discount from a charge.
        https://developer.rechargepayments.com/2021-11/charges/remove_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/remove_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/remove_discount", None)

    def skip(self, charge_id: str, body: ChargeSkipBody):
        """Skip a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_skip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/skip", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/skip", body)

    def unskip(self, charge_id: str, body: ChargeSkipBody):
        """Unskip a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_unskip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/unskip", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/unskip", body)

    def refund(self, charge_id: str, body: ChargeRefundBody):
        """Refund a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_refund
        """
        required_scopes: list[RechargeScope] = ["write_orders", "write_payment_methods"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/refund", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/refund", body)

    def process(self, charge_id: str):
        """Process a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_process
        """
        required_scopes: list[RechargeScope] = ["write_payments"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/process", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/process", None)

    def capture(self, charge_id: str):
        """Capture a charge.
        https://developer.rechargepayments.com/2021-11/charges/charge_capture
        """
        required_scopes: list[RechargeScope] = [
            "write_orders",
            "write_payment_methods",
            "write_subscriptions",
            "write_customers",
        ]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/capture", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/capture_payment", None)
