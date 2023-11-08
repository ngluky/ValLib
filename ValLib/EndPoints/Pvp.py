import httpx
import json
from uuid import UUID
from ..structs import Auth
from ..helper import make_headers, get_shard, get_region
from .structs import PlayerLoadout, PlayerMMRResponse, MatchHistoryResponse


class Pvp:
    def __init__(self, auth: Auth):
        self.auth = auth
        self.region = get_region(self.auth)
        self.shard = get_shard(self.region)

    def Fetch_Content(self):
        url = f"https://shared.{self.shard}.a.pvp.net/content-service/v3/content"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return resp.json()

    def Account_XP(self, puuid):
        url = f"https://pd.{self.shard}.a.pvp.net/account-xp/v1/players/{puuid}"
        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return resp.json()

    def Player_Loadout(self, player_UUID: UUID) -> PlayerLoadout.PlayerLoadout:
        puuid = player_UUID if player_UUID is not None else self.auth.user_id

        url = f"https://pd.{self.shard}.a.pvp.net/personalization/v2/players/{puuid}/playerloadout"
        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return PlayerLoadout.player_loadout_from_dict(resp.json())

    # not test
    def Set_Player_Loadout(self, player_loadout: PlayerLoadout.PlayerLoadout) -> PlayerLoadout.PlayerLoadout:
        url = f"https://pd.{self.shard}.a.pvp.net/personalization/v2/players/{self.auth.user_id}/playerloadout"

        resp = httpx.put(url, json=player_loadout.to_dict())
        return PlayerLoadout.PlayerLoadout.from_dict(resp.json())

    def Player_MMR(self, player_UUID: UUID = None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id
        url = f"https://pd.{self.shard}.a.pvp.net/mmr/v1/players/{puuid}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return PlayerMMRResponse.player_mmr_response_from_dict(resp.json())

    def Match_History(self, player_UUID: UUID = None, startIndex: int = 0, endIndex: int = 20, queue=None):
        puuid = player_UUID if player_UUID is not None else self.auth.user_id

        url = f"https://pd.{self.shard}.a.pvp.net/match-history/v1/history/{puuid}?startIndex={startIndex}&endIndex={endIndex}"

        if queue is not None:
            url += f"& queue = {queue}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return MatchHistoryResponse.match_history_response_from_dict(resp.json())

    def Match_Details(self, matchID: UUID):

        url = f"https://pd.{self.shard}.a.pvp.net/match-details/v1/matches/{matchID}"

        headers = make_headers(self.auth)

        resp = httpx.get(url, headers=headers)

        return  resp.json()

