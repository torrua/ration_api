# product.py
from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase


class ParticipantBase(OrmBase):
    title: str
    description: str | None = None
    coefficient: float = Field(default=1.0)


class ParticipantCreate(ParticipantBase):
    pass


class ParticipantUpdate(ParticipantBase):
    title: str | None = None
    coefficient: float | None = Field(default=1.0)

    class Config:
        exclude_unset = True


class ParticipantInDB(ParticipantBase):
    id: int
    user_id: int


# Properties to return via API
class Participant(ParticipantInDB):
    trips: "TripInDB"

    class Config:
        exclude_unset = True


from .trip import TripInDB

Participant.model_rebuild()
