from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.models._employee import Employee
from iris.models._room import Room
from iris.models._timeslot import Timeslot


class ScheduleExtraSubstitution(BaseModel):
    id: int = Field(alias="Id")
    class_absence: bool = Field(alias="ClassAbsence")
    date_: date | None = Field(alias="DateAt")
    journal_id: int = Field(alias="JournalId")
    lesson_date: date | None = Field(alias="LessonDateAt")
    no_room: bool = Field(alias="NoRoom")
    pupil_note: str | None = Field(alias="PupilNote")
    reason: str | None = Field(alias="Reason")
    room: Room | None = Field(alias="Room")
    schedule_extra_id: int = Field(alias="ScheduleExtraId")
    teacher_absence_effect_name: str | None = Field(alias="TeacherAbsenceEffectName")
    teacher_absence_reason_id: int | None = Field(alias="TeacherAbsenceReasonId")
    teacher: Employee | None = Field(alias="Teacher")
    time_end: str | None = Field(alias="TimeEnd")
    time_start: str | None = Field(alias="TimeStart")
    unit_id: int = Field(alias="UnitId")
    modified_at: datetime = Field(alias="ModifiedAt")


class ScheduleExtra(BaseModel):
    id: int = Field(alias="Id")
    schedule_extra_id: int = Field(alias="ScheduleExtraId")
    unit_id: int = Field(alias="UnitId")
    type: int = Field(alias="Type")
    year: int = Field(alias="Year")
    day: date = Field(alias="DateAt")
    extra_description: str = Field(alias="ExtraDescription")
    schedule_description: str = Field(alias="ScheduleDescription")
    schedule_pupil_description: str = Field(alias="SchedulePupilDescription")
    teacher: Employee = Field(alias="Teacher")
    time_slot: Timeslot = Field(alias="TimeSlot")
    room: Room | None = Field(alias="Room")
    substitution: ScheduleExtraSubstitution | None = Field(alias="Substitution")
