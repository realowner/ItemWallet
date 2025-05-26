from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetItemType(TunedModel):
    id: int
    title: str
    game_id: int


#TODO: разделить методы
class CreateUpdateGetItemType(TunedModel):
    title: str
    game_id: int


class DeleteGetItemTypeResponse(TunedModel):
    id: int
