from iris._http_client import HttpClient
from iris._utils import get_base_url_by_token
from iris.api._base import IrisApi
from iris.credentials import ICredential

APP_NAME = "DzienniczekPlus 2.0"
APP_VERSION = "25.08.11 (G)"
APP_VERSION_CODE = "756"


class IrisHebeApi(IrisApi):
    def __init__(self, credential: ICredential):
        self._credential = credential
        self._http = HttpClient(
            credential=credential,
            app_name=APP_NAME,
            app_version=APP_VERSION,
            app_version_code=APP_VERSION_CODE,
        )

    async def register_by_token(self, security_token: str, pin: str, tenant: str):
        base_url = get_base_url_by_token(security_token.upper())
        await self._http.request(
            method="POST",
            endpoint="mobile/register/token",
            rest_url=f"{base_url}/{tenant}/api",
            payload={
                "OS": self._credential.device_os,
                "Certificate": self._credential.certificate,
                "CertificateType": self._credential.type,
                "DeviceModel": self._credential.device_model,
                "SelfIdentifier": self._credential.device_id,
                "CertificateThumbprint": self._credential.fingerprint,
                "SecurityToken": security_token.upper(),
                "PIN": pin,
            },
        )
        self._credential.rest_url = f"{base_url}/{tenant}/api"
        return self._credential.rest_url
