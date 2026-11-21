# captions/

2026-09-14のスコープ変更以降の出力先。各ファイルは `schema/caption_brief.schema.json` 準拠で、
リサーチ結果とIG/TikTokキャプション・ハッシュタグのみを持つ（画像候補・カルーセル構成は含まない）。

ファイル名は `<date>-<slug>.json`。`data/candidates/` の対応する候補（`candidate_id` で参照）と対で管理する。

新規追加時は `python3 scripts/validate.py` で必須項目チェックを通してからコミットすること。
