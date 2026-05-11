"""Regression tests for Bug 9: onetimes list_all used _http_get not _paginate."""
from unittest.mock import MagicMock, patch

import responses as responses_lib

from recharge.api.v2.onetimes import OnetimeResource
from tests.conftest import BASE_URL, make_resource

ONETIME_DATA = {
    "id": 1,
    "address_id": 10,
    "external_variant_id": {"ecommerce": "var_1"},
    "next_charge_scheduled_at": "2024-02-01T00:00:00",
    "product_title": "Test Product",
    "quantity": 1,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
}


def test_list_all_calls_paginate(client):
    """Bug 9 fix: list_all must call _paginate, not _http_get."""
    resource = make_resource(OnetimeResource, client)
    with patch.object(resource, "_paginate", return_value=[ONETIME_DATA]) as mock_paginate:
        results = resource.list_all()
    mock_paginate.assert_called_once_with(f"{BASE_URL}/onetimes", None)
    assert results[0].id == 1


def test_list_calls_http_get(client):
    """list_ (non-paginating) should use _http_get."""
    resource = make_resource(OnetimeResource, client)
    with patch.object(resource, "_http_get", return_value=[ONETIME_DATA]) as mock_get:
        results = resource.list_()
    mock_get.assert_called_once()
    assert results[0].id == 1


@responses_lib.activate
def test_list_all_paginates_multiple_pages(client):
    """list_all should follow pagination cursors."""
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/onetimes",
        json={"onetimes": [ONETIME_DATA], "next_cursor": "cursor1"},
        status=200,
    )
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/onetimes",
        json={"onetimes": [{**ONETIME_DATA, "id": 2}], "next_cursor": None},
        status=200,
    )
    resource = make_resource(OnetimeResource, client)
    results = resource.list_all()
    assert len(results) == 2
    assert results[0].id == 1
    assert results[1].id == 2
