from pydantic import BaseModel, Field


class PresenceMonthStats(BaseModel):
    period_id: int = Field(alias="PeriodId")
    month: int = Field(alias="Month")
    presence_percentage: float = Field(alias="PresencePercentage")
    absences: int = Field(alias="Absences")
    absences_justified: int = Field(alias="AbsencesJustified")
    late_arrivals: int = Field(alias="LateArrivals")
    late_arrivals_justified: int = Field(alias="LateArrivalsJustified")
    exemptions: int = Field(alias="Exemptions")
    absences_due_to_school: int = Field(alias="AbsencesDueToSchool")
