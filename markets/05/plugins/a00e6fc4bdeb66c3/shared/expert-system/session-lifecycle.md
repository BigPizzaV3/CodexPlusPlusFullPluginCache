# Session lifecycle

Canonical provider-neutral session policy, extracted from coding execution. It controls context selection, not provider configuration or memory deletion. Use [Context Package](context-package.md) for the next task, not a full conversation replay.

## Start, continue, checkpoint, resume

- START: confirm objective, actual accessible scope, governing authority, source freshness, current observed state, unknowns, acceptance and permissions. If observations are missing use UNKNOWN, not a healthy/clean claim.
- CONTINUE: recheck material deltas since the last confirmed checkpoint; do not repeat unchanged audits. A corrected user instruction supersedes an old instruction only within the applicable authority/scope. Surface conflicts.
- CHECKPOINT: persist verified outcomes, artifact/source identities, unresolved failures, decisions, approvals, next action and evidence in the existing task/handoff record when continuity matters. No mandatory new file after each small action.
- HANDOFF / RESUME: verify receiver access, current sources, observed state and authority before executing the next action. An old chat summary is historical input, not reliable persistence or execution permission. For repository work additionally check revision/snapshot, dirty ownership, active contract, harness, gate and rollback.
- RESET: preserve a corrected resume package before a supported reset/new session. Do not erase chats, memories or global settings, launch new tasks, or mutate provider configuration without the relevant authorization and supported mechanism. If unavailable, prepare a manual resume and disclose it.

## Task-start capability and freshness decision

At a relevant START or RESUME, resolve the selected/closed method and its scope, then required capabilities, observed environment, applicable method/guidance freshness and authority before dependent execution. Use the existing [provider capability gate](provider-capability-routing.md) and [method freshness record](decision-authority-model.md); this session policy coordinates them, not another registry or capability inspector.

Classify only decision-relevant needs (more than one can apply):

| Route | Action |
|---|---|
| A — STABLE / METHOD_CLOSED / NO_RECHECK_NEEDED | Reuse applicable, sufficiently fresh method and environment evidence; execute within existing authority. A does not waive normal acceptance tests. |
| B — VERSION_SENSITIVE / TARGETED_FRESHNESS_CHECK_REQUIRED | Check only the affected version/guidance claim and its applicability. Revalidation alone does not reopen a method. |
| C — CAPABILITY_UNKNOWN / ENVIRONMENT_CHECK_REQUIRED | Inspect the local or available target environment first. Unknown installation, access or version is not by itself a research question. |
| D — NEW_PROBLEM / RESEARCH_REQUIRED | Research a genuine unresolved method/domain question not answered by applicable production knowledge; research does not grant implementation authority. |

If C and B/D coexist, establish the relevant observable environment first wherever accessible, then research only remaining decision-critical unknowns. Missing access is reported, not resolved through speculative web research. Reuse confirmed evidence until a relevant change trigger occurs. A new task label, elapsed time alone or “perhaps something new exists” does not justify tool shopping, whole-machine inventory or whole-vendor research. Higher-priority explicit research requirements remain binding.

An already confirmed capability/version/access gap stays on C's environment-prerequisite path with the check marked completed; use the provider gate's specific result and repair/block action instead of repeating inspection. This does not block authorized research or other work independent of the unavailable environment.

Use a compact view in the existing task/checkpoint record only when material: task, selected method/lock, route(s), required capability reference, environment result, method freshness (`CURRENT | RECHECK_REQUIRED | UNKNOWN`), guidance freshness (`CURRENT | TARGETED_CHECK_REQUIRED | UNKNOWN | NOT_APPLICABLE`), new research required (`YES | NO | UNKNOWN`), execution ready (`YES | NO`) and the exact pending dependency. Unknown required inputs cannot yield YES. Recheck only affected dependencies and continue unrelated authorized work; trivial self-contained work needs no extra form, skill or approval.

## Context health and drift

| Health | Observable evidence | Response |
|---|---|---|
| HEALTHY | Active sources and recent interpretations agree | Continue related bounded work |
| DEGRADED | Repeated corrections, stale assumptions or observed compaction loss | Rebuild the necessary slice and diagnose |
| CONTAMINATED | Revoked/conflicting instructions continue to drive decisions | Stop dependent work; inspect instruction sources |
| RESET_REQUIRED | Unresolved contamination or unsafe continuity after fundamental source replacement | Correct package and inherited inputs; use a clean resume |

UNKNOWN means not assessed, not a fifth health diagnosis. Context rot is evidenced loss of alignment with current authority/state, not a guess based on message count. Two repeats of the same unexplained failure require diagnosis; three repeats of the same unresolved interpretation require a fresh-session route unless evidence identifies an external cause. Missing tools, faulty specs, unsuitable representation and broken tests need their own repair, not endless resets. Never invent hidden token usage or a universal context limit.

Compaction risk warrants a checkpoint when essential decisions/evidence are no longer recoverable from current context or a material transition is imminent. Prefer logical cuts over arbitrary time/token thresholds. START_FRESH_SESSION and CONTINUE_CURRENT_SESSION record a brief evidence-based reason; an unknown session does not automatically require reset.

## Fresh is not clean or independent

Inspect relevant inherited/project instructions, available memory mechanisms, automatically loaded skills and source versions before claiming isolation. Uninspectable inheritance means CLEAN_CONTEXT_NOT_VERIFIED. A request to ignore unrelated memory is an instruction boundary, not evidence that memory was removed. Route conflicting persistent configuration for authorized correction.

A fresh chat of the builder is not an independent reviewer. Give a genuinely independent reviewer criteria and original evidence, not the builder's desired verdict. Preserve [risk-adaptive assurance](risk-adaptive-assurance-model.md); no reset or summary can waive a required security, perceptual or owner gate.
