from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy import event
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base
from .connect_tables import t_connect_dish_portion
from .mixins import (
    NutritionCalculableMixin,
    RefUserMixin,
    round_nutrition_value,
)

if TYPE_CHECKING:  # pragma: no cover
    from .user import User
    from .unit import Unit
    from .product import Product
    from .dish import Dish


class Portion(RefUserMixin, NutritionCalculableMixin, Base):
    __tablename__ = "portion"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "product_id",
            "unit_id",
            "value",
            name="_user_product_unit_value_uc",
        ),
    )
    user: Mapped[User] = relationship(back_populates="relationship_portions")

    value: Mapped[float]
    description: Mapped[str | None]
    is_fixed: Mapped[bool] = mapped_column(default=False)

    unit_id: Mapped[int] = mapped_column(ForeignKey("unit.id"))
    unit: Mapped[Unit] = relationship(back_populates="relationship_portions")

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped[Product] = relationship(back_populates="relationship_portions")

    relationship_dishes: Mapped[list[Dish]] = relationship(
        secondary=t_connect_dish_portion,
        back_populates="relationship_portions",
        lazy="dynamic",
    )

    @property
    def product_category(self):
        return self.product.product_category

    @property
    def product_category_id(self):
        return self.product.product_category_id

    @hybrid_property
    def title(self):
        return f"{self.product.name} - {self.value} {self.unit.name}"

    @property
    @round_nutrition_value
    def carbohydrates(self) -> float:
        return self.product.carbohydrates / 100 * self.value

    @property
    @round_nutrition_value
    def fat(self) -> float:
        return self.product.fat / 100 * self.value

    @property
    @round_nutrition_value
    def protein(self) -> float:
        return self.product.protein / 100 * self.value

    @property
    @round_nutrition_value
    def calories(self) -> float:
        return self.product.calories / 100 * self.value


@event.listens_for(Portion, "before_insert")
def set_portion_user_id(_, __, portion):
    if portion.product.user and portion.product.user.id:
        portion.user_id = portion.product.user.id
