from app.schemas.extra.market import CreateUpdateMarket
from app.repositories.base import BaseRepository


class MarketService:
    def __init__(self, market_repo: BaseRepository):
        self.market_repo = market_repo

    async def add_market(self, data: CreateUpdateMarket):
        data_dict = data.model_dump()
        market_object = await self.market_repo.add_object(data_dict)
        return market_object

    async def get_all(self):
        market_object = await self.market_repo.get_all()
        return market_object

    async def get_one(self, market_id: int):
        market_object = await self.market_repo.get_one(market_id)
        return market_object

    async def delete_market(self, market_id: int):
        market_object = await self.market_repo.delete_object(market_id)
        return market_object

    async def update_market(self, market_id: int, data: CreateUpdateMarket):
        data_dict = data.model_dump()
        market_object = await self.market_repo.update_object(market_id, data_dict)
        return market_object
