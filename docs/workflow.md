# 旅ログ AI Production OS｜ワークフロー

## 全体

```
Discovery
  ↓
Notion登録
  ↓
Production
  ↓
QA
  ↓
Canva保存
  ↓
投稿管理
```

## A. Discoveryレーン

```
RESEARCHING
  ↓
EVALUATED
  ↓
FACT_CHECKED
  ↓
CAPTION_READY
  ↓
REGISTERED_TO_NOTION
```

### ルール

- 候補探索時のみ採点を利用する。
- 不採用候補も理由を残す。
- Notion「贅沢旅リサーチ帖」に登録した時点でProduction対象となる。

## B. Productionレーン

```
QUEUED
  ↓
WEB_RECHECK
  ↓
PHOTO_REVIEW
  ↓
CANVA_BUILDING
  ↓
QA
  ↓
SAVED
```

### QUEUED
Notionに登録済みで、まだCanva制作されていない。

### WEB_RECHECK
正式名称、営業状況、価格、時間、アクセス、最新のお知らせを再確認。

### PHOTO_REVIEW
ユーザー提供写真と利用可能な公式実写素材を整理。
必要に応じてGemini Proで表紙向き度やページ割りを第二レビュー。

### CANVA_BUILDING
既存MASTERを使って5ページ制作。

### QA
ChatGPTの最終確認に加え、可能ならGemini Proへ完成PDFを渡して別視点で確認。

### SAVED
Canva保存・専用フォルダ整理・Notion更新まで完了。

## エラー系

- `NEEDS_FACT_REVIEW` — 公式情報に矛盾・不明点
- `NEEDS_ASSET_PERMISSION` — 写真利用条件が確認できない
- `CANVA_ERROR` — Canva編集に失敗
- `QA_FAILED` — 誤字、レイアウト、写真不一致等
- `PAUSED` — 施設休業等で制作保留

## 最重要ルール

**Production対象をスコアで除外しない。**

Notion登録後に中止できるのは、
営業終了・安全上の問題・事実確認不能・権利問題など
「投稿を作るべきではない新しい事実」が判明した場合のみ。

その場合は理由を明記して保留する。
