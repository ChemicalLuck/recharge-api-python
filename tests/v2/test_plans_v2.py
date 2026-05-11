"""Regression tests for Bug 1: plans bulk_create/bulk_update isinstance guard was wrong."""
import responses as responses_lib

from recharge.api.v2.plans import PlanResource
from tests.conftest import BASE_URL, make_resource

PLAN_DATA = {
    "id": 1,
    "title": "Monthly Plan",
    "type": "subscription",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "external_product_id": {"ecommerce": "prod_1"},
    "subscription_preferences": {
        "charge_interval_frequency": 1,
        "interval_unit": "month",
        "order_interval_frequency": 1,
    },
}


@responses_lib.activate
def test_bulk_create_returns_list(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/products/123/plans-bulk",
        json={"plans": [PLAN_DATA, {**PLAN_DATA, "id": 2}]},
        status=200,
    )
    resource = make_resource(PlanResource, client)
    results = resource.bulk_create("123", {"plans": []})
    assert len(results) == 2
    assert results[0].id == 1
    assert results[1].id == 2


@responses_lib.activate
def test_bulk_update_returns_list(client):
    responses_lib.add(
        responses_lib.PUT,
        f"{BASE_URL}/products/456/plans-bulk",
        json={"plans": [PLAN_DATA]},
        status=200,
    )
    resource = make_resource(PlanResource, client)
    results = resource.bulk_update("456", {"plans": []})
    assert len(results) == 1
    assert results[0].id == 1


@responses_lib.activate
def test_create_plan(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/plans",
        json={"plan": PLAN_DATA},
        status=200,
    )
    resource = make_resource(PlanResource, client)
    result = resource.create({
        "external_product_id": {"ecommerce": "prod_1"},
        "subscription_preferences": {"charge_interval_frequency": 1, "interval_unit": "month", "order_interval_frequency": 1},
        "title": "Monthly Plan",
        "type": "subscription",
    })
    assert result.id == 1
    assert result.type == "subscription"
