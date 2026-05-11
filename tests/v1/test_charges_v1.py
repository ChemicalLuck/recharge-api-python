import responses as responses_lib

from recharge.api.v1.charges import ChargeResource
from tests.conftest import BASE_URL, make_resource

CHARGE_DATA = {
    "id": 1,
    "address_id": 10,
    "customer_id": "5",
    "status": "SUCCESS",
    "type": "RECURRING",
    "line_items": [],
    "scheduled_at": "2024-02-01T00:00:00",
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
        json={"charges": [CHARGE_DATA, {**CHARGE_DATA, "id": 2}]},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    results = resource.list_()
    assert len(results) == 2


@responses_lib.activate
def test_charge_with_extra_fields(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/charges/1",
        json={"charge": {**CHARGE_DATA, "future_api_field": "value"}},
        status=200,
    )
    resource = make_resource(ChargeResource, client)
    result = resource.get(1)
    assert result.id == 1
    assert result.model_extra.get("future_api_field") == "value"
