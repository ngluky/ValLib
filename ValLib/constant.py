import httpx
from .exceptions import ValorantAPIError
from .structs import classproperty

def fetch_versions():
    r = httpx.get("https://valorant-api.com/v1/version")
    if r.is_error:
        raise ValorantAPIError
    data = r.json()["data"]
    return data


def fetch_sketchy():
    r = httpx.get("https://valorant-api.com/internal/ritoclientversion")
    if r.is_error:
        raise ValorantAPIError
    data = r.json()["data"]
    return data



class Constant:
    __valorantVersion__ = ''
    __riotVersion__ = ''
    __sdkVersion__ = ''
    __shard__ = ''

    platform = {
        "platformType": "PC",
        "platformOS": "Windows",
        "platformOSVersion": "10.0.22621.1.768.64bit",
        "platformChipset": "Unknown"
    }

    @classproperty
    def valorantVersion(cls):
        if not cls.__riotVersion__:
            data = fetch_versions()
            if "riotClientVersion" in data:
                cls.__valorantVersion__ = data["riotClientVersion"]

            if "riotClientBuild" in data:
                cls.__riotVersion__ = data["riotClientBuild"]

        return cls.__valorantVersion__

    @classproperty
    def riotVersion(cls):
        if not cls.__riotVersion__:
            data = fetch_versions()
            if "riotClientVersion" in data:
                cls.__valorantVersion__ = data["riotClientVersion"]

            if "riotClientBuild" in data:
                cls.__riotVersion__ = data["riotClientBuild"]

        return cls.__riotVersion__

    @classproperty
    def sdkVersion(cls):
        if not cls.__sdkVersion__:
            data = fetch_sketchy()
            try:
                sdk_version = data["riotGamesApiInfo"]["VS_FIXEDFILEINFO"]["FileVersion"]
            except KeyError:
                sdk_version = "23.8.0.1382"

            cls.__sdkVersion__ = sdk_version

        return cls.__sdkVersion__
