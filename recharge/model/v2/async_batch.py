from typing import Literal, Optional, TypedDict

from recharge.api import RechargeVersion

AsyncBatchStatus = Literal["not_started", "processing", "completed", "failed"]
AsyncBatchTaskStatus = Literal["pending", "processing", "failed", "success"]

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
