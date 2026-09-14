# CLAUDE.md

このリポジトリで作業するエージェントは、以下を必ず踏まえること。

## このリポジトリの役割

「Luxury Travel Influencer Autopilot」— 旅行リサーチャーとして、少し贅沢な旅の候補を自分でWeb調査・
評価・ファクトチェックし、キャプション（文章）を制作するリサーチ＆ライティングパイプライン。完全な運用原則は
[`docs/operating-principles.md`](docs/operating-principles.md) にある。要点：

- 場所をユーザーに聞き返さず、自分でWeb調査から開始する（自律探索モード）。
- 候補は100点満点で採点し、75点未満・主要レビュー4.0未満は原則不採用。
- 実際に訪問していないことを前提に、実体験を捏造した文章を書かない。
- 地域・カテゴリの連続を避ける（`captions/` と `posts/` の直近投稿を必ず確認する）。

> **スコープについて（2026-09-14〜）**: 投稿画像の構成（カルーセル・スライド設計・`image_candidates`）は
> 作らない。カメラマン／デザイン側の工程はこのリポジトリの担当外。ここでやるのは
> **①ホテル・観光施設のリサーチ＆採点 → ②キャプション（IG/TikTok文章）の執筆** まで。
> `posts/` 以下の既存3件（カルーセル付き）は過去の成果物としてそのまま残すが、新規には作らない。

## 「次の情報収集をして」「次のキャプションを作って」と言われたら（通常の依頼／定期実行 共通）

1. `docs/operating-principles.md` を読み、`captions/` と `posts/` の直近エントリ（地域・カテゴリ）を確認する。
2. WebSearch/WebFetchで最低3件の候補をリサーチし、`data/candidates/<date>-<theme>.json` に
   `schema/candidate.schema.json` 準拠で記録する（不採用も理由付きで残す）。
3. BEST候補を1件選び、`captions/<date>-<slug>.json` に `schema/caption_brief.schema.json` 準拠で
   施設概要・推薦理由・評価根拠・ターゲット・IG/TikTokキャプション・ハッシュタグ・ソースを記録する。
   カルーセル構成・画像候補（`carousel`, `image_candidates`）は**作らない**。
4. `python3 scripts/validate.py` で必須項目チェックを実行する。
5. コミットし、リモートにpushする（既存のPRブランチがあればそこに積む）。

## 制約

- このセッションのネットワーク環境では、多くの旅行系ドメイン（じゃらん・一休・公式ホテルサイト等）への
  WebFetchが `EGRESS_BLOCKED` になることがある。その場合はWebSearchのスニペットから得られる情報を情報源として
  明記し、画像の著作権確認ができない場合は正直に `NEEDS_ASSET_APPROVAL` にする（存在しない許諾を捏造しない）。
- SNS自動投稿ツール（Metricool等）は現時点で未接続。投稿は `READY`/`SCHEDULED` までを作り、
  Publishing Queueに保持する。
