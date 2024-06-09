from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import User, Product as ItemORM
from ...auth.base_config import current_user
from ..schemas.product import Product as Item, ProductCreate as ItemCreate
from ...database import get_async_session

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_product(
    item: ItemCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    new_item = ItemORM(**item.dict(), user_id=user.id)
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item


@router.get("/")
async def read_products(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    items = await session.execute(select(ItemORM).where(ItemORM.user_id == user.id))
    return [Item.model_validate(item) for item in items.scalars().all()]


@router.get("/{item_id}")
async def read_product(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    item = await session.execute(
        select(ItemORM).where(ItemORM.id == item_id, ItemORM.user_id == user.id)
    )
    return Item.model_validate(item.scalars().first())
