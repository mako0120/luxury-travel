#!/usr/bin/env python3
"""Dependency-free structural validation for candidate/post JSON files.

Checks required fields and a few business rules from docs/operating-principles.md
(minimum score threshold, minimum source count, valid status values, status-history
transitions, and that a `selected` candidate actually clears every eligibility gate
the rubric requires). This is not a full JSON Schema validator; schema/*.json remain
the authoritative reference.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VALID_STATUSES = {
    "RESEARCHING", "DRAFT", "FACT_CHECKED", "ASSET_CHECKED", "READY",
    "SCHEDULED", "POSTED", "NEEDS_REVIEW", "NEEDS_ASSET_APPROVAL", "FAILED",
}

# The happy-path sequence a post's status_history is expected to accumulate as it
# advances (docs/workflow.md). NEEDS_REVIEW / NEEDS_ASSET_APPROVAL / FAILED are
# off-path exception statuses and are not checked against this sequence.
NORMAL_PATH = ["RESEARCHING", "DRAFT", "FACT_CHECKED", "ASSET_CHECKED", "READY", "SCHEDULED", "POSTED"]

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
        if "decision" in c and c["decision"] not in {"selected", "shortlisted", "rejected"}:
            err(errors, path, f"[{cid}] decisionの値が不正です: {c['decision']}")

        # review_scores entries are meant to be numeric evidence (schema requires
        # score/scale/review_count as number/number/integer). A ranking mention with
        # no numeric value (e.g. "OZmallアワード9位") belongs in recommendation_reason
        # text, not as a null-valued review_scores entry.
        for rs in c.get("review_scores", []):
            if rs.get("score") is None or rs.get("scale") is None or rs.get("review_count") is None:
                err(
                    errors, path,
                    f"[{cid}] review_scoresの要素(source={rs.get('source')})はscore/scale/review_countに"
                    "数値が必要です。数値のない話題性・ランキング言及はrecommendation_reasonに記載してください",
                )

        if c.get("decision") == "selected":
            score = c.get("score")
            if score is not None and score < 75:
                err(errors, path, f"[{cid}] selectedなのにscore({score})が75未満です（原則6）")

            breakdown = c.get("score_breakdown", {})
            numeric_parts = [v for v in breakdown.values() if isinstance(v, (int, float))]
            if breakdown and score is not None:
                total = sum(numeric_parts)
                if abs(total - score) > 0.01:
                    err(
                        errors, path,
                        f"[{cid}] score({score})がscore_breakdownの合計({total})と一致しません",
                    )

            normalized = [
                rs["score"] / rs["scale"] * 5
                for rs in c.get("review_scores", [])
                if isinstance(rs.get("score"), (int, float))
                and isinstance(rs.get("scale"), (int, float))
                and rs["scale"] > 0
            ]
            if not normalized or max(normalized) < 4.0:
                err(
                    errors, path,
                    f"[{cid}] selectedなのに主要レビューサイト評価4.0以上（5点満点換算）を満たす"
                    "review_scoresがありません（原則6）",
                )

            nrc = c.get("negative_review_check", {})
            if not nrc.get("checked") or nrc.get("disqualifying_issues_found"):
                err(
                    errors, path,
                    f"[{cid}] selectedならnegative_review_checkはchecked=trueかつ"
                    "disqualifying_issues_found=falseである必要があります（原則10）",
                )
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

    history = data.get("status_history", [])
    if not history:
        err(errors, path, f"[{pid}] status_historyが空です（原則23）")
    history_statuses = set()
    for h in history:
        hs = h.get("status")
        if hs not in VALID_STATUSES:
            err(errors, path, f"[{pid}] status_history内に不正なstatus: {hs}")
        history_statuses.add(hs)

    if status in NORMAL_PATH:
        idx = NORMAL_PATH.index(status)
        required_prior = set(NORMAL_PATH[1:idx + 1])  # DRAFT..status, RESEARCHING excluded
        missing = required_prior - history_statuses
        if missing:
            err(
                errors, path,
                f"[{pid}] status={status} だがstatus_historyに必須の遷移"
                f"{sorted(missing)}が記録されていません（原則23）",
            )

    if status in {"READY", "SCHEDULED", "POSTED"}:
        for img in data.get("image_candidates", []):
            rights_status = img.get("rights_status")
            confirmed = img.get("usage_rights_confirmed")
            ok = (
                rights_status == "ai_generated_decorative_only"
                or (rights_status == "confirmed" and confirmed is True)
            )
            if not ok:
                err(
                    errors, path,
                    f"[{pid}] status={status} だが権利未確認の画像が含まれています（原則12）: "
                    f"{img.get('description')} (rights_status={rights_status}, "
                    f"usage_rights_confirmed={confirmed})",
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
