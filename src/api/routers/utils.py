from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.models import User


async def create_item(item, class_orm, session: AsyncSession, user: User):
    new_item = class_orm(**item.dict(), user_id=user.id)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item


async def delete_item(item_id: int, class_orm, session: AsyncSession, user: User):
    item = await session.execute(
        select(class_orm).where(class_orm.id == item_id, class_orm.user_id == user.id)
    )
    deleted = item.scalars().first()
    await session.delete(deleted)
    await session.commit()
    return deleted


async def read_item(item_id: int, class_orm, session, user: User):
    item = await session.execute(
        select(class_orm).where(class_orm.id == item_id, class_orm.user_id == user.id)
    )
    return item.scalars().first()


async def read_items(
    class_orm,
    session: AsyncSession,
    user: User,
):
    try:
        items = await session.execute(
            select(class_orm).where(class_orm.user_id == user.id)
        )
        return items.scalars().all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        ) from e
