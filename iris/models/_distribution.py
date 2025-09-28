from pydantic import BaseModel, Field


class Distribution(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    shortcut: str = Field(alias="Shortcut")
    name: str = Field(alias="Name")
    part_type: str = Field(alias="PartType")
