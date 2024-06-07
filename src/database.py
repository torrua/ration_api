from typing import AsyncGenerator

from sqlalchemy.pool import NullPool

from .config import DATABASE_URI, SQL_REQUESTS_ECHO, APP_NAME
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

engine = create_async_engine(
    DATABASE_URI,
    poolclass=NullPool,
    pool_recycle=5,
    pool_pre_ping=True,
    echo=SQL_REQUESTS_ECHO,
    connect_args={
        "application_name": APP_NAME,
    },
)

async_session_maker = async_sessionmaker(
    bind=engine, future=True, expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
