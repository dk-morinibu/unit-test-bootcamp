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


class Card(BaseModel, frozen=True):
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{self.rank.name} of {self.suit.name}"
