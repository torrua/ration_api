from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base
from .connect_tables import t_connect_trip_participant
from .mixins import (
    NutritionCalculableMixin,
    UserIdTitleUCMixin,
    WeightCalculableMixin,
    round_nutrition_value,
)

if TYPE_CHECKING:  # pragma: no cover
    from .user import User
    from .participant import Participant
    from .mealtime import Mealtime
    from .portion import Portion


class Trip(UserIdTitleUCMixin, WeightCalculableMixin, NutritionCalculableMixin, Base):
    """
    Фактически путешествие в разрезе продуктовой раскладки это
    отсортированный по времени перечень приемов пищи с учетом
    количества и типа участников.
    """

    user: Mapped[User] = relationship(back_populates="trips")

    mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="trip",
        lazy="joined",
        cascade="all, delete-orphan",
    )

    started_at: Mapped[datetime | None] = mapped_column((DateTime(timezone=False)))
    ended_at: Mapped[datetime | None] = mapped_column((DateTime(timezone=False)))

    participants: Mapped[list[Participant]] = relationship(
        secondary=t_connect_trip_participant,
        back_populates="trips",
        lazy="joined",
    )

    @property
    def number_of_participants(self) -> int:
        return len(self.participants)

    @property
    @round_nutrition_value
    def common_coefficient(self) -> float:
        return sum(participant.coefficient for participant in self.participants)

    @property
    def portions(self) -> list[Portion]:
        return [portion for mealtime in self.mealtimes for portion in mealtime.portions]

    @property
    @round_nutrition_value
    def carbohydrates(self) -> float:
        return sum(mealtime.carbohydrates for mealtime in self.mealtimes)

    @property
    @round_nutrition_value
    def fat(self) -> float:
        return sum(mealtime.fat for mealtime in self.mealtimes)

    @property
    @round_nutrition_value
    def protein(self) -> float:
        return sum(mealtime.protein for mealtime in self.mealtimes)

    @property
    @round_nutrition_value
    def calories(self) -> float:
        return sum(mealtime.calories for mealtime in self.mealtimes)

    @property
    @round_nutrition_value
    def weight(self) -> float:
        return sum(mealtime.weight for mealtime in self.mealtimes)
