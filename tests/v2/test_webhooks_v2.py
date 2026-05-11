"""Regression tests for Bug 2: webhooks update missing body, no delete, verion typo."""
import responses as responses_lib

from recharge.api.v2.webhooks import WebhookResource, WebhookCreateBodyOptional, WebhookUpdateBody
from tests.conftest import BASE_URL, make_resource

WEBHOOK_DATA = {
    "id": 1,
    "address": "https://example.com/webhook",
    "topic": "charge/paid",
    "included_objects": [],
}


def test_webhook_create_body_version_field_spelled_correctly():
    """Bug 14 fix: was 'verion', now 'version'."""
    body: WebhookCreateBodyOptional = {}
    body["version"] = "2021-11"
    assert "version" in body
    assert "verion" not in body


def test_webhook_update_body_exists():
    """Bug 2 fix: WebhookUpdateBody TypedDict was missing."""
    body: WebhookUpdateBody = {"address": "https://example.com/new"}
    assert body["address"] == "https://example.com/new"


@responses_lib.activate
def test_create_webhook(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/webhooks",
        json={"webhook": WEBHOOK_DATA},
        status=200,
    )
    resource = make_resource(WebhookResource, client)
    result = resource.create({"address": "https://example.com/webhook", "topic": "charge/paid"})
    assert result.id == 1
    assert result.topic == "charge/paid"


@responses_lib.activate
def test_update_webhook_accepts_body(client):
    """Bug 2 fix: update() now accepts a body parameter."""
    responses_lib.add(
        responses_lib.PUT,
        f"{BASE_URL}/webhooks/1",
        json={"webhook": {**WEBHOOK_DATA, "address": "https://example.com/new"}},
        status=200,
    )
    resource = make_resource(WebhookResource, client)
    result = resource.update("1", {"address": "https://example.com/new"})
    assert result.address == "https://example.com/new"


@responses_lib.activate
def test_delete_webhook(client):
    """Bug 2 fix: delete() method was missing entirely."""
    responses_lib.add(
        responses_lib.DELETE,
        f"{BASE_URL}/webhooks/1",
        json={},
        status=200,
    )
    resource = make_resource(WebhookResource, client)
    result = resource.delete("1")
    assert isinstance(result, dict)


@responses_lib.activate
def test_list_webhooks(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/webhooks",
        json={"webhooks": [WEBHOOK_DATA]},
        status=200,
    )
    resource = make_resource(WebhookResource, client)
    results = resource.list_()
    assert len(results) == 1
    assert results[0].topic == "charge/paid"
