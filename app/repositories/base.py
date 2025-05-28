from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository(ABC):
    @abstractmethod
    async def add_object(self, data: dict):
        raise NotImplemented

    @abstractmethod
    async def get_all(self):
        raise NotImplemented

    @abstractmethod
    async def get_one(self, object_id: int):
        raise NotImplemented

    @abstractmethod
    async def delete_object(self, object_id: int):
        raise NotImplemented

    @abstractmethod
    async def update_object(self, object_id: int, data: dict):
        raise NotImplemented


class SQLAlchemyRepository(BaseRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_object(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one()

    async def get_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one(self, object_id: int):
        stmt = select(self.model).where(self.model.id == object_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete_object(self, object_id: int):
        stmt = select(self.model).where(self.model.id == object_id)
        result = await self.session.execute(stmt)
        obj = result.scalar_one_or_none()

        if obj:
            await self.session.delete(obj)
            await self.session.commit()

        return obj

    async def update_object(self, object_id: int, data: dict):
        stmt = select(self.model).where(self.model.id == object_id)
        result = await self.session.execute(stmt)
        obj = result.scalar_one_or_none()

        if obj:
            for key, value in data.items():
                if value:
                    setattr(obj, key, value)

            await self.session.commit()
            await self.session.refresh(obj)

        return obj
