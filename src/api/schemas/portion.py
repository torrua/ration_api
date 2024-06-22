# product.py
from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase
from .utils import partial_model


class PortionBase(OrmBase):
    title: str
    description: str | None = None
    product_id: int
    unit_id: int
    value: float
    is_fixed: bool = Field(default=False)


class PortionCreate(PortionBase):
    pass


@partial_model
class PortionUpdate(PortionBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class PortionInDB(PortionBase):
    id: int
    user_id: int


# Properties to return via API
class Portion(PortionInDB):
    product: "ProductInDB"
    unit: "UnitInDB"
    dishes: list["DishInDB"]


from .product import ProductInDB
from .unit import UnitInDB
from .dish import DishInDB

Portion.model_rebuild()
