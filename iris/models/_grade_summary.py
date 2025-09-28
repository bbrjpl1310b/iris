from datetime import datetime

from pydantic import BaseModel, Field

from iris.models._subject import Subject


class GradeSummary(BaseModel):
    id: int = Field(alias="Id")
    pupil_id: int = Field(alias="PupilId")
    period_id: int = Field(alias="PeriodId")
    subject: Subject = Field(alias="Subject")
    entry_1: str | None = Field(alias="Entry_1")
    entry_2: str | None = Field(alias="Entry_2")
    entry_3: str | None = Field(alias="Entry_3")
    modified_at: datetime | None = Field(alias="ModifiedAt")
