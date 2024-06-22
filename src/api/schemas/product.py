# product.py
from __future__ import annotations

from typing import Optional

from pydantic import Field

from .orm_base import OrmBase
from .utils import partial_model


class ProductBase(OrmBase):
    title: str
    description: str | None = None
    protein: float = Field(default=0, ge=0)
    fat: float = Field(default=0, ge=0)
    carbohydrates: float = Field(default=0, ge=0)
    calories: float = Field(default=0, ge=0)
    product_category_id: int | None = None


class ProductCreate(ProductBase):
    pass


@partial_model
class ProductUpdate(ProductBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class ProductInDB(ProductBase):
    id: int
    user_id: int


# Properties to return via API
class Product(ProductInDB):
    product_category: Optional["ProductCategoryInDB"] = None
    portions: list["PortionInDB"]


from .product_category import ProductCategoryInDB
from .portion import PortionInDB

Product.model_rebuild()
