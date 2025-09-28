from datetime import date, datetime, time

from pydantic import BaseModel, Field


class UserEvent(BaseModel):
    id: int = Field(alias="Id")
    pupil_id: int = Field(alias="PupilId")
    name: str = Field(alias="Name")
    description: str | None = Field(alias="Description")
    display_mode: int = Field(alias="DisplayMode")
    date_: date = Field(alias="DateAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    start_time: time = Field(alias="StartTime")
    end_time: time = Field(alias="EndTime")
    repeat_mode: int = Field(alias="RepeatMode")
    end_at: datetime | None = Field(alias="EndAt")
    is_owner: bool = Field(alias="IsOwner")
