from pydantic import BaseModel, Field


class PresenceExtraInfo(BaseModel):
    id: int = Field(alias="Id")
    label: str = Field(alias="Label")
    values: any = Field(alias="Values")

    class Config:
        arbitrary_types_allowed = True
