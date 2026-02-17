# CLAUDE.md

## プロジェクト概要

ポーカーの役判定を題材にした単体テストBootcamp。参加者が `evaluate_hand()` の実装とテストを書く。

## 技術スタック

- Python 3.13 / uv / Pydantic
- テスト: pytest
- lint/format: ruff
- 型チェック: pyright
- git hooks: pre-commit

## コマンド

```bash
uv sync                          # 依存インストール
uv run pytest                    # テスト実行
uv run ruff check . --fix        # lint
uv run ruff format .             # format
uv run pyright                   # 型チェック
uv run pre-commit run --all-files # 全フック実行
```

## プロジェクト構成

```
src/poker/          # プロダクションコード
  card.py           # Suit(IntEnum), Rank(IntEnum), Card(BaseModel, frozen)
  deck.py           # Deck: 52枚生成・シャッフル・配布
  evaluator.py      # evaluate_hand(): 参加者が実装する役判定
  game.py           # play(): デッキ→配布→役判定の流れ
tests/              # テストコード
```

## ルール

- 言語は日本語で応答する
- コードのコメント・docstringは日本語可
- テストファイルは `tests/test_*.py` の命名規則に従う
- テスト関数名は `test_<日本語の仕様>` とし、仕様がわかる名前にする
  - 良い例: `test_5枚のカードのうち2枚が同じランクならワンペア`
  - 悪い例: `test_one_pair`, `test_case1`
- 型アノテーションを必ず付ける
- `uv run` 経由でツールを実行する（直接 `pytest` や `ruff` を呼ばない）
- テストは `Arrange-Act-Assert` パターンで書く
- 既存の `Card`, `Suit`, `Rank` の定義は変更しない
- `evaluate_hand()` の戻り値の型は実装者が決める
