from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .connect_tables import t_connect_trip_participant
from .mixins import RefUserMixin

if TYPE_CHECKING:  # pragma: no cover
    from .trip import Trip
    from .user import User


class Participant(RefUserMixin, Base):
    # TODO При создании нового пользователя добавлять стандартного участника
    __tablename__ = "participant"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "title",
            name=f"_{__tablename__}_user_id_title_uc",
        ),
    )
    user: Mapped[User] = relationship(back_populates="participants")

    title: Mapped[str]
    description: Mapped[str | None]

    coefficient: Mapped[float] = mapped_column(default=1.0)

    trips: Mapped[list[Trip]] = relationship(
        secondary=t_connect_trip_participant,
        back_populates="participants",
    )
