from typing import Literal, TypedDict

RetentionStrategyCancellationFlowType = Literal["subscription", "membership"]

RetentionStrategyIncentiveType = Literal[
    "delay_subscription", "discount", "skip_charge", "swap_product"
]


class RetentionStrategy(TypedDict):
    id: int
    cancellation_flow_type: RetentionStrategyCancellationFlowType
    created_at: str
    discount_code: str
    incentive_type: RetentionStrategyIncentiveType
    prevention_text: str
    reason: str
    updated_at: str
