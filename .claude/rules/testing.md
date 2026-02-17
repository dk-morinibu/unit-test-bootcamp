---
description: テストコードを書くとき
globs: tests/**/*.py
---

- テスト関数名は `test_<日本語の仕様>` とし、仕様がわかる名前にする
  - 良い例: `test_5枚のカードのうち2枚が同じランクならワンペア`
  - 悪い例: `test_one_pair`, `test_case1`
- テストは Arrange-Act-Assert パターンで書く
- 型アノテーションを必ず付ける
- テストファイルは `tests/test_*.py` の命名規則に従う
