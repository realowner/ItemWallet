from app.schemas.extra.itemfloat import CreateItemFloat, UpdateItemFloat
from app.repositories.base import BaseRepository


class ItemFloatService:
    def __init__(self, float_repo: BaseRepository):
        self.float_repo = float_repo

    async def add_float(self, data: CreateItemFloat):
        data_dict = data.model_dump()
        float_object = await self.float_repo.add_object(data_dict)
        return float_object

    async def get_all(self):
        float_object = await self.float_repo.get_all()
        return float_object

    async def get_one(self, float_id: int):
        float_object = await self.float_repo.get_one(float_id)
        return float_object

    async def delete_float(self, float_id: int):
        float_object = await self.float_repo.delete_object(float_id)
        return float_object

    async def update_float(self, float_id: int, data: UpdateItemFloat):
        data_dict = data.model_dump()
        float_object = await self.float_repo.update_object(float_id, data_dict)
        return float_object
