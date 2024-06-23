from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .connect_tables import t_connect_meal_dish
from .dish import Dish
from .mealtime import Mealtime
from .mixins import (
    UserIdTitleUCMixin,
    NutritionCalculableMixin,
    WeightCalculableMixin,
)
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class Meal(UserIdTitleUCMixin, WeightCalculableMixin, NutritionCalculableMixin, Base):

    user: Mapped[User] = relationship(back_populates="meals")

    dishes: Mapped[list[Dish]] = relationship(
        secondary=t_connect_meal_dish,
        back_populates="meals",
        lazy="joined",
    )
    mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="meal",
    )

    @property
    def portions(self) -> list[Portion]:
        return [portion for dish in self.dishes for portion in dish.portions]

    @property
    def carbohydrates(self) -> float:
        return sum(dish.carbohydrates for dish in self.dishes)

    @property
    def fat(self) -> float:
        return sum(dish.fat for dish in self.dishes)

    @property
    def protein(self) -> float:
        return sum(dish.protein for dish in self.dishes)

    @property
    def calories(self) -> float:
        return sum(dish.calories for dish in self.dishes)

    @property
    def weight(self) -> float:
        return sum(portion.weight for portion in self.portions)
