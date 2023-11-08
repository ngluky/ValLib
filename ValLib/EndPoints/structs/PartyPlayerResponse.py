from dataclasses import dataclass
from typing import Any, List, TypeVar, Callable, Type, cast
from uuid import UUID

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class PlatformInfo:
    platform_type: str
    platform_os: str
    platform_os_version: str
    platform_chipset: str

    @staticmethod
    def from_dict(obj: Any) -> 'PlatformInfo':
        assert isinstance(obj, dict)
        platform_type = from_str(obj.get("platformType"))
        platform_os = from_str(obj.get("platformOS"))
        platform_os_version = from_str(obj.get("platformOSVersion"))
        platform_chipset = from_str(obj.get("platformChipset"))
        return PlatformInfo(platform_type, platform_os, platform_os_version, platform_chipset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["platformType"] = from_str(self.platform_type)
        result["platformOS"] = from_str(self.platform_os)
        result["platformOSVersion"] = from_str(self.platform_os_version)
        result["platformChipset"] = from_str(self.platform_chipset)
        return result


@dataclass
class PartyPlayerResponse:
    subject: UUID
    version: int
    current_party_id: UUID
    invites: None
    requests: List[Any]
    platform_info: PlatformInfo

    @staticmethod
    def from_dict(obj: Any) -> 'PartyPlayerResponse':
        assert isinstance(obj, dict)
        subject = UUID(obj.get("Subject"))
        version = from_int(obj.get("Version"))
        current_party_id = UUID(obj.get("CurrentPartyID"))
        invites = from_none(obj.get("Invites"))
        requests = from_list(lambda x: x, obj.get("Requests"))
        platform_info = PlatformInfo.from_dict(obj.get("PlatformInfo"))
        return PartyPlayerResponse(subject, version, current_party_id, invites, requests, platform_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Subject"] = str(self.subject)
        result["Version"] = from_int(self.version)
        result["CurrentPartyID"] = str(self.current_party_id)
        result["Invites"] = from_none(self.invites)
        result["Requests"] = from_list(lambda x: x, self.requests)
        result["PlatformInfo"] = to_class(PlatformInfo, self.platform_info)
        return result


def party_player_response_from_dict(s: Any) -> PartyPlayerResponse:
    return PartyPlayerResponse.from_dict(s)


def party_player_response_to_dict(x: PartyPlayerResponse) -> Any:
    return to_class(PartyPlayerResponse, x)
