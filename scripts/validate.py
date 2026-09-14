#!/usr/bin/env python3
"""Dependency-free structural validation for candidate/post JSON files.

Checks required fields and a few business rules from docs/operating-principles.md
(minimum score threshold, minimum source count, valid status values). This is not
a full JSON Schema validator; schema/*.json remain the authoritative reference.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_STATUSES = {
    "RESEARCHING", "DRAFT", "FACT_CHECKED", "ASSET_CHECKED", "READY",
    "SCHEDULED", "POSTED", "NEEDS_REVIEW", "NEEDS_ASSET_APPROVAL", "FAILED",
}

CANDIDATE_REQUIRED = [
    "id", "name", "region", "category", "review_scores", "price_range_jpy",
    "unique_experience", "target_audience", "score", "score_breakdown",
    "recommendation_reason", "sources", "negative_review_check", "decision",
]

POST_REQUIRED = [
    "id", "candidate_id", "status", "status_history", "facility_overview",
    "recommendation_reasons", "evaluation_basis", "target_audience",
    "image_candidates", "carousel", "captions", "hashtags", "schedule",
    "sources", "created_date", "region", "category",
]


def err(errors, path, msg):
    errors.append(f"{path}: {msg}")


def validate_candidate_file(path):
    errors = []
    data = json.loads(path.read_text())
    candidates = data.get("candidates", [])
    if not candidates:
        err(errors, path, "candidates配列が空です")
    for c in candidates:
        cid = c.get("id", "<no id>")
        for field in CANDIDATE_REQUIRED:
            if field not in c:
                err(errors, path, f"[{cid}] 必須項目 '{field}' がありません")
        if "sources" in c and len(c["sources"]) < 2:
            err(errors, path, f"[{cid}] sourcesは2件以上必要です（原則7）")
        if "score" in c and c.get("decision") == "selected" and c["score"] < 75:
            err(errors, path, f"[{cid}] selectedなのにscore({c['score']})が75未満です（原則6）")
        if "decision" in c and c["decision"] not in {"selected", "shortlisted", "rejected"}:
            err(errors, path, f"[{cid}] decisionの値が不正です: {c['decision']}")
    return errors


def validate_post_file(path):
    errors = []
    data = json.loads(path.read_text())
    pid = data.get("id", "<no id>")
    for field in POST_REQUIRED:
        if field not in data:
            err(errors, path, f"[{pid}] 必須項目 '{field}' がありません")
    status = data.get("status")
    if status and status not in VALID_STATUSES:
        err(errors, path, f"[{pid}] statusの値が不正です: {status}")
    if status in {"READY", "SCHEDULED", "POSTED"}:
        for img in data.get("image_candidates", []):
            if img.get("rights_status") == "unconfirmed_needs_approval":
                err(
                    errors, path,
                    f"[{pid}] status={status} だが権利未確認の画像が含まれています（原則12）: "
                    f"{img.get('description')}",
                )
    if len(data.get("sources", [])) < 2:
        err(errors, path, f"[{pid}] sourcesは2件以上必要です（原則7）")
    return errors


def main():
    all_errors = []
    for path in sorted((ROOT / "data" / "candidates").glob("*.json")):
        all_errors.extend(validate_candidate_file(path))
    for path in sorted((ROOT / "posts").glob("*/post.json")):
        all_errors.extend(validate_post_file(path))

    if all_errors:
        print(f"NG: {len(all_errors)}件の問題が見つかりました\n")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)

    print("OK: すべての候補・投稿データが必須項目を満たしています")


if __name__ == "__main__":
    main()
