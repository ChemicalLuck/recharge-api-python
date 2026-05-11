"""Regression tests for Bug 10: events EventListQuery had 'create_at_min' typo."""
from recharge.api.v2.events import EventListQuery


def test_event_list_query_has_created_at_min():
    """Bug 10 fix: was 'create_at_min', now 'created_at_min'."""
    query: EventListQuery = {"created_at_min": "2024-01-01T00:00:00"}
    assert "created_at_min" in query


def test_event_list_query_no_typo_key():
    query: EventListQuery = {}
    assert "create_at_min" not in EventListQuery.__annotations__


def test_event_list_query_all_fields():
    annotations = EventListQuery.__annotations__
    assert "created_at_min" in annotations
    assert "created_at_max" in annotations
    assert "object_type" in annotations
    assert "object_id" in annotations
    assert "customer_id" in annotations
