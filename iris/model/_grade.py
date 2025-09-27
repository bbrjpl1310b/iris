from datetime import datetime

from pydantic import BaseModel, Field

from iris.model._employee import Employee
from iris.model._subject import Subject


class GradeCategory(BaseModel):
    id: int = Field(alias="Id")
    name: str = Field(alias="Name")
    code: str = Field(alias="Code")


class GradeColumn(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    period_id: int = Field(alias="PeriodId")
    name: str = Field(alias="Name")
    code: str = Field(alias="Code")
    group: str = Field(alias="Group")
    number: int = Field(alias="Number")
    color: int = Field(alias="Color")
    weight: float = Field(alias="Weight")
    subject: Subject = Field(alias="Subject")
    category: GradeCategory | None = Field(alias="Category")


class Grade(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    pupil_id: int = Field(alias="PupilId")
    content_raw: str = Field(alias="ContentRaw")
    content: str = Field(alias="Content")
    comment: str = Field(alias="Comment")
    value: float | None = Field(alias="Value")
    numerator: int | None = Field(alias="Numerator")
    denominator: int | None = Field(alias="Denominator")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    creator: Employee = Field(alias="Creator")
    modifier: Employee = Field(alias="Modifier")
    column: GradeColumn = Field(alias="Column")
    corrected_grade: str | None = Field(alias="CorrectedGrade")
