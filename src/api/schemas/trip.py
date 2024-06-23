# product.py
from __future__ import annotations

from datetime import datetime

from .orm_base import OrmBase
from .utils import partial_model


class TripBase(OrmBase):
    title: str
    description: str | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None

    carbohydrates: float
    fat: float
    protein: float
    calories: float
    weight: float


class TripCreate(TripBase):
    pass


@partial_model
class TripUpdate(TripBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class TripInDB(TripBase):
    id: int
    user_id: int


# Properties to return via API
class Trip(TripInDB):
    mealtimes: list["MealtimeInDB"]
    participants: list["ParticipantInDB"]


from .mealtime import MealtimeInDB
from .participant import ParticipantInDB

Trip.model_rebuild()
