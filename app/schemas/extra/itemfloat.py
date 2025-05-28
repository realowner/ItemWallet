from typing import Optional

from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetItemFloat(TunedModel):
    id: int
    title: str
    abbr: str
    min_value: float
    max_value: float


class CreateItemFloat(TunedModel):
    title: str
    abbr: str
    min_value: float
    max_value: float


class UpdateItemFloat(TunedModel):
    title: Optional[str] = None
    abbr: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None


class DeleteItemFloatResponse(TunedModel):
    id: int
