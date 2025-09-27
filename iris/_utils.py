import hashlib
import re
from urllib.parse import quote

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from iris._exceptions import WrongTokenException


def pem_getraw(pem: bytes) -> str:
    return pem.decode("utf-8").replace("\n", "").split("-----")[2]


def generate_fingerprint(text: str):
    return hashlib.md5(text.encode()).digest().hex()


def generate_rsa_key_pair() -> tuple[str, str, str]:
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return (
        pem_getraw(public_pem),
        pem_getraw(private_pem),
        generate_fingerprint(public_pem.decode()),
    )


def get_encoded_path(path: str) -> str:
    match = re.search("(api/mobile/.*)", path)
    return quote(match[0] if match else path, safe="").lower()


TOKEN_PREFIXES = {
    "3S1": "https://lekcjaplus.vulcan.net.pl",
    "TA1": "https://uonetplus-komunikacja.umt.tarnow.pl",
    "OP1": "https://uonetplus-komunikacja.eszkola.opolskie.pl",
    "RZ1": "https://uonetplus-komunikacja.resman.pl",
    "GD1": "https://uonetplus-komunikacja.edu.gdansk.pl",
    "KA1": "https://uonetplus-komunikacja.mcuw.katowice.eu",
    "KA2": "https://uonetplus-komunikacja-test.mcuw.katowice.eu",
    "LU1": "https://uonetplus-komunikacja.edu.lublin.eu",
    "LU2": "https://test-uonetplus-komunikacja.edu.lublin.eu",
    "P03": "https://efeb-komunikacja-pro-efebmobile.pro.vulcan.pl",
    "P01": "http://efeb-komunikacja.pro-hudson.win.vulcan.pl",
    "P02": "http://efeb-komunikacja.pro-hudsonrc.win.vulcan.pl",
    "P90": "http://efeb-komunikacja-pro-mwujakowska.neo.win.vulcan.pl",
    "KO1": "https://uonetplus-komunikacja.eduportal.koszalin.pl",
}


def get_base_url_by_token(token: str):
    base_url = TOKEN_PREFIXES.get(token)
    if not base_url:
        raise WrongTokenException()
    return base_url
