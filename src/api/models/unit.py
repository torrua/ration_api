from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import RefUserMixin, UserIdTitleUCMixin

if TYPE_CHECKING:  # pragma: no cover
    from .portion import Portion
    from .user import User


class Unit(RefUserMixin, Base):
    __tablename__ = "unit"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "name",
            name=f"_{__tablename__}_user_id_name_uc",
        ),
    )
    user: Mapped[User] = relationship(back_populates="units")

    name: Mapped[str]
    portions: Mapped[list[Portion]] = relationship(
        back_populates="unit",
    )
