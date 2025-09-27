from pydantic import BaseModel, Field


class Clazz(BaseModel):
    id: int = Field(alias="Id")
    key: str = Field(alias="Key")
    display_name: str = Field(alias="DisplayName")
    symbol: str = Field(alias="Symbol")
