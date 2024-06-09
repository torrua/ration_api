from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins import RefUserMixin, UserIdTitleUCMixin

if TYPE_CHECKING:  # pragma: no cover
    from .mealtime import Mealtime
    from .user import User


class MealtimeType(UserIdTitleUCMixin, Base):
    """
    Тип приема пищи: завтрак, обед, ужин, полдник, перекус
    """

    user: Mapped[User] = relationship(back_populates="mealtime_types")

    title: Mapped[str]
    mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="mealtime_type",
    )
