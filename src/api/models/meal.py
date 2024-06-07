from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .connect_tables import t_connect_meal_dish
from .dish import Dish
from .mealtime import Mealtime
from .mixins import RefUserMixin
from .portion import Portion

if TYPE_CHECKING:  # pragma: no cover
    from .user import User


class Meal(RefUserMixin, Base):
    __tablename__ = "meal"
    user: Mapped[User] = relationship(back_populates="relationship_meals")

    title: Mapped[str]
    description: Mapped[str | None]

    relationship_dishes: Mapped[list[Dish]] = relationship(
        secondary=t_connect_meal_dish,
        back_populates="relationship_meals",
        lazy="dynamic",
    )
    relationship_mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="meal",
        lazy="dynamic",
    )

    @property
    def portions(self) -> list[Portion]:
        return [
            portion
            for dish in self.relationship_dishes
            for portion in dish.relationship_portions
        ]
