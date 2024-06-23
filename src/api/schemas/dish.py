from __future__ import annotations

from .orm_base import OrmBase
from .utils import partial_model


class DishBase(OrmBase):
    title: str
    description: str | None = None

    carbohydrates: float
    fat: float
    protein: float
    calories: float
    weight: float
    is_fixed: bool


class DishCreate(DishBase):
    pass


@partial_model
class DishUpdate(DishBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class DishInDB(DishBase):
    id: int
    user_id: int


# Properties to return via API
class Dish(DishInDB):
    portions: list["PortionInDB"]
    meals: list["MealInDB"]


from .portion import PortionInDB
from .meal import MealInDB

Dish.model_rebuild()
