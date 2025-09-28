from pydantic import BaseModel, Field


class Teacher(BaseModel):
    description: str = Field(alias="Description")
    position: int = Field(alias="Position")
    box_id: str = Field(alias="BoxId")
    id: int = Field(alias="Id")
    surname: str | None = Field(alias="Surname")
    name: str | None = Field(alias="Name")
    display_name: str = Field(alias="DisplayName")
