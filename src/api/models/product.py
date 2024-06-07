from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base
from .mixins import RefUserMixin
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .product_category import ProductCategory
    from .user import User


class Product(RefUserMixin, Base):
    __tablename__ = "product"
    __table_args__ = (
        UniqueConstraint("name", "user_id", name="_product_name_user_id_uc"),
    )
    user: Mapped[User] = relationship(back_populates="relationship_products")

    name: Mapped[str]
    description: Mapped[str | None]

    protein: Mapped[float] = mapped_column(default=0)
    fat: Mapped[float] = mapped_column(default=0)
    carbohydrates: Mapped[float] = mapped_column(default=0)
    calories: Mapped[float] = mapped_column(default=0)

    product_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("product_category.id")
    )
    product_category: Mapped[ProductCategory] = relationship(
        back_populates="relationship_products"
    )

    relationship_portions: Mapped[list[Portion]] = relationship(
        back_populates="product",
        lazy="dynamic",
    )

    @hybrid_property
    def title(self) -> str:
        return (
            f"#{self.id or ''} {self.name} "
            f"{self.protein:.1f}/{self.fat:.1f}/{self.carbohydrates:.1f} "
            f"({self.calories:.1f})"
        )

    def __str__(self) -> str:
        return str(self.title)
