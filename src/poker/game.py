from poker.card import Card
from poker.deck import Deck
from poker.evaluator import HandRank, evaluate_hand, format_hand_rank


def format_hand(hand: list[Card]) -> str:
    return " ".join(str(card) for card in hand)


def format_player_hand(player_name: str, hand: list[Card], hand_rank: HandRank) -> str:
    return f"{player_name}の手札: {format_hand(hand)} ({format_hand_rank(hand_rank)})"


def play() -> str:
    deck = Deck()
    player_a_hand = deck.deal(5)
    player_b_hand = deck.deal(5)

    player_a_rank = evaluate_hand(player_a_hand)
    player_b_rank = evaluate_hand(player_b_hand)

    if player_a_rank > player_b_rank:
        result = "Aの勝ち"
    elif player_a_rank < player_b_rank:
        result = "Bの勝ち"
    else:
        result = "引き分け"

    return "\n".join(
        [
            format_player_hand("A", player_a_hand, player_a_rank),
            format_player_hand("B", player_b_hand, player_b_rank),
            result,
        ]
    )
