from pydantic import BaseModel, Field


class MealMenuEntry(BaseModel):
    name: str = Field(alias="Name")
    metadata: any = Field(alias="Metadata")

    class Config:
        arbitrary_types_allowed = True


class MealMenu(BaseModel):
    inner_id: int = Field(alias="InnerId")
    id: int = Field(alias="Id")
    diet_name: str = Field(alias="DietName")
    meal_name: str = Field(alias="MealName")
    dishes: str = Field(alias="Dishes")
    metadata: any = Field(alias="Metadata")
    entries: list[MealMenuEntry] = Field(alias="Entires")

    class Config:
        arbitrary_types_allowed = True
