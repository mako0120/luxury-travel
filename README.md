# Luxury Travel Influencer Autopilot

「少し贅沢だけれど、旅行するならぜひ行ってみたい」宿・体験を、自分でリサーチ・評価・ファクトチェックし、
Instagram / TikTok 投稿として制作するためのコンテンツパイプラインです。

このリポジトリはSNSに自動投稿する仕組みそのものではありません（対応連携先が未接続のため）。
`RESEARCHING → ... → READY` まで**投稿可能な状態に仕上げて Publishing Queue に積む**ところまでを自動化し、
実際の配信は Metricool 等の投稿ツールが接続され次第つなぎ込む前提の構成です。

## 運用フロー

```
発見 → 評価 → ファクトチェック → 画像探索 → 投稿企画 → 投稿画像構成 → キャプション → 投稿 → 分析 → 改善
```

詳細な運用原則（採点基準・ファクトチェックルール・著作権ルール・トーン方針など）は
[`docs/operating-principles.md`](docs/operating-principles.md) を参照してください。
Claude Code などのエージェントがこのリポジトリで作業する際は [`CLAUDE.md`](CLAUDE.md) を読み込むことで
同じペルソナ・同じルールで次サイクルを継続できます。

## ディレクトリ構成

| パス | 内容 |
|---|---|
| `docs/` | 運用原則・採点基準・ステータス管理・画像/著作権ルールのドキュメント |
| `schema/` | 候補データ／投稿データの構造定義（JSON Schema） |
| `data/candidates/` | サイクルごとの候補リサーチ結果（採点・却下理由つき） |
| `posts/` | 候補から選ばれたBEST候補ごとの投稿制作物一式 |
| `queue/publishing_queue.json` | 投稿ステータス管理（Publishing Queue） |
| `analytics/` | 投稿後のパフォーマンス記録と学習ログ |
| `scripts/validate.py` | 候補・投稿データがスキーマの必須項目を満たしているかの簡易チェック |

## 新しいサイクルの回し方（エージェント向け）

1. `docs/operating-principles.md` の候補選定基準・除外基準に沿って、Web上で3件以上の候補をリサーチする。
2. `data/candidates/<date>-<theme>.json` に `schema/candidate.schema.json` の形式で採点結果を記録する（不採用理由も残す）。
3. 直近の `posts/` を確認し、地域・カテゴリが連続しないように重複防止ルール（原則29）を適用してBEST候補を1つ選ぶ。
4. `posts/<date>-<slug>/` を作成し、`post.json`（構造化データ）＋ `README.md`（人間レビュー用の要約）を作成する。
5. 画像の転載権限が確認できない場合は `status` を `NEEDS_ASSET_APPROVAL` のまま止め、`READY` にしない。
6. `queue/publishing_queue.json` にエントリを追加・更新する。
7. `python3 scripts/validate.py` で必須項目の欠落がないか確認する。
8. 投稿後は `analytics/` にパフォーマンスを記録し、学習結果を次回の候補選定基準に反映する。

## 検証

```bash
python3 scripts/validate.py
```

依存パッケージなしで `data/candidates/*.json` と `posts/*/post.json` の必須項目・型・ステータス遷移の妥当性をチェックします。
