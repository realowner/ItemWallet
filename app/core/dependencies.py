from fastapi import Depends

from app.db.session import get_db

from app.repositories.item import ItemRepository
from app.repositories.extra import (ItemTypeRepository, GameRepository, GameAccountRepository, ItemFloatRepository,
                                    MarketRepository)

from app.services.extra.itemtype import ItemTypeService
from app.services.extra.game import GameService
from app.services.extra.gameaccount import AccountService
from app.services.extra.itemfloat import ItemFloatService
from app.services.extra.market import MarketService
from app.services.item import ItemService

from sqlalchemy.ext.asyncio import AsyncSession


async def get_game_repository(session: AsyncSession = Depends(get_db)):
    return GameRepository(session)


async def get_game_service(repo: GameRepository = Depends(get_game_repository)):
    return GameService(repo)


async def get_itemtype_repository(session: AsyncSession = Depends(get_db)):
    return ItemTypeRepository(session)


async def get_itemtype_service(repo: ItemTypeRepository = Depends(get_itemtype_repository)):
    return ItemTypeService(repo)


async  def get_account_repository(session: AsyncSession = Depends(get_db)):
    return GameAccountRepository(session)


async def get_account_service(repo: GameAccountRepository = Depends(get_account_repository)):
    return AccountService(repo)


async def get_itemfloat_repository(session: AsyncSession = Depends(get_db)):
    return ItemFloatRepository(session)


async def get_itemfloat_service(repo: ItemFloatRepository = Depends(get_itemfloat_repository)):
    return ItemFloatService(repo)


async def get_market_repository(session: AsyncSession = Depends(get_db)):
    return MarketRepository(session)


async def get_market_service(repo: MarketRepository = Depends(get_market_repository)):
    return MarketService(repo)


async def get_item_repository(session: AsyncSession = Depends(get_db)):
    return ItemRepository(session)


async def get_item_service(repo: ItemRepository = Depends(get_item_repository)):
    return ItemService(repo)
