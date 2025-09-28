from datetime import datetime

from pydantic import BaseModel, Field

from iris.models._attachment import Attachment


class MessageAddressExtras(BaseModel):
    displayed_class: str = Field(alias="DisplayedClass")


class MessageAddress(BaseModel):
    global_key: str = Field(alias="GlobalKey")
    name: str = Field(alias="Name")
    has_read: bool | None = Field(alias="HasRead")
    extras: MessageAddressExtras | None = Field(alias="Extras")


class Message(BaseModel):
    id: str = Field(alias="Id")
    global_key: str = Field(alias="GlobalKey")
    thread_key: str = Field(alias="ThreadKey")
    subject: str = Field(alias="Subject")
    content: str = Field(alias="Content")
    sent_at: datetime = Field(alias="SentAt")
    read_at: datetime | None = Field(alias="ReadAt")
    status: int = Field(alias="Status")
    sender: MessageAddress = Field(alias="Sender")
    receiver: list[MessageAddress] = Field(alias="Receiver")
    attachments: list[Attachment] = Field(alias="Attachments")
    # importance: int | None = Field(alis="Importance")
    widthdrawn: bool = Field(alias="Withdrawn")
