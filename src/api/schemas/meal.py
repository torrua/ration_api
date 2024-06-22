from __future__ import annotations

from .orm_base import OrmBase


class MealBase(OrmBase):
    title: str
    description: str | None = None


class MealCreate(MealBase):
    pass


class MealUpdate(MealBase):
    title: str | None = None

    class Config:
        exclude_unset = True


class MealInDB(MealBase):
    id: int
    user_id: int


# Properties to return via API
class Meal(MealInDB):
    dishes: list["DishInDB"]
    mealtimes: list["MealtimeInDB"]

    class Config:
        exclude_unset = True


from .dish import DishInDB
from .mealtime import MealtimeInDB

Meal.model_rebuild()
