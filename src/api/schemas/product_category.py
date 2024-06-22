from __future__ import annotations

from .orm_base import OrmBase
from .utils import partial_model


class ProductCategoryBase(OrmBase):
    title: str
    description: str | None = None


class ProductCategoryCreate(ProductCategoryBase):
    pass


@partial_model
class ProductCategoryUpdate(ProductCategoryBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class ProductCategoryInDB(ProductCategoryBase):
    id: int
    user_id: int


# Properties to return via API
class ProductCategory(ProductCategoryInDB):
    products: list["ProductInDB"] = None  # Postponed annotation


from .product import ProductInDB

ProductCategory.model_rebuild()
