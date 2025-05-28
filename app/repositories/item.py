from app.models.item import Item
from app.repositories.base import SQLAlchemyRepository


class ItemRepository(SQLAlchemyRepository):
    model = Item
