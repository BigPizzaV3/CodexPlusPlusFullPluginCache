# Progress Contract

Users should feel the agent is working, not hiding.

## Before Paid Work

Use `./cli-workflow.md` for ordinary queue preflight and account recovery, and
`./generation-confirmation.md` for the effective confirmation policy. Every new paid
batch, including retries and bounded repairs, needs a fresh preflight. The policy
controls whether to wait; a progress update does not grant approval or change preferences.

For an explicitly selected Canvas target, follow
`../skills-internal/pixverse-agent-canvas/SKILL.md`: show its bound `canvas paid preflight`
sheet and execute its exact returned command under the effective policy. Do not replace
it with queue commands or add another confirmation round.

Explain the immediate work briefly: the direct or production route and why, intended
outputs and task count, selected models/key parameters, account and balance when useful,
exploration or final intent, and any requested checks. Keep exact batch details in the
preflight record. Never invent an exact price or imply an automatic QA stage.

Keep preflight lightweight. For a straightforward task, do not build route boards,
dependency graphs or dry-run loops unless they reveal a real blocker. Mention advisory
notes compactly and proceed when the execution and confirmation gates allow it.

## During Waits

For long tasks, give timely, useful updates. Host-tool round trips are often slower than the local CLI itself, so keep the queue inside one long-lived yielded/background command instead of repeatedly launching status commands. When the host supports it, yield promptly and poll the same command session every 20–30 seconds.

Never leave an active user-facing generation silent for more than 45 seconds. A useful update explains creative movement, not only provider state:

- "Submitted 2 video tasks; I will keep this same session alive and update you at the next useful milestone."
- "Video slot is full, waiting rather than resubmitting."
- "shot_01 still Generating, code 10; elapsed 1m30s; task 123..."
- "The board is done; using it as the reference for the film render."
- "Two of five assets are ready; the finished world board has unlocked both story shots."

Do not spam per-second logs. The CLI should emit task-level lines only when provider state or progress percentage changes; a 30-second studio heartbeat owns repeated no-change reassurance. Translate its overall ready/rendering/waiting/failed counts into natural commentary. If the CLI returns `progress_percent`, show it; otherwise show status, elapsed time, asset role, and task id only when useful. Report generation success from a terminal provider result; claim visual or technical QA only when it was requested and actually performed.

The initial paid submission is also a wait state. If PixVerse has not returned a task id within the feedback interval, say that the same request is still in flight and that no duplicate retry was sent. If the submission itself times out, report the structured `submit_timeout_unknown` state: no task id was returned, provider receipt and credits are unknown, no duplicate retry was sent, and dependent paid tasks were stopped. Never turn that uncertainty into a traceback or an automatic retry. After generation succeeds, `queue run` downloads the asset and emits `Local preview ready` with an absolute `local_path`. Show the primary image/video from that local file immediately, before deep QA, credit attribution, ledger reconciliation, or packaging. Provider URLs are audit/share metadata and must not be used as Codex inline preview sources. If the free download fails, report it and retry the free localization rather than running QA or regenerating.

For a Canvas paid batch, use one bounded `canvas paid follow` call rather than repeated host-tool status
commands. It may keep running after emitting the first `Canvas node ready` line; show the Canvas preview
immediately, then continue waiting on the same process for the remaining nodes. A terminal node is ready
for preview and downstream work even when audit attribution is incomplete. The Canvas skill's
**Cloud Preview And On-Demand Delivery** contract applies only to an explicitly selected Canvas target:
no automatic download, local QA, or post-generation balance refresh, including after success. Use
`--download` and `--credits` only for the respective explicit user request. Unrequested work is
`not_requested`; unverified technical properties are `not_checked`. Treat dependency `BLOCKED` as
nonterminal while an upstream followed node is still running. For requested downloads only, retry a
failed free localization at most three times; never substitute an arbitrary historical task ID or
regenerate the media to repair a download. IAB failure means return the Canvas link, not auto-download.

A fast asset download should return immediately without waiting for a scheduled update. Only when it remains active should the CLI emit an early follow-up, measure local byte growth and recent throughput, then adapt later download heartbeats from a few seconds up to 30 seconds. Slow or stalled starts need reassurance; fast transfers and already-large files should back off to avoid noisy updates. Include percentage and ETA only when a trustworthy total byte count is available. This download cadence is separate from the 30-second generation/studio heartbeat.

Make the wait feel accompanied, not merely monitored. When there is evidence, include one perceptive observation about the finished board, image, motion, identity, palette, or story beat. Avoid empty enthusiasm and never claim quality before inspection; truthful specificity creates more emotional value than generic praise.

## Host-Tool Call Budget

Use the two-call fast path in `./cli-workflow.md` for ordinary one-shot generation and
`./cli-workflow-details.md` for dependent queues. Batch deterministic preparation until
model judgment or user input is actually needed. Keep generation in the same long-lived
process; these progress updates do not require extra status, setup, ledger or QA calls.

## After Work

Recap:

- what succeeded
- where the asset is
- requested quality checks and their results, if any; do not add an automatic QA recap
- any weak, failed, or rejected assets that influenced the result
- what you recommend next

For multi-stage production or an explicit handoff request, after every meaningful stage also show `"${PIXVERSE_RUNTIME}" project handoff <slug> --stage <stage-name> --format markdown` so the user can inspect and edit plans, prompts, queues, memory, QA/audit records, media, and deliverables.

For Canvas work, accompany that handoff with `Stage N/M`, an explicit statement of whether the requested
final deliverable is finished, the remaining stages, and the next paid task count. Distinguish cloud
Canvas nodes from local-only plans and explicitly requested download copies. Pass `--surface canvas` and the handoff's structured
stage options so this status is persisted rather than supplied only as surrounding prose.

Keep CLI command details in project memory unless the user wants the exact technical trace.
