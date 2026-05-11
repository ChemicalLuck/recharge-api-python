import responses as responses_lib

from recharge.pagination import get_next_page_url
from recharge.transport import RequestsTransport

import requests


class _FakeResponse:
    def __init__(self, status_code=200, json_body=None, links=None, url="https://example.com"):
        self.status_code = status_code
        self._json = json_body or {}
        self.links = links or {}
        self.url = url
        self.text = ""

    def json(self):
        return self._json

    def raise_for_status(self):
        pass


def test_v1_link_header_next():
    resp = _FakeResponse(
        links={"next": {"url": "https://api.rechargeapps.com/charges?page=2"}},
        url="https://api.rechargeapps.com/charges",
    )
    url = get_next_page_url(resp, "2021-01")
    assert url == "https://api.rechargeapps.com/charges?page=2"


def test_v1_no_next_link():
    resp = _FakeResponse(links={}, url="https://api.rechargeapps.com/charges")
    url = get_next_page_url(resp, "2021-01")
    assert url == ""


def test_v2_cursor_next():
    resp = _FakeResponse(
        json_body={"charges": [], "next_cursor": "abc123"},
        url="https://api.rechargeapps.com/charges?limit=250",
    )
    url = get_next_page_url(resp, "2021-11")
    assert "cursor=abc123" in url
    assert "limit=250" in url


def test_v2_no_cursor():
    resp = _FakeResponse(
        json_body={"charges": [], "next_cursor": None},
        url="https://api.rechargeapps.com/charges",
    )
    url = get_next_page_url(resp, "2021-11")
    assert url == ""


def test_v2_cursor_strips_other_params():
    resp = _FakeResponse(
        json_body={"charges": [], "next_cursor": "xyz999"},
        url="https://api.rechargeapps.com/charges?status=QUEUED&limit=50",
    )
    url = get_next_page_url(resp, "2021-11")
    assert "status=" not in url
    assert "cursor=xyz999" in url
    assert "limit=50" in url
