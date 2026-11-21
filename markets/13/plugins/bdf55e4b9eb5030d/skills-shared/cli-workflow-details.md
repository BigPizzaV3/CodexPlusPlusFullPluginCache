# Advanced CLI Workflow Reference

Detailed creative and execution guidance retained for multi-stage, reference-controlled,
manual, or unfamiliar workflows. Start with `./cli-workflow.md`; simple direct tasks
do not need this full reference. It is not a public skill or another routing stage.

For an explicitly selected Canvas target, follow
`../skills-internal/pixverse-agent-canvas/SKILL.md` and its **Cloud Preview And On-Demand Delivery**
contract instead. A directory binding alone does not activate Canvas rules.

For manual CLI commands or queue specs, read `../skills-internal/pixverse-agent-gateway/SKILL.md`.
Use `../skills-internal/pixverse-agent-project-memory/SKILL.md` when decisions or assets need
to carry forward. Read `../skills-internal/pixverse-agent-quality/SKILL.md` only for
user-requested QA or named checks required by the selected specialized workflow.
Ordinary image/video generation has no automatic QA stage. These are shared references,
not extra public routing stages.

Apply `./quality-policy.md` for image/video defaults, automatic Seedance prompt enhancement and membership choices.

## Scope And First Move

Codex's advantage here is local, patient creative reasoning. Use that advantage to understand the brief, choose the right PixVerse control layer, organize project memory, and build queues. Do not turn it into slow bureaucracy: simple tasks should still move quickly.

Choose production depth by the requested result, not a rigid duration rule. A short product/character shot may need a control image; a 30-second abstract loop may not. Classify the job by continuity risk, number of beats/shots, recurring cast or products, dialogue, exact visual locks, delivery stakes, and expected future revisions. Tell the user why it is being treated as a quick task or a production project.

After the first direct preview is visible, accept feedback without stopping the remaining requested work; ask only when a material creative choice is unresolved. Offer stronger control as optional remedies—opening frame, character/scene references, per-shot storyboard frames, transition keyframes, motion reference, or a multi-shot plan—and state the added time and paid stages.

For a serious film such as a 30-second character animation, use the cinematic film workflow: lock the character first, then scenes/look, then detailed per-shot storyboard frames, then video. For feature-length work such as a 90-minute film, build script and production bibles first, divide by act/reel/scene/shot, and quote/approve reusable assets and scene batches separately. Never materialize a whole long-form project as one giant queue.

For a continuation request, recover the likely project and its useful state in one call before loading raw history:

```bash
"${PIXVERSE_RUNTIME}" project resume [title-or-slug-hint] --format markdown
```

Prepared `route queue` projects retain their compact route intent, so this resume call can show the latest task count, model chain, control layer, and reason before any paid run.

Use `project portfolio --format markdown` only when several projects may match. For a non-trivial or capability-sensitive route, `"${PIXVERSE_RUNTIME}" route recommend --kind <image|video> ... --format markdown` gives a compact current default before you write the queue.

Read `./creative-orchestration.md` when the user wants planning or a non-trivial creative result. Keep a simple direct task on the selected workflow’s fast path.
Read `./web-handoff.md` before any PixVerse OAuth, subscription,
workspace-management, or Canvas browser action.


## Dependent Queue Preparation

Use `./cli-workflow.md` for a direct one-shot task. For multi-stage work, keep
`./generation-confirmation.md` as the paid-work contract and `./progress-contract.md`
as the waiting and user-update contract.

For a dependent queue, batch project initialization, prompt saves, `queue write`, and every `queue append` into one fail-fast shell invocation; put `--preflight --format markdown` on the final append. Do not make one host tool call per deterministic helper command.

When the user explicitly chooses an additional paid board and no judgment is needed between board and video, compose the advanced chain directly:

```bash
"${PIXVERSE_RUNTIME}" route queue projects/<slug>/queue.json --project <slug> --kind video --intent final --mode board-to-video --board-prompt <board-prompt-or-file> --prompt <video-prompt-or-file> --preflight --format markdown
```

Add `--run-if-allowed` under the same stored-confirmation rules. This writes the Sunburst 2K/high board and Seedance dependency as one queue; keep manual `queue write`/`append` when references, prompts, or creative selection need inspection between stages.

The same builder handles reference-controlled stills: use `--kind image` and repeat `--reference` for one or more subject, product, character, or style anchors. It chooses `--image` versus `--images` and retains the Sunburst 2K/high defaults and explicit user-selected model controls in the generated queue.

Under the default automatic policy or an explicit skip preference, add `--run-if-allowed` to the final queue mutation. It prints the preflight first and continues into the normal queue-run gate within the same host-tool call. It never bypasses the preference gate: when confirmation is enabled, it returns the confirmation sheet and does not run.

## Creative Stance

- Treat skills as expert playbooks, not rails.
- Respect explicit user choices first: model, style, aspect, duration, count, flaws, and things to avoid.
- Preserve user-provided subject references in the generation chain unless the user clearly says they are only for explanation.
- Use local artifacts when they help: route boards, storyboard tables, asset maps, queue specs, Mermaid canvases, QA ledgers, and project memory.
- Match the user's aesthetic target. Do not automatically beautify deliberately rough, historical, amateur, broken, or low-budget requests.

## Execution And Delivery

Apply `./generation-confirmation.md` before each paid batch, including retries and
later stages. It owns preflight details, default automatic execution, optional approval,
preference scope and blocker recovery. Ordinary execution uses `./cli-workflow.md`.
For an explicitly selected Canvas target, use its canonical bound preflight and
**Cloud Preview And On-Demand Delivery** contract instead of queue delivery below.

When the user or a specialized workflow requests whole-project QA, run `"${PIXVERSE_RUNTIME}" qa project <slug> --all-runs` once to inspect unique historical assets without rechecking idempotent reruns. Multiple generation batches alone do not enable QA.

When generated assets complete, wait only for `queue run` to download each one, then show its absolute `local_path` promptly with a role label. Use the local file for Codex image/video rendering; never use the provider URL as the inline preview source. Billing reconciliation continues in the running command after the first local preview is visible. Ordinary images and clips deliver directly; run QA only for a user request or named specialized-workflow checks. Final recaps must include an invoice-style ledger with task id, asset role, model/mode, status, local path, provider URL, and actual or observed credit cost when available.

For multi-stage production or a requested handoff, after planning, character lock, storyboard, control-asset, preview, render, and final stages, run and show:

```bash
"${PIXVERSE_RUNTIME}" project handoff <slug> --stage <stage-name> --format markdown
```

The user should see editable plans/prompts/queues, learned memory, QA and billing audit files, generated assets, and deliverables. If their repeated preferences form a stable production method, update `workflow-profile.md` and offer to package it as a custom Codex skill only after they choose to do so.

Generated media and local project state belong under `projects/`.

