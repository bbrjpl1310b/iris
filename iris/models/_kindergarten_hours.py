from datetime import time

from pydantic import BaseModel, Field


class KindergartenHours(BaseModel):
    constituent_unit_id: int = Field(alias="Id")
    hour_from: time = Field(alias="HourFrom")
    hour_to: time = Field(alias="HourTo")
