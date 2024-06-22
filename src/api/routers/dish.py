from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import create, read_all, read_one, delete, update
from ..models import User, Dish as ItemORM
from ..schemas.dish import (
    Dish as Item,
    DishCreate as ItemCreate,
    DishUpdate as ItemUpdate,
    DishInDB as ItemInDB,
)
from ...auth.base_config import current_user
from ...database import get_async_session

router = APIRouter(
    prefix="/dishes",
    tags=["dishes"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=ItemInDB, status_code=status.HTTP_201_CREATED)
async def create_dish(
    item: ItemCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await create(data=item, class_orm=ItemORM, session=session, user=user)


@router.put("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_dish(
    item_id: int,
    item_update: ItemUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await update(item_id=item_id, data=item_update, class_orm=ItemORM, session=session, user=user)


@router.get("/", response_model=list[ItemInDB], status_code=status.HTTP_200_OK)
async def read_dishes(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_all(class_orm=ItemORM, session=session, user=user)


@router.get("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def read_dish(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_one(
        item_id=item_id, class_orm=ItemORM, session=session, user=user,
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dish(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await delete(
        item_id=item_id, class_orm=ItemORM, session=session, user=user
    )
