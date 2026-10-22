# 旅ログ｜Integration Capability Map

更新: 2026-10-22

## 正本

GitHub `mako0120/luxury-travel` が運用ルールのSingle Source of Truth。

## Canva

現行の第一制作スタイル:
- `docs/canva-full-photo-style-v3.md`
- 1080×1350
- 標準8ページ
- 1ページ1枚の全面写真
- 白い短文
- 写真品質最優先

旧5ページMASTER:
- `DAHVoXJDBFw`
- 互換・旧投稿修正用

V2正式出力:
- `贅沢旅リサーチ帖｜V2再制作`
- folder_id: `FAHYuHEOty4`

## Notion

### 贅沢旅リサーチ帖
制作候補の正本。

### 旅ログ｜自動制作モニター
制作状態の管理。

Gemini関連列は履歴として残してよいが、
現在の制作ゲート・完成条件には使わない。

## ChatGPT

Production Orchestrator。

役割:
- Notionキュー確認
- Web最新確認
- 高品質写真収集 / 選定
- 写真補正方針
- Canva制作
- 視覚QA
- Canva保存
- Notion更新
- キャプション工程への引き継ぎ

## Claude

Discovery担当。

- 候補探索
- 初期調査
- 採点
- Notionへの候補投入

## Gemini

現在はProductionフローから外す。
API・手動Geminiレビューともに必須ではない。

将来必要になれば再度オプションとして利用できるが、
現在のCanva制作はGemini待ちで停止しない。

## Web

制作直前の公式情報再確認に使う。

## Google Drive

V2の資料置き場として利用可能。
Gemini専用の待ち工程は現在使用しない。

## Automations

定期監視:
- Notion未制作候補を検知
- V2 Canva重複確認
- 最新公式情報再確認
- 写真品質を確認
- FULL PHOTO STYLEで制作
- ChatGPT QA
- Canva保存
- Notion更新

## 安全弁

停止条件:
- 写真権利不明
- 公式情報の重大な矛盾
- 閉業 / 長期休止
- 高品質写真を必要枚数確保できない
- AI生成実景・不正確な素材混入疑い
- 視覚QA不合格

継続条件:
- 最新情報確認済み
- 写真権利確認済み
- 高品質写真6〜8枚確保
- Canva QA合格
