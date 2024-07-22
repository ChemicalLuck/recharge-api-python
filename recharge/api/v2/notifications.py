from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.notification import (
    NotificationTemplateType,
    NotificationTemplateVars,
)


class NotificationSendEmailBody(TypedDict):
    type: Literal["email"]
    template_type: NotificationTemplateType
    template_vars: NotificationTemplateVars


class NotificationResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/notifications
    """

    object_list_key = "notifications"
    object_dict_key = "notification"
    recharge_version: RechargeVersion = "2021-11"

    def send_email(self, customer_id: str, body: NotificationSendEmailBody) -> dict:
        """
        Send an email notification to a customer.
        https://developer.rechargepayments.com/2021-11/notifications/notifications_send
        """
        required_scopes: list[RechargeScope] = ["write_notifications"]
        self._check_scopes(
            f"POST /customers/:customer_id/{self.object_list_key}", required_scopes
        )

        url = f"{self.base_url}/customers/{customer_id}/{self.object_list_key}"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data
