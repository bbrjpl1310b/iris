from pydantic import BaseModel, Field


class PushSetting(BaseModel):
    id: int = Field(alias="Id")
    mobile_certificate_id: int = Field(alias="MobileCertyfikatId")
    option: str = Field(alias="Option")
    active: bool = Field(alias="Active")
