from __future__ import annotations

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None

    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    email: str
    password: str

    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None

    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False
