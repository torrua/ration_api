# product.py
from __future__ import annotations

from pydantic import Field

from .orm_base import OrmBase
from .utils import partial_model


class ParticipantBase(OrmBase):
    title: str
    description: str | None = None
    coefficient: float = Field(default=1.0)


class ParticipantCreate(ParticipantBase):
    pass


@partial_model
class ParticipantUpdate(ParticipantBase):

    class Config:  # pylint: disable=R0903
        exclude_unset = True


class ParticipantInDB(ParticipantBase):
    id: int
    user_id: int


# Properties to return via API
class Participant(ParticipantInDB):
    trips: "TripInDB"


from .trip import TripInDB

Participant.model_rebuild()
