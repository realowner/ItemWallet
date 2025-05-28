from app.models.extra import Game, ItemType, GameAccounts, ItemFloat, Market
from app.repositories.base import SQLAlchemyRepository


class GameRepository(SQLAlchemyRepository):
    model = Game


class ItemTypeRepository(SQLAlchemyRepository):
    model = ItemType


class GameAccountRepository(SQLAlchemyRepository):
    model = GameAccounts


class ItemFloatRepository(SQLAlchemyRepository):
    model = ItemFloat


class MarketRepository(SQLAlchemyRepository):
    model = Market
