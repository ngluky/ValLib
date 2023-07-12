import ssl
import requests
from typing import Any, Dict, Tuple
from requests import Session
from requests.adapters import HTTPAdapter

from .exceptions import AuthException
from .structs import Auth, User
from .parsing import encode_json, magic_decode
from .version import Version

platform = {
    "platformType": "PC",
    "platformOS": "Windows",
    "platformOSVersion": "10.0.19045.1.256.64bit",
    "platformChipset": "Unknown"
}

FORCED_CIPHERS = [
    "ECDHE-ECDSA-AES128-GCM-SHA256",
    "ECDHE-ECDSA-CHACHA20-POLY1305",
    "ECDHE-RSA-AES128-GCM-SHA256",
    "ECDHE-RSA-CHACHA20-POLY1305",
    "ECDHE+AES128",
    "RSA+AES128",
    "ECDHE+AES256",
    "RSA+AES256",
    "ECDHE+3DES",
    "RSA+3DES"
]


def get_user_agent() -> str:
    version = Version().riot
    os = "(Windows;10;;Professional, x64)"
    userAgent = f"RiotClient/{version} rso-auth {os}"
    return userAgent


def get_token(uri: str) -> Tuple[str, str]:
    access_token = uri.split("access_token=")[1].split("&scope")[0]
    token_id = uri.split("id_token=")[1].split("&")[0]
    return access_token, token_id


def post(session: Session, access_token: str, url: str) -> Any:
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {access_token}",
    }
    r = session.post(url, headers=headers, json={})
    return magic_decode(r.text)


def setup_session() -> Session:
    class SSLAdapter(HTTPAdapter):
        def init_poolmanager(self, *args: Any, **kwargs: Any) -> None:
            ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ctx.set_ciphers(":".join(FORCED_CIPHERS))
            kwargs["ssl_context"] = ctx
            return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

    session = requests.session()
    session.headers.update({
        "User-Agent": get_user_agent(),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "application/json, text/plain, */*"
    })
    session.mount("https://", SSLAdapter())
    return session


def authenticate(user: User, remember=False) -> Auth:
    session = setup_session()

    setup_auth(session)

    access_token, id_token, cookies = get_auth_token(session, user, remember)

    entitlements_token = get_entitlement(session, access_token)

    user_id = get_user_info(session, access_token)

    session.close()

    auth = Auth(access_token, id_token, entitlements_token, user_id, cookies)

    return auth


def setup_auth(session: Session):
    data = {
        "client_id": "riot-client",
        "nonce": "1",
        "redirect_uri": "http://localhost/redirect",
        "response_type": "token id_token",
        "scope": "account openid",
    }

    session.post(f"https://auth.riotgames.com/api/v1/authorization", json=data)


def get_auth_token(session: Session, user: User, remember=False) -> Tuple[str, str, Dict[str, str]]:
    data = {
        "type": "auth",
        "username": user.username,
        "password": user.password
    }

    if remember:
        data["remember"] = "true"

    r = session.put(
        f"https://auth.riotgames.com/api/v1/authorization", json=data)
    cookies = r.cookies.get_dict()
    data = r.json()
    if "error" in data:
        raise AuthException(data["error"])
    uri = data["response"]["parameters"]["uri"]
    access_token, id_token = get_token(uri)

    return access_token, id_token, cookies


def get_entitlement(session: Session, access_token: str) -> str:
    data = post(session, access_token,
                "https://entitlements.auth.riotgames.com/api/token/v1")
    return data["entitlements_token"]


def get_user_info(session: Session, access_token: str) -> str:
    data = post(session, access_token, "https://auth.riotgames.com/userinfo")
    return data["sub"]


def make_headers(auth: Auth) -> Dict[str, str]:
    return {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": get_user_agent(),
        "Authorization": f"Bearer {auth.access_token}",
        "X-Riot-Entitlements-JWT": auth.entitlements_token,
        "X-Riot-ClientPlatform": encode_json(platform),
        "X-Riot-ClientVersion": Version().valorant
    }
