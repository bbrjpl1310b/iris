from pydantic import BaseModel, Field


class Address(BaseModel):
    global_key: str = Field(alias="GlobalKey")
    name: str = Field(alias="Name")
    group: str | None = Field(alias="Group")
