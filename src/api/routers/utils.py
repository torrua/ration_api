from __future__ import annotations

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status

from src.api.models import User


class CRUDService:

    @staticmethod
    def select_stmt(class_orm, user_id: int, item_id: int = None):
        stmt = select(class_orm).where(class_orm.user_id == user_id)
        if item_id is not None:
            stmt = stmt.where(class_orm.id == item_id)
        return stmt

    @classmethod
    async def read_one(cls, item_id: int, class_orm, session, user: User):
        stmt = cls.select_stmt(class_orm, user.id, item_id)
        for r in class_orm.relationships():
            stmt = stmt.options(selectinload(getattr(class_orm, r)))
        result = await session.execute(stmt)
        item = result.scalars().first()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return item

    @classmethod
    async def read_all(cls, class_orm, session: AsyncSession, user: User):
        try:
            items = await session.execute(cls.select_stmt(class_orm, user.id))
            return items.scalars().all()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
            ) from e

    @classmethod
    async def create_item(cls, data, class_orm, session: AsyncSession, user: User):
        new_item = class_orm(**data.dict(), user_id=user.id)
        session.add(new_item)
        await session.commit()
        await session.refresh(new_item)
        return new_item

    @classmethod
    async def update(cls, item_id, data, class_orm, session, user):
        item_db = await session.execute(cls.select_stmt(class_orm, user.id, item_id))
        item_db = item_db.scalars().first()
        if item_db is None:
            raise HTTPException(status_code=404, detail="Item not found")
        for key, value in data.dict(exclude_unset=True).items():
            setattr(item_db, key, value)
        await session.commit()
        await session.refresh(item_db)
        return item_db

    @classmethod
    async def delete(cls, item_id: int, class_orm, session: AsyncSession, user: User):
        item = await session.execute(cls.select_stmt(class_orm, user.id, item_id))
        deleted = item.scalars().first()
        await session.delete(deleted)
        await session.commit()
        return deleted
