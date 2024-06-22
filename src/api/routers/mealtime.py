from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .utils import create, read_all, read_one, delete, update
from ..models import User, Mealtime as ItemORM
from ..schemas.mealtime import (
    Mealtime as Item,
    MealtimeCreate as ItemCreate,
    MealtimeUpdate as ItemUpdate,
    MealtimeInDB as ItemInDB,
)
from ...auth.base_config import current_user
from ...database import get_async_session

router = APIRouter(
    prefix="/mealtimes",
    tags=["mealtimes"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=ItemInDB, status_code=status.HTTP_201_CREATED)
async def create_mealtime(
    item: ItemCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await create(data=item, class_orm=ItemORM, session=session, user=user)


@router.put("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_mealtime(
    item_id: int,
    item_update: ItemUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await update(item_id=item_id, data=item_update, class_orm=ItemORM, session=session, user=user)


@router.get("/", response_model=list[ItemInDB], status_code=status.HTTP_200_OK)
async def read_mealtimes(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_all(class_orm=ItemORM, session=session, user=user)


@router.get("/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def read_mealtime(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await read_one(
        item_id=item_id, class_orm=ItemORM, session=session, user=user,
    )


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_mealtime(
    item_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    return await delete(
        item_id=item_id, class_orm=ItemORM, session=session, user=user
    )
