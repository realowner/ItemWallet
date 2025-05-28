from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetMarket(TunedModel):
    id: int
    title: str


class CreateUpdateMarket(TunedModel):
    title: str


class DeleteMarketResponse(TunedModel):
    id: int
