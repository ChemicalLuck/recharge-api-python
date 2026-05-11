import random
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable


@runtime_checkable
class RetryStrategy(Protocol):
    def should_retry(self, attempt: int, status_code: int) -> bool: ...
    def delay_for(self, attempt: int) -> float: ...


@dataclass
class ExponentialBackoffRetry:
    max_retries: int = 3
    base_delay: float = 2.0
    retryable_status_codes: frozenset[int] = field(
        default_factory=lambda: frozenset({429, 500, 502, 503, 504})
    )

    def should_retry(self, attempt: int, status_code: int) -> bool:
        return attempt < self.max_retries and status_code in self.retryable_status_codes

    def delay_for(self, attempt: int) -> float:
        return (self.base_delay * (2**attempt)) + random.uniform(0, 1)
