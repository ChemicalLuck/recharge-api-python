from typing import Literal, TypedDict

from recharge.api import RechargeResource
from recharge.api.tokens import TokenScope

type NotificationTemplateType = Literal["upcoming_charge", "get_account_access"]


class NotificationTemplateVars(TypedDict):
    address_id: int
    charge_id: int


class NotificationSendEmailBody(TypedDict):
    type: Literal["email"]
    template_type: NotificationTemplateType
    template_vars: NotificationTemplateVars


class NotificationResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/notifications
    """

    def send_email(self, customer_id, body: NotificationSendEmailBody):
        """
        Send an email notification to a customer.
        https://developer.rechargepayments.com/2021-01/notifications/notifications_get_account_access
        """
        required_scopes: list[TokenScope] = ["write_notifications"]
        self.check_scopes(
            f"POST /customers/{customer_id}/notifications", required_scopes
        )

        return self.http_post(f"{self.url}/customers/{customer_id}/notifications", body)
