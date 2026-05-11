from pydantic import BaseModel, ConfigDict


class EventSource(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    account_id: str
    api_token_id: str
    api_token_name: str
    account_email: str
    origin: str
    user_type: str


class EventCustomAttributes(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    key: str
    value: str


class Event(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

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
