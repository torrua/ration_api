from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import create_item, read_items, read_item, delete_item
from ..models import User, Product as ItemORM
from ..schemas.product import (
    Product as Item,
    ProductCreate as ItemCreate,
    ProductBase as ItemBase,
    ProductUpdate as ItemUpdate,
)
from ...auth.base_config import current_user
from ...database import get_async_session

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ItemBase)
async def create_product(
    item: ItemCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await create_item(item=item, class_orm=ItemORM, session=session, user=user)


async def check_item_ownership(
    item_id: int,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
) -> ItemORM:
    item_db = await session.execute(select(ItemORM).where(ItemORM.id == item_id))
    item_db = item_db.scalars().first()
    if item_db is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if item_db.user_id != user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to update this item"
        )
    return item_db


@router.put("/{item_id}", response_model=ItemBase)
async def update_product(
    item_update: ItemUpdate,
    item_db: ItemORM = Depends(check_item_ownership),
    session: AsyncSession = Depends(get_async_session),
):
    for key, value in item_update.dict(exclude_unset=True).items():
        setattr(item_db, key, value)
    session.add(item_db)
    await session.commit()
    await session.refresh(item_db)
    return item_db


@router.get("/", response_model=list[Item], status_code=status.HTTP_200_OK)
async def read_products(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_items(class_orm=ItemORM, session=session, user=user)


@router.get("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def read_product(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_item(
        item_id=item_id, class_orm=ItemORM, session=session, user=user
    )


@router.delete("/{item_id}", response_model=ItemBase, status_code=status.HTTP_200_OK)
async def delete_product(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """
    Deletes a product by its ID.
    Args:
        item_id (int): The ID of the product to delete.
        session (AsyncSession, optional): The database session.
        Defaults to Depends(get_async_session).
        user (User, optional): The authenticated user. Defaults to Depends(current_user).
    Returns:
        None: If the product is successfully deleted.
    Raises:
        HTTPException: If the product is not found or the user is not authorized to delete it.
    """
    return await delete_item(
        item_id=item_id, class_orm=ItemORM, session=session, user=user
    )
