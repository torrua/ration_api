from __future__ import annotations

from .orm_base import OrmBase


class ProductCategoryBase(OrmBase):
    title: str
    description: str | None = None


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryUpdate(ProductCategoryBase):
    pass


class ProductCategoryInDBBase(ProductCategoryBase):
    id: int
    user_id: int


# Properties to return via API
class ProductCategory(ProductCategoryInDBBase):
    products: list["ProductInDBBase"]
