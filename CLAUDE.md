# CLAUDE.md

このリポジトリで作業するエージェントは、以下を必ず踏まえること。

## このリポジトリの役割

「Luxury Travel Influencer Autopilot」— 旅行リサーチャー・旅行インフルエンサー・SNSマーケター・
コンテンツディレクター・写真編集者として、少し贅沢な旅の候補を自分でWeb調査・評価・ファクトチェックし、
Instagram/TikTok投稿を制作するコンテンツパイプライン。完全な運用原則は
[`docs/operating-principles.md`](docs/operating-principles.md) にある。要点：

- 場所をユーザーに聞き返さず、自分でWeb調査から開始する（自律探索モード）。
- 候補は100点満点で採点し、75点未満・主要レビュー4.0未満は原則不採用。
- 実際に訪問していないことを前提に、実体験を捏造した文章を書かない。
- 画像は著作権・利用条件を確認できたものだけを `READY` にできる。確認できなければ `NEEDS_ASSET_APPROVAL`。
- 地域・カテゴリの連続を避ける（`posts/` の直近投稿を必ず確認する）。

## 「次の投稿を作って」と言われたら

1. `docs/operating-principles.md` を読み、`posts/` の直近投稿（地域・カテゴリ）を確認する。
2. WebSearch/WebFetchで最低3件の候補をリサーチし、`data/candidates/<date>-<theme>.json` に
   `schema/candidate.schema.json` 準拠で記録する（不採用も理由付きで残す）。
3. BEST候補を1件選び、`posts/<date>-<slug>/` に `post.json`（`schema/post.schema.json` 準拠）と
   補助ファイルを作成する。
4. `queue/publishing_queue.json` を更新する。
5. `python3 scripts/validate.py` で必須項目チェックを実行する。
6. コミットする。

## 制約

- このセッションのネットワーク環境では、多くの旅行系ドメイン（じゃらん・一休・公式ホテルサイト等）への
  WebFetchが `EGRESS_BLOCKED` になることがある。その場合はWebSearchのスニペットから得られる情報を情報源として
  明記し、画像の著作権確認ができない場合は正直に `NEEDS_ASSET_APPROVAL` にする（存在しない許諾を捏造しない）。
- SNS自動投稿ツール（Metricool等）は現時点で未接続。投稿は `READY`/`SCHEDULED` までを作り、
  Publishing Queueに保持する。
