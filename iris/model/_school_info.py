from datetime import date, datetime

from pydantic import BaseModel, Field


class SchoolInfo(BaseModel):
    id: int = Field(alias="Id")
    unit_id: int = Field(alias="UnitId")
    date_: date = Field(alias="DateAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    availability: int = Field(alias="Availability")
    topic: str = Field(alias="Topic")
    content: str = Field(alias="Content")
