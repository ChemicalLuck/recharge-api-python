import pytest
import responses as responses_lib

from recharge.client import RechargeClient
from recharge.retry import ExponentialBackoffRetry
from recharge.transport import RequestsTransport
from recharge.types import RechargeScope


BASE_URL = "https://api.rechargeapps.com"
TEST_TOKEN = "test_token_abc123"

ALL_SCOPES: list[RechargeScope] = [
    "write_orders",
    "read_orders",
    "write_products",
    "read_products",
    "write_customers",
    "read_customers",
    "write_subscriptions",
    "read_subscriptions",
    "write_payments",
    "read_payments",
    "write_payment_methods",
    "read_payment_methods",
    "read_batches",
    "write_batches",
    "read_checkouts",
    "write_checkouts",
    "read_events",
    "store_info",
]


@pytest.fixture
def client() -> RechargeClient:
    return RechargeClient(
        access_token=TEST_TOKEN,
        retry_strategy=ExponentialBackoffRetry(max_retries=0),
        logging_level=50,  # CRITICAL only
    )


@pytest.fixture
def scoped_client() -> RechargeClient:
    """Client with zero retries for predictable tests."""
    return RechargeClient(
        access_token=TEST_TOKEN,
        retry_strategy=ExponentialBackoffRetry(max_retries=0),
        logging_level=50,
    )


def make_resource(resource_cls, client: RechargeClient, scopes: list[RechargeScope] | None = None):
    if scopes is None:
        scopes = ALL_SCOPES
    return resource_cls(client=client, scopes=scopes)
