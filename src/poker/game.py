from poker.card import Card
from poker.deck import Deck
from poker.evaluator import evaluate_hand, hand_rank


def play() -> str:
    """2人のプレイヤーに6枚ずつ配り、勝敗を判定する。"""
    deck = Deck()
    hand1: list[Card] = deck.deal(6)
    hand2: list[Card] = deck.deal(6)

    result1: str = evaluate_hand(hand1)
    result2: str = evaluate_hand(hand2)

    rank1: int = hand_rank(result1)
    rank2: int = hand_rank(result2)

    if rank1 > rank2:
        return f"プレイヤー1の勝ち ({result1} vs {result2})"
    if rank2 > rank1:
        return f"プレイヤー2の勝ち ({result2} vs {result1})"
    return f"引き分け ({result1})"
