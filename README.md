# unit-test-bootcamp
単体テストを理解してAI開発効率化をする

## IntEnum の使い方

`Suit` と `Rank` は `IntEnum` を継承しています。普通の `Enum` と違い、**整数として比較・演算ができます**。

### 数値として比較できる

```python
Rank.ACE < Rank.KING   # True (1 < 13)
Rank.TEN == 10          # True
Rank.QUEEN > Rank.JACK  # True (12 > 11)
```

### 名前と値の取得

```python
Rank.ACE.name   # "ACE"（文字列）
Rank.ACE.value  # 1（整数）
Suit.SPADES.name   # "SPADES"
Suit.SPADES.value  # 1
```

### ループで全メンバーを取得できる

```python
list(Suit)  # [Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS]
list(Rank)  # [Rank.ACE, Rank.TWO, ..., Rank.KING]
```

### 集計に使える

```python
from collections import Counter

ranks = [card.rank for card in hand]
Counter(ranks)  # Counter({Rank.ACE: 2, Rank.TEN: 1, Rank.FIVE: 1, Rank.KING: 1})
```

### Card について

`Card` は Pydantic の `BaseModel`（`frozen=True`）です。

```python
card = Card(suit=Suit.SPADES, rank=Rank.ACE)
card.suit   # Suit.SPADES
card.rank   # Rank.ACE
str(card)   # "ACE of SPADES"
```

- `frozen=True` なのでカードの値は変更不可（イミュータブル）
- `set()` に入れたり、重複チェックに使える
