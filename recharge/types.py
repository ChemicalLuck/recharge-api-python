from typing import Literal

RechargeVersion = Literal["2021-01", "2021-11"]

RechargeScope = Literal[
    "write_orders",
    "read_orders",
    "read_discounts",
    "write_discounts",
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
    "read_bundle_products",
    "read_credit_summary",
    "write_free_gifts",
]
