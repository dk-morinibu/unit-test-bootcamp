from enum import IntEnum

from pydantic import BaseModel


class Suit(IntEnum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4


class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


SUIT_SYMBOLS = {
    Suit.SPADES: "♠",
    Suit.HEARTS: "♥",
    Suit.DIAMONDS: "♦",
    Suit.CLUBS: "♣",
}

RANK_LABELS = {
    Rank.ACE: "A",
    Rank.TWO: "2",
    Rank.THREE: "3",
    Rank.FOUR: "4",
    Rank.FIVE: "5",
    Rank.SIX: "6",
    Rank.SEVEN: "7",
    Rank.EIGHT: "8",
    Rank.NINE: "9",
    Rank.TEN: "10",
    Rank.JACK: "J",
    Rank.QUEEN: "Q",
    Rank.KING: "K",
}


class Card(BaseModel, frozen=True):
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{SUIT_SYMBOLS[self.suit]}{RANK_LABELS[self.rank]}"
