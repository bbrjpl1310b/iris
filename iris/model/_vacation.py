from datetime import date

from pydantic import BaseModel, Field


class Vacation(BaseModel):
    id: int = Field(alias="Id")
    name: str = Field(alias="Name")
    date_from: date = Field(alias="From")
    date_to: date = Field(alias="To")
