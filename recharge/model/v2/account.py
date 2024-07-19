from typing import TypedDict


class Account(TypedDict):
    id: int
    user_id: int
    created_at: str
    invited_at: str
    is_owner: bool
