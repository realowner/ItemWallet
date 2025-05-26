import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# МОИ МОДЕЛИ
from app.db.base import Base  # DeclarativeBase
from app.models.extra import Game, ItemType

# Alembic config object
config = context.config
fileConfig(config.config_file_name)

# Установка URL через settings
config.set_main_option("sqlalchemy.url", 'postgresql+asyncpg://postgres:password@localhost/itemwallet_dev')

target_metadata = Base.metadata


def run_migrations_offline():
    """Синхронные миграции без подключения"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    """Сами миграции"""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        render_as_batch=True,  # полезно для SQLite и сложных миграций
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Асинхронные миграции с подключением к БД"""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
    await connectable.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())