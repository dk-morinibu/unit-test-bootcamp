from poker.card import Card, Rank, Suit
from poker.evaluator import evaluate_hand


def _hand(specs: list[tuple[Suit, Rank]]) -> list[Card]:
    """テスト用ヘルパー: (Suit, Rank) のリストから手札を生成する。"""
    return [Card(suit=s, rank=r) for s, r in specs]


# === スリーセブン ===


class Test_スリーセブン:
    def test_7が3枚あればスリーセブン(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.DIAMONDS, Rank.SEVEN),
                (Suit.CLUBS, Rank.TWO),
                (Suit.SPADES, Rank.FOUR),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーセブン"

    def test_7が4枚あればスリーセブンではなくフォーカード(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.DIAMONDS, Rank.SEVEN),
                (Suit.CLUBS, Rank.SEVEN),
                (Suit.SPADES, Rank.TWO),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フォーカード"

    def test_7が2枚ではスリーセブンにならない(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.DIAMONDS, Rank.THREE),
                (Suit.CLUBS, Rank.TWO),
                (Suit.SPADES, Rank.FOUR),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result != "スリーセブン"

    def test_7が3枚でフルハウスの形でもスリーセブンが優先(self) -> None:
        # Arrange: [7,7,7,K,K,K] -> スリーセブンが最強なのでスリーセブン
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.DIAMONDS, Rank.SEVEN),
                (Suit.CLUBS, Rank.KING),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーセブン"


# === ストレートフラッシュ ===


class Test_ストレートフラッシュ:
    def test_6枚全て同スートかつ連番ならストレートフラッシュ(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.HEARTS, Rank.THREE),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.HEARTS, Rank.FIVE),
                (Suit.HEARTS, Rank.SIX),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.HEARTS, Rank.EIGHT),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレートフラッシュ"

    def test_Ahighストレートフラッシュ(self) -> None:
        # Arrange: A,9,10,J,Q,K 全て同スート
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.ACE),
                (Suit.SPADES, Rank.NINE),
                (Suit.SPADES, Rank.TEN),
                (Suit.SPADES, Rank.JACK),
                (Suit.SPADES, Rank.QUEEN),
                (Suit.SPADES, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレートフラッシュ"


# === フォーカード ===


class Test_フォーカード:
    def test_同ランク4枚と異なる2枚ならフォーカード(self) -> None:
        # Arrange: [4,4,4,4,2,9] -> rank_counts [4,1,1]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.FOUR),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.FOUR),
                (Suit.CLUBS, Rank.FOUR),
                (Suit.SPADES, Rank.TWO),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フォーカード"

    def test_同ランク4枚とペア1組でもフォーカード(self) -> None:
        # Arrange: [4,4,4,4,9,9] -> rank_counts [4,2]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.FOUR),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.FOUR),
                (Suit.CLUBS, Rank.FOUR),
                (Suit.SPADES, Rank.NINE),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フォーカード"


# === フルハウス ===


class Test_フルハウス:
    def test_スリーカードとペアでフルハウス(self) -> None:
        # Arrange: [3,3,3,K,K,2] -> rank_counts [3,2,1]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.THREE),
                (Suit.DIAMONDS, Rank.THREE),
                (Suit.CLUBS, Rank.KING),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.TWO),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フルハウス"

    def test_スリーカード2組でもフルハウス(self) -> None:
        # Arrange: [3,3,3,K,K,K] -> rank_counts [3,3]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.THREE),
                (Suit.DIAMONDS, Rank.THREE),
                (Suit.CLUBS, Rank.KING),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フルハウス"


# === フラッシュ ===


class Test_フラッシュ:
    def test_6枚全て同スートで連番でなければフラッシュ(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.DIAMONDS, Rank.TWO),
                (Suit.DIAMONDS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.SIX),
                (Suit.DIAMONDS, Rank.EIGHT),
                (Suit.DIAMONDS, Rank.TEN),
                (Suit.DIAMONDS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フラッシュ"

    def test_5枚同スートで1枚異なればフラッシュにならない(self) -> None:
        # Arrange
        hand: list[Card] = _hand(
            [
                (Suit.DIAMONDS, Rank.TWO),
                (Suit.DIAMONDS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.SIX),
                (Suit.DIAMONDS, Rank.EIGHT),
                (Suit.DIAMONDS, Rank.TEN),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result != "フラッシュ"


# === ストレート ===


class Test_ストレート:
    def test_6枚連番で異なるスートならストレート(self) -> None:
        # Arrange: 3,4,5,6,7,8 異なるスート
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.FIVE),
                (Suit.CLUBS, Rank.SIX),
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.EIGHT),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレート"

    def test_Alowストレート_A2345_6(self) -> None:
        # Arrange: A,2,3,4,5,6
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.ACE),
                (Suit.HEARTS, Rank.TWO),
                (Suit.DIAMONDS, Rank.THREE),
                (Suit.CLUBS, Rank.FOUR),
                (Suit.SPADES, Rank.FIVE),
                (Suit.HEARTS, Rank.SIX),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレート"

    def test_Ahighストレート_A_9_10_J_Q_K(self) -> None:
        # Arrange: A,9,10,J,Q,K 異なるスート
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.ACE),
                (Suit.HEARTS, Rank.NINE),
                (Suit.DIAMONDS, Rank.TEN),
                (Suit.CLUBS, Rank.JACK),
                (Suit.SPADES, Rank.QUEEN),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレート"

    def test_5枚だけ連番で1枚飛んでいればストレートにならない(self) -> None:
        # Arrange: 3,4,5,6,7,10 (5枚連番だが6枚ではない)
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.FIVE),
                (Suit.CLUBS, Rank.SIX),
                (Suit.SPADES, Rank.SEVEN),
                (Suit.HEARTS, Rank.TEN),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result != "ストレート"


# === スリーペア ===


class Test_スリーペア:
    def test_ペア3組ならスリーペア(self) -> None:
        # Arrange: [2,2,5,5,K,K] -> rank_counts [2,2,2]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.TWO),
                (Suit.HEARTS, Rank.TWO),
                (Suit.DIAMONDS, Rank.FIVE),
                (Suit.CLUBS, Rank.FIVE),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーペア"


# === スリーカード ===


class Test_スリーカード:
    def test_同ランク3枚と異なる3枚ならスリーカード(self) -> None:
        # Arrange: [J,J,J,2,5,9] -> rank_counts [3,1,1,1]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.JACK),
                (Suit.HEARTS, Rank.JACK),
                (Suit.DIAMONDS, Rank.JACK),
                (Suit.CLUBS, Rank.TWO),
                (Suit.SPADES, Rank.FIVE),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーカード"


# === ツーペア ===


class Test_ツーペア:
    def test_ペア2組と異なる2枚ならツーペア(self) -> None:
        # Arrange: [3,3,9,9,K,2] -> rank_counts [2,2,1,1]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.THREE),
                (Suit.DIAMONDS, Rank.NINE),
                (Suit.CLUBS, Rank.NINE),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.TWO),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ツーペア"


# === ワンペア ===


class Test_ワンペア:
    def test_ペア1組と異なる4枚ならワンペア(self) -> None:
        # Arrange: [Q,Q,2,5,8,K] -> rank_counts [2,1,1,1,1]
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.QUEEN),
                (Suit.HEARTS, Rank.QUEEN),
                (Suit.DIAMONDS, Rank.TWO),
                (Suit.CLUBS, Rank.FIVE),
                (Suit.SPADES, Rank.EIGHT),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ワンペア"


# === ハイカード ===


class Test_ハイカード:
    def test_どの役にも該当しなければハイカード(self) -> None:
        # Arrange: [2,4,6,8,10,K] 異なるスート混在、連番でない
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.TWO),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.SIX),
                (Suit.CLUBS, Rank.EIGHT),
                (Suit.SPADES, Rank.TEN),
                (Suit.HEARTS, Rank.KING),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ハイカード"


# === 境界ケース・誤判定の検出 ===


class Test_境界ケース:
    def test_7を含むストレートはスリーセブンにならない(self) -> None:
        # Arrange: [5,6,7,8,9,10] 7が1枚だけ -> ストレート
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.FIVE),
                (Suit.HEARTS, Rank.SIX),
                (Suit.DIAMONDS, Rank.SEVEN),
                (Suit.CLUBS, Rank.EIGHT),
                (Suit.SPADES, Rank.NINE),
                (Suit.HEARTS, Rank.TEN),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレート"

    def test_スリーカードとペア1組はフルハウスでスリーペアではない(self) -> None:
        # Arrange: [3,3,3,K,K,2] -> rank_counts [3,2,1] -> フルハウス
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.THREE),
                (Suit.HEARTS, Rank.THREE),
                (Suit.DIAMONDS, Rank.THREE),
                (Suit.CLUBS, Rank.KING),
                (Suit.SPADES, Rank.KING),
                (Suit.HEARTS, Rank.TWO),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フルハウス"
        assert result != "スリーペア"

    def test_スリーカードのみでフルハウスにならない(self) -> None:
        # Arrange: [J,J,J,2,5,9] -> rank_counts [3,1,1,1] -> スリーカード
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.JACK),
                (Suit.HEARTS, Rank.JACK),
                (Suit.DIAMONDS, Rank.JACK),
                (Suit.CLUBS, Rank.TWO),
                (Suit.SPADES, Rank.FIVE),
                (Suit.HEARTS, Rank.NINE),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーカード"
        assert result != "フルハウス"

    def test_ストレートフラッシュに含まれる7はスリーセブンにならない(self) -> None:
        # Arrange: [♥5,♥6,♥7,♥8,♥9,♥10] -> 7は1枚 -> ストレートフラッシュ
        hand: list[Card] = _hand(
            [
                (Suit.HEARTS, Rank.FIVE),
                (Suit.HEARTS, Rank.SIX),
                (Suit.HEARTS, Rank.SEVEN),
                (Suit.HEARTS, Rank.EIGHT),
                (Suit.HEARTS, Rank.NINE),
                (Suit.HEARTS, Rank.TEN),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "ストレートフラッシュ"

    def test_スリーペアがツーペアに誤判定されない(self) -> None:
        # Arrange: [4,4,8,8,Q,Q] -> rank_counts [2,2,2] -> スリーペア
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.FOUR),
                (Suit.HEARTS, Rank.FOUR),
                (Suit.DIAMONDS, Rank.EIGHT),
                (Suit.CLUBS, Rank.EIGHT),
                (Suit.SPADES, Rank.QUEEN),
                (Suit.HEARTS, Rank.QUEEN),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "スリーペア"
        assert result != "ツーペア"

    def test_フルハウス33パターンがスリーカードに誤判定されない(self) -> None:
        # Arrange: [5,5,5,Q,Q,Q] -> rank_counts [3,3] -> フルハウス
        hand: list[Card] = _hand(
            [
                (Suit.SPADES, Rank.FIVE),
                (Suit.HEARTS, Rank.FIVE),
                (Suit.DIAMONDS, Rank.FIVE),
                (Suit.CLUBS, Rank.QUEEN),
                (Suit.SPADES, Rank.QUEEN),
                (Suit.HEARTS, Rank.QUEEN),
            ]
        )
        # Act
        result: str = evaluate_hand(hand)
        # Assert
        assert result == "フルハウス"
        assert result != "スリーカード"
