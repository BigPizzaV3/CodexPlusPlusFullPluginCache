# Task execution and continuation

The existing report task owns required work, criteria and results. `action_room_execution` stores an execution checklist in its checkpoint; it is not another roadmap. Preserve report task order and business criteria. Research readiness, prepared documents, sent messages and business outcomes remain different facts.

## Read, execute, check

1. Read the current Room and `action_room_execution` with `action:"read",room_id,task_id`. Reconcile local `execution-checkpoint --task <task_id> --read true` and existing artifact/action receipts. Report an already-successful external action; never repeat it because reporting was interrupted.
2. Save the task's actual required steps before executing. Use the exact report `completion_criteria`. Include research, preparation, external action and verification only where the original criterion requires them. A step may cover a defined population; record the full scope in `total`, not a conveniently small first batch. Use source-linked selection/exclusion reasoning; not every discovered candidate needs a proposal. Keep candidate facts in the research ledger, not duplicated here.
3. Work through authorized runnable steps. Record cumulative counts and evidence after meaningful groups. `done` means the stated step is actually done, not a draft or attempted action. Use provider result IDs, existing artifact IDs or concise verification references, without secrets, private paths or URLs. For each external unit, keep a stable operation identity tied to its candidate/target and approved content version in the existing task support checkpoint before acting. Use provider idempotency when supported. Immediately after success save that unit's provider receipt, then record it in the execution step's `receipts`. If reporting or the effect itself is uncertain, use the saved identity for readback; block only its reconciliation and never blindly retry it.
4. Ask necessary questions in Codex without stopping independent work. Block only the units depending on that approval/input/access/external event. Give the exact reason, attempted alternatives, and condition for resuming. A missing sender account blocks sending, not public research or drafting. Do not call unexplored work blocked or exclude it to reach zero.
5. Read the server-derived summary before final reporting and at the start of every continued turn. `continue`: execute `next_steps` or resolve the reported issues. `submit`: verify the original criterion, then use the existing submission checkpoint; completion of this checklist does not submit the task. `wait_for_dependency`: all remaining units must have concrete blockers; report them, then wait without busy polling. For an unfinished report task, retain its own execution checkpoint and report the Room outcome as waiting; do not create `goal_work` just to record its wait. The goal `wait` action is for an already-existing follow-up work item. Record a real scheduler only when available and needed for a future external event.

Do not narrow scope or lower criteria because of time spent, a batch size, partial results, an approval request or context compaction. Save state and continue from it. Honor explicit user interruption, pause, exhausted limits, revoked bindings and achieved objectives. System limits may end an incomplete turn; preserve the next action instead of calling it complete. Never override limits with another process or Goal.

## Save and recover

Before calling the server, save the exact mutation with local `execution-checkpoint --task <task_id>` and stdin:

```json
{
  "payload": {
    "action": "save",
    "room_id": "...",
    "task_id": "...",
    "binding_id": "...",
    "codex_session_id": "...",
    "mutation_id": "...",
    "expected_revision": 0,
    "patch_json": "..."
  }
}
```

Call `action_room_execution` with that unchanged payload. Then save `{ "receipt": <exact successful response> }` through the same helper. A timeout is not a rejection: replay the same mutation ID and payload. Only a definitive revision/payload/scope/incomplete/terminal rejection can be recorded as `{ "rejected": { "mutation_id":"...", "code":"..." } }`; then reread and form a new mutation. Reporting retries never repeat external effects.

`patch_json` contains:

```json
{
  "completion_criteria": "Exact criterion from the original task",
  "steps": [
    {
      "id": "prepare",
      "label": "Prepare proposals for qualified organizations",
      "kind": "preparation",
      "total": 30,
      "done": 6,
      "excluded": 0,
      "blocked": 0,
      "evidence": "Existing proposal artifact reference for six organizations",
      "exclusion_reason": "",
      "next_action": "Prepare the next qualified organization",
      "blocker": null
    }
  ],
  "criteria_met": false,
  "result_evidence": ""
}
```

The count is an example, not a prescribed scope or stopping threshold. Step kinds: `research`, `preparation`, `action`, `verification`. `blocked` counts unresolved units with a blocker `{kind:"approval"|"input"|"external"|"access",reason,attempts,resume_when}`. `done`, `excluded`, `blocked` cannot exceed `total`. Unresolved unblocked units are runnable. Exclusions require a factual reason; completed units require evidence. An action step must include `receipts:[{unit_id:"stable-target-and-approved-version",reference:"provider-result-id"}]` with one immutable entry per completed unit. These references map back to the existing local per-unit recovery record; they must not contain addresses, message bodies or secrets. Stable step IDs merge without deletion; scope and completed counts cannot shrink. Omitted steps remain. Set `criteria_met:true` and `result_evidence` only after every required step resolves and the original criterion is verified.

Keep the research checkpoint current. A changed research revision or expired sources invalidate the execution assessment until it is checked again. Partial research requires an unresolved research step; it cannot disappear behind six completed drafts. Stage counts are separate units and must not be added into a business-completion percentage.

## Native Codex Goal

If the user explicitly requests final completion or continuous goal execution, use available native Goal tools to retain that request across turns. The Goal should point to the selected Room and original outcome, require the execution summary to be checked before stopping, and preserve approval boundaries. Do not mark the host Goal complete because of a first batch, task count, upload, or a Room waiting status. Follow the host's actual blocked/pause/budget contract; a server waiting response does not authorize changing those controls. No tool calls solely to spin through waiting turns.
