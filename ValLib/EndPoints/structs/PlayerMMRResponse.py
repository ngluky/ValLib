from dataclasses import dataclass
from uuid import UUID
from typing import Any, Dict, Optional, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class LatestCompetitiveUpdate:
    match_id: UUID
    map_id: str
    season_id: UUID
    match_start_time: int
    tier_after_update: int
    tier_before_update: int
    ranked_rating_after_update: int
    ranked_rating_before_update: int
    ranked_rating_earned: int
    ranked_rating_performance_bonus: int
    competitive_movement: str
    afk_penalty: int

    @staticmethod
    def from_dict(obj: Any) -> 'LatestCompetitiveUpdate':
        assert isinstance(obj, dict)
        match_id = UUID(obj.get("MatchID"))
        map_id = from_str(obj.get("MapID"))
        season_id = UUID(obj.get("SeasonID"))
        match_start_time = from_int(obj.get("MatchStartTime"))
        tier_after_update = from_int(obj.get("TierAfterUpdate"))
        tier_before_update = from_int(obj.get("TierBeforeUpdate"))
        ranked_rating_after_update = from_int(obj.get("RankedRatingAfterUpdate"))
        ranked_rating_before_update = from_int(obj.get("RankedRatingBeforeUpdate"))
        ranked_rating_earned = from_int(obj.get("RankedRatingEarned"))
        ranked_rating_performance_bonus = from_int(obj.get("RankedRatingPerformanceBonus"))
        competitive_movement = from_str(obj.get("CompetitiveMovement"))
        afk_penalty = from_int(obj.get("AFKPenalty"))
        return LatestCompetitiveUpdate(match_id, map_id, season_id, match_start_time, tier_after_update, tier_before_update, ranked_rating_after_update, ranked_rating_before_update, ranked_rating_earned, ranked_rating_performance_bonus, competitive_movement, afk_penalty)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MatchID"] = str(self.match_id)
        result["MapID"] = from_str(self.map_id)
        result["SeasonID"] = str(self.season_id)
        result["MatchStartTime"] = from_int(self.match_start_time)
        result["TierAfterUpdate"] = from_int(self.tier_after_update)
        result["TierBeforeUpdate"] = from_int(self.tier_before_update)
        result["RankedRatingAfterUpdate"] = from_int(self.ranked_rating_after_update)
        result["RankedRatingBeforeUpdate"] = from_int(self.ranked_rating_before_update)
        result["RankedRatingEarned"] = from_int(self.ranked_rating_earned)
        result["RankedRatingPerformanceBonus"] = from_int(self.ranked_rating_performance_bonus)
        result["CompetitiveMovement"] = from_str(self.competitive_movement)
        result["AFKPenalty"] = from_int(self.afk_penalty)
        return result


@dataclass
class The2_De5423B4_Aad02_Ad8_D9BC0A931958861:
    season_id: UUID
    number_of_wins: int
    number_of_wins_with_placements: int
    number_of_games: int
    rank: int
    capstone_wins: int
    leaderboard_rank: int
    competitive_tier: int
    ranked_rating: int
    wins_by_tier: Dict[str, int]
    games_needed_for_rating: int
    total_wins_needed_for_rank: int

    @staticmethod
    def from_dict(obj: Any) -> 'The2_De5423B4_Aad02_Ad8_D9BC0A931958861':
        assert isinstance(obj, dict)
        season_id = UUID(obj.get("SeasonID"))
        number_of_wins = from_int(obj.get("NumberOfWins"))
        number_of_wins_with_placements = from_int(obj.get("NumberOfWinsWithPlacements"))
        number_of_games = from_int(obj.get("NumberOfGames"))
        rank = from_int(obj.get("Rank"))
        capstone_wins = from_int(obj.get("CapstoneWins"))
        leaderboard_rank = from_int(obj.get("LeaderboardRank"))
        competitive_tier = from_int(obj.get("CompetitiveTier"))
        ranked_rating = from_int(obj.get("RankedRating"))
        wins_by_tier = from_dict(from_int, obj.get("WinsByTier"))
        games_needed_for_rating = from_int(obj.get("GamesNeededForRating"))
        total_wins_needed_for_rank = from_int(obj.get("TotalWinsNeededForRank"))
        return The2_De5423B4_Aad02_Ad8_D9BC0A931958861(season_id, number_of_wins, number_of_wins_with_placements, number_of_games, rank, capstone_wins, leaderboard_rank, competitive_tier, ranked_rating, wins_by_tier, games_needed_for_rating, total_wins_needed_for_rank)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SeasonID"] = str(self.season_id)
        result["NumberOfWins"] = from_int(self.number_of_wins)
        result["NumberOfWinsWithPlacements"] = from_int(self.number_of_wins_with_placements)
        result["NumberOfGames"] = from_int(self.number_of_games)
        result["Rank"] = from_int(self.rank)
        result["CapstoneWins"] = from_int(self.capstone_wins)
        result["LeaderboardRank"] = from_int(self.leaderboard_rank)
        result["CompetitiveTier"] = from_int(self.competitive_tier)
        result["RankedRating"] = from_int(self.ranked_rating)
        result["WinsByTier"] = from_dict(from_int, self.wins_by_tier)
        result["GamesNeededForRating"] = from_int(self.games_needed_for_rating)
        result["TotalWinsNeededForRank"] = from_int(self.total_wins_needed_for_rank)
        return result


@dataclass
class The0981_A8824_E7D371_A70_C4C3B4F46C504A:
    season_id: UUID
    number_of_wins: int
    number_of_wins_with_placements: int
    number_of_games: int
    rank: int
    capstone_wins: int
    leaderboard_rank: int
    competitive_tier: int
    ranked_rating: int
    games_needed_for_rating: int
    total_wins_needed_for_rank: int
    wins_by_tier: Optional[Dict[str, int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'The0981_A8824_E7D371_A70_C4C3B4F46C504A':
        assert isinstance(obj, dict)
        season_id = UUID(obj.get("SeasonID"))
        number_of_wins = from_int(obj.get("NumberOfWins"))
        number_of_wins_with_placements = from_int(obj.get("NumberOfWinsWithPlacements"))
        number_of_games = from_int(obj.get("NumberOfGames"))
        rank = from_int(obj.get("Rank"))
        capstone_wins = from_int(obj.get("CapstoneWins"))
        leaderboard_rank = from_int(obj.get("LeaderboardRank"))
        competitive_tier = from_int(obj.get("CompetitiveTier"))
        ranked_rating = from_int(obj.get("RankedRating"))
        games_needed_for_rating = from_int(obj.get("GamesNeededForRating"))
        total_wins_needed_for_rank = from_int(obj.get("TotalWinsNeededForRank"))
        wins_by_tier = from_union([lambda x: from_dict(from_int, x), from_none], obj.get("WinsByTier"))
        return The0981_A8824_E7D371_A70_C4C3B4F46C504A(season_id, number_of_wins, number_of_wins_with_placements, number_of_games, rank, capstone_wins, leaderboard_rank, competitive_tier, ranked_rating, games_needed_for_rating, total_wins_needed_for_rank, wins_by_tier)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SeasonID"] = str(self.season_id)
        result["NumberOfWins"] = from_int(self.number_of_wins)
        result["NumberOfWinsWithPlacements"] = from_int(self.number_of_wins_with_placements)
        result["NumberOfGames"] = from_int(self.number_of_games)
        result["Rank"] = from_int(self.rank)
        result["CapstoneWins"] = from_int(self.capstone_wins)
        result["LeaderboardRank"] = from_int(self.leaderboard_rank)
        result["CompetitiveTier"] = from_int(self.competitive_tier)
        result["RankedRating"] = from_int(self.ranked_rating)
        result["GamesNeededForRating"] = from_int(self.games_needed_for_rating)
        result["TotalWinsNeededForRank"] = from_int(self.total_wins_needed_for_rank)
        result["WinsByTier"] = from_union([lambda x: from_dict(from_int, x), from_none], self.wins_by_tier)
        return result


@dataclass
class WINSByTier:
    the_12: int

    @staticmethod
    def from_dict(obj: Any) -> 'WINSByTier':
        assert isinstance(obj, dict)
        the_12 = from_int(obj.get("12"))
        return WINSByTier(the_12)

    def to_dict(self) -> dict:
        result: dict = {}
        result["12"] = from_int(self.the_12)
        return result


@dataclass
class The4401F9Fd41702E4C4Bc3F3B4D7D150D1:
    season_id: UUID
    number_of_wins: int
    number_of_wins_with_placements: int
    number_of_games: int
    rank: int
    capstone_wins: int
    leaderboard_rank: int
    competitive_tier: int
    ranked_rating: int
    wins_by_tier: WINSByTier
    games_needed_for_rating: int
    total_wins_needed_for_rank: int

    @staticmethod
    def from_dict(obj: Any) -> 'The4401F9Fd41702E4C4Bc3F3B4D7D150D1':
        assert isinstance(obj, dict)
        season_id = UUID(obj.get("SeasonID"))
        number_of_wins = from_int(obj.get("NumberOfWins"))
        number_of_wins_with_placements = from_int(obj.get("NumberOfWinsWithPlacements"))
        number_of_games = from_int(obj.get("NumberOfGames"))
        rank = from_int(obj.get("Rank"))
        capstone_wins = from_int(obj.get("CapstoneWins"))
        leaderboard_rank = from_int(obj.get("LeaderboardRank"))
        competitive_tier = from_int(obj.get("CompetitiveTier"))
        ranked_rating = from_int(obj.get("RankedRating"))
        wins_by_tier = WINSByTier.from_dict(obj.get("WinsByTier"))
        games_needed_for_rating = from_int(obj.get("GamesNeededForRating"))
        total_wins_needed_for_rank = from_int(obj.get("TotalWinsNeededForRank"))
        return The4401F9Fd41702E4C4Bc3F3B4D7D150D1(season_id, number_of_wins, number_of_wins_with_placements, number_of_games, rank, capstone_wins, leaderboard_rank, competitive_tier, ranked_rating, wins_by_tier, games_needed_for_rating, total_wins_needed_for_rank)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SeasonID"] = str(self.season_id)
        result["NumberOfWins"] = from_int(self.number_of_wins)
        result["NumberOfWinsWithPlacements"] = from_int(self.number_of_wins_with_placements)
        result["NumberOfGames"] = from_int(self.number_of_games)
        result["Rank"] = from_int(self.rank)
        result["CapstoneWins"] = from_int(self.capstone_wins)
        result["LeaderboardRank"] = from_int(self.leaderboard_rank)
        result["CompetitiveTier"] = from_int(self.competitive_tier)
        result["RankedRating"] = from_int(self.ranked_rating)
        result["WinsByTier"] = to_class(WINSByTier, self.wins_by_tier)
        result["GamesNeededForRating"] = from_int(self.games_needed_for_rating)
        result["TotalWinsNeededForRank"] = from_int(self.total_wins_needed_for_rank)
        return result


@dataclass
class CompetitiveSeasonalInfoBySeasonID:
    the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a: The0981_A8824_E7D371_A70_C4C3B4F46C504A
    the_2_de5423_b_4_aad_02_ad_8_d9_b_c0_a931958861: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_34093_c29_430643_de_452_f_3_f944_bde22_be: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_3_e47230_a_463_c_a301_eb7_d_67_bb60357_d4_f: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_4401_f9_fd_41702_e4_c_4_bc3_f3_b4_d7_d150_d1: The4401F9Fd41702E4C4Bc3F3B4D7D150D1
    the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_7_a85_de9_a_403261_a9_61_d8_f4_aa2_b4_a84_b6: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    the_9_c91_a445_4_f78_1_baa_a3_ea_8_f8_aadf4914_d: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    aca29595_40_e4_01_f5_3_f35_b1_b3_d304_c96_e: The2_De5423B4_Aad02_Ad8_D9BC0A931958861
    d929_bc38_4_ab6_7_da4_94_f0_ee84_f8_ac141_e: The2_De5423B4_Aad02_Ad8_D9BC0A931958861

    @staticmethod
    def from_dict(obj: Any) -> 'CompetitiveSeasonalInfoBySeasonID':
        assert isinstance(obj, dict)
        the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a = The0981_A8824_E7D371_A70_C4C3B4F46C504A.from_dict(obj.get("0981a882-4e7d-371a-70c4-c3b4f46c504a"))
        the_2_de5423_b_4_aad_02_ad_8_d9_b_c0_a931958861 = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("2de5423b-4aad-02ad-8d9b-c0a931958861"))
        the_34093_c29_430643_de_452_f_3_f944_bde22_be = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("34093c29-4306-43de-452f-3f944bde22be"))
        the_3_e47230_a_463_c_a301_eb7_d_67_bb60357_d4_f = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("3e47230a-463c-a301-eb7d-67bb60357d4f"))
        the_4401_f9_fd_41702_e4_c_4_bc3_f3_b4_d7_d150_d1 = The4401F9Fd41702E4C4Bc3F3B4D7D150D1.from_dict(obj.get("4401f9fd-4170-2e4c-4bc3-f3b4d7d150d1"))
        the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704 = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("573f53ac-41a5-3a7d-d9ce-d6a6298e5704"))
        the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427 = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("67e373c7-48f7-b422-641b-079ace30b427"))
        the_7_a85_de9_a_403261_a9_61_d8_f4_aa2_b4_a84_b6 = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("7a85de9a-4032-61a9-61d8-f4aa2b4a84b6"))
        the_9_c91_a445_4_f78_1_baa_a3_ea_8_f8_aadf4914_d = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("9c91a445-4f78-1baa-a3ea-8f8aadf4914d"))
        aca29595_40_e4_01_f5_3_f35_b1_b3_d304_c96_e = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("aca29595-40e4-01f5-3f35-b1b3d304c96e"))
        d929_bc38_4_ab6_7_da4_94_f0_ee84_f8_ac141_e = The2_De5423B4_Aad02_Ad8_D9BC0A931958861.from_dict(obj.get("d929bc38-4ab6-7da4-94f0-ee84f8ac141e"))
        return CompetitiveSeasonalInfoBySeasonID(the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a, the_2_de5423_b_4_aad_02_ad_8_d9_b_c0_a931958861, the_34093_c29_430643_de_452_f_3_f944_bde22_be, the_3_e47230_a_463_c_a301_eb7_d_67_bb60357_d4_f, the_4401_f9_fd_41702_e4_c_4_bc3_f3_b4_d7_d150_d1, the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704, the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427, the_7_a85_de9_a_403261_a9_61_d8_f4_aa2_b4_a84_b6, the_9_c91_a445_4_f78_1_baa_a3_ea_8_f8_aadf4914_d, aca29595_40_e4_01_f5_3_f35_b1_b3_d304_c96_e, d929_bc38_4_ab6_7_da4_94_f0_ee84_f8_ac141_e)

    def to_dict(self) -> dict:
        result: dict = {}
        result["0981a882-4e7d-371a-70c4-c3b4f46c504a"] = to_class(The0981_A8824_E7D371_A70_C4C3B4F46C504A, self.the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a)
        result["2de5423b-4aad-02ad-8d9b-c0a931958861"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_2_de5423_b_4_aad_02_ad_8_d9_b_c0_a931958861)
        result["34093c29-4306-43de-452f-3f944bde22be"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_34093_c29_430643_de_452_f_3_f944_bde22_be)
        result["3e47230a-463c-a301-eb7d-67bb60357d4f"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_3_e47230_a_463_c_a301_eb7_d_67_bb60357_d4_f)
        result["4401f9fd-4170-2e4c-4bc3-f3b4d7d150d1"] = to_class(The4401F9Fd41702E4C4Bc3F3B4D7D150D1, self.the_4401_f9_fd_41702_e4_c_4_bc3_f3_b4_d7_d150_d1)
        result["573f53ac-41a5-3a7d-d9ce-d6a6298e5704"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704)
        result["67e373c7-48f7-b422-641b-079ace30b427"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427)
        result["7a85de9a-4032-61a9-61d8-f4aa2b4a84b6"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_7_a85_de9_a_403261_a9_61_d8_f4_aa2_b4_a84_b6)
        result["9c91a445-4f78-1baa-a3ea-8f8aadf4914d"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.the_9_c91_a445_4_f78_1_baa_a3_ea_8_f8_aadf4914_d)
        result["aca29595-40e4-01f5-3f35-b1b3d304c96e"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.aca29595_40_e4_01_f5_3_f35_b1_b3_d304_c96_e)
        result["d929bc38-4ab6-7da4-94f0-ee84f8ac141e"] = to_class(The2_De5423B4_Aad02_Ad8_D9BC0A931958861, self.d929_bc38_4_ab6_7_da4_94_f0_ee84_f8_ac141_e)
        return result


@dataclass
class Competitive:
    total_games_needed_for_rating: int
    total_games_needed_for_leaderboard: int
    current_season_games_needed_for_rating: int
    seasonal_info_by_season_id: CompetitiveSeasonalInfoBySeasonID

    @staticmethod
    def from_dict(obj: Any) -> 'Competitive':
        assert isinstance(obj, dict)
        total_games_needed_for_rating = from_int(obj.get("TotalGamesNeededForRating"))
        total_games_needed_for_leaderboard = from_int(obj.get("TotalGamesNeededForLeaderboard"))
        current_season_games_needed_for_rating = from_int(obj.get("CurrentSeasonGamesNeededForRating"))
        seasonal_info_by_season_id = CompetitiveSeasonalInfoBySeasonID.from_dict(obj.get("SeasonalInfoBySeasonID"))
        return Competitive(total_games_needed_for_rating, total_games_needed_for_leaderboard, current_season_games_needed_for_rating, seasonal_info_by_season_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TotalGamesNeededForRating"] = from_int(self.total_games_needed_for_rating)
        result["TotalGamesNeededForLeaderboard"] = from_int(self.total_games_needed_for_leaderboard)
        result["CurrentSeasonGamesNeededForRating"] = from_int(self.current_season_games_needed_for_rating)
        result["SeasonalInfoBySeasonID"] = to_class(CompetitiveSeasonalInfoBySeasonID, self.seasonal_info_by_season_id)
        return result


@dataclass
class Deathmatch:
    total_games_needed_for_rating: int
    total_games_needed_for_leaderboard: int
    current_season_games_needed_for_rating: int
    seasonal_info_by_season_id: Dict[str, The0981_A8824_E7D371_A70_C4C3B4F46C504A]

    @staticmethod
    def from_dict(obj: Any) -> 'Deathmatch':
        assert isinstance(obj, dict)
        total_games_needed_for_rating = from_int(obj.get("TotalGamesNeededForRating"))
        total_games_needed_for_leaderboard = from_int(obj.get("TotalGamesNeededForLeaderboard"))
        current_season_games_needed_for_rating = from_int(obj.get("CurrentSeasonGamesNeededForRating"))
        seasonal_info_by_season_id = from_dict(The0981_A8824_E7D371_A70_C4C3B4F46C504A.from_dict, obj.get("SeasonalInfoBySeasonID"))
        return Deathmatch(total_games_needed_for_rating, total_games_needed_for_leaderboard, current_season_games_needed_for_rating, seasonal_info_by_season_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TotalGamesNeededForRating"] = from_int(self.total_games_needed_for_rating)
        result["TotalGamesNeededForLeaderboard"] = from_int(self.total_games_needed_for_leaderboard)
        result["CurrentSeasonGamesNeededForRating"] = from_int(self.current_season_games_needed_for_rating)
        result["SeasonalInfoBySeasonID"] = from_dict(lambda x: to_class(The0981_A8824_E7D371_A70_C4C3B4F46C504A, x), self.seasonal_info_by_season_id)
        return result


@dataclass
class HurmSeasonalInfoBySeasonID:
    the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a: The0981_A8824_E7D371_A70_C4C3B4F46C504A

    @staticmethod
    def from_dict(obj: Any) -> 'HurmSeasonalInfoBySeasonID':
        assert isinstance(obj, dict)
        the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a = The0981_A8824_E7D371_A70_C4C3B4F46C504A.from_dict(obj.get("0981a882-4e7d-371a-70c4-c3b4f46c504a"))
        return HurmSeasonalInfoBySeasonID(the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a)

    def to_dict(self) -> dict:
        result: dict = {}
        result["0981a882-4e7d-371a-70c4-c3b4f46c504a"] = to_class(The0981_A8824_E7D371_A70_C4C3B4F46C504A, self.the_0981_a882_4_e7_d_371_a_70_c4_c3_b4_f46_c504_a)
        return result


@dataclass
class Hurm:
    total_games_needed_for_rating: int
    total_games_needed_for_leaderboard: int
    current_season_games_needed_for_rating: int
    seasonal_info_by_season_id: HurmSeasonalInfoBySeasonID

    @staticmethod
    def from_dict(obj: Any) -> 'Hurm':
        assert isinstance(obj, dict)
        total_games_needed_for_rating = from_int(obj.get("TotalGamesNeededForRating"))
        total_games_needed_for_leaderboard = from_int(obj.get("TotalGamesNeededForLeaderboard"))
        current_season_games_needed_for_rating = from_int(obj.get("CurrentSeasonGamesNeededForRating"))
        seasonal_info_by_season_id = HurmSeasonalInfoBySeasonID.from_dict(obj.get("SeasonalInfoBySeasonID"))
        return Hurm(total_games_needed_for_rating, total_games_needed_for_leaderboard, current_season_games_needed_for_rating, seasonal_info_by_season_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TotalGamesNeededForRating"] = from_int(self.total_games_needed_for_rating)
        result["TotalGamesNeededForLeaderboard"] = from_int(self.total_games_needed_for_leaderboard)
        result["CurrentSeasonGamesNeededForRating"] = from_int(self.current_season_games_needed_for_rating)
        result["SeasonalInfoBySeasonID"] = to_class(HurmSeasonalInfoBySeasonID, self.seasonal_info_by_season_id)
        return result


@dataclass
class NewmapSeasonalInfoBySeasonID:
    the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427: The0981_A8824_E7D371_A70_C4C3B4F46C504A

    @staticmethod
    def from_dict(obj: Any) -> 'NewmapSeasonalInfoBySeasonID':
        assert isinstance(obj, dict)
        the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427 = The0981_A8824_E7D371_A70_C4C3B4F46C504A.from_dict(obj.get("67e373c7-48f7-b422-641b-079ace30b427"))
        return NewmapSeasonalInfoBySeasonID(the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427)

    def to_dict(self) -> dict:
        result: dict = {}
        result["67e373c7-48f7-b422-641b-079ace30b427"] = to_class(The0981_A8824_E7D371_A70_C4C3B4F46C504A, self.the_67_e373_c7_48_f7_b422_641_b_079_ace30_b427)
        return result


@dataclass
class Newmap:
    total_games_needed_for_rating: int
    total_games_needed_for_leaderboard: int
    current_season_games_needed_for_rating: int
    seasonal_info_by_season_id: NewmapSeasonalInfoBySeasonID

    @staticmethod
    def from_dict(obj: Any) -> 'Newmap':
        assert isinstance(obj, dict)
        total_games_needed_for_rating = from_int(obj.get("TotalGamesNeededForRating"))
        total_games_needed_for_leaderboard = from_int(obj.get("TotalGamesNeededForLeaderboard"))
        current_season_games_needed_for_rating = from_int(obj.get("CurrentSeasonGamesNeededForRating"))
        seasonal_info_by_season_id = NewmapSeasonalInfoBySeasonID.from_dict(obj.get("SeasonalInfoBySeasonID"))
        return Newmap(total_games_needed_for_rating, total_games_needed_for_leaderboard, current_season_games_needed_for_rating, seasonal_info_by_season_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TotalGamesNeededForRating"] = from_int(self.total_games_needed_for_rating)
        result["TotalGamesNeededForLeaderboard"] = from_int(self.total_games_needed_for_leaderboard)
        result["CurrentSeasonGamesNeededForRating"] = from_int(self.current_season_games_needed_for_rating)
        result["SeasonalInfoBySeasonID"] = to_class(NewmapSeasonalInfoBySeasonID, self.seasonal_info_by_season_id)
        return result


@dataclass
class SeedingSeasonalInfoBySeasonID:
    the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704: The0981_A8824_E7D371_A70_C4C3B4F46C504A

    @staticmethod
    def from_dict(obj: Any) -> 'SeedingSeasonalInfoBySeasonID':
        assert isinstance(obj, dict)
        the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704 = The0981_A8824_E7D371_A70_C4C3B4F46C504A.from_dict(obj.get("573f53ac-41a5-3a7d-d9ce-d6a6298e5704"))
        return SeedingSeasonalInfoBySeasonID(the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704)

    def to_dict(self) -> dict:
        result: dict = {}
        result["573f53ac-41a5-3a7d-d9ce-d6a6298e5704"] = to_class(The0981_A8824_E7D371_A70_C4C3B4F46C504A, self.the_573_f53_ac_41_a5_3_a7_d_d9_ce_d6_a6298_e5704)
        return result


@dataclass
class Seeding:
    total_games_needed_for_rating: int
    total_games_needed_for_leaderboard: int
    current_season_games_needed_for_rating: int
    seasonal_info_by_season_id: SeedingSeasonalInfoBySeasonID

    @staticmethod
    def from_dict(obj: Any) -> 'Seeding':
        assert isinstance(obj, dict)
        total_games_needed_for_rating = from_int(obj.get("TotalGamesNeededForRating"))
        total_games_needed_for_leaderboard = from_int(obj.get("TotalGamesNeededForLeaderboard"))
        current_season_games_needed_for_rating = from_int(obj.get("CurrentSeasonGamesNeededForRating"))
        seasonal_info_by_season_id = SeedingSeasonalInfoBySeasonID.from_dict(obj.get("SeasonalInfoBySeasonID"))
        return Seeding(total_games_needed_for_rating, total_games_needed_for_leaderboard, current_season_games_needed_for_rating, seasonal_info_by_season_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["TotalGamesNeededForRating"] = from_int(self.total_games_needed_for_rating)
        result["TotalGamesNeededForLeaderboard"] = from_int(self.total_games_needed_for_leaderboard)
        result["CurrentSeasonGamesNeededForRating"] = from_int(self.current_season_games_needed_for_rating)
        result["SeasonalInfoBySeasonID"] = to_class(SeedingSeasonalInfoBySeasonID, self.seasonal_info_by_season_id)
        return result


@dataclass
class QueueSkills:
    competitive: Competitive
    deathmatch: Deathmatch
    ggteam: Deathmatch
    hurm: Hurm
    newmap: Newmap
    onefa: Deathmatch
    seeding: Seeding
    spikerush: Deathmatch
    swiftplay: Deathmatch
    unrated: Deathmatch

    @staticmethod
    def from_dict(obj: Any) -> 'QueueSkills':
        assert isinstance(obj, dict)
        competitive = Competitive.from_dict(obj.get("competitive"))
        deathmatch = Deathmatch.from_dict(obj.get("deathmatch"))
        ggteam = Deathmatch.from_dict(obj.get("ggteam"))
        hurm = Hurm.from_dict(obj.get("hurm"))
        newmap = Newmap.from_dict(obj.get("newmap"))
        onefa = Deathmatch.from_dict(obj.get("onefa"))
        seeding = Seeding.from_dict(obj.get("seeding"))
        spikerush = Deathmatch.from_dict(obj.get("spikerush"))
        swiftplay = Deathmatch.from_dict(obj.get("swiftplay"))
        unrated = Deathmatch.from_dict(obj.get("unrated"))
        return QueueSkills(competitive, deathmatch, ggteam, hurm, newmap, onefa, seeding, spikerush, swiftplay, unrated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["competitive"] = to_class(Competitive, self.competitive)
        result["deathmatch"] = to_class(Deathmatch, self.deathmatch)
        result["ggteam"] = to_class(Deathmatch, self.ggteam)
        result["hurm"] = to_class(Hurm, self.hurm)
        result["newmap"] = to_class(Newmap, self.newmap)
        result["onefa"] = to_class(Deathmatch, self.onefa)
        result["seeding"] = to_class(Seeding, self.seeding)
        result["spikerush"] = to_class(Deathmatch, self.spikerush)
        result["swiftplay"] = to_class(Deathmatch, self.swiftplay)
        result["unrated"] = to_class(Deathmatch, self.unrated)
        return result


@dataclass
class PlayerMMRResponse:
    version: int
    subject: UUID
    new_player_experience_finished: bool
    queue_skills: QueueSkills
    latest_competitive_update: LatestCompetitiveUpdate
    is_leaderboard_anonymized: bool
    is_act_rank_badge_hidden: bool

    @staticmethod
    def from_dict(obj: Any) -> 'PlayerMMRResponse':
        assert isinstance(obj, dict)
        version = from_int(obj.get("Version"))
        subject = UUID(obj.get("Subject"))
        new_player_experience_finished = from_bool(obj.get("NewPlayerExperienceFinished"))
        queue_skills = QueueSkills.from_dict(obj.get("QueueSkills"))
        latest_competitive_update = LatestCompetitiveUpdate.from_dict(obj.get("LatestCompetitiveUpdate"))
        is_leaderboard_anonymized = from_bool(obj.get("IsLeaderboardAnonymized"))
        is_act_rank_badge_hidden = from_bool(obj.get("IsActRankBadgeHidden"))
        return PlayerMMRResponse(version, subject, new_player_experience_finished, queue_skills, latest_competitive_update, is_leaderboard_anonymized, is_act_rank_badge_hidden)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Version"] = from_int(self.version)
        result["Subject"] = str(self.subject)
        result["NewPlayerExperienceFinished"] = from_bool(self.new_player_experience_finished)
        result["QueueSkills"] = to_class(QueueSkills, self.queue_skills)
        result["LatestCompetitiveUpdate"] = to_class(LatestCompetitiveUpdate, self.latest_competitive_update)
        result["IsLeaderboardAnonymized"] = from_bool(self.is_leaderboard_anonymized)
        result["IsActRankBadgeHidden"] = from_bool(self.is_act_rank_badge_hidden)
        return result


def player_mmr_response_from_dict(s: Any) -> PlayerMMRResponse:
    return PlayerMMRResponse.from_dict(s)


def player_mmr_response_to_dict(x: PlayerMMRResponse) -> Any:
    return to_class(PlayerMMRResponse, x)
