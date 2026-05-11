import responses as responses_lib

from recharge.api.v1.subscriptions import SubscriptionResource
from tests.conftest import BASE_URL, make_resource

SUB_DATA = {
    "id": 1,
    "address_id": 10,
    "customer_id": 5,
    "status": "ACTIVE",
    "order_interval_unit": "month",
}


@responses_lib.activate
def test_get_subscription(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/subscriptions/1",
        json={"subscription": SUB_DATA},
        status=200,
    )
    resource = make_resource(SubscriptionResource, client)
    result = resource.get(1)
    assert result.id == 1
    assert result.status == "ACTIVE"


@responses_lib.activate
def test_list_subscriptions(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/subscriptions",
        json={"subscriptions": [SUB_DATA]},
        status=200,
    )
    resource = make_resource(SubscriptionResource, client)
    results = resource.list_()
    assert len(results) == 1


@responses_lib.activate
def test_cancel_subscription(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/subscriptions/1/cancel",
        json={"subscription": {**SUB_DATA, "status": "CANCELLED"}},
        status=200,
    )
    resource = make_resource(SubscriptionResource, client)
    result = resource.cancel(1, {"cancellation_reason": "Test"})
    assert result.status == "CANCELLED"
