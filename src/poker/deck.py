import random

from poker.card import Card, Rank, Suit


class Deck:
    def __init__(self) -> None:
        self._cards = [Card(suit=s, rank=r) for s in Suit for r in Rank]
        random.shuffle(self._cards)

    def deal(self, num: int = 5) -> list[Card]:
        return [self._cards.pop() for _ in range(num)]
