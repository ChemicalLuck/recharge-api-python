from typing import Literal, TypeAlias, TypedDict

from recharge.api import RechargeResource, RechargeScope


NotificationTemplateType: TypeAlias = Literal["upcoming_charge", "get_account_access"]


class NotificationTemplateVars(TypedDict, total=False):
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
        required_scopes: list[RechargeScope] = ["write_notifications"]
        self.check_scopes("POST /customers/:customer_id/notifications", required_scopes)

        return self._http_post(
            f"{self.url}/customers/{customer_id}/notifications", body
        )
