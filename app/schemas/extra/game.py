from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetGame(TunedModel):
    id: int
    title: str


class CreateUpdateGame(TunedModel):
    title: str


class DeleteGameResponse(TunedModel):
    id: int
