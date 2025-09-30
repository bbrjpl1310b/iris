from datetime import date

from pydantic import BaseModel, Field

from iris.models._presence_type import PresenceType
from iris.models._timeslot import Timeslot


class PresenceExtra(BaseModel):
    id: int = Field(alias="Id")
    presence_type: PresenceType | None = Field(alias="PresenceType")
    day: date = Field(alias="DayAt")
    time_slot: Timeslot = Field(alias="TimeSlot")
    id_weak_ref: int | None = Field(alias="IdWeakRef")
    type: int = Field(alias="Type")
