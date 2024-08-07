from __future__ import annotations

from fastapi_users import schemas
from pydantic import StringConstraints
from typing_extensions import Annotated


class UserRead(schemas.BaseUser[int]):  # pylint: disable=R0903
    id: int
    email: str
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:  # pylint: disable=R0903
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: Annotated[str, StringConstraints(min_length=10)]

    first_name: str | None = None
    last_name: str | None = None
    username: Annotated[str, StringConstraints(min_length=3)] | None = None

    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
