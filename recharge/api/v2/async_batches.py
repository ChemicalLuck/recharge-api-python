from typing import Literal, TypedDict, Optional, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

from .discounts import DiscountCreateBody, DiscountUpdateBody, DiscountDeleteBody
from .plans import (
    PlanCreateBody,
    PlanUpdateBody,
    PlanDeleteBody,
)
from .onetimes import OnetimeCreateBody, OnetimeDeleteBody


AsyncBatchType = Literal[
    "discount_create",
    "discount_delete",
    "discount_update",
    "bulk_plans_create",
    "bulk_plans_update",
    "bulk_plans_delete",
    "onetime_create",
    "onetime_delete",
]


class AsyncBatchCreateBody(TypedDict):
    batch_type: AsyncBatchType


AsyncBatchBody = Union[
    DiscountCreateBody,
    DiscountDeleteBody,
    DiscountUpdateBody,
    PlanCreateBody,
    PlanUpdateBody,
    PlanDeleteBody,
    OnetimeCreateBody,
    OnetimeDeleteBody,
]


class AsyncBatchCreateTaskBody(TypedDict):
    body: AsyncBatchBody


class AsyncBatchListTasksQuery(TypedDict, total=False):
    ids: str


class AsyncBatchResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/async_batch_endpoints
    """

    object_list_key = "async_batches"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: AsyncBatchCreateBody):
        """Create an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_create
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def create_task(self, batch_id: str, body: AsyncBatchCreateTaskBody):
        """Create a task for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_create
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self._http_post(f"{self.url}/{batch_id}/tasks", body)

    def get(self, batch_id: str):
        """Get an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(f"GET /{self.object_list_key}/:batch_id", required_scopes)

        return self._http_get(f"{self.url}/{batch_id}")

    def list_(self):
        """List async batches.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_list
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url)

    def list_tasks(
        self,
        batch_id: str,
        query: Optional[AsyncBatchListTasksQuery] = None,
    ):
        """List tasks for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        return self._http_get(f"{self.url}/{batch_id}/tasks", query)

    def process(self, batch_id: str):
        """Process an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_process
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self.check_scopes(
            f"POST /{self.object_list_key}/:batch_id/process", required_scopes
        )

        return self._http_post(f"{self.url}/{batch_id}/process", None)
