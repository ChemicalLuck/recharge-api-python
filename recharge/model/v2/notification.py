from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

NotificationTemplateType = Literal[
    "upcoming_charge", "get_account_access", "shopify_update_payment_information"
]


class NotificationTemplateVars(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    address_id: Optional[int] = None
    charge_id: Optional[int] = None
