from typing import TypedDict, Union

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v1.async_batch import AsyncBatch, AsyncBatchTask, AsyncBatchType

from .addresses import AddressApplyDiscountBody, AddressRemoveDiscountBody
from .discounts import DiscountCreateBody, DiscountDeleteBody, DiscountUpdateBody
from .onetimes import OnetimeCreateBody, OnetimeDeleteBody
from .products import ProductCreateBody, ProductDeleteBody, ProductUpdateBody
from .subscriptions import (
    SubscriptionBulkCreateBody,
    SubscriptionBulkDeleteBody,
    SubscriptionBulkUpdateBody,
    SubscriptionCancelBody,
)


class AsyncBatchCreateBody(TypedDict):
    batch_type: AsyncBatchType


AsyncBatchBody = Union[
    AddressApplyDiscountBody,
    AddressRemoveDiscountBody,
    DiscountCreateBody,
    DiscountDeleteBody,
    DiscountUpdateBody,
    ProductCreateBody,
    ProductUpdateBody,
    ProductDeleteBody,
    OnetimeCreateBody,
    OnetimeDeleteBody,
    SubscriptionBulkCreateBody,
    SubscriptionBulkUpdateBody,
    SubscriptionBulkDeleteBody,
    SubscriptionCancelBody,
]


class AsyncBatchCreateTaskBody(TypedDict):
    body: AsyncBatchBody


class AsyncBatchResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-01/async_batch_endpoints
    """

    object_list_key = "async_batches"
    object_dict_key = "async_batch"
    recharge_version: RechargeVersion = "2021-01"

    def create(self, body: AsyncBatchCreateBody) -> AsyncBatch:
        """Create an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["write_batches"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return AsyncBatch(**data)

    def create_task(self, batch_id: str, body: AsyncBatchCreateTaskBody) -> int:
        """Create a task for an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
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
            raise RechargeAPIError(f"Expected 'count' key in list, got {data}")
        return data["count"]

    def get(self, batch_id: str) -> AsyncBatch:
        """Get an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
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
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [AsyncBatch(**batch) for batch in data]

    def list_all(self) -> list[AsyncBatch]:
        """List all async batches.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        url = f"{self._url}/all"
        data = self._paginate(url)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [AsyncBatch(**batch) for batch in data]

    def list_tasks(
        self,
        batch_id: str,
    ) -> list[AsyncBatchTask]:
        """List tasks for an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
        """
        required_scopes: list[RechargeScope] = ["read_batches"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:batch_id/tasks", required_scopes
        )

        url = f"{self._url}/{batch_id}/tasks"
        data = self._http_get(url, expected=list, response_key="async_batch_tasks")
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [AsyncBatchTask(**task) for task in data]

    def process(self, batch_id: str) -> AsyncBatch:
        """Process an async batch.
        https://developer.rechargepayments.com/2021-01/async_batch_endpoints
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
