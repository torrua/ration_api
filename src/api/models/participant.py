from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr

from .base import Base
from .connect_tables import t_connect_trip_participant
from .mixins import RefUserMixin

if TYPE_CHECKING:  # pragma: no cover
    from .trip import Trip
    from .user import User


class Participant(RefUserMixin, Base):
    # TODO При создании нового пользователя добавлять стандартного участника

    @declared_attr
    def __table_args__(self):
        return (UniqueConstraint("user_id", "name", name=f"_{self.__name__}_user_id_name_uc", ),)

    user: Mapped[User] = relationship(back_populates="participants")

    name: Mapped[str]
    coefficient: Mapped[float] = mapped_column(default=1.0)

    trips: Mapped[list[Trip]] = relationship(
        secondary=t_connect_trip_participant,
        back_populates="participants",
    )
