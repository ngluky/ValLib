from enum import Enum
from dataclasses import dataclass
from uuid import UUID
from typing import Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class QueueID(Enum):
    COMPETITIVE = "competitive"
    DEATHMATCH = "deathmatch"
    UNRATED = "unrated"


@dataclass
class History:
    match_id: UUID
    game_start_time: int
    queue_id: QueueID

    @staticmethod
    def from_dict(obj: Any) -> 'History':
        assert isinstance(obj, dict)
        match_id = UUID(obj.get("MatchID"))
        game_start_time = from_int(obj.get("GameStartTime"))
        queue_id = QueueID(obj.get("QueueID"))
        return History(match_id, game_start_time, queue_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatchID"] = str(self.match_id)
        result["GameStartTime"] = from_int(self.game_start_time)
        result["QueueID"] = to_enum(QueueID, self.queue_id)
        return result


@dataclass
class MatchHistoryResponse:
    subject: UUID
    begin_index: int
    end_index: int
    total: int
    history: List[History]

    @staticmethod
    def from_dict(obj: Any) -> 'MatchHistoryResponse':
        assert isinstance(obj, dict)
        subject = UUID(obj.get("Subject"))
        begin_index = from_int(obj.get("BeginIndex"))
        end_index = from_int(obj.get("EndIndex"))
        total = from_int(obj.get("Total"))
        history = from_list(History.from_dict, obj.get("History"))
        return MatchHistoryResponse(subject, begin_index, end_index, total, history)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Subject"] = str(self.subject)
        result["BeginIndex"] = from_int(self.begin_index)
        result["EndIndex"] = from_int(self.end_index)
        result["Total"] = from_int(self.total)
        result["History"] = from_list(lambda x: to_class(History, x), self.history)
        return result


def match_history_response_from_dict(s: Any) -> MatchHistoryResponse:
    return MatchHistoryResponse.from_dict(s)


def match_history_response_to_dict(x: MatchHistoryResponse) -> Any:
    return to_class(MatchHistoryResponse, x)
