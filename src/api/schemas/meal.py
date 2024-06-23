from __future__ import annotations

from .orm_base import OrmBase
from .utils import partial_model


class MealBase(OrmBase):
    title: str
    description: str | None = None

    carbohydrates: float
    fat: float
    protein: float
    calories: float
    weight: float


class MealCreate(MealBase):
    pass


@partial_model
class MealUpdate(MealBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class MealInDB(MealBase):
    id: int
    user_id: int


# Properties to return via API
class Meal(MealInDB):
    dishes: list["DishInDB"]
    mealtimes: list["MealtimeInDB"]


from .dish import DishInDB
from .mealtime import MealtimeInDB

Meal.model_rebuild()
