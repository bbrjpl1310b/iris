import hashlib
from base64 import b64decode, b64encode
from typing import Literal
from uuid import uuid4

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from iris._utils import generate_rsa_key_pair
from iris.credentials._icredential import ICredential


class RsaCredential(ICredential):
    @staticmethod
    def create_new(
            device_os: Literal["Android", "iOS"],
            device_model: str,
            rest_url: str | None = None,
            notification_token: str | None = None,
    ) -> "RsaCredential":
        certificate, private_key, fingerprint = generate_rsa_key_pair()

        return RsaCredential(
            type="RSA_PEM",
            rest_url=rest_url,
            certificate=certificate,
            private_key=private_key,
            fingerprint=fingerprint,
            notification_token=notification_token,
            device_id=str(uuid4()),
            device_os=device_os,
            device_model=device_model,
        )

    def sign(self, headers: dict[str, str], body: str | None) -> dict[str, str]:
        private_key: RSAPrivateKey = serialization.load_der_private_key(
            b64decode(self.private_key), password=None, backend=default_backend()
        )

        if body is not None:
            headers["Digest"] = self._get_digest(body)

        signature_header_names = (
            ["vCanonicalUrl", "Digest", "vDate"]
            if body is not None
            else ["vCanonicalUrl", "vDate"]
        )
        signature_headers = {k: headers[k] for k in signature_header_names}

        headers["Signature"] = self._get_signature_header(
            signature_headers, private_key, self.fingerprint
        )

        if "Digest" in headers:
            headers["Digest"] = f"SHA-256={headers["Digest"]}"

        return headers

    def _get_digest(self, body: str) -> str:
        return b64encode(hashlib.sha256(body.encode()).digest()).decode()

    def _get_signature_header(
            self, headers: dict[str, str], private_key: RSAPrivateKey, fingerprint: str
    ) -> str:
        header_names = " ".join(headers.keys())
        header_values = "".join(headers.values())

        signature = private_key.sign(
            header_values.encode(), padding.PKCS1v15(), hashes.SHA256()
        )
        signature_b64 = b64encode(signature).decode()

        return (
            f'keyId="{fingerprint}",'
            f'headers="{header_names}",'
            f'algorithm="sha256withrsa",'
            f"signature=Base64(SHA256withRSA({signature_b64}))"
        )
