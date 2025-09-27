from datetime import time

from pydantic import BaseModel, Field


class Timeslot(BaseModel):
    id: int = Field(alias="Id")
    start: time = Field(alias="Start")
    end: time = Field(alias="End")
    display: str = Field(alias="Display")
    position: int = Field(alias="Position")
