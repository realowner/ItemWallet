from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetAccount(TunedModel):
    id: int
    title: str


class CreateUpdateAccount(TunedModel):
    title: str


class DeleteAccountResponse(TunedModel):
    id: int
