from typing import Optional, TypedDict

from recharge.api import RechargeResource, RechargeScope, RechargeVersion
from recharge.exceptions import RechargeAPIError
from recharge.model.v2.event import Event


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
    object_dict_key = "event"
    recharge_version: RechargeVersion = "2021-11"

    def list_(self, query: Optional[EventListQuery] = None) -> list[Event]:
        """List events.
        https://developer.rechargepayments.com/2021-11/events/events_list
        """
        required_scopes: list[RechargeScope] = ["read_events"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._http_get(self._url, query, list)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Event(**event) for event in data]

    def list_all(self, query: Optional[EventListQuery] = None) -> list[Event]:
        """List all events.
        https://developer.rechargepayments.com/2021-11/events/events_list
        """
        required_scopes: list[RechargeScope] = ["read_events"]
        self._check_scopes(f"GET /{self.object_list_key}", required_scopes)

        data = self._paginate(self._url, query)
        if not isinstance(data, list):
            raise RechargeAPIError(f"Expected list, got {type(data).__name__}")
        return [Event(**event) for event in data]
