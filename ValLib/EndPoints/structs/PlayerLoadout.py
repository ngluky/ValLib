from dataclasses import dataclass
from uuid import UUID
from typing import List, Any, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Gun:
    id: UUID
    skin_id: UUID
    skin_level_id: UUID
    chroma_id: UUID
    attachments: List[Any]
    charm_instance_id: Optional[UUID] = None
    charm_id: Optional[UUID] = None
    charm_level_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Gun':
        assert isinstance(obj, dict)
        id = UUID(obj.get("ID"))
        skin_id = UUID(obj.get("SkinID"))
        skin_level_id = UUID(obj.get("SkinLevelID"))
        chroma_id = UUID(obj.get("ChromaID"))
        attachments = from_list(lambda x: x, obj.get("Attachments"))
        charm_instance_id = from_union([lambda x: UUID(x), from_none], obj.get("CharmInstanceID"))
        charm_id = from_union([lambda x: UUID(x), from_none], obj.get("CharmID"))
        charm_level_id = from_union([lambda x: UUID(x), from_none], obj.get("CharmLevelID"))
        return Gun(id, skin_id, skin_level_id, chroma_id, attachments, charm_instance_id, charm_id, charm_level_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = str(self.id)
        result["SkinID"] = str(self.skin_id)
        result["SkinLevelID"] = str(self.skin_level_id)
        result["ChromaID"] = str(self.chroma_id)
        result["Attachments"] = from_list(lambda x: x, self.attachments)
        if self.charm_instance_id is not None:
            result["CharmInstanceID"] = from_union([lambda x: str(x), from_none], self.charm_instance_id)
        if self.charm_id is not None:
            result["CharmID"] = from_union([lambda x: str(x), from_none], self.charm_id)
        if self.charm_level_id is not None:
            result["CharmLevelID"] = from_union([lambda x: str(x), from_none], self.charm_level_id)
        return result


@dataclass
class Identity:
    player_card_id: UUID
    player_title_id: UUID
    account_level: int
    preferred_level_border_id: UUID
    hide_account_level: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Identity':
        assert isinstance(obj, dict)
        player_card_id = UUID(obj.get("PlayerCardID"))
        player_title_id = UUID(obj.get("PlayerTitleID"))
        account_level = from_int(obj.get("AccountLevel"))
        preferred_level_border_id = UUID(obj.get("PreferredLevelBorderID"))
        hide_account_level = from_bool(obj.get("HideAccountLevel"))
        return Identity(player_card_id, player_title_id, account_level, preferred_level_border_id, hide_account_level)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlayerCardID"] = str(self.player_card_id)
        result["PlayerTitleID"] = str(self.player_title_id)
        result["AccountLevel"] = from_int(self.account_level)
        result["PreferredLevelBorderID"] = str(self.preferred_level_border_id)
        result["HideAccountLevel"] = from_bool(self.hide_account_level)
        return result


@dataclass
class Spray:
    equip_slot_id: UUID
    spray_id: UUID
    spray_level_id: None

    @staticmethod
    def from_dict(obj: Any) -> 'Spray':
        assert isinstance(obj, dict)
        equip_slot_id = UUID(obj.get("EquipSlotID"))
        spray_id = UUID(obj.get("SprayID"))
        spray_level_id = from_none(obj.get("SprayLevelID"))
        return Spray(equip_slot_id, spray_id, spray_level_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EquipSlotID"] = str(self.equip_slot_id)
        result["SprayID"] = str(self.spray_id)
        result["SprayLevelID"] = from_none(self.spray_level_id)
        return result


@dataclass
class PlayerLoadout:
    guns: List[Gun]
    sprays: List[Spray]
    identity: Identity
    incognito: bool

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerLoadout':
        assert isinstance(obj, dict)
        guns = from_list(Gun.from_dict, obj.get("Guns"))
        sprays = from_list(Spray.from_dict, obj.get("Sprays"))
        identity = Identity.from_dict(obj.get("Identity"))
        incognito = from_bool(obj.get("Incognito"))
        return PlayerLoadout(guns, sprays, identity, incognito)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Guns"] = from_list(lambda x: to_class(Gun, x), self.guns)
        result["Sprays"] = from_list(lambda x: to_class(Spray, x), self.sprays)
        result["Identity"] = to_class(Identity, self.identity)
        result["Incognito"] = from_bool(self.incognito)
        return result


def player_loadout_from_dict(s: Any) -> PlayerLoadout:
    return PlayerLoadout.from_dict(s)


def player_loadout_to_dict(x: PlayerLoadout) -> Any:
    return to_class(PlayerLoadout, x)
