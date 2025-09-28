from datetime import date, time

from pydantic import BaseModel, Field

from iris.models._addressbook import Address


class AccountLinks(BaseModel):
    root: str = Field(alias="Root")
    group: str = Field(alias="Group")
    symbol: str = Field(alias="Symbol")
    alias: str | None = Field(alias="Alias")
    questionnaire_root: str = Field(alias="QuestionnaireRoot")
    ex_resources_url: str = Field(alias="ExResourcesUrl")


class Unit(BaseModel):
    id: int = Field(alias="Id")
    symbol: str = Field(alias="Symbol")
    short: str = Field(alias="Short")
    rest_url: str = Field(alias="RestURL")
    name: str = Field(alias="Name")
    address: str | None = Field(alias="Address")
    patron: str | None = Field(alias="Patron")
    display_name: str = Field(alias="DisplayName")
    school_topic: str = Field(alias="SchoolTopic")


class ConstituentUnit(BaseModel):
    id: int = Field(alias="Id")
    short: str = Field(alias="Short")
    name: str = Field(alias="Name")
    address: str | None = Field(alias="Address")
    patron: str | None = Field(alias="Patron")
    school_topic: str = Field(alias="SchoolTopic")


class Pupil(BaseModel):
    id: int = Field(alias="Id")
    login_id: int = Field(alias="LoginId")
    first_name: str = Field(alias="FirstName")
    second_name: str = Field(alias="SecondName")
    surname: str = Field(alias="Surname")
    sex: bool = Field(alias="Sex")


class Period(BaseModel):
    capabilites: list[str] = Field(alias="Capabilities")
    id: int = Field(alias="Id")
    level: int = Field(alias="Level")
    number: int = Field(alias="Number")
    start: date = Field(alias="StartAt")
    end: date = Field(alias="EndAt")
    current: bool = Field(alias="Current")
    last: bool = Field(alias="Last")


class Journal(BaseModel):
    id: int = Field(alias="Id")
    start: date = Field(alias="StartAt")
    end: date = Field(alias="EndAt")
    pupil_number: int = Field(alias="PupilNumber")


class Constraints(BaseModel):
    absence_days_before: int = Field(alias="AbsenceDaysBefore")
    absence_hours_before: time = Field(alias="AbsenceHoursBefore")
    presence_blocade: any = Field(alias="PresenceBlocade")

    class Config:
        arbitrary_types_allowed = True


class MessageBox(BaseModel):
    id: int = Field(alias="Id")
    global_key: str = Field(alias="GlobalKey")
    name: str = Field(alias="Name")


class Account(BaseModel):
    top_level_partition: str = Field(alias="TopLevelPartition")
    partition: str = Field(alias="Partition")
    links: AccountLinks = Field(alias="Links")
    class_display: str | None = Field(alias="ClassDisplay")
    info_display: str | None = Field(alias="InfoDisplay")
    login: any = Field(alias="Login")
    unit: Unit = Field(alias="Unit")
    constituent_unit: ConstituentUnit = Field(alias="ConstituentUnit")
    capabilities: list[str] = Field(alias="Capabilities")
    educators_list: list[Address] = Field(alias="EducatorsList")
    pupil: Pupil = Field(alias="Pupil")
    caretaker_id: int | None = Field(alias="CaretakerId")
    periods: list[Period] = Field(alias="Periods")
    journal: Journal | None = Field(alias="Journal")
    constraints: Constraints = Field(alias="Constraints")
    state: int = Field(alias="State")
    message_box: MessageBox | None = Field(alias="MessageBox")
    profile_id: str | None = Field(alias="ProfileId")

    class Config:
        arbitrary_types_allowed = True
