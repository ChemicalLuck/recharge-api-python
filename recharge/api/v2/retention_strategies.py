from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.retention_strategy import (
    RetentionStrategy,
    RetentionStrategyCancellationFlowType,
    RetentionStrategyIncentiveType,
)


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
    object_dict_key = "retention_strategy"
    recharge_version: RechargeVersion = "2021-11"

    def create(self, body: RetentionStrategyCreateBody) -> RetentionStrategy:
        """Create a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_create
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self._check_scopes(f"POST /{self.object_list_key}", required_scopes)

        data = self._http_post(self._url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return RetentionStrategy(**data)

    def get(self, retention_strategy_id: int) -> RetentionStrategy:
        """Get a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_retrieve
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(
            f"GET /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        url = f"{self._url}/{retention_strategy_id}"
        data = self._http_get(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return RetentionStrategy(**data)

    def update(
        self, retention_strategy_id: int, body: RetentionStrategyUpdateBody
    ) -> RetentionStrategy:
        """Update a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_update
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self._check_scopes(
            f"PUT /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        url = f"{self._url}/{retention_strategy_id}"
        data = self._http_put(url, body)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return RetentionStrategy(**data)

    def delete(self, retention_strategy_id: int) -> dict:
        """Delete a retention strategy.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_delete
        """
        required_scopes: list[RechargeScope] = ["write_retention_strategies"]
        self._check_scopes(
            f"DELETE /{self.object_list_key}/:retention_strategy_id", required_scopes
        )

        url = f"{self._url}/{retention_strategy_id}"
        data = self._http_delete(url)
        if not isinstance(data, dict):
            raise RechargeAPIError(f"Expected dict, got {type(data).__name__}")
        return data

    def list_(self) -> list[RetentionStrategy]:
        """List retention strategies.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, expected=list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [RetentionStrategy(**item) for item in data]

    def list_all(self) -> list[RetentionStrategy]:
        """List all retention strategies.
        https://developer.rechargepayments.com/2021-11/retention_strategies/retention_strategies_list
        """
        required_scopes: list[RechargeScope] = ["read_subscriptions"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [RetentionStrategy(**item) for item in data]
