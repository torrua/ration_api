from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
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
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name=f"_{__tablename__}_user_id_title_uc",
        ),
    )
    user: Mapped[User] = relationship(back_populates="meals")

    title: Mapped[str]
    description: Mapped[str | None]

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
        return [
            portion
            for dish in self.dishes
            for portion in dish.portions
        ]
