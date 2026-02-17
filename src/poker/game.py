from poker.deck import Deck
from poker.evaluator import evaluate_hand


def play() -> str:
    deck = Deck()
    hand = deck.deal(5)
    result = evaluate_hand(hand)
    return result
