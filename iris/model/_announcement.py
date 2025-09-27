from datetime import date, datetime

from pydantic import BaseModel, Field

from iris.model._attachment import Attachment
from iris.model._employee import Employee


class Announcement(BaseModel):
    id: int = Field(alias="Id")
    unit_id: int = Field(alias="IdUnit")
    title: str = Field(alias="Title")
    content: str = Field(alias="Content")
    category: str | None = Field(alias="Category")
    date_from: date = Field(alias="From")
    date_to: date = Field(alias="To")
    sender: Employee = Field(alias="Sender")
    attachments: list[Attachment] = Field(alias="Attachments")
    created_at: datetime = Field(alias="CreatedAt")
    modified_at: datetime = Field(alias="ModifiedAt")
