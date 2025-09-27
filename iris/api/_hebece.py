from iris._http_client import HttpClient
from iris.api._base import IrisApi
from iris.credentials import ICredential

APP_NAME = "DzienniczekPlus 3.0"
APP_VERSION = "25.09.24 (G)"
APP_VERSION_CODE = "802"
API_BASE_URL = "https://lekcjaplus.vulcan.net.pl"


class IrisHebeCeApi(IrisApi):
    def __init__(self, credential: ICredential):
        self._credential = credential
        self._http = HttpClient(
            credential=credential,
            app_name=APP_NAME,
            app_version=APP_VERSION,
            app_version_code=APP_VERSION_CODE,
        )

    async def register_by_jwt(self, tokens: list[str], tenant: str):
        await self._http.request(
            method="POST",
            endpoint="mobile/register/jwt",
            rest_url=f"{API_BASE_URL}/{tenant}/api",
            payload={
                "OS": self._credential.device_os,
                "Certificate": self._credential.certificate,
                "CertificateType": self._credential.type,
                "DeviceModel": self._credential.device_model,
                "SelfIdentifier": self._credential.device_id,
                "CertificateThumbprint": self._credential.fingerprint,
                "Tokens": tokens,
            },
        )
        self._credential.rest_url = f"{API_BASE_URL}/{tenant}/api"
        return self._credential.rest_url
