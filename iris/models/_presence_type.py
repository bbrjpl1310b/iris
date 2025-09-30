from pydantic import BaseModel, Field


class PresenceType(BaseModel):
    id: int = Field(alias="Id")
    symbol: str = Field(alias="Symbol")
    name: str = Field(alias="Name")
    category_id: int = Field(alias="CategoryId")
    category_name: str = Field(alias="CategoryName")
    position: int = Field(alias="Position")
    presence: bool = Field(alias="Presence")
    absence: bool = Field(alias="Absence")
    legal_absence: bool = Field(alias="LegalAbsence")
    late: bool = Field(alias="Late")
    absence_justified: bool = Field(alias="AbsenceJustified")
    removed: bool = Field(alias="Removed")
