from collections import Counter

from poker.card import Card, Rank


def evaluate_hand(hand: list[Card]) -> str:
    """6枚の手札からポーカーの役を判定して役名を返す。"""
    ranks: list[int] = sorted(card.rank.value for card in hand)
    rank_counts: list[int] = sorted(Counter(ranks).values(), reverse=True)

    is_flush: bool = len({card.suit for card in hand}) == 1
    is_straight: bool = _is_straight(ranks)

    seven_count: int = sum(1 for card in hand if card.rank == Rank.SEVEN)
    if seven_count == 3:
        return "スリーセブン"
    if is_flush and is_straight:
        return "ストレートフラッシュ"
    if rank_counts[0] == 4:
        return "フォーカード"
    if rank_counts[0] == 3 and rank_counts[1] >= 2:
        return "フルハウス"
    if is_flush:
        return "フラッシュ"
    if is_straight:
        return "ストレート"
    if rank_counts == [2, 2, 2]:
        return "スリーペア"
    if rank_counts[0] == 3:
        return "スリーカード"
    if rank_counts == [2, 2, 1, 1]:
        return "ツーペア"
    if rank_counts[0] == 2:
        return "ワンペア"
    return "ハイカード"


HAND_RANKINGS: dict[str, int] = {
    "スリーセブン": 11,
    "ストレートフラッシュ": 10,
    "フォーカード": 9,
    "フルハウス": 8,
    "フラッシュ": 7,
    "ストレート": 6,
    "スリーペア": 5,
    "スリーカード": 4,
    "ツーペア": 3,
    "ワンペア": 2,
    "ハイカード": 1,
}


def hand_rank(hand_name: str) -> int:
    """役名から強さを返す。数値が大きいほど強い。"""
    return HAND_RANKINGS[hand_name]


def _is_straight(ranks: list[int]) -> bool:
    """ソート済みランク6枚が全て連番かどうかを判定する。"""
    if len(set(ranks)) != 6:
        return False
    # 通常のストレート: 最大 - 最小 == 5
    if ranks[-1] - ranks[0] == 5:
        return True
    # A-high ストレート: A(1), 9, 10, J, Q, K
    return ranks == [Rank.ACE, Rank.NINE, Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING]
