from pydantic import BaseModel, Field


class Subject(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    name: str = Field(alias="Name")
    code: str = Field(alias="Kod")
    position: int = Field(alias="Position")
