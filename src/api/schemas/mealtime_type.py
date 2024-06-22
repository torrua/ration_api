from __future__ import annotations

from datetime import datetime

from .orm_base import OrmBase


class MealtimeTypeBase(OrmBase):
    title: str
    description: str | None = None


class MealtimeTypeCreate(MealtimeTypeBase):
    pass


class MealtimeTypeUpdate(MealtimeTypeBase):
    title: str | None = None

    class Config:
        exclude_unset = True


class MealtimeTypeInDB(MealtimeTypeBase):
    id: int
    user_id: int


class MealtimeType(MealtimeTypeInDB):
    mealtimes: "MealtimeInDB"

    class Config:
        exclude_unset = True


from .mealtime import MealtimeInDB

MealtimeType.model_rebuild()
