from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.webhook import (
    Webhook,
    WebhookIncludedObject,
    WebhookTopic,
    WebhookTopicMap,
)


class WebhookCreateBodyOptional(TypedDict, total=False):
    included_objects: list[WebhookIncludedObject]
    verion: str


class WebhookCreateBody(WebhookCreateBodyOptional):
    address: str
    topic: WebhookTopic


class WebhookResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_object
    """

    object_list_key = "webhooks"
    object_dict_key = "webhook"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: WebhookCreateBody) -> Webhook:
        """Create a webhook.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_create
        """
        resource = body["topic"].split("/")[0]
        required_scopes: list[RechargeScope] = [WebhookTopicMap[resource]]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Webhook(**data)

    def get(self, webhook_id: str) -> Webhook:
        """Get a webhook.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_retrieve
        """

        url = f"{self._url}/{webhook_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Webhook(**data)

    def update(self, webhook_id: str) -> Webhook:
        """Update a webhook.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_update
        """
        url = f"{self._url}/{webhook_id}"
        data = self._http_put(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return Webhook(**data)

    def list_(self) -> list[Webhook]:
        """List webhooks.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_list
        """

        data = self._http_get(self._url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Webhook(**item) for item in data]

    def list_all(self) -> list[Webhook]:
        """List all webhooks.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_list
        """

        data = self._paginate(self._url)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Webhook(**item) for item in data]

    def test(self, webhook_id: str) -> dict:
        """Test a webhook.
        https://developer.rechargepayments.com/2021-11/webhooks_endpoints/webhooks_test
        """
        url = f"{self._url}/{webhook_id}/test"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data
