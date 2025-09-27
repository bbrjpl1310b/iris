from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.model._employee import Employee


class NoteCategory(BaseModel):
    id: int = Field(alias="Id")
    name: str = Field(alias="Name")
    type: str | None = Field(alias="Type")
    default_points: int | None = Field(alias="DefaultPoints")


class Note(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    id_pupil: int = Field(alias="IdPupil")
    positive: bool = Field(alias="Positive")
    date_valid: date = Field(alias="ValidAt")
    date_modify: datetime = Field(alias="ModifiedAt")
    creator: Employee = Field(alias="Creator")
    category: NoteCategory | None = Field(alias="Category")
    content: str = Field(alias="Content")
    points: int | None = Field(alias="Points")
