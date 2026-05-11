"""Regression tests for Bug 3: addresses merge/skip used self.base_url instead of self._url."""
import responses as responses_lib

from recharge.api.v2.addresses import AddressResource
from tests.conftest import BASE_URL, make_resource

ADDRESS_DATA = {
    "id": 1,
    "customer_id": 10,
    "address1": "123 Main St",
    "city": "London",
    "country_code": "GB",
    "first_name": "Joe",
    "last_name": "Smith",
    "phone": "07700900000",
    "province": "England",
    "zip": "SW1A 1AA",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
}


@responses_lib.activate
def test_merge_url_uses_addresses_prefix(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/addresses/merge",
        json={"address": ADDRESS_DATA},
        status=200,
    )
    resource = make_resource(AddressResource, client)
    result = resource.merge(
        {"target_address": {"id": "1"}, "source_addresses": ["2"]}
    )
    assert result.id == 1
    called_url = responses_lib.calls[0].request.url
    assert "/addresses/merge" in called_url
    assert called_url.startswith(f"{BASE_URL}/addresses/merge")


@responses_lib.activate
def test_skip_url_uses_addresses_prefix(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/addresses/42/charges/skip",
        json={"address": ADDRESS_DATA},
        status=200,
    )
    resource = make_resource(AddressResource, client)
    result = resource.skip("42", {"date": "2024-02-01", "subscription_ids": ["1"]})
    assert result.id == 1
    called_url = responses_lib.calls[0].request.url
    assert "/addresses/42/charges/skip" in called_url


@responses_lib.activate
def test_create_address(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/addresses",
        json={"address": ADDRESS_DATA},
        status=200,
    )
    resource = make_resource(AddressResource, client)
    result = resource.create({
        "customer_id": "10",
        "address1": "123 Main St",
        "address2": "",
        "city": "London",
        "country_code": "GB",
        "first_name": "Joe",
        "last_name": "Smith",
        "phone": "07700900000",
        "province": "England",
        "zip": "SW1A 1AA",
    })
    assert result.id == 1


@responses_lib.activate
def test_get_address(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/addresses/1",
        json={"address": ADDRESS_DATA},
        status=200,
    )
    resource = make_resource(AddressResource, client)
    result = resource.get("1")
    assert result.id == 1


@responses_lib.activate
def test_list_addresses(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/addresses",
        json={"addresses": [ADDRESS_DATA]},
        status=200,
    )
    resource = make_resource(AddressResource, client)
    results = resource.list_()
    assert len(results) == 1
    assert results[0].id == 1
