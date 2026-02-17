from collections import Counter

from poker.card import Card, Rank


def evaluate_hand(hand: list[Card]) -> str:
    """5枚の手札からポーカーの役を判定して役名を返す。"""
    ranks: list[int] = sorted(card.rank.value for card in hand)
    rank_counts: list[int] = sorted(Counter(ranks).values(), reverse=True)

    is_flush: bool = len({card.suit for card in hand}) == 1
    is_straight: bool = _is_straight(ranks)

    if is_flush and is_straight:
        return "ストレートフラッシュ"
    if rank_counts == [4, 1]:
        return "フォーカード"
    if rank_counts == [3, 2]:
        return "フルハウス"
    if is_flush:
        return "フラッシュ"
    if is_straight:
        return "ストレート"
    if rank_counts == [3, 1, 1]:
        return "スリーカード"
    if rank_counts == [2, 2, 1]:
        return "ツーペア"
    if rank_counts == [2, 1, 1, 1]:
        return "ワンペア"
    return "ハイカード"


def _is_straight(ranks: list[int]) -> bool:
    """ソート済みランクが連続する5枚かどうかを判定する。"""
    if len(set(ranks)) != 5:
        return False
    # 通常のストレート: 最大 - 最小 == 4
    if ranks[-1] - ranks[0] == 4:
        return True
    # A-high ストレート: A(1), 10, J, Q, K
    return ranks == [Rank.ACE, Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING]
