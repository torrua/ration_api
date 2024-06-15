from __future__ import annotations

from .orm_base import OrmBase


class UserBase(OrmBase):
    email: str


class User(UserBase):
    first_name: str | None
    last_name: str | None
    username: str | None

    is_active: bool
    is_superuser: bool
    is_verified: bool
