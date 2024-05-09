from typing import Literal, Required, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope


ChargeStatus: TypeAlias = Literal[
    "SUCCESS", "QUEUED", "ERROR", "REFUNDED", "PARTIALLY_REFUNDED", "SKIPPED"
]


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


class ChargeSkupSubscriptionIds(TypedDict, total=True):
    subscription_ids: list[str]


ChargeSkipBody: TypeAlias = ChargeSkipSubscriptionId | ChargeSkupSubscriptionIds


class ChargeRefundBody(TypedDict, total=False):
    amount: Required[str]
    full_refund: bool


class ChargeApplyDiscountCodeBody(TypedDict):
    discount_code: str


class ChargeApplyDiscountIdBody(TypedDict):
    discount_id: str


ChargeApplyDiscountBody: TypeAlias = (
    ChargeApplyDiscountCodeBody | ChargeApplyDiscountIdBody
)


class ChargeResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/charges
    """

    object_list_key = "charges"

    def get(self, charge_id: str):
        """Get a charge by id.
        https://developer.rechargepayments.com/2021-01/charges/charge_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/:charge_id", required_scopes)

        return self._http_get(f"{self.url}/{charge_id}")

    def list(self, query: ChargeListQuery | None = None):
        """List charges.
        https://developer.rechargepayments.com/2021-01/charges/charge_list
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)

    def count(self, query: ChargeCountQuery | None = None):
        """Count charges.
        https://developer.rechargepayments.com/2021-01/charges/charge_count
        """
        required_scopes: list[RechargeScope] = ["read_orders"]
        self.check_scopes(f"GET /{self.object_list_key}/count", required_scopes)

        return self._http_get(f"{self.url}/count", query)

    def change_next_charge_date(
        self, charge_id: str, body: ChargeChangeNextChargeDateBody
    ):
        """Change the date of a queued charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_change_next_date
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/change_next_charge_date",
            required_scopes,
        )

        return self._http_put(f"{self.url}/{charge_id}/change_next_charge_date", body)

    def skip(self, charge_id: str, body: ChargeSkipBody):
        """Skip a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_skip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/skip", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/skip", body)

    def unskip(self, charge_id: str, body: ChargeSkipBody):
        """Unskip a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_unskip
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/unskip", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/unskip", body)

    def refund(self, charge_id: str, body: ChargeRefundBody):
        """Refund a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_refund
        """
        required_scopes: list[RechargeScope] = ["write_orders", "write_payments"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/refund", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/refund", body)

    def process(self, charge_id: str):
        """Process a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_process
        """
        required_scopes: list[RechargeScope] = ["write_payments"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/process", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/process", None)

    def capture(self, charge_id: str):
        """Capture a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_capture
        """
        required_scopes: list[RechargeScope] = [
            "write_orders",
            "write_payments",
            "write_subscriptions",
            "write_customers",
        ]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/capture", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/capture_payment", None)

    def apply_discount(self, charge_id: str, body: ChargeApplyDiscountBody):
        """Apply a discount to a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_apply_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/apply_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/apply_discount", body)

    def remove_discount(self, charge_id: str):
        """Remove a discount from a charge.
        https://developer.rechargepayments.com/2021-01/charges/charge_remove_discount
        """
        required_scopes: list[RechargeScope] = ["write_orders"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:charge_id/remove_discount", required_scopes
        )

        return self._http_post(f"{self.url}/{charge_id}/remove_discount")
