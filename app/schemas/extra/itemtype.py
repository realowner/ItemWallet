from typing import Optional

from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetItemType(TunedModel):
    id: int
    title: str
    game_id: int


class CreateItemType(TunedModel):
    title: str
    game_id: int


class UpdateItemType(TunedModel):
    title: Optional[str] = None
    game_id: Optional[int] = None


class DeleteItemTypeResponse(TunedModel):
    id: int
