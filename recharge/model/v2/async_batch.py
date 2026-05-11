from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

from recharge.types import RechargeVersion

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


class AsyncBatch(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    batch_type: AsyncBatchType
    closed_at: Optional[str] = None
    created_at: str
    deleted_at: Optional[str] = None
    fail_task_count: int
    status: AsyncBatchStatus
    submitted_at: Optional[str] = None
    success_task_count: int
    total_task_count: int
    updated_at: str
    version: Optional[RechargeVersion] = None


class AsyncBatchTask(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    batch_id: int
    body: dict
    completed_at: Optional[str] = None
    created_at: str
    deleted_at: Optional[str] = None
    id: int
    queued_at: Optional[str] = None
    result: dict
    started_at: Optional[str] = None
    status: AsyncBatchStatus
    updated_at: str
