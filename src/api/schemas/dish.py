from __future__ import annotations

from .orm_base import OrmBase


class DishBase(OrmBase):
    title: str
    description: str | None = None


class DishCreate(DishBase):
    pass


class DishUpdate(DishBase):
    title: str | None = None

    class Config:
        exclude_unset = True


class DishInDB(DishBase):
    id: int
    user_id: int


# Properties to return via API
class Dish(DishInDB):
    portions: list["PortionInDB"]
    meals: list["MealInDB"]

    class Config:
        exclude_unset = True


from .portion import PortionInDB
from .meal import MealInDB

Dish.model_rebuild()
