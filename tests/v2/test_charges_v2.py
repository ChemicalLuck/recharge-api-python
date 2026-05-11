import responses as responses_lib

from recharge.api.v2.charges import ChargeResource
from tests.conftest import BASE_URL, make_resource

CHARGE_DATA = {
    "id": 1,
    "address_id": 10,
    "customer_id": 5,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
    "status": "SUCCESS",
    "type": "RECURRING",  # uppercase in v2 ChargeType
    "line_items": [],
    "total_price": "9.99",
    "subtotal_price": "9.99",
    "total_tax": "0.00",
    "currency": "GBP",
    "billing_address": {},
    "client_details": {},
    "shipping_address": {},
    "payment_processor": "stripe",
    "scheduled_at": "2024-02-01T00:00:00",
    "processed_at": "2024-01-15T00:00:00",
}


@responses_lib.activate
def test_get_charge(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges/1",
        json={"charge": CHARGE_DATA},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    result = resource.get(1)
    assert result.id == 1
    assert result.type == "RECURRING"


@responses_lib.activate
def test_list_charges(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges",
        json={"charges": [CHARGE_DATA]},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    results = resource.list_()
    assert len(results) == 1
    assert results[0].status == "SUCCESS"


@responses_lib.activate
def test_charge_type_field_accessible(client):
    """type field should be a proper field, not __annotations__ hack."""
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges/1",
        json={"charge": CHARGE_DATA},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    result = resource.get(1)
    assert result.type == "RECURRING"


@responses_lib.activate
def test_capture_charge(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/charges/1/capture_payment",  # actual endpoint path
        json={"charge": {**CHARGE_DATA, "status": "SUCCESS"}},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    result = resource.capture(1)
    assert result.status == "SUCCESS"
