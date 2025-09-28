from datetime import datetime

from pydantic import BaseModel, Field


class Meeting(BaseModel):
    id: int = Field(alias="Id")
    when: datetime = Field(alias="DateAt")
    where: str = Field(alias="Where")
    why: str = Field(alias="Why")
    agenda: str = Field(alias="Agenda")
    additional_info: str | None = Field(alias="AdditionalInfo")
    online: str = Field(alias="Online")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
