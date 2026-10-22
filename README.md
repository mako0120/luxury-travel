# Luxury Travel / 旅ログ AI Production OS

「まだ知られていない良い場所を、写真を主役に、正確で上品なPRとして届ける」ための旅行メディア運用リポジトリです。

このリポジトリは **GitHubを運用ルールの正本（Single Source of Truth）** とし、
Claude / ChatGPT / Gemini Pro / Notion / Canva / Google Drive の役割を分離して、
リサーチから投稿制作・QAまで同じ基準で継続できるようにします。

## 最上位の制作思想

- 映えのために場所を誇張しない。
- 写真を派手にデザインしすぎず、その場所そのものの空気感を伝える。
- 有名かどうかに関係なく、良さが十分知られていない場所を発見し、幅広く紹介する。
- 「どんな場所か」「何が良いか」「何ができるか」「どう行くか」「行く前に何を知るべきか」が初見でも分かる投稿にする。
- PRとして魅力はしっかり伝えるが、広告っぽい煽りや実体験の捏造はしない。
- 投稿写真は実写を原則とし、実在施設・観光地をAI生成画像で代替しない。

## 二つのレーン

### A. Discovery / Research レーン

主担当: Claude などの調査エージェント

```
発見 → Web調査 → 評価 → ファクトチェック → キャプション下書き → Notion登録
```

候補探索では採点を利用してよい。採点は「何を優先して調べるか」を決める編集判断のための指標です。

**重要:** Notion「贅沢旅リサーチ帖」に登録された候補は、その時点で制作対象として承認済みです。
制作レーンではスコアで再採点・再除外しません。

### B. Production / PR レーン

主担当: ChatGPT + Canva  
第二レビュー: Gemini Pro（APIなし）

```
Notion取得
→ 最新Web再確認
→ ユーザー写真 / 利用可能な公式実写素材の確認
→ Gemini Proで写真・情報を第二レビュー
→ ChatGPTが投稿構成を確定
→ Canva MASTERで5ページ制作
→ Gemini Proで完成稿を客観QA
→ ChatGPT最終QA
→ Canva保存
→ Notion制作状況更新
```

## ツールの役割

| ツール | 役割 |
|---|---|
| GitHub | ルール・プロンプト・テンプレートの正本 |
| Claude | 自律的な候補発見、初期調査、評価、Notion登録用情報 |
| Notion | 候補キュー、制作進捗、キャプション、運用状態 |
| ChatGPT | 制作司令塔、最新確認、文章決定、Canva制作、最終QA |
| Gemini Pro | APIなしの第二AI。Deep Research、写真評価、完成稿QA |
| Canva | Instagram 4:5 / 5ページの最終デザイン |
| Google Drive | Gemini Proとの画像・PDF受け渡し、監査資料の保管 |

## 必ず読むファイル

- [docs/operating-principles.md](docs/operating-principles.md) — 全体原則
- [docs/production-os.md](docs/production-os.md) — 投稿制作の正式フロー
- [docs/canva-rules.md](docs/canva-rules.md) — Canva制作規則
- [docs/gemini-pro-workflow.md](docs/gemini-pro-workflow.md) — APIなしGemini Pro連携
- [docs/workflow.md](docs/workflow.md) — 状態遷移
- [GEMINI.md](GEMINI.md) — Gemini Proが最初に読む入口
- [CLAUDE.md](CLAUDE.md) — Claudeが最初に読む入口

## 既存データ

既存の `data/candidates/` と `captions/` はDiscoveryレーンの成果物として継続利用します。
`posts/` の過去成果物も履歴として残します。

過去の「このリポジトリでは画像制作をしない」という制約は廃止ではなく、
**ClaudeのDiscoveryレーンには残し、Productionレーンを別工程として追加**しました。

## 検証

既存JSONデータの検証:

```bash
python3 scripts/validate.py
```

制作時の視覚QAは [docs/canva-rules.md](docs/canva-rules.md) のチェックリストを使用します。
