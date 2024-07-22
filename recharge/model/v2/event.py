from typing import TypedDict


class EventSource(TypedDict):
    account_id: str
    api_token_id: str
    api_token_name: str
    account_email: str
    origin: str
    user_type: str


class EventCustomAttributes(TypedDict):
    key: str
    value: str


class Event(TypedDict):
    id: int
    object_id: int
    customer_id: int
    created_at: str
    object_type: str
    verb: str
    description: str
    updated_attributes: dict
    source: EventSource
    custom_attributes: EventCustomAttributes
