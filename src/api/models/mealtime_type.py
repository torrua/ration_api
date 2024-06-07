from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins import RefUserMixin

if TYPE_CHECKING:  # pragma: no cover
    from .mealtime import Mealtime
    from .user import User


class MealtimeType(RefUserMixin, Base):
    """
    Тип приема пищи: завтрак, обед, ужин, полдник, перекус
    """

    __tablename__ = "mealtime_type"
    user: Mapped[User] = relationship(back_populates="relationship_mealtime_types")

    title: Mapped[str]
    description: Mapped[str | None]
    relationship_mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="mealtime_type",
        lazy="dynamic",
    )
