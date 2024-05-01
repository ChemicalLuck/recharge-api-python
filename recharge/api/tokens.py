from recharge.api import RechargeResource

from typing import TypedDict, Literal


class TokenClient(TypedDict):
    name: str
    email: str


type TokenScope = Literal[
    "write_orders",
    "read_orders",
    "write_discounts",
    "read_discounts",
    "write_subscriptions",
    "read_subscriptions",
    "write_payments",
    "read_payments",
    "write_payment_methods",
    "read_payment_methods",
    "write_customers",
    "read_customers",
    "write_products",
    "read_products",
    "store_info",
    "write_batches",
    "read_batches",
    "read_accounts",
    "write_checkouts",
    "read_checkouts",
    "write_notifications",
    "read_events",
    "write_retention_strategies",
    "read_gift_purchases",
    "write_gift_purchases",
    "read_gift_purchases",
    "write_gift_purchases",
    "read_bundle_products",
]


class TokenInformation(TypedDict):
    client: TokenClient
    contact_email: str
    name: str
    scopes: list[TokenScope]


class TokenResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/token_information/token_information_object
    """

    object_list_key = "tokens_information"

    def get(self) -> TokenInformation:
        """Get token information.
        https://developer.rechargepayments.com/2021-01/token_information/token_information_retrieve
        """
        return self.http_get(f"{self.url}")
