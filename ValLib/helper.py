from typing import Any, Dict
from secrets import token_urlsafe

import httpx
from httpx import Client, AsyncClient

from .parsing import encode_json, magic_decode
from .structs import Auth, Token
from .constant import Constant
from .exceptions import AuthException, ValorantAPIError

import time


def get_region(auth: Auth) -> str:
    data = {
        "id_token": auth.id_token
    }
    apiURL = "https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant"

    data = httpx.put(apiURL, headers=make_headers(auth), json=data)
    jsonData = data.json()
    region = jsonData["affinities"]["live"]
    return region


async def async_get_region(auth: Auth):
    data = {
        "id_token": auth.id_token
    }
    apiURL = "https://riot-geo.pas.si.riotgames.com/pas/v1/product/valorant"

    async with AsyncClient() as client:
        data = await client.put(apiURL, headers=make_headers(auth), data=data)
        jsonData = data.json()
        region = jsonData["affinities"]["live"]
        return region

def get_shard(region: str) -> str:
    if region in ["latam", "br", "pbe"]:
        return "na"
    return region


async def async_setup_session() -> AsyncClient:
    session = AsyncClient()
    session.headers.update({
        "User-Agent": get_user_agent(),
        "Cache-Control": "no-cache",
        "Accept": "application/json",
        "Content-Type": "application/json"
    })
    session.cookies.update({
        "tdid": "", "asid": "", "did": "", "clid": ""
    })

    return session


async def async_setup_auth(session: AsyncClient):
    data = {
        "client_id": "riot-client",
        "nonce": token_urlsafe(16),
        "redirect_uri": "http://localhost/redirect",
        "response_type": "token id_token",
        "scope": "account openid",
    }
    url = "https://auth.riotgames.com/api/v1/authorization"
    r = await session.post(url, json=data)
    return r


def make_headers(auth: Auth) -> Dict[str, str]:
    return {
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": get_user_agent(),
        "Authorization": f"Bearer {auth.access_token}",
        "X-Riot-Entitlements-JWT": auth.entitlements_token,
        "X-Riot-ClientPlatform": encode_json(Constant.platform),
        "X-Riot-ClientVersion": Constant.valorantVersion
    }


def post(session: Client, token: Token, url: str) -> Any:
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {token.access_token}",
    }
    r = session.post(url, headers=headers, json={})
    return magic_decode(r.text)


def get_user_agent(app="rso-auth") -> str:
    version = "Version.riot"
    os = "(Windows;10;;Professional, x64)"
    userAgent = f"RiotClient/{version} {app} {os}"
    return userAgent


async def async_get_entitlement(session: AsyncClient, token: Token):
    url = "https://entitlements.auth.riotgames.com/api/token/v1"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {token.access_token}",
        "User-Agent": get_user_agent("entitlements"),
    }
    r = await session.post(url, headers=headers, json={})
    data = magic_decode(r.text)
    return data["entitlements_token"]


def get_user_info(session: Client, token: Token) -> str:
    data = post(session, token, "https://auth.riotgames.com/userinfo")
    return data["sub"]


async def async_get_user_info(session: AsyncClient, token: Token):
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": f"Bearer {token.access_token}",
    }
    r = await session.post("https://auth.riotgames.com/userinfo", headers=headers, json={})
    data = magic_decode(r.text)
    return data["sub"]


async def async_get_auth_data(session: AsyncClient):
    r = await async_setup_auth(session)
    cookies = dict(r.cookies)
    data = r.json()
    if "error" in data:
        raise AuthException(data["error"])
    if "response" not in data:
        msg = "Missing params from auth response, ussually invalid cookies"
        raise AuthException(msg)

    uri = data["response"]["parameters"]["uri"]
    token = get_token(uri)
    return token, cookies


def get_token(uri: str) -> Token:
    access_token = uri.split("access_token=")[1].split("&scope")[0]
    token_id = uri.split("id_token=")[1].split("&")[0]
    expires_in = uri.split("expires_in=")[1].split("&")[0]
    timestamp = time.time() + float(expires_in)
    token = Token(access_token, token_id, timestamp)
    return token

