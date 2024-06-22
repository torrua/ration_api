# product.py
from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase


class PortionBase(OrmBase):
    title: str
    description: str | None = None
    product_id: int
    unit_id: int
    value: float
    is_fixed: bool = Field(default=False)


class PortionCreate(PortionBase):
    pass


class PortionUpdate(PortionBase):
    title: str | None = None
    product_id: int | None = None
    unit_id: int | None = None

    class Config:
        exclude_unset = True


class PortionInDB(PortionBase):
    id: int
    user_id: int


# Properties to return via API
class Portion(PortionInDB):
    product: "ProductInDB"
    unit: "UnitInDB"
    dishes: list["DishInDB"]

    class Config:
        exclude_unset = True


from .product import ProductInDB
from .unit import UnitInDB
from .dish import DishInDB

Portion.model_rebuild()
