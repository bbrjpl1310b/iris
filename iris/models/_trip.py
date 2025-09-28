from datetime import date

from pydantic import BaseModel, Field

from iris.models._timeslot import Timeslot


class Trip(BaseModel):
    id: int = Field(alias="Id")
    trip_id: int = Field(alias="TripId")
    date_from: date = Field(alias="From")
    date_to: date = Field(alias="To")
    description: str = Field(alias="Description")
    supervisor: str = Field(alias="Supervisor")
    goal: str = Field(alias="Goal")
    route: str = Field(alias="Route")
    transport: str = Field(alias="Transport")
    start_timeslot: Timeslot | None = Field(alias="StartTimeslot")
    end_timeslot: Timeslot | None = Field(alias="EndTimeslot")
