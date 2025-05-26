from app.models.extra import Game, ItemType
from app.repositories.base import SQLAlchemyRepository


class GameRepository(SQLAlchemyRepository):
    model = Game


class ItemTypeRepository(SQLAlchemyRepository):
    model = ItemType
