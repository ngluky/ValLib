import asyncio

from ..structs import Auth, User
from ..helper import async_setup_auth, async_setup_session, async_get_auth_data, async_get_user_info, \
    async_get_entitlement

from .captcha import async_captcha_flow


async def authenticate(user: User) -> Auth:
    session = await async_setup_session()

    await async_setup_auth(session)

    await async_captcha_flow(session, user)

    token, cookies = await async_get_auth_data(session)

    entitlements_token = await async_get_entitlement(session, token)

    user_id = await async_get_user_info(session, token)

    await session.aclose()

    auth = Auth(token, entitlements_token, user_id, cookies)

    return auth


async def async_login_cookie(auth: Auth):
    session = await async_setup_session()
    session.cookies.update(
        auth.cookies
    )
    token, cookies = await async_get_auth_data(session)
    entitlements_token = await async_get_entitlement(session, token)
    auth = Auth(token, entitlements_token, auth.user_id, cookies)
    return auth

