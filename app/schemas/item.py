from typing import Optional

from pydantic import BaseModel, ConfigDict


class TunedModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class GetItem(TunedModel):
    id: int
    title: str
    type_id: int
    float_id: int
    float_value: float
    purchase_price: float
    sale_price: Optional[float] = None
    status: str
    account_id: int
    market_id: Optional[int] = None


class CreateItem(TunedModel):
    title: str
    type_id: int
    float_id: int
    float_value: float
    purchase_price: float
    sale_price: Optional[float] = None
    status: str
    account_id: int
    market_id: Optional[int] = None


class UpdateItem(TunedModel):
    title: Optional[str] = None
    type_id: Optional[int] = None
    float_id: Optional[int] = None
    float_value: Optional[float] = None
    purchase_price: Optional[float] = None
    sale_price: Optional[float] = None
    status: Optional[str] = None
    account_id: Optional[int] = None
    market_id: Optional[int] = None


class DeleteItemResponse(TunedModel):
    id: int
