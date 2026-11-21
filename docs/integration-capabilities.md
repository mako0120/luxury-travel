# 旅ログ｜Integration Capability Map

更新: 2026-10-22

## 正本
GitHub `mako0120/luxury-travel` が運用ルールのSingle Source of Truth。

## Canva
現行正式MASTER:
- `旅ログ｜MASTER 7PHOTO｜1ページ1枚`
- design_id: `DAHYun12-UY`
- 1080×1350
- 7ページ
- 写真7枚
- 1ページ1写真
- master folder_id: `FAHYuZnyMZU`

元になったユーザー指定Canva:
- `DAHYuli8hkQ`
- https://canva.link/p6alciswlh8gp9j

完成保存先:
- `ラグジュアリー旅行`
- folder_id: `FAHYuFhOnLM`

制作は必ずMASTERコピーから開始する。

## Notion
### 贅沢旅リサーチ帖
制作候補の正本。
### 旅ログ｜自動制作モニター
制作状態の管理。

## ChatGPT
Production Orchestrator:
- Notionキュー確認
- Web最新確認
- 高品質実写7枚の収集/選定
- 非生成補正
- Canva MASTERコピー
- 7ページ制作
- 視覚QA
- ラグジュアリー旅行へ保存
- Notion更新

## Claude
Discovery担当。候補探索、初期調査、採点、Notion投入。

## Gemini
現在のProductionフローでは使用しない。Gemini待ちで停止しない。

## Automations
- Notion未制作候補検知
- 完成フォルダで重複確認
- 最新公式情報再確認
- 高品質写真7枚確認
- MASTERコピー
- 7ページ制作
- ChatGPT QA
- ラグジュアリー旅行へ保存
- Notion更新

## 安全弁
停止条件:
- 写真権利不明
- 公式情報重大矛盾
- 閉業/長期休止
- 高品質写真7枚を確保できない
- PHOTO INTEGRITY違反疑い
- 視覚QA不合格
