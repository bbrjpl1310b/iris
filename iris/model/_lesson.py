from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.model._clazz import Clazz
from iris.model._distribution import Distribution
from iris.model._employee import Employee
from iris.model._subject import Subject
from iris.model._timeslot import Timeslot


class PresenceType(BaseModel):
    id: int = Field(alias="Id")
    symbol: str = Field(alias="Symbol")
    name: str = Field(alias="Name")
    category_id: int = Field(alias="CategoryId")
    category_name: str = Field(alias="CategoryName")
    position: int = Field(alias="Position")
    presence: bool = Field(alias="Presence")
    absence: bool = Field(alias="Absence")
    legal_absence: bool = Field(alias="LegalAbsence")
    late: bool = Field(alias="Late")
    absence_justified: bool = Field(alias="AbsenceJustified")
    removed: bool = Field(alias="Removed")


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
    distirbution: Distribution | None = Field(alias="Distribution")
    didactics: any = Field(alias="Didactics")

    class Config:
        arbitrary_types_allowed = True
