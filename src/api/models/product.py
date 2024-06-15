from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base
from .mixins import UserIdTitleUCMixin
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .product_category import ProductCategory
    from .user import User


class Product(UserIdTitleUCMixin, Base):

    user: Mapped[User] = relationship(back_populates="products")

    protein: Mapped[float] = mapped_column(default=0)
    fat: Mapped[float] = mapped_column(default=0)
    carbohydrates: Mapped[float] = mapped_column(default=0)
    calories: Mapped[float] = mapped_column(default=0)

    product_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("product_category.id", ondelete="SET NULL")
    )
    product_category: Mapped[ProductCategory | None] = relationship(
        back_populates="products",
        lazy="joined",
    )

    portions: Mapped[list[Portion]] = relationship(
        back_populates="product",
        cascade="all, delete",
    )

    def __str__(self) -> str:
        return (
            f"#{self.id or ''} {self.title} "
            f"{self.protein:.1f}/{self.fat:.1f}/{self.carbohydrates:.1f} "
            f"({self.calories:.1f})"
        )
