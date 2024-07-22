from typing import Literal, Optional, TypedDict

from recharge.api import RechargeVersion

AsyncBatchStatus = Literal["not_started", "processing", "completed", "failed"]
AsyncBatchTaskStatus = Literal["pending", "processing", "failed", "success"]

AsyncBatchType = Literal[
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


class AsyncBatch(TypedDict):
    id: int
    batch_type: AsyncBatchType
    closed_at: Optional[str]
    created_at: str
    deleted_at: Optional[str]
    fail_task_count: int
    status: AsyncBatchStatus
    submitted_at: Optional[str]
    success_task_count: int
    total_task_count: int
    updated_at: str
    expired_at: Optional[str]
    version: RechargeVersion


class AsyncBatchTask(TypedDict):
    batch_id: int
    body: dict
    completed_at: Optional[str]
    created_at: str
    deleted_at: Optional[str]
    id: int
    queued_at: Optional[str]
    result: dict
    started_at: Optional[str]
    status: AsyncBatchStatus
    updated_at: str
