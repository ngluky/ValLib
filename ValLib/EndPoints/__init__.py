from .Pvp import Pvp
from .Party import Party
from .CurrentGame import CurrentGame
from .Setting import Setting

from ..structs import Auth
from ..helper import get_region, get_shard, make_headers


class EndPoints:
    def __init__(self, auth: Auth, region=None, shard=None):
        self.auth = auth
        self.region = get_region(self.auth) if region is None else region
        self.shard = get_shard(self.region) if shard is None else shard

        self.Pvp = Pvp(self.auth, self.region, self.shard)
        self.Party = Party(self.auth, self.region, self.shard)
        self.CurrentGame = CurrentGame(self.auth, self.region, self.shard)
        self.Setting = Setting(self.auth, self.region, self.shard)


__all__ = {
    "EndPoints"
}
