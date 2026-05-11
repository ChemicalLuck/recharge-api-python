import threading
import time

import pytest
import responses as responses_lib

from recharge.client import RechargeClient
from recharge.exceptions import RechargeHTTPError, RechargeRequestException
from recharge.retry import ExponentialBackoffRetry

BASE_URL = "https://api.rechargeapps.com"


def _make_client(max_retries=0):
    return RechargeClient(
        access_token="test",
        retry_strategy=ExponentialBackoffRetry(max_retries=max_retries, base_delay=0.001),
        logging_level=50,
    )


@responses_lib.activate
def test_get_returns_data():
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"charges": [{"id": 1}]},
        status=200,
    )
    client = _make_client()
    data = client.get(f"{BASE_URL}/charges", response_key="charges", expected=list)
    assert data == [{"id": 1}]


@responses_lib.activate
def test_post_sends_body():
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/charges",
        json={"charge": {"id": 2}},
        status=200,
    )
    client = _make_client()
    data = client.post(f"{BASE_URL}/charges", body={"key": "val"}, response_key="charge")
    assert data["id"] == 2


@responses_lib.activate
def test_404_raises_recharge_http_error():
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges/999",
        json={"error": "Not found"},
        status=404,
    )
    client = _make_client()
    with pytest.raises(RechargeHTTPError) as exc_info:
        client.get(f"{BASE_URL}/charges/999")
    assert exc_info.value.status_code == 404


@responses_lib.activate
def test_401_raises_recharge_http_error():
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"error": "bad authentication"},
        status=401,
    )
    client = _make_client()
    with pytest.raises(RechargeHTTPError) as exc_info:
        client.get(f"{BASE_URL}/charges")
    assert exc_info.value.status_code == 401
    assert exc_info.value.body == {"error": "bad authentication"}


@responses_lib.activate
def test_retry_on_429_then_success():
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"error": "rate limited"},
        status=429,
    )
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"charge": {"id": 3}},
        status=200,
    )
    client = _make_client(max_retries=1)
    data = client.get(f"{BASE_URL}/charges", response_key="charge")
    assert data["id"] == 3
    assert len(responses_lib.calls) == 2


@responses_lib.activate
def test_retry_exhausted_raises():
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"error": "rate limited"},
        status=429,
    )
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"error": "rate limited"},
        status=429,
    )
    client = _make_client(max_retries=1)
    with pytest.raises(RechargeHTTPError) as exc_info:
        client.get(f"{BASE_URL}/charges")
    assert exc_info.value.status_code == 429


def test_thread_safe_retry_counters():
    """Concurrent requests on the same client each get independent retry state (Bug 7 fix).

    A single shared client is used by N threads. The transport returns 429
    for the first request from each thread, then 200. All threads must
    succeed — if retry state were shared (the old bug), some threads would
    see a corrupted counter and fail.
    """
    import json as _json

    class _FakeResponse:
        def __init__(self, status, data):
            self.status_code = status
            self._data = data
            self.text = _json.dumps(data)
            self.url = f"{BASE_URL}/charges"
            self.links = {}

        def json(self):
            return self._data

        def raise_for_status(self):
            if self.status_code >= 400:
                from requests.exceptions import HTTPError
                raise HTTPError(response=self)

    class _ThreadLocalTransport:
        """Returns 429 the first time each thread calls, then 200."""

        def __init__(self):
            self._local = threading.local()

        def send(self, method, url, headers, params, json_body):
            count = getattr(self._local, "count", 0) + 1
            self._local.count = count
            if count == 1:
                return _FakeResponse(429, {"error": "rate limited"})
            return _FakeResponse(200, {"charge": {"id": threading.get_ident()}})

    transport = _ThreadLocalTransport()
    # Single shared client — this is what the bug affected
    shared_client = RechargeClient(
        access_token="test",
        transport=transport,
        retry_strategy=ExponentialBackoffRetry(max_retries=1, base_delay=0.001),
        logging_level=50,
    )

    results = []
    errors = []

    def make_request():
        try:
            data = shared_client.get(f"{BASE_URL}/charges", response_key="charge")
            results.append(data["id"])
        except Exception as e:
            errors.append(e)

    threads = [threading.Thread(target=make_request) for _ in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert not errors, f"Unexpected errors in threads: {errors}"
    assert len(results) == 8, f"Expected 8 results, got {len(results)}"
