from typing import Literal, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion

RetentionStrategyCancellationFlowType = Literal["subscription", "membership"]

RetentionStrategyIncentiveType = Literal[
    "delay_subscription", "discount", "skip_charge", "swap_product"
]


class RetentionStrategyCreateBodyOptional(TypedDict, total=False):
    cancellation_flow_type: RetentionStrategyCancellationFlowType
    incentive_type: RetentionStrategyIncentiveType
    discount_code: str


class RetentionStrategyCreateBody(RetentionStrategyCreateBodyOptional):
    prevention_text: str
    reason: str


class RetentionStrategyUpdateBody(TypedDict, total=False):
    cancellation_flow_type: RetentionStrategyCancellationFlowType
    incentive_type: RetentionStrategyIncentiveType
    discount_code: str
    prevention_text: str
    reason: str


class RetentionStrategyResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/retention_strategies
    """

    object_list_key = "retention_strategies"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: RetentionStrategyCreateBody):
        """Create a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_create
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self.check_scopes(f"POST /{self.object_list_key}", required_scopes)

        return self._http_post(self.url, body)

    def get(self, retention_strategy_id: int):
        """Get a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(
            f"GET /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        return self._http_get(f"{self.url}/{retention_strategy_id}")

    def update(self, retention_strategy_id: int, body: RetentionStrategyUpdateBody):
        """Update a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_update
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self.check_scopes(
            f"PUT /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        return self._http_put(f"{self.url}/{retention_strategy_id}", body)

    def delete(self, retention_strategy_id: int):
        """Delete a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_delete
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self.check_scopes(
            f"DELETE /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        return self._http_delete(f"{self.url}/{retention_strategy_id}")

    def list_(self):
        """List retention strategies.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url)
