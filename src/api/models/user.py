from __future__ import annotations

from typing import Any

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, Mapped

from .base import Base
from .dish import Dish
from .meal import Meal
from .mealtime import Mealtime
from .mealtime_type import MealtimeType
from .participant import Participant
from .portion import Portion
from .product import Product
from .product_category import ProductCategory
from .trip import Trip
from .unit import Unit


class User(SQLAlchemyBaseUserTable[int], Base):  # type: ignore
    __tablename__ = "user"
    __table_args__ = (
        UniqueConstraint("email", name="_user_email_uc"),
        UniqueConstraint("username", name="_user_username_uc"),
    )

    email: Mapped[str] = mapped_column(unique=True, index=True)  # type: ignore
    hashed_password: Mapped[str]  # type: ignore

    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]

    is_active: Mapped[bool] = mapped_column(default=True)  # type: ignore
    is_superuser: Mapped[bool] = mapped_column(default=False)  # type: ignore
    is_verified: Mapped[bool] = mapped_column(default=False)  # type: ignore

    _properties: dict[str, Any] = {
        "back_populates": __tablename__,
        "cascade": "all, delete, delete-orphan",
    }
    product_categories: Mapped[list[ProductCategory]] = relationship(**_properties)
    meals: Mapped[list[Meal]] = relationship(**_properties)
    dishes: Mapped[list[Dish]] = relationship(**_properties)
    products: Mapped[list[Product]] = relationship(**_properties)
    units: Mapped[list[Unit]] = relationship(**_properties)
    portions: Mapped[list[Portion]] = relationship(**_properties)
    trips: Mapped[list[Trip]] = relationship(**_properties)
    mealtimes: Mapped[list[Mealtime]] = relationship(**_properties)
    mealtime_types: Mapped[list[MealtimeType]] = relationship(**_properties)
    participants: Mapped[list[Participant]] = relationship(**_properties)
