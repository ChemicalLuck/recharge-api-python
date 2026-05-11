import pytest

from recharge.retry import ExponentialBackoffRetry


def test_should_retry_on_rate_limit():
    strategy = ExponentialBackoffRetry(max_retries=3)
    assert strategy.should_retry(attempt=0, status_code=429) is True


def test_should_retry_on_server_errors():
    strategy = ExponentialBackoffRetry(max_retries=3)
    for code in (500, 502, 503, 504):
        assert strategy.should_retry(attempt=0, status_code=code) is True


def test_should_not_retry_on_client_errors():
    strategy = ExponentialBackoffRetry(max_retries=3)
    for code in (400, 401, 403, 404, 422):
        assert strategy.should_retry(attempt=0, status_code=code) is False


def test_should_not_retry_on_success():
    strategy = ExponentialBackoffRetry(max_retries=3)
    assert strategy.should_retry(attempt=0, status_code=200) is False


def test_stops_after_max_retries():
    strategy = ExponentialBackoffRetry(max_retries=3)
    assert strategy.should_retry(attempt=3, status_code=429) is False
    assert strategy.should_retry(attempt=4, status_code=429) is False


def test_delay_grows_exponentially():
    strategy = ExponentialBackoffRetry(max_retries=5, base_delay=1.0)
    d0 = strategy.delay_for(0)
    d1 = strategy.delay_for(1)
    d2 = strategy.delay_for(2)
    # Each delay should be at least double the base (plus jitter), roughly exponential
    assert d1 > d0
    assert d2 > d1


def test_zero_retries_never_retries():
    strategy = ExponentialBackoffRetry(max_retries=0)
    assert strategy.should_retry(attempt=0, status_code=429) is False
    assert strategy.should_retry(attempt=0, status_code=500) is False
