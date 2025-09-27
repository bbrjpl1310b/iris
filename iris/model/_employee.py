from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int = Field(alias="Id")
    surname: str = Field(alias="Surname")
    name: str = Field(alias="Name")
    display_name: str = Field(alias="DisplayName")
