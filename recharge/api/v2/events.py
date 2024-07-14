from typing import TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion


class EventListQuery(TypedDict, total=False):
    create_at_min: str
    created_at_max: str
    object_type: str
    object_id: int
    verbs: str
    customer_id: int
    origin: str


class EventResource(RechargeResource):
    """
    https://developer.rechargepayments.com/2021-11/events
    """

    object_list_key = "events"
    recharge_version: RechargeVersion = "2021-11"

    def list_(self, query: EventListQuery | None = None):
        """List events.
        https://developer.rechargepayments.com/2021-11/events/events_list
        """
        required_scopes: list[RechargeScope] = ["read_events"]
        self.check_scopes(f"GET /{self.object_list_key}", required_scopes)

        return self._http_get(self.url, query)
