from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
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
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name=f"_{__tablename__}_user_id_title_uc",
        ),
    )
    user: Mapped[User] = relationship(back_populates="mealtime_types")

    title: Mapped[str]
    description: Mapped[str | None]
    mealtimes: Mapped[list[Mealtime]] = relationship(
        back_populates="mealtime_type",
    )
