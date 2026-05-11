from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

if TYPE_CHECKING:
    from recharge.transport import HttpResponse
    from recharge.types import RechargeVersion


def get_next_page_url(response: "HttpResponse", version: "RechargeVersion") -> str:
    if version == "2021-01":
        return response.links.get("next", {}).get("url", "")
    if version == "2021-11":
        try:
            data = response.json()
            cursor = data.get("next_cursor")
            if cursor:
                parsed = urlparse(response.url)
                params = parse_qs(parsed.query)
                params = {k: v for k, v in params.items() if k in ("cursor", "limit")}
                params["cursor"] = [cursor]
                new_query = urlencode(params, doseq=True)
                return urlunparse(parsed._replace(query=new_query))
        except Exception:
            pass
    return ""
