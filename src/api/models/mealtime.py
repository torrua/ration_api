from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, DateTime, event
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .mixins import RefUserMixin

if TYPE_CHECKING:  # pragma: no cover
    from .trip import Trip
    from .user import User
    from .meal import Meal
    from .mealtime_type import MealtimeType
    from .portion import Portion


class Mealtime(RefUserMixin, Base):
    """
    Прием пищи с привязкой к категории и времени.
    Это необходимо, потому что один прием пищи может быть в разных категориях,
    например, та же гречка с тушенкой может быть как на завтрак, так и на ужин.
    """

    __tablename__ = "mealtime"
    user: Mapped[User] = relationship(back_populates="relationship_mealtimes")

    title: Mapped[str]
    description: Mapped[str | None]

    trip_id: Mapped[int] = mapped_column(ForeignKey("trip.id"))
    trip: Mapped[Trip] = relationship(back_populates="relationship_mealtimes")

    meal_id: Mapped[int] = mapped_column(ForeignKey("meal.id"))
    meal: Mapped[Meal] = relationship(back_populates="relationship_mealtimes")

    mealtime_type_id: Mapped[int | None] = mapped_column(ForeignKey("mealtime_type.id"))
    mealtime_type: Mapped[MealtimeType] = relationship(
        back_populates="relationship_mealtimes"
    )

    scheduled_at: Mapped[datetime | None] = mapped_column(
        (DateTime(timezone=False)), nullable=True
    )

    @property
    def portions(self) -> list[Portion]:
        return self.meal.portions


@event.listens_for(Mealtime, "before_insert")
def set_mealtime_user_id(_, __, mealtime):
    if mealtime.meal.user and mealtime.meal.user.id:
        mealtime.user_id = mealtime.meal.user.id