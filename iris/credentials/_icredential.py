from typing import Literal

from pydantic import BaseModel


class ICredential(BaseModel):
    type: str
    rest_url: str | None
    certificate: str
    private_key: str | None
    fingerprint: str
    notification_token: str | None
    device_id: str
    device_os: Literal["Android", "iOS"]
    device_model: str

    @staticmethod
    def create_new(
            device_os: Literal["Android", "iOS"],
            device_model: str,
            rest_url: str | None,
            notification_token: str | None = None,
    ) -> "ICredential":
        pass

    def sign(self, headers: dict[str, str], body: str | None) -> dict[str, str]:
        pass
