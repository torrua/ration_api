# product.py
from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase
from .portion import PortionInDB


class UnitBase(OrmBase):
    title: str
    description: str | None = None
    ratio_gr: float


class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    title: str | None = None
    ratio_gr: float | None = Field(default=1.0)

    class Config:
        exclude_unset = True


class UnitInDB(UnitBase):
    id: int
    user_id: int


# Properties to return via API
class Unit(UnitInDB):
    portions: list["PortionInDB"]

    class Config:
        exclude_unset = True


Unit.model_rebuild()
