from uuid import UUID

import httpx

from ..structs import Auth
from ..helper import get_region, get_shard, make_headers


class Party:
    def __init__(self, auth: Auth, region=None, shard=None):
        self.auth = auth
        self.region = get_region(self.auth) if region is None else region
        self.shard = get_shard(self.region) if shard is None else shard

    def Get_Party(self, partyId: UUID):
        url = f"https://glz-{self.region}-1.{self.shard}.a.pvp.net/parties/v1/parties/{partyId}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return resp.json()

    def Party_Player(self, player_UUID: UUID = None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id
        url = f"https://glz-{self.region}-1.{self.shard}.a.pvp.net/parties/v1/players/{puuid}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return resp.json()

    async def async_Party_Player(self, player_UUID: UUID = None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id
        url = f"https://glz-{self.region}-1.{self.shard}.a.pvp.net/parties/v1/players/{puuid}"

        headers = make_headers(self.auth)

        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers)
            return resp.json()

    def Pre_Game_Player(self, player_UUID: UUID = None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id

        url = f"https://glz-{self.region}-1.{self.shard}.a.pvp.net/pregame/v1/players/{puuid}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return resp.json()

    async def async_Pre_Game_Player(self, player_UUID: UUID = None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id

        url = f"https://glz-{self.region}-1.{self.shard}.a.pvp.net/pregame/v1/players/{puuid}"

        headers = make_headers(self.auth)

        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers)
            return resp.json()

