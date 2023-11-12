import json
from uuid import UUID

import httpx

from ..structs import Auth
from ..helper import get_region, get_shard, make_headers
from ..parsing import zloads, zdumps


class Setting:
    def __init__(self, auth: Auth, region=None, shard=None):
        self.auth = auth
        self.region = get_region(self.auth) if region is None else region
        self.shard = get_shard(self.region) if shard is None else shard

    def Fetch_Preference(self):
        url = "https://playerpreferences.riotgames.com/playerPref/v3/getPreference/Ares.PlayerSettings"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        jsonData = resp.json()
        if "data" not in jsonData:
            return {}
        data = zloads(jsonData["data"])
        print(json.dumps(data))
        return data

    async def async_Fetch_Preference(self):
        url = "https://playerpreferences.riotgames.com/playerPref/v3/getPreference/Ares.PlayerSettings"

        headers = make_headers(self.auth)

        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers)

            jsonData = resp.json()
            if "data" not in jsonData:
                return {}
            data = zloads(jsonData["data"])
            return data


    def Put_Preference(self, data):
        rawData = {
            "type": "Ares.PlayerSettings",
            "data": zdumps(data)
        }
        url = "https://playerpreferences.riotgames.com/playerPref/v3/savePreference"
        headers = make_headers(self.auth)
        resp = httpx.put(url, headers=headers, json=rawData)
        return resp

    async def async_Put_Preference(self, data):
        rawData = {
            "type": "Ares.PlayerSettings",
            "data": zdumps(data)
        }
        url = "https://playerpreferences.riotgames.com/playerPref/v3/savePreference"
        headers = make_headers(self.auth)
        async with httpx.AsyncClient() as client:
            resp = await client.put(url, headers=headers, json=rawData)

            return resp



