from collections import Counter
from enum import IntEnum

from poker.card import Card


class HandRank(IntEnum):
    """ポーカーの役 (強さの昇順)"""

    HIGH_CARD = 0
    ONE_PAIR = 1


HAND_RANK_LABELS = {
    HandRank.HIGH_CARD: "ハイカード",
    HandRank.ONE_PAIR: "ワンペア",
}


def format_hand_rank(hand_rank: HandRank) -> str:
    return f"{HAND_RANK_LABELS[hand_rank]} {hand_rank.value}"


# TODO: 参加者が役判定を実装する
def evaluate_hand(hand: list[Card]) -> HandRank:
    rank_counts = Counter(card.rank for card in hand)

    if 2 in rank_counts.values():
        return HandRank.ONE_PAIR
    return HandRank.HIGH_CARD
