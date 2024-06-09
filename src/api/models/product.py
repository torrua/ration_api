from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped, mapped_column, declared_attr

from .base import Base
from .mixins import RefUserMixin, UserIdTitleUCMixin
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .product_category import ProductCategory
    from .user import User


class Product(RefUserMixin, Base):
    @declared_attr
    def __table_args__(self):
        return (
            UniqueConstraint(
                "user_id",
                "name",
                name=f"_{self.__name__}_user_id_name_uc",
            ),
        )

    user: Mapped[User] = relationship(back_populates="products")

    name: Mapped[str]

    protein: Mapped[float] = mapped_column(default=0)
    fat: Mapped[float] = mapped_column(default=0)
    carbohydrates: Mapped[float] = mapped_column(default=0)
    calories: Mapped[float] = mapped_column(default=0)

    product_category_id: Mapped[int | None] = mapped_column(
        ForeignKey("product_category.id", ondelete='SET NULL')
    )
    product_category: Mapped[ProductCategory | None] = relationship(
        back_populates="products",
        lazy="joined",
    )

    portions: Mapped[list[Portion]] = relationship(
        back_populates="product",
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
