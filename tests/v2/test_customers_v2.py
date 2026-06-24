"""Tests for CustomerResource, including the `include` query-param behaviour.

Regression: Customer.get previously sent `includes` (plural), which Recharge
silently ignores, so referral_info / punch_card_progress never came back. The
API expects a single comma-separated `include` param and returns the extra
objects nested under an `include` envelope.
"""
from urllib.parse import parse_qs, urlparse

import responses as responses_lib

from recharge.api.v2.customers import CustomerResource
from tests.conftest import BASE_URL, make_resource

CUSTOMER_DATA = {
    "id": 1,
    "apply_credit_to_next_recurring_charge": True,
    "created_at": "2024-01-01T00:00:00",
    "email": "joe@example.com",
    "first_name": "Joe",
    "has_payment_method_in_dunning": False,
    "has_valid_payment_method": True,
    "hash": "abc123",
    "last_name": "Smith",
    "subscriptions_active_count": 1,
    "subscriptions_total_count": 1,
    "tax_exempt": False,
    "updated_at": "2024-01-01T00:00:00",
}


@responses_lib.activate
def test_get_customer(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/customers/1",
        json={"customer": CUSTOMER_DATA},
        status=200,
    )
    resource = make_resource(CustomerResource, client)
    result = resource.get("1")
    assert result.id == 1


@responses_lib.activate
def test_get_customer_sends_comma_separated_include(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/customers/1",
        json={"customer": CUSTOMER_DATA},
        status=200,
    )
    resource = make_resource(CustomerResource, client)
    resource.get("1", includes=["referral_info", "punch_card_progress"])

    query = parse_qs(urlparse(responses_lib.calls[0].request.url).query)
    # Single `include` param, comma-separated — not `includes`, not repeated.
    assert "includes" not in query
    assert query["include"] == ["referral_info,punch_card_progress"]


@responses_lib.activate
def test_get_customer_lifts_include_envelope_onto_customer(client):
    customer_with_include = {
        **CUSTOMER_DATA,
        "include": {
            "referral_info": {
                "referral_url": {"slug": "joe-x", "url": "https://rc-refer.com/joe-x"}
            },
            "punch_card_progress": {
                "614": {"punch_card_order_count": 2, "punch_card_streak_count": 0}
            },
        },
    }
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/customers/1",
        json={"customer": customer_with_include},
        status=200,
    )
    resource = make_resource(CustomerResource, client)
    result = resource.get("1", includes=["referral_info", "punch_card_progress"])

    extra = result.model_extra or {}
    # The envelope is flattened: included objects are top-level attributes.
    assert "include" not in extra
    assert extra["referral_info"]["referral_url"]["url"] == "https://rc-refer.com/joe-x"
    assert extra["punch_card_progress"]["614"]["punch_card_order_count"] == 2
