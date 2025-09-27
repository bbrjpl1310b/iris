import json
from datetime import datetime, date
from urllib.parse import urlencode, quote
from uuid import uuid4

from aiohttp import ClientSession

from iris._exceptions import (
    CertificateNotFoundException,
    ConstraintViolationException,
    EntityNotFoundException,
    ExpiredTokenException,
    FailedRequestException,
    HttpUnsuccessfullStatusException,
    InternalServerErrorException,
    InvalidBodyModelException,
    InvalidHeaderException,
    InvalidParameterValueException,
    InvalidSignatureException,
    MissingHeaderException,
    MissingUnitSymbolException,
    ResponseInvalidContentTypeException,
    UsedTokenException,
    IrisApiException,
    WrongPINException,
    WrongTokenException,
)
from iris._utils import get_encoded_path
from iris.credentials import ICredential
from iris.model import EnvelopeResponse

USER_AGENT = "Dart/3.8 (dart:io)"
API_VERSION = 1


class HttpClient:
    def __init__(
            self,
            credential: ICredential,
            app_name: str,
            app_version: str,
            app_version_code: str,
    ):
        self._credential = credential
        self._app_name = app_name
        self._app_version = app_version
        self._app_version_code = app_version_code
        self._client = ClientSession(skip_auto_headers={"Accept", "Content-Length"})

    def _serialize_query(self, query: dict[str, any]):
        datetime_format = "%Y-%m-%d %H:%M:%S"
        date_format = "%Y-%m-%d"

        stringify = {}
        for key, value in query.items():
            if isinstance(value, str):
                stringify[key] = value
            elif isinstance(value, datetime):
                stringify[key] = value.strftime(datetime_format)
            elif isinstance(value, date):
                stringify[key] = value.strftime(date_format)
            else:
                stringify[key] = str(value)
        return urlencode(
            stringify,
            quote_via=lambda s, safe, encoding=None, errors=None: quote(
                s, safe="", encoding=encoding, errors=errors
            ),
        )

    def _build_body(self, envelope: any):
        now = datetime.now()
        return json.dumps(
            {
                "AppName": self._app_name,
                "AppVersion": self._app_version,
                "NotificationToken": self._credential.notification_token or "",
                "API": API_VERSION,
                "RequestId": str(uuid4()),
                "Timestamp": int(now.timestamp()),
                "TimestampFormatted": now.strftime("%Y-%m-%d %H:%M:%S"),
                "Envelope": envelope,
            }
        )

    def _build_headers(self, url: str, body: str | None, pupil_id: int | None):
        headers = {
            "Accept-Encoding": "gzip",
            "vOS": self._credential.device_os,
            "vVersionCode": self._app_version_code,
            "vAPI": str(API_VERSION),
            "vCanonicalUrl": get_encoded_path(url),
            "vDate": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
            "User-Agent": USER_AGENT,
        }

        if pupil_id:
            headers["vHint"] = str(pupil_id)
        headers["Content-Type"] = (
            "application/json; charset=utf-8" if body else "application/json"
        )
        if body:
            headers["Content-Length"] = str(len(body))
        headers = self._credential.sign(headers, body)

        headers = {k.lower(): v for k, v in headers.items()}
        return headers

    async def request(
            self,
            method: str,
            endpoint: str,
            rest_url: str,
            pupil_id: int | None = None,
            query: dict[str, any] | None = None,
            payload: any = None,
            verify_response: bool = True
    ):
        url = f"{rest_url}/{endpoint}"
        if query:
            url += f"?{self._serialize_query(query)}"

        body = self._build_body(payload) if payload else None
        headers = self._build_headers(url, body, pupil_id)

        try:
            response = await self._client.request(
                method=method, url=url, data=body, headers=headers
            )
        except Exception as exception:
            raise FailedRequestException(exception)

        if response.status != 200:
            raise HttpUnsuccessfullStatusException(
                f"{response.status}: {await response.text()}"
            )

        if "!DOCTYPE" in await response.text():
            raise ResponseInvalidContentTypeException()

        if verify_response:
            response_envelope = EnvelopeResponse.model_validate(await response.json())
            self._check_envelope_status(
                response_envelope.status.code, response_envelope.status.message
            )
            return response_envelope.envelope

    def _check_envelope_status(self, code: int, message: str) -> None:
        match code:
            case 0:
                return
            case -1:
                raise InternalServerErrorException(message)
            case 100:
                raise InvalidSignatureException(message)
            case 101:
                raise InvalidBodyModelException(message)
            case 102:
                raise MissingHeaderException(message)
            case 103:
                raise InvalidHeaderException(message)
            case 104:
                raise MissingUnitSymbolException(message)
            case 154:
                raise CertificateNotFoundException(message)
            case 200:
                raise EntityNotFoundException(message)
            case 201:
                raise UsedTokenException(message)
            case 202:
                raise WrongTokenException(message)
            case 203:
                raise WrongPINException(message)
            case 204:
                raise ExpiredTokenException(message)
            case 206:
                raise InvalidParameterValueException(message)
            case 214:
                raise ConstraintViolationException(message)
            case _:
                raise IrisApiException(f"{code}: {message}")

    async def __aexit__(self):
        await self._session.close()
