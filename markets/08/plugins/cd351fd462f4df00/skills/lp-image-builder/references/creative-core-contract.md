# Optional creative checks

Read this reference only when an already available creative-check connection applies to the current work, or the user explicitly asks to use it. These are additive checks. Keep every local Skill rule, source requirement, validator, approval artifact, and handoff binding. The four local Skills remain usable without a MyMarketer account. The basic connection described here is a development candidate and is **not currently provided in production**; never probe them or present them as installed merely because this reference exists.

## Choose the applicable authority

| Mode | Account / scope | What the host may rely on |
| --- | --- | --- |
| Local free | No MyMarketer account | User sources, local Skill rules, and host review. |
| Connected basic | Free account; `/mcp/creative-basic`; `creative_basic_v1`; `creative_basic`; `mcp:read` only; `projectAccess: none` | Deterministic checks of supplied structured fields. No project context, server AI, file transfer, or persistent input/output storage. |
| Existing quality | Paid account; `/mcp/quality`; `quality_preview`; `mcp:read` | The existing four reads and host review under [connected-quality-policy.json](connected-quality-policy.json). Its paid gate and explicit-save boundary still apply. |

Do not promote an account, connection or upgrade during ordinary completion. Only use a known available connection. An explicit connection request may use the host connection UI under the existing outcome-assistance policy. Public installation configuration is unchanged.

## Connected basic

Call `getCreativeBasicContract` to obtain the current version, input schema and limitations before the first applicable basic check in a run. Use `evaluateCreativeBasics` with one advertised `judgment`:

- `lp_route_consistency`: `selectedRoute`, the approved and proposed `who`, `what`, `offer`, `goal`, `coreMessage`, the article CTA kind, diagnostic outcome binding and source references. This compares supplied values; it does not select the best-selling route or verify semantic truth.
- `video_expression`: the existing `creative-context.json` classification, source fields and actual historical signals, if any. Do not invent classifications or claim that source references have been independently checked.
- `video_fit`: the hook/body IDs, promise, open question/answer, and the fixed/actual body IDs for a declared hook or body test. This does not watch the video or establish causal ad performance.

Use the advertised schema exactly. Send only the relevant structured fields, not files, the full conversation, customer records, or paid project data. Missing material classifications remain unknown and use the existing clarification/local-review path. A missing field is not permission to guess.

The response authority is `deterministic_basic`, with `serverAiUsed: false` and `paidReviewReceipt: null`. `consistent` means only that supplied fields passed those checks; `guidance` is a policy suggestion. Neither is a creative PASS, a paid review, evidence of source truth, human approval, or pixel/audio/video QC. Preserve approved expression policy and commercial meaning when suggestions differ; show the material difference and obtain approval before changing them. Never change the artifact's free mode or attach a paid project fingerprint from this response.

If basic is unavailable, expired, denied, incompatible, or fails, use the unchanged local rules and validators. Preserve approved structure, direction, WHO/WHAT, offer, CTA, claims, outcome, candidate selection, cost authorization, and immutable handoff hashes. Do not rerun creative generation, overwrite approved artifacts, request paid authorization, or turn a missing basic response into PASS. For a run that tried the connection, say once: 「共通チェック未適用：ローカルの制作ルールとレビューで続行します。」 A run that began local needs no connection notice.

## Review and saved history

MyMarketer does not provide server AI review, scoring, image inspection or video inspection. Do not request a paid judgment or invoke the retired `startCreativeReview`, `transferCreativeReviewFiles`, or `requestCreativeJudgment` tools. Continue source-grounded creation and review in the host. Record what was checked and what remains unverified; do not describe formal storage as quality approval.

When a user asks about an existing historical receipt, `getCreativeReview` may retrieve it with its original access and retention rules. The bundled [legacy receipt validator](../scripts/validate_creative_review.py) remains for reading historical records only. It never authorizes current work, selects a candidate, approves spend, finalizes a strategy or publishes an ad. New work uses host review and human decisions.

For paid project continuity, use [paid-continuity.md](paid-continuity.md) to save actual files, production conditions, results and proposed learning. This storage workflow does not request MyMarketer AI review.
