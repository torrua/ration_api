from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import RefUserMixin
from .product import Product

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class ProductCategory(RefUserMixin, Base):
    __tablename__ = "product_category"
    user: Mapped[User] = relationship(back_populates="relationship_product_categories")

    title: Mapped[str]
    description: Mapped[str | None]

    relationship_products: Mapped[list[Product]] = relationship(
        back_populates="product_category",
        lazy="dynamic",
    )
