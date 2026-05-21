from typing import Literal, Optional

from recharge.model.base import RechargeModel

RetentionStrategyCancellationFlowType = Literal["subscription", "membership"]

RetentionStrategyIncentiveType = Literal[
    "delay_subscription", "discount", "skip_charge", "swap_product"
]


class RetentionStrategy(RechargeModel):
    id: int
    cancellation_flow_type: RetentionStrategyCancellationFlowType
    created_at: str
    discount_code: Optional[str] = None
    incentive_type: Optional[RetentionStrategyIncentiveType] = None
    prevention_text: str
    reason: str
    updated_at: str
