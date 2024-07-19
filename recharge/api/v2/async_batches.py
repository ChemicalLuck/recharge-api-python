from typing import TypedDict, Optional, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.model.v2.async_batch import AsyncBatchType, AsyncBatch, AsyncBatchTask
from recharge.exceptions import RechargeAPIError

from .discounts import DiscountCreateBody, DiscountUpdateBody, DiscountDeleteBody
from .plans import (
    PlanCreateBody,
    PlanUpdateBody,
    PlanDeleteBody,
)
from .onetimes import OnetimeCreateBody, OnetimeDeleteBody


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
    object_dict_key = "async_batch"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: AsyncBatchCreateBody) -> AsyncBatch:
        """Create an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_create
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return AsyncBatch(**data)

    def create_task(self, batch_id: str, body: AsyncBatchCreateTaskBody) -> int:
        """Create a task for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_create
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        url = f"{self._url}/{batch_id}/tasks"
        data = self._http_post(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        if "count" not in data:
            raise RechargeAPIError(f"Expected 'count' in response, got {data}")
        return data["count"]

    def get(self, batch_id: str) -> AsyncBatch:
        """Get an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(f"GET /{self.object_list_key}/:batch_id", required_scopes)

        url = f"{self._url}/{batch_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return AsyncBatch(**data)

    def list_(self) -> list[AsyncBatch]:
        """List async batches.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_list
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [AsyncBatch(**item) for item in data]

    def list_tasks(
        self,
        batch_id: str,
        query: Optional[AsyncBatchListTasksQuery] = None,
    ) -> list[AsyncBatchTask]:
        """List tasks for an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_tasks/async_batch_tasks_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        url = f"{self._url}/{batch_id}/tasks"
        self.object_list_key = "async_batch_tasks"
        data = self._http_get(url, query, expected=list)
        self.object_list_key = "async_batches"
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [AsyncBatchTask(**item) for item in data]

    def process(self, batch_id: str) -> AsyncBatch:
        """Process an async batch.
        https://developer.rechargepayments.com/2021-11/async_batch_endpoints/async_batch_endpoints_process
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self._check_scopes(
            f"POST /{self.object_list_key}/:batch_id/process", required_scopes
        )

        url = f"{self._url}/{batch_id}/process"
        data = self._http_post(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return AsyncBatch(**data)
