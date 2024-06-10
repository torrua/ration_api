from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase
from .product_category import ProductCategoryInDBBase


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


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: int
    user_id: int


# Properties to return via API
class Product(ProductInDBBase):
    product_category: ProductCategoryInDBBase | None = None
    # portions: list[Portion]
