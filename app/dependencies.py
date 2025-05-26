from fastapi import Depends

from app.db.session import get_db
from app.repositories.extra import ItemTypeRepository, GameRepository
from app.services.extra.itemtype import ItemTypeService
from app.services.extra.game import GameService

from sqlalchemy.ext.asyncio import AsyncSession


async def get_game_repository(session: AsyncSession = Depends(get_db)):
    return GameRepository(session)


async def get_game_service(repo: GameRepository = Depends(get_game_repository)):
    return GameService(repo)


async def get_itemtype_repository(session: AsyncSession = Depends(get_db)):
    return ItemTypeRepository(session)


async def get_itemtype_service(repo: ItemTypeRepository = Depends(get_itemtype_repository)):
    return ItemTypeService(repo)
