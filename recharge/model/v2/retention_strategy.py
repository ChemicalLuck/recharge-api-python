from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

RetentionStrategyCancellationFlowType = Literal["subscription", "membership"]

RetentionStrategyIncentiveType = Literal[
    "delay_subscription", "discount", "skip_charge", "swap_product"
]


class RetentionStrategy(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    cancellation_flow_type: RetentionStrategyCancellationFlowType
    created_at: str
    discount_code: Optional[str] = None
    incentive_type: Optional[RetentionStrategyIncentiveType] = None
    prevention_text: str
    reason: str
    updated_at: str
