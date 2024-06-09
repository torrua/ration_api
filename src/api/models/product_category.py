from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import RefUserMixin
from .product import Product

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class ProductCategory(RefUserMixin, Base):
    __tablename__ = "product_category"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name=f"_{__tablename__}_user_id_title_uc",
        ),
    )

    user: Mapped[User] = relationship(back_populates="product_categories")
    title: Mapped[str]
    description: Mapped[str | None]

    products: Mapped[list[Product]] = relationship(
        back_populates="product_category",
    )
