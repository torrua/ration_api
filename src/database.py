from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.pool import NullPool

from .api.models import Base
from .config import (
    SQL_REQUESTS_ECHO,
    APP_NAME,
    DB_HOST,
    DB_NAME,
    DB_PASS,
    DB_PORT,
    DB_USER,
)
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(
    DATABASE_URL,
    poolclass=NullPool,
    pool_recycle=5,
    pool_pre_ping=True,
    echo=SQL_REQUESTS_ECHO,
    connect_args={"server_settings": {"application_name": APP_NAME}},
)

async_session_maker = async_sessionmaker(
    bind=engine, future=True, expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
