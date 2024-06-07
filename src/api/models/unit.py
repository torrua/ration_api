from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import RefUserMixin

if TYPE_CHECKING:  # pragma: no cover
    from .portion import Portion
    from .user import User


class Unit(RefUserMixin, Base):
    __tablename__ = "unit"
    __table_args__ = (
        UniqueConstraint("name", "user_id", name="_unit_name_user_id_uc"),
    )
    user: Mapped[User] = relationship(back_populates="relationship_units")

    name: Mapped[str]
    description: Mapped[str | None]

    relationship_portions: Mapped[list[Portion]] = relationship(
        back_populates="unit",
        lazy="dynamic",
    )
