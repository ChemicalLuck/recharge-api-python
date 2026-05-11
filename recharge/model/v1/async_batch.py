from typing import Any, Literal, Optional

from pydantic import BaseModel, ConfigDict

from recharge.types import RechargeVersion

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
    expired_at: Optional[str] = None
    version: Optional[RechargeVersion] = None


class AsyncBatchTask(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    batch_id: int
    body: Optional[dict[str, Any]] = None
    completed_at: Optional[str] = None
    created_at: str
    deleted_at: Optional[str] = None
    id: int
    queued_at: Optional[str] = None
    result: Optional[dict[str, Any]] = None
    started_at: Optional[str] = None
    status: AsyncBatchStatus
    updated_at: str
