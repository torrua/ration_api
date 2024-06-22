from __future__ import annotations

from datetime import datetime

from .orm_base import OrmBase


class MealtimeBase(OrmBase):
    title: str
    description: str | None = None
    trip_id: int
    meal_id: int
    mealtime_type_id: int | None = None
    scheduled_at: datetime | None = None


class MealtimeCreate(MealtimeBase):
    pass


class MealtimeUpdate(MealtimeBase):
    title: str | None = None
    trip_id: int | None = None
    meal_id: int | None = None

    class Config:
        exclude_unset = True


class MealtimeInDB(MealtimeBase):
    id: int
    user_id: int


# Properties to return via API
class Mealtime(MealtimeInDB):
    trip: list["TripInDB"]
    meal: "MealInDB"
    mealtime_type: "MealtimeTypeInDB"

    class Config:
        exclude_unset = True


from .trip import TripInDB
from .meal import MealInDB
from .mealtime_type import MealtimeTypeInDB

Mealtime.model_rebuild()
