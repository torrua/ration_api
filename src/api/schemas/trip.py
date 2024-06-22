# product.py
from __future__ import annotations

from datetime import datetime

from .orm_base import OrmBase


class TripBase(OrmBase):
    title: str
    description: str | None = None
    started_at: datetime | None = None
    ended_at: datetime | None = None


class TripCreate(TripBase):
    pass


class TripUpdate(TripBase):
    title: str | None = None

    class Config:
        exclude_unset = True


class TripInDB(TripBase):
    id: int
    user_id: int


# Properties to return via API
class Trip(TripInDB):
    mealtimes: list["MealtimeInDB"]
    participants: list["ParticipantInDB"]

    class Config:
        exclude_unset = True


from .mealtime import MealtimeInDB
from .participant import ParticipantInDB

Trip.model_rebuild()
