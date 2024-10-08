from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime, event
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .mixins import (
    UserIdTitleUCMixin,
    round_nutrition_value,
    NutritionCalculableMixin,
    WeightCalculableMixin,
)

if TYPE_CHECKING:  # pragma: no cover
    from .trip import Trip
    from .user import User
    from .meal import Meal
    from .mealtime_type import MealtimeType
    from .portion import Portion
    from .dish import Dish


class Mealtime(
    UserIdTitleUCMixin, WeightCalculableMixin, NutritionCalculableMixin, Base
):
    """
    Прием пищи с привязкой к категории и времени.
    Это необходимо, потому что один прием пищи может быть в разных категориях,
    например, та же гречка с тушенкой может быть как на завтрак, так и на ужин.
    """

    user: Mapped[User] = relationship(back_populates="mealtimes")

    trip_id: Mapped[int] = mapped_column(ForeignKey("trip.id"))
    trip: Mapped[Trip] = relationship(back_populates="mealtimes", lazy="joined")

    meal_id: Mapped[int] = mapped_column(ForeignKey("meal.id"))
    meal: Mapped[Meal] = relationship(back_populates="mealtimes", lazy="joined")

    mealtime_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("mealtime_type.id", ondelete="SET NULL"),
    )
    mealtime_type: Mapped[MealtimeType | None] = relationship(
        back_populates="mealtimes",
        lazy="joined",
    )

    scheduled_at: Mapped[datetime | None] = mapped_column(
        (DateTime(timezone=False)), nullable=True
    )

    @property
    def default_title(self) -> str:
        date = f"{' '+self.scheduled_at.strftime('%Y-%m-%d') if self.scheduled_at else ''}"
        return f"{self.mealtime_type.title}{date}: {self.meal.title}"

    @property
    def portions(self) -> list[Portion]:
        return self.meal.portions

    @property
    def dishes(self) -> list[Dish]:
        return self.meal.dishes

    @round_nutrition_value
    def _calculate_total_nutrient(self, nutrient_name: str) -> float:
        total_nutrient = 0.0
        for dish in self.meal.dishes:
            dish_coefficient = (
                self.trip.number_of_participants
                if dish.is_fixed
                else self.trip.common_coefficient
            )
            nutrient_value = getattr(dish, nutrient_name)
            total_nutrient += nutrient_value * dish_coefficient
        return float(total_nutrient)

    @property
    def carbohydrates(self) -> float:
        return self._calculate_total_nutrient("carbohydrates")

    @property
    def fat(self) -> float:
        return self._calculate_total_nutrient("fat")

    @property
    def protein(self) -> float:
        return self._calculate_total_nutrient("protein")

    @property
    def calories(self) -> float:
        return self._calculate_total_nutrient("calories")

    @property
    def weight(self) -> float:
        return self._calculate_total_nutrient("weight")


@event.listens_for(Mealtime, "before_insert")
def set_mealtime_user_id(_, __, mealtime):
    if mealtime.meal.user and mealtime.meal.user.id:
        mealtime.user_id = mealtime.meal.user.id
