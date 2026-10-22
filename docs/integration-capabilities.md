# 旅ログ｜Integration Capability Map

更新: 2026-10-22

このドキュメントは、使える連携・スキルをどこで使うかの正本。

## GitHub

役割:
- 制作思想
- ルール
- Gemini / ChatGPT / Claude用プロンプト
- Canva Autofillフィールド仕様
- 案件Handoff
- 変更履歴

原則:
GitHubが運用ルールのSingle Source of Truth。

## Notion

### 贅沢旅リサーチ帖
Discoveryの候補キュー。

### 旅ログ｜自動制作モニター
Productionの状態管理。

追加済みAI連携フィールド:
- Gemini調査
- Gemini写真
- Gemini QA
- 写真権利
- Drive案件
- GitHub Handoff

追加ビュー:
- AI連携｜Gemini・Canva

Notion登録済み候補をスコアで制作除外しない。

## Canva

MASTER:
`DAHVoXJDBFw`

確認済み:
- 5ページ
- 1080×1350
- Autofill datasetあり

第一制作経路:
`Production Brief → Assets → Autofill → Visual QA → 微修正 → 保存`

これにより毎回テキストボックスや画像枠を手探りで編集しない。

## Google Drive

共有作業場:
`旅ログAI連携`

工程:
- 00_制作ルール
- 01_Gemini調査待ち
- 02_写真選定
- 03_Canva制作中
- 04_Gemini_QA待ち
- 05_完成

Gemini ProをAPIなしで利用するための受け渡しレイヤー。

## Gemini Pro

APIなし。

役割:
- Deep Research
- Photo Review
- Final QA

GitHub `GEMINI.md` を入口にする。
画像生成担当にはしない。

## ChatGPT

制作オーケストレーター。

役割:
- Notionキュー確認
- 最新Web再調査
- GitHubルール確認
- Drive作業フォルダ確認
- Canva dataset確認
- Canva Autofill
- 視覚QA / 微修正
- Canva保存
- Notion更新

## Claude

Discovery担当。

役割:
- 候補探索
- 初期調査
- 採点
- キャプション草案
- Notionへの候補投入

## Web Search

制作直前の変動情報を再確認するために使う。
特に料金・時間・休止・工事・アクセス・季節情報。

## Automations

定期監視に使用する。

理想:
- Notion未制作候補を検知
- Drive上のGemini成果物を検知
- Canva重複確認
- 作れる案件をAutofill制作へ進める
- QA結果とNotionを同期

ただしGemini Pro自体はAPIなしのため、Geminiの画面操作は自動化しない。
Driveに成果物が置かれた後を再開点にする。

## 安全弁

自動停止条件:
- 写真権利不明
- 公式情報の重大な矛盾
- 閉業 / 長期休止
- Canva dataset変更でマッピング不能
- Gemini QA = FAIL
- AI生成の実景混入疑い

自動継続条件:
- ユーザー提供写真
- 最新事実確認済み
- Autofill schema一致
- QA合格
