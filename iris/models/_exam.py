from datetime import datetime

from pydantic import BaseModel, Field

from iris.models._employee import Employee
from iris.models._subject import Subject


class Exam(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    type: str = Field(alias="Type")
    type_id: int = Field(alias="TypeId")
    content: str = Field(alias="Content")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
    deadline: datetime = Field(alias="DeadlineAt")
    creator: Employee = Field(alias="Creator")
    subject: Subject = Field(alias="Subject")
    pupil_id: int = Field(alias="PupilId")
    didactics: any = Field(alias="Didactics")

    class Config:
        arbitrary_types_allowed = True
