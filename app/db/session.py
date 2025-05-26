from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os

#TODO: перенести в config с env переменныии
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@localhost/itemwallet_dev")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
