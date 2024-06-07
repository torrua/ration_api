from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .connect_tables import (
    t_connect_meal_dish,
    t_connect_dish_portion,
)
from .mixins import (
    NutritionCalculableMixin,
    RefUserMixin,
    round_nutrition_value,
)

if TYPE_CHECKING:  # pragma: no cover
    from src.api.models.meal import Meal
    from src.api.models.portion import Portion
    from src.api.models.user import User


class Dish(RefUserMixin, NutritionCalculableMixin, Base):
    __tablename__ = "dish"
    user: Mapped[User] = relationship(back_populates="relationship_dishes")

    title: Mapped[str]
    description: Mapped[str | None]
    # TODO add category for dishes

    relationship_portions: Mapped[list[Portion]] = relationship(
        secondary=t_connect_dish_portion,
        back_populates="relationship_dishes",
        lazy="dynamic",
    )

    relationship_meals: Mapped[list[Meal]] = relationship(
        secondary=t_connect_meal_dish,
        back_populates="relationship_dishes",
        lazy="dynamic",
    )

    @property
    @round_nutrition_value
    def carbohydrates(self) -> float:
        return sum(portion.carbohydrates for portion in self.relationship_portions)

    @property
    @round_nutrition_value
    def fat(self) -> float:
        return sum(portion.fat for portion in self.relationship_portions)

    @property
    @round_nutrition_value
    def protein(self) -> float:
        return sum(portion.protein for portion in self.relationship_portions)

    @property
    @round_nutrition_value
    def calories(self) -> float:
        return sum(portion.calories for portion in self.relationship_portions)

    @property
    def is_fixed(self) -> bool:
        return any(portion.is_fixed for portion in self.relationship_portions)
