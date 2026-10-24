# Analytics / 学習ログ

投稿が実際にSNSへ配信された後、可能な範囲で以下の指標を `results/<post_id>.json` に記録する（原則26）。

- 閲覧数 / リーチ
- 保存数・保存率
- シェア
- コメント
- いいね
- プロフィール訪問
- フォロー増加
- リンククリック

## record.schema.json（記録フォーマットの目安）

```json
{
  "post_id": "2026-09-14-hotel-gyokusen",
  "posted_date": "2026-09-17",
  "metrics": {
    "views": null,
    "reach": null,
    "saves": null,
    "save_rate": null,
    "shares": null,
    "comments": null,
    "likes": null,
    "profile_visits": null,
    "new_follows": null,
    "link_clicks": null
  },
  "learnings": "伸びた/伸びなかった要因（地域・価格帯・写真・表紙コピー・投稿枚数・投稿時間・季節）の分析メモ",
  "applied_to_next_cycle": "次回の候補選定基準にどう反映したか"
}
```

投稿実績がまだないため、このディレクトリには現時点で `results/` は存在しない。最初の投稿が `POSTED` になった時点で
このフォーマットに沿ってファイルを追加すること。
