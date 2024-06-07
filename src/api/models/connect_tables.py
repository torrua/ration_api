from __future__ import annotations

from sqlalchemy import Table, Column, ForeignKey

from .base import Base

t_connect_meal_dish = Table(
    "connect_meal_dish",
    Base.metadata,
    Column("meal_id", ForeignKey("meal.id"), primary_key=True),
    Column("dish_id", ForeignKey("dish.id"), primary_key=True),
)
t_connect_dish_portion = Table(
    "connect_dish_portion",
    Base.metadata,
    Column("dish_id", ForeignKey("dish.id"), primary_key=True),
    Column("portion_id", ForeignKey("portion.id"), primary_key=True),
)

t_connect_trip_participant = Table(
    "connect_trip_participant",
    Base.metadata,
    Column("trip_id", ForeignKey("trip.id"), primary_key=True),
    Column("participant_id", ForeignKey("participant.id"), primary_key=True),
)
