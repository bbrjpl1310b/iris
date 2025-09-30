from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.models._clazz import Clazz
from iris.models._distribution import Distribution
from iris.models._employee import Employee
from iris.models._presence_type import PresenceType
from iris.models._subject import Subject
from iris.models._timeslot import Timeslot


class Lesson(BaseModel):
    lesson_id: int = Field(alias="LessonId")
    presence_type: PresenceType | None = Field(alias="PresenceType")
    collection: list[any] = Field(alias="Collection")
    justification_status: int | None = Field(alias="JustificationStatus")
    id: int = Field(alias="Id")
    lesson_class_id: int = Field(alias="LessonClassId")
    day: date = Field(alias="DayAt")
    calculate_presence: bool = Field(alias="CalculatePresence")
    group_definition: str | None = Field(alias="GroupDefinition")
    public_resources: str | None = Field(alias="PublicResources")
    remote_resources: str | None = Field(alias="RemoteResources")
    replacement: bool = Field(alias="Replacement")
    modified_at: datetime = Field(alias="ModifiedAt")
    global_key: str = Field(alias="GlobalKey")
    note: str | None = Field(alias="Note")
    topic: str | None = Field(alias="Topic")
    lesson_number: int | None = Field(alias="LessonNumber")
    lesson_class_global_key: str = Field(alias="LessonClassGlobalKey")
    time_slot: Timeslot = Field(alias="TimeSlot")
    subject: Subject | None = Field(alias="Subject")
    teacher_primary: Employee = Field(alias="TeacherPrimary")
    teacher_secondary: Employee | None = Field(alias="TeacherSecondary")
    teacher_mod: Employee = Field(alias="TeacherMod")
    clazz: Clazz = Field(alias="Clazz")
    distribution: Distribution | None = Field(alias="Distribution")
    didactics: any = Field(alias="Didactics")

    class Config:
        arbitrary_types_allowed = True
