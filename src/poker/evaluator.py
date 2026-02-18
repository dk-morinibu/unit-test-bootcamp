from enum import IntEnum

from poker.card import Card


class HandRank(IntEnum):
    """ポーカーの役 (強さの昇順)"""

    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


# TODO: 参加者が役判定を実装する
def evaluate_hand(hand: list[Card]) -> HandRank:
    return HandRank.HIGH_CARD
