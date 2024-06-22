# product.py
from __future__ import annotations

from .orm_base import OrmBase
from .utils import partial_model


class UnitBase(OrmBase):
    title: str
    description: str | None = None
    ratio_gr: float


class UnitCreate(UnitBase):
    pass


@partial_model
class UnitUpdate(UnitBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class UnitInDB(UnitBase):
    id: int
    user_id: int


# Properties to return via API
class Unit(UnitInDB):
    portions: list["PortionInDB"]


from .portion import PortionInDB

Unit.model_rebuild()
