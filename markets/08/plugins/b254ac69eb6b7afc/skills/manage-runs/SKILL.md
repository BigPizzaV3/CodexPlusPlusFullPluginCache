---
name: manage-runs
description: Start and manage Manifestly runs and their assignments. Use for finding assigned work, collecting step data, completing or skipping tasks, reassigning tasks, and changing run or task deadlines. Applies to executions of existing workflows, not creating or editing reusable workflow templates.
---

# Manage runs

A workflow is a reusable template. A run is one execution of it, with its own run steps, assignments, field values, and dates. Use this skill for run work across any connected customer's workflows.

Follow the user's explicit scope and preferences over this skill's defaults. A request to inspect work does not authorize changing it. A clear request to perform an available action supplies authorization for that action; do not add a routine confirmation step.

## Establish context

- Use the connected account selected by the user or established in the conversation. If several accounts could satisfy a write and the intended one is unclear, ask which account. Discover IDs from tools, not sample data or remembered IDs from another account.
- Resolve runs with `list_runs` or `get_run`, retaining the returned run ID across follow-ups. A workflow ID, workflow-step ID, run ID, and run-step ID are different identifiers. Run-step IDs come from run responses or assignments.
- Resolve references such as "that task" from the active run and previous results. Ask when several records match; report a missing record without substituting one. Follow pagination when needed to establish a match or complete list.
- Tool names here refer to operations on the connected Manifestly MCP server. Follow the current tool schema. Use `docs` for unfamiliar behavior; its index identifies recipes and error explanations.

## Start a run and find work

Use `start_run_by_workflow_name` for a named workflow, or discover a workflow and use `create_run` with its ID. Resolve an ambiguous workflow or department before creation. Create the requested run once, retain its returned ID, and report preparation status if its steps are not yet ready. Do not start a run merely because the user asks to see workflows.

Use `list_my_assignments` for the authenticated user's assigned tasks. Narrow with its filters rather than paging and filtering client-side: `state: "overdue"` for overdue work, `due_after` and `due_before` (ISO 8601) for a date window such as "due this week", `kind: "approval"` for pending decisions, `search` for a title match, and `sort` (`due_asc` default, undated tasks last). By default only actionable steps are listed; pass `include_locked: "true"` to also see steps locked behind a stop task or approval, and `include_completed: "true"` to see finished ones. For "in this run," match returned assignments against the active run ID; a title search alone does not establish identity. For the next assigned task, use incomplete actionable assignments in due-date order, with undated tasks last. Respect a different priority requested by the user. Do not treat every step in a run as assigned to the user.

Use `get_my_status` for a broad workload overview. It is a dashboard, not an inventory: each list is a sample of at most 10 rows, and the real totals are in `counts`. Report numbers from `counts`, never from an array's length, and switch to `list_my_assignments` or `list_runs` to work through everything behind a count.

## Complete work and collect data

Inspect the target step with `get_run_step` when its type, prerequisites, or state are unknown. Section headers group steps. Calling `complete_run_step` on a header can also complete its child tasks, so skip headers when resolving "the first step" or "the next step." Do not bypass locked steps or mark prerequisites completed merely to unlock the target.

- **Data collection:** Call `get_fields` to discover field IDs, required values, and allowed options. Ask for missing required values without inventing them. Save supplied values using `set_fields`, or `update_field` for an isolated field update. Check every field result: a successful batch response may contain individual errors. Filling all required data auto-completes eligible steps; do not follow it with a redundant `complete_run_step`. Verify returned completion state or fetch the step if necessary.
- **Subtasks:** A step with `subtasks_required: true` cannot be completed until every subtask is done. Complete each one with `complete_subtask`, passing the run-step ID as `step_id` and the subtask ID from the step's `subtasks` array, and only when the user's instruction or supplied evidence supports marking that work done. `uncomplete_subtask` reverses one. Subtask changes never complete the parent step.
- **Ordinary tasks:** When required data and subtasks are satisfied, use `complete_run_step` with `include: ["next_steps", "progress"]`.
- **Approvals:** Use `approve_run_step` or `reject_run_step` only for a requested decision, never `complete_run_step`. Before deciding, fetch each step in `reviewed_run_step_ids` with `get_run_step` and inspect its data and comments. Both decisions require a non-blank comment. Check `can_decide` for either decision and `can_approve` for approval; explain blockers. A user who completed any reviewed step cannot approve or reject its approval.
- **Rejection scope:** Omitting `rejected_run_step_ids` from `reject_run_step` reopens every completed reviewed step. Choose the scope deliberately: for targeted rework, pass only the relevant IDs from `reviewed_run_step_ids`. Ask when the requested scope is unclear instead of defaulting to reopening everything. Rejection keeps downstream work gated by the approval locked; only approval releases that gate. Report which reviewed steps were reopened.
- **Retraction:** Use `retract_run_step` only when the user requests withdrawing an earlier approval and `can_retract` is true. It requires a non-blank comment explaining the reason. Retraction reopens the approval for a new decision and relocks downstream steps that the approval had unlocked; it does not record a rejection. Report those effects.
- **Skipping:** Use `skip_run_step` when the user asks to skip. Report it as skipped, even if the progress percentage increases. Skipping a stop task does not release its gate: unskip it, then complete it.
- **Reversing:** `uncomplete_run_step` reopens a completed step and `unskip_run_step` a skipped one; they are the same operation. Only `uncomplete_run_step` accepts `clear_data: true`, which also wipes the step's collected values. Without it the values survive and the step auto-completes again as soon as the last required field is refilled.
- **Comments:** `add_comment` posts a note on a run step and `list_run_step_comments` reads them. Comments never change step state.

Step-collected values and run-level fields are separate systems. For whole-run metadata, inspect the run's field definitions and use `set_run_field_values` with the appropriate workflow-field IDs. Consult `docs` for the `data` or `start-run-with-fields` page when needed.

## Change assignments and deadlines

For a task deadline, use `update_run_step_due_date`; for the run's own deadline, use `update_run`. Resolve relative dates in the user's established timezone. Ask only for date or target details that remain ambiguous, preserve an existing time when only the date changes, and send a timezone-qualified datetime.

Assign a person with `assign_run_step_by_email` or `assign_run_step_by_name` when appropriate. Direct `assign_run_step` uses a membership ID for the run's department, not a user ID. AI agents must be assigned by membership ID; their synthetic email addresses are not contact addresses. Resolve missing or multiple matches before writing.

Adding a step with `create_run_step` is supported only on ad-hoc runs, not runs started from templates. A template edit will not add the step to an existing run. Explain the applicable limitation rather than altering the template as a substitute.

## Report outcomes and failures

Confirm the actual task or run affected, saved values or deadline as relevant, returned progress, and a returned app link. Distinguish partial success from completion. Do not derive run progress from a workflow's step count.

Treat permission, not-found, and validation responses as reasons to resolve the specific issue, not to probe other accounts or retry unchanged requests. For an uncertain write outcome, read back the state before retrying; reuse the same idempotency key where supported.

Do not close a run as routine cleanup. `close_run` abandons a run; a run that finishes reaches `completed` on its own when its last step is resolved. Closing requires an explicit request, is admin-only, cannot be undone through these tools (only the app can reopen a closed run), and is refused for a run already in `completed`. After closing, every step write on that run returns a 422; reads still work. "Close this out" often means finish the remaining steps, so confirm which the user means before calling it.
