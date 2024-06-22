from __future__ import annotations

from datetime import datetime

from .orm_base import OrmBase
from .utils import partial_model


class MealtimeBase(OrmBase):
    title: str
    description: str | None = None
    trip_id: int
    meal_id: int
    mealtime_type_id: int | None = None
    scheduled_at: datetime | None = None

    carbohydrates: float
    fat: float
    protein: float
    calories: float


class MealtimeCreate(MealtimeBase):
    pass


@partial_model
class MealtimeUpdate(MealtimeBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class MealtimeInDB(MealtimeBase):
    id: int
    user_id: int


# Properties to return via API
class Mealtime(MealtimeInDB):
    trip: list["TripInDB"]
    meal: "MealInDB"
    mealtime_type: "MealtimeTypeInDB"


from .trip import TripInDB
from .meal import MealInDB
from .mealtime_type import MealtimeTypeInDB

Mealtime.model_rebuild()
