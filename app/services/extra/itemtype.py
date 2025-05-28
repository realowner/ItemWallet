from app.schemas.extra.itemtype import CreateItemType, UpdateItemType
from app.repositories.base import BaseRepository


class ItemTypeService:
    def __init__(self, item_type_repo: BaseRepository):
        self.item_type_repo = item_type_repo

    async def add_type(self, data: CreateItemType):
        data_dict = data.model_dump()
        item_type = await self.item_type_repo.add_object(data_dict)
        return item_type

    async def get_all(self):
        item_types = await self.item_type_repo.get_all()
        return item_types

    async def get_one(self, type_id: int):
        item_type = await self.item_type_repo.get_one(type_id)
        return item_type

    async def delete_type(self, type_id: int):
        item_type = await self.item_type_repo.delete_object(type_id)
        return item_type

    async def update_type(self, type_id: int, data: UpdateItemType):
        data_dict = data.model_dump()
        item_type = await self.item_type_repo.update_object(type_id, data_dict)
        return item_type
