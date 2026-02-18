from poker.deck import Deck
from poker.evaluator import evaluate_hand


def play() -> str:
    deck = Deck()
    player_a_hand = deck.deal(5)
    player_b_hand = deck.deal(5)

    player_a_rank = evaluate_hand(player_a_hand)
    player_b_rank = evaluate_hand(player_b_hand)

    if player_a_rank > player_b_rank:
        return "プレイヤーAの勝ち"
    elif player_a_rank < player_b_rank:
        return "プレイヤーBの勝ち"
    else:
        return "引き分け"
