from recharge.api import RechargeResource
from typing import TypedDict, Literal

from recharge.api.tokens import TokenScope


class AsyncBatchCreateBody(TypedDict):
    batch_type: Literal[
        "address_discount_apply",
        "address_discount_remove",
        "change_next_charge_date",
        "discount_create",
        "discount_delete",
        "discount_update",
        "product_create",
        "product_update",
        "product_delete",
        "onetime_create",
        "onetime_delete",
        "bulk_subscriptions_create",
        "bulk_subscriptions_update",
        "bulk_subscriptions_delete",
        "subscription_cancel",
    ]


class AsyncBatchResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/async_batch_endpoints
    """

    object_list_key = "async_batches"

    def create(self, data):
        """Create an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["write_batches"]
        self.check_scopes("POST /async_batches", required_scopes)

        return self.http_post(self.url, data)

    def create_task(self, batch_id, data):
        """Create a task for an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self.http_post(f"{self.url}/{batch_id}/tasks", data)

    def get(self, batch_id):
        """Get an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["read_batches"]
        self.check_scopes("GET /async_batches/:batch_id", required_scopes)

        return self.http_get(f"{self.url}/{batch_id}")

    def list(self):
        """List async batches.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["read_batches"]
        self.check_scopes("GET /async_batches", required_scopes)

        return self.http_get(self.url)

    def list_tasks(
        self,
        batch_id,
    ):
        """List tasks for an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["read_batches"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self.http_get(f"{self.url}/{batch_id}/tasks")

    def process(self, batch_id):
        """Process an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[TokenScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/process", required_scopes
        )

        return self.http_post(f"{self.url}/{batch_id}/process", None)
