from __future__ import annotations

from typing import List, Type

from .orm_base import OrmBase


class ProductCategoryBase(OrmBase):
    title: str
    description: str | None = None


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryUpdate(ProductCategoryBase):
    title: str | None = None


class ProductCategoryInDB(ProductCategoryBase):
    id: int
    user_id: int


# Properties to return via API
class ProductCategory(ProductCategoryInDB):
    products: List["ProductInDB"] = None  # Postponed annotation


from .product import ProductInDB

ProductCategory.model_rebuild()
