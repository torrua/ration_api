from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .mixins import UserIdTitleUCMixin

if TYPE_CHECKING:  # pragma: no cover
    from .portion import Portion
    from .user import User


class Unit(UserIdTitleUCMixin, Base):
    user: Mapped[User] = relationship(back_populates="units")
    portions: Mapped[list[Portion]] = relationship(
        back_populates="unit",
    )
