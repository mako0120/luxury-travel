# Gemini Pro連携｜APIなし運用

Gemini APIは使用しない。
Gemini Pro / Google AI ProのWebアプリを、人が操作する第二AIとして活用する。

## 1. GitHubとのつなぎ方

GitHub `mako0120/luxury-travel` を制作ルールの正本にする。

Gemini側でGitHubコード / リポジトリのインポートが利用できる場合:
1. Geminiを開く
2. GitHubから `mako0120/luxury-travel` を読み込む
3. 最初に `GEMINI.md` を読むよう指示する
4. `docs/operating-principles.md`, `docs/production-os.md`, `docs/canva-rules.md` を基準にする

重要:
GitHubインポートは常時同期とは限らない。
ルール更新後はGemini側の参照を更新 / 再読み込みする。

## 2. 専用Gem

Geminiに専用Gemを作れる場合、名称:

**旅ログ｜リサーチ＆品質監査**

Gemの基本指示には `GEMINI.md` の内容を使用する。

Geminiは投稿画像の生成担当ではない。
役割は「調べる・見る・比べる・監査する」。

## 3. Google Driveを受け渡し場所にする

推奨フォルダ:

```
旅ログAI連携/
├── 00_制作ルール
├── 01_Gemini調査待ち
├── 02_写真選定
├── 03_Canva制作中
├── 04_Gemini_QA待ち
└── 05_完成
```

1案件の推奨構成:

```
<スポット名>/
├── 01_research.md
├── 02_photos/
├── 03_gemini_review.md
├── 04_production_brief.md
└── 05_canva_qa.pdf
```

写真レビューはGeminiへ画像を直接渡す。
完成QAはCanvaからPDFを書き出し、Geminiへ渡す。

## 4. Geminiの3つの仕事

### A. Research
`prompts/GEMINI_RESEARCH.md`

公式情報を中心に独立再調査する。

### B. Photo Review
`prompts/GEMINI_PHOTO_REVIEW.md`

複数写真を比較し、ページ役割を決める。

### C. Final QA
`prompts/GEMINI_FINAL_QA.md`

Canva完成PDFを第三者視点で監査する。

## 5. 優先順位

矛盾した場合:

1. 最新の公式一次情報
2. GitHubの最新ルール
3. ユーザーの今回の明示指示
4. ChatGPT / Geminiの提案

AIの推測を事実より優先しない。

## 6. Geminiへ任せないこと

- 実在スポット写真の生成
- 権利不明素材を使用可と断定
- Canvaデザインの最終決定
- Notion登録済み候補をスコアで制作除外
- 未確認価格や営業時間の補完
