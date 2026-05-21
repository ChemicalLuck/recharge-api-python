from typing import get_origin

from pydantic import BaseModel, ConfigDict, model_validator


class RechargeModel(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    @model_validator(mode="before")
    @classmethod
    def _coerce_none_lists(cls, data):
        if not isinstance(data, dict):
            return data
        for field_name, field_info in cls.model_fields.items():
            if get_origin(field_info.annotation) is list and data.get(field_name) is None:
                data[field_name] = []
        return data
