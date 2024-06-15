from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .utils import create_item, read_items, delete_item
from ..models import User, ProductCategory as ItemORM
from ..schemas.product_category import ProductCategory as Item
from ..schemas.product_category import (
    ProductCategoryCreate as ItemCreate,
    ProductCategoryUpdate as ItemUpdate,
)
from ..schemas.product_category import ProductCategoryInDBBase as ItemInDBBase
from ...auth.base_config import current_user
from ...database import get_async_session

router = APIRouter(
    prefix="/product_categories",
    tags=["product_categories"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_product_category(
    item: ItemCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await create_item(item=item, class_orm=ItemORM, session=session, user=user)


@router.get("/", response_model=list[ItemInDBBase])
async def read_product_categories(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_items(class_orm=ItemORM, session=session, user=user)


@router.get("/{item_id}")
async def read_product_category(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    item = await session.execute(
        select(ItemORM)
        .options(joinedload(ItemORM.products))
        .where(ItemORM.id == item_id, ItemORM.user_id == user.id)
    )
    return Item.model_validate(item.scalars().first())


@router.put("/{item_id}")
async def update_product_category(
    item_id: int,
    item: ItemUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    item_db = await session.execute(
        select(ItemORM).where(ItemORM.id == item_id, ItemORM.user_id == user.id)
    )
    item_db = item_db.scalars().first()
    item_db.title = item.title
    item_db.description = item.description
    await session.commit()
    return item_db


@router.delete("/{item_id}")
async def delete_product_category(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await delete_item(
        item_id=item_id, class_orm=ItemORM, session=session, user=user
    )
