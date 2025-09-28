from datetime import date

from pydantic import BaseModel, Field


class LuckyNumber(BaseModel):
    day: date = Field(alias="Day")
    number: int = Field(alias="Number")
