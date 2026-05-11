"""Regression tests for Bug 13: CollectionCreateBody had 'titel' typo."""
import responses as responses_lib

from recharge.api.v2.collections import CollectionCreateBody, CollectionResource
from tests.conftest import BASE_URL, make_resource

COLLECTION_DATA = {
    "id": 1,
    "title": "Test Collection",
    "description": "A test collection",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-01T00:00:00",
}


def test_collection_create_body_has_title_not_titel():
    """Bug 13 fix: was 'titel', now 'title'."""
    body: CollectionCreateBody = {"title": "My Collection", "description": "Desc"}
    assert "title" in body
    assert "titel" not in body


def test_collection_create_body_annotations():
    annotations = CollectionCreateBody.__annotations__
    assert "title" in annotations
    assert "titel" not in annotations


@responses_lib.activate
def test_create_collection(client):
    responses_lib.add(
        responses_lib.POST,
        f"{BASE_URL}/collections",
        json={"collection": COLLECTION_DATA},
        status=200,
    )
    resource = make_resource(CollectionResource, client)
    result = resource.create({"title": "Test Collection", "description": "A test collection"})
    assert result.id == 1
    assert result.title == "Test Collection"


@responses_lib.activate
def test_get_collection(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/collections/1",
        json={"collection": COLLECTION_DATA},
        status=200,
    )
    resource = make_resource(CollectionResource, client)
    result = resource.get("1")
    assert result.id == 1


@responses_lib.activate
def test_list_collections(client):
    responses_lib.add(
        responses_lib.GET,
        f"{BASE_URL}/collections",
        json={"collections": [COLLECTION_DATA]},
        status=200,
    )
    resource = make_resource(CollectionResource, client)
    results = resource.list_()
    assert len(results) == 1
