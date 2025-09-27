from datetime import datetime, date

from pydantic import BaseModel, Field

from iris.model._attachment import Attachment
from iris.model._employee import Employee
from iris.model._subject import Subject


class Homework(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    id_pupil: int = Field(alias="IdPupil")
    id_homework: int = Field(alias="IdHomework")
    content: str = Field(alias="Content")
    is_answer_required: bool = Field(alias="IsAnswerRequired")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    date_: date = Field(alias="DateAt")
    answer_at: datetime | None = Field(alias="AnswerAt")
    deadline: date = Field(alias="DeadlineAt")
    creator: Employee = Field(alias="Creator")
    subject: Subject = Field(alias="Subject")
    attachments: list[Attachment] = Field(alias="Attachments")
    didactics: any = Field(alias="Didactics")

    class Config:
        arbitrary_types_allowed = True
