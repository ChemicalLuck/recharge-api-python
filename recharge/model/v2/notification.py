from typing import Literal, Optional

from recharge.model.base import RechargeModel

NotificationTemplateType = Literal[
    "upcoming_charge", "get_account_access", "shopify_update_payment_information"
]


class NotificationTemplateVars(RechargeModel):
    address_id: Optional[int] = None
    charge_id: Optional[int] = None
