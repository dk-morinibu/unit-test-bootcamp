# unit-test-bootcamp
単体テストを理解してAI開発効率化をする

## 1. Setup

#### 準備

- **Git** 2.x 以上
- **uv** 0.10 以上

> Python 3.13 は `uv sync` 時に自動でインストールされるため、手動インストールは不要です。

#### uv のインストール

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### セットアップ

```bash
git clone <repo-url>
cd unit-test-bootcamp
uv sync
uv run pre-commit install
```

#### 動作確認

```bash
uv run pytest
uv run ruff check .
uv run pyright
```

## 2. 検証の自動化

このリポジトリでは **commit するだけ** で自動的に以下が実行されます（pre-commit hooks）。

| チェック | ツール | 内容 |
|---------|--------|------|
| lint | ruff | コードの問題検出・自動修正 |
| format | ruff | コードフォーマット |
| 型チェック | pyright | 静的型解析 |
| テスト | pytest | 単体テストの実行 |

手動で全チェックを実行する場合:

```bash
uv run pre-commit run --all-files
```

#### AI駆動開発での活用

- Claude Code などのAIツールでも、プロンプトや検証ルールに pytest を組み込んでおくと、生成コードの品質を担保できる
- このリポジトリでは `.claude/rules/` にテスト命名規則などのルールを定義済み

#### CI での実行

ローカルの pre-commit hooks はスキップできてしまうため、**CI（GitHub Actions 等）でも同じチェックを必ず実行する**こと。

## 3. Tips

#### IntEnum の使い方

`Suit` と `Rank` は `IntEnum` を継承しています。普通の `Enum` と違い、**整数として比較・演算ができます**。

#### 数値として比較できる

```python
Rank.ACE < Rank.KING   # True (1 < 13)
Rank.TEN == 10          # True
Rank.QUEEN > Rank.JACK  # True (12 > 11)
```

#### 名前と値の取得

```python
Rank.ACE.name   # "ACE"（文字列）
Rank.ACE.value  # 1（整数）
Suit.SPADES.name   # "SPADES"
Suit.SPADES.value  # 1
```

#### ループで全メンバーを取得できる

```python
list(Suit)  # [Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS]
list(Rank)  # [Rank.ACE, Rank.TWO, ..., Rank.KING]
```

#### 集計に使える

```python
from collections import Counter

ranks = [card.rank for card in hand]
Counter(ranks)  # Counter({Rank.ACE: 2, Rank.TEN: 1, Rank.FIVE: 1, Rank.KING: 1})
```

#### Card について

`Card` は Pydantic の `BaseModel`（`frozen=True`）です。

```python
card = Card(suit=Suit.SPADES, rank=Rank.ACE)
card.suit   # Suit.SPADES
card.rank   # Rank.ACE
str(card)   # "ACE of SPADES"
```

- `frozen=True` なのでカードの値は変更不可（イミュータブル）
- `set()` に入れたり、重複チェックに使える

### Poker
[Rule](https://light-three.com/pokerroom-recommend/)

### ゲームの実行

```bash
uv run python -m poker
```