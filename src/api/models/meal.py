from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .connect_tables import t_connect_meal_dish
from .dish import Dish
from .mealtime import Mealtime
from .mixins import UserIdTitleUCMixin, round_nutrition_value, NutritionCalculableMixin
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class Meal(UserIdTitleUCMixin, NutritionCalculableMixin, Base):

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
    @round_nutrition_value
    def carbohydrates(self) -> float:
        return sum(dish.carbohydrates for dish in self.dishes)

    @property
    @round_nutrition_value
    def fat(self) -> float:
        return sum(dish.fat for dish in self.dishes)

    @property
    @round_nutrition_value
    def protein(self) -> float:
        return sum(dish.protein for dish in self.dishes)

    @property
    @round_nutrition_value
    def calories(self) -> float:
        return sum(dish.calories for dish in self.dishes)
