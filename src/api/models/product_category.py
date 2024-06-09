from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import UserIdTitleUCMixin
from .product import Product

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class ProductCategory(UserIdTitleUCMixin, Base):
    user: Mapped[User] = relationship(back_populates="product_categories")
    products: Mapped[list[Product]] = relationship(
        back_populates="product_category",
    )
