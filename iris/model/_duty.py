from datetime import date, datetime

from pydantic import BaseModel, Field


class Duty(BaseModel):
    id: int = Field(alias="Id")
    unit_id: int = Field(alias="UnitId")
    journal_id: int = Field(alias="JournalId")
    pupil_id: int = Field(alias="PupilId")
    date_: date = Field(alias="DateAt")
    modified_at: datetime = Field(alias="ModifiedAt")
