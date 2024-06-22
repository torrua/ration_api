from __future__ import annotations

from .orm_base import OrmBase
from .utils import partial_model


class MealtimeTypeBase(OrmBase):
    title: str
    description: str | None = None


class MealtimeTypeCreate(MealtimeTypeBase):
    pass


@partial_model
class MealtimeTypeUpdate(MealtimeTypeBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class MealtimeTypeInDB(MealtimeTypeBase):
    id: int
    user_id: int


class MealtimeType(MealtimeTypeInDB):
    mealtimes: "MealtimeInDB"


from .mealtime import MealtimeInDB

MealtimeType.model_rebuild()
