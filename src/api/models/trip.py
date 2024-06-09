from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base
from .connect_tables import t_connect_trip_participant
from .mixins import (
    NutritionCalculableMixin,
    RefUserMixin,
    round_nutrition_value, UserIdTitleUCMixin,
)

if TYPE_CHECKING:  # pragma: no cover
    from .user import User
    from .participant import Participant
    from .mealtime import Mealtime
    from .portion import Portion


class Trip(UserIdTitleUCMixin, NutritionCalculableMixin, Base):
    """
    Фактически путешествие в разрезе продуктовой раскладки это
    отсортированный по времени перечень приемов пищи с учетом
    количества и типа участников.
    """

    user: Mapped[User] = relationship(back_populates="trips")

    title: Mapped[str]

    mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="trip",
        lazy="joined",
    )

    started_at: Mapped[datetime | None] = mapped_column((DateTime(timezone=False)))
    ended_at: Mapped[datetime | None] = mapped_column((DateTime(timezone=False)))

    participants: Mapped[list[Participant]] = relationship(
        secondary=t_connect_trip_participant,
        back_populates="trips",
        lazy="joined",
    )

    @property
    @round_nutrition_value
    def number_of_participants(self) -> int:
        return len(self.participants)

    @property
    def common_coefficient(self) -> float:
        return sum(
            participant.coefficient for participant in self.participants
        )

    @property
    @round_nutrition_value
    def portions(self) -> list[Portion]:
        return [
            portion for meal in self.mealtimes for portion in meal.portions
        ]

    @property
    @round_nutrition_value
    def carbohydrates(self) -> float:
        total_carbohydrates = 0
        for portion in self.portions:
            portion_coefficient = (
                self.number_of_participants
                if portion.is_fixed
                else self.common_coefficient
            )
            total_carbohydrates += portion.carbohydrates * portion_coefficient
        return total_carbohydrates

    @property
    @round_nutrition_value
    def fat(self) -> float:
        total_fat = 0
        for mealtime in self.mealtimes:
            for portion in mealtime.portions:
                portion_coefficient = (
                    self.number_of_participants
                    if portion.is_fixed
                    else self.common_coefficient
                )
                total_fat += portion.fat * portion_coefficient
        return total_fat

    @property
    @round_nutrition_value
    def protein(self) -> float:
        total_protein = 0
        for mealtime in self.mealtimes:
            for portion in mealtime.portions:
                portion_coefficient = (
                    self.number_of_participants
                    if portion.is_fixed
                    else self.common_coefficient
                )
                total_protein += portion.protein * portion_coefficient
        return total_protein

    @property
    @round_nutrition_value
    def calories(self) -> float:
        total_calories = 0
        for mealtime in self.mealtimes:
            for portion in mealtime.portions:
                portion_coefficient = (
                    self.number_of_participants
                    if portion.is_fixed
                    else self.common_coefficient
                )
                total_calories += portion.calories * portion_coefficient
        return total_calories
