from typing import Literal, TypedDict

NotificationTemplateType = Literal[
    "upcoming_charge", "get_account_access", "shopify_update_payment_information"
]


class NotificationTemplateVars(TypedDict, total=False):
    address_id: int
    charge_id: int
