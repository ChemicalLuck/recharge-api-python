from typing import Optional

from pydantic import BaseModel, ConfigDict


class Account(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    user_id: int
    created_at: str
    invited_at: Optional[str] = None
    is_owner: bool
