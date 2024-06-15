from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .connect_tables import t_connect_trip_participant
from .mixins import UserIdTitleUCMixin

if TYPE_CHECKING:  # pragma: no cover
    from .trip import Trip
    from .user import User


class Participant(UserIdTitleUCMixin, Base):

    user: Mapped[User] = relationship(back_populates="participants")
    coefficient: Mapped[float] = mapped_column(default=1.0)

    trips: Mapped[list[Trip]] = relationship(
        secondary=t_connect_trip_participant,
        back_populates="participants",
    )
