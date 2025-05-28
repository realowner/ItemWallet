from app.schemas.item import CreateItem, UpdateItem
from app.repositories.base import BaseRepository


class ItemService:
    def __init__(self, item_repo: BaseRepository):
        self.item_repo = item_repo

    async def add_item(self, data: CreateItem):
        data_dict = data.model_dump()
        item_object = await self.item_repo.add_object(data_dict)
        return item_object

    async def get_all(self):
        item_object = await self.item_repo.get_all()
        return item_object

    async def get_one(self, item_id: int):
        item_object = await self.item_repo.get_one(item_id)
        return item_object

    async def delete_item(self, item_id: int):
        item_object = await self.item_repo.delete_object(item_id)
        return item_object

    async def update_item(self, item_id: int, data: UpdateItem):
        data_dict = data.model_dump()
        item_object = await self.item_repo.update_object(item_id, data_dict)
        return item_object
