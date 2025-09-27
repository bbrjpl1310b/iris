from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.model._clazz import Clazz
from iris.model._distribution import Distribution
from iris.model._employee import Employee
from iris.model._room import Room
from iris.model._subject import Subject
from iris.model._timeslot import Timeslot


class ScheduleChange(BaseModel):
    id: int = Field(alias="Id")
    type: int = Field(alias="Type")
    is_merge: bool = Field(alias="IsMerge")
    separation: bool = Field(alias="Separation")


class ScheduleSubstitution(BaseModel):
    id: int = Field(alias="Id")
    unit_id: int = Field(alias="UnitId")
    schedule_id: int = Field(alias="ScheduleId")
    date_: date = Field(alias="DateAt")
    change_date: date | None = Field(alias="ChangeDateAt")
    pupil_note: str | None = Field(alias="PupilNote")
    reason: str | None = Field(alias="Reason")
    event: str | None = Field(alias="Event")
    room: Room | None = Field(alias="Room")
    time_slot: Timeslot | None = Field(alias="TimeSlot")
    subject: Subject | None = Field(alias="Subject")
    teacher_primary: Employee | None = Field(alias="TeacherPrimary")
    teacher_absence_reason_id: int | None = Field(alias="TeacherAbsenceReasonId")
    teacher_absence_effect_name: str | None = Field(alias="TeacherAbsenceEffectName")
    teacher_secondary: Employee | None = Field(alias="TeacherSecondary")
    teacher_secondary_absence_reason_id: int | None = Field(
        alias="TeacherSecondaryAbsenceReasonId"
    )
    teacher_secondary_absence_effect_name: str | None = Field(
        alias="TeacherSecondaryAbsenceEffectName"
    )
    teacher_secondary2: Employee | None = Field(alias="TeacherSecondary2")
    teacher_secondary_absence_reason_id: int | None = Field(
        alias="TeacherSecondary2AbsenceReasonId"
    )
    teacher_secondary_absence_effect_name: str | None = Field(
        alias="TeacherSecondary2AbsenceEffectName"
    )
    change: ScheduleChange | None = Field(alias="Change")
    clazz: Clazz | None = Field(alias="Clazz")
    distribution: Distribution | None = Field(alias="Distribution")
    class_absence: bool = Field(alias="ClassAbsence")
    no_room: bool = Field(alias="NoRoom")
    modified_at: datetime = Field(alias="ModifiedAt")
    description: str | None = Field(alias="Description")


class Schedule(BaseModel):
    id: int = Field(alias="Id")
    merge_change_id: int | None = Field(alias="MergeChangeId")
    event: str | None = Field(alias="Event")
    date_: date = Field(alias="DateAt")
    room: Room | None = Field(alias="Room")
    time_slot: Timeslot = Field(alias="TimeSlot")
    subject: Subject | None = Field(alias="Subject")
    teacher_primary: Employee | None = Field(alias="TeacherPrimary")
    teacher_secondary: Employee | None = Field(alias="TeacherSecondary")
    teacher_secondary2: Employee | None = Field(alias="TeacherSecondary2")
    clazz: Clazz = Field(alias="Clazz")
    distribution: Distribution | None = Field(alias="Distribution")
    pupil_alias: str | None = Field(alias="PupilAlias")
    substitution: ScheduleSubstitution | None = Field(alias="Substitution")
    parent: str | None = Field(alias="Parent")
