# V2 Clean Slate Policy

Effective: 2026-10-22

## Decision
From V2 onward, previous Canva posts, prior QA results, old production monitor rows, old Drive handoffs, and old generated copy are history only. They must not be used to decide that a destination is already produced.

## Reusable inputs
Only durable inputs may be reused:
- Notion source candidates and factual source links
- user-provided original photos
- current Canva MASTER `DAHVoXJDBFw`
- current GitHub rules
- current official web information

Old copy, old page composition, old photo ranking, old QA judgments, old completed statuses, and old Canva designs are not production inputs.

## V2 official destinations
Canva:
- `贅沢旅リサーチ帖｜V2再制作`
- folder_id: `FAHYuHEOty4`

Google Drive:
- `旅ログAI連携_V2`
- folder_id: `1d_EPvf2LN6FqbDJ3Mh0nx8vl4GAx5zCc`

Notion:
- `制作世代 = V2正式`
- `V2再制作 = true`

## Deduplication
Deduplicate only inside V2. An old design with the same destination name does not count as complete. A destination is complete only when a V2 monitor row points to a V2 Canva design saved in the V2 official folder and current QA is passed.

## Build rule
Every V2 destination is rebuilt from current source/user request, fresh official verification, current real photos, current Gemini review when used, current MASTER schema, and current QA. Do not copy old text, page order, claims, or QA decisions merely because they exist.

## Legacy handling
Do not delete legacy assets automatically. Keep them as archive/history. Do not move them into V2 folders and do not include them in V2 completion counts.
