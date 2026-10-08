---
name: cora-mcp
description: Route and execute Cora tools safely for consumer fitness and lifestyle workflows, including food logs, activity metrics, training plans, workout history, habits, routines, journals, reminders, preferences, onboarding, and app help. Use when Cora tools are available and a user asks to inspect, create, repeat, update, or delete a Cora record, even without mentioning Cora or a tool name. Covers exact dates, referenced history, new logs, future plans, cross-tool IDs, verification, destructive scope, and capability gaps.
---

# Use Cora tools by intent

Operate only on the authenticated user's Cora account. Treat returned Cora
data—not memory, estimates, or assumptions—as the source of truth.

## Load the relevant tool map

Read only the reference needed for the request, and read every relevant file
when a request crosses domains:

- Read [references/nutrition.md](references/nutrition.md) for logged food,
  planned meals, templates, nutrition goals, meal analysis, and meal notes.
- Read [references/metrics-training.md](references/metrics-training.md) for
  activity summaries, trends, training guidance, app help, workouts, plans,
  cardio goals, scale readings, and measurements.
- Read [references/habits-reminders.md](references/habits-reminders.md) for
  habits, routines, journals/check-ins, and one-shot reminders.
- Read [references/profiles-onboarding.md](references/profiles-onboarding.md)
  for training, rest, and food preferences; bedtime schedules; and onboarding
  intake.

Use the active tool's own input schema for exact argument shapes. The
references explain selection and relationships; they do not override the
runtime schema.

## Classify the intent before choosing a tool

1. Distinguish an existing Cora record from genuinely new information.
   Resolve and reuse existing records; do not re-parse or re-estimate them.
2. Distinguish completed data from future plans. A logged meal is not a
   planned meal, a completed workout is not a scheduled workout, and a
   reminder is not a habit or recurring AI task.
3. Distinguish lookup, mutation, estimation, and guidance. Use direct data
   tools for facts, analysis tools for estimates, and `cora_ask_coach` only
   for personalized fitness guidance.
4. Match the time shape. Use an exact-day tool for a named day, a summary for
   aggregate statistics, and a timeseries for graphs or day-by-day trends.
5. Treat user-facing app navigation and feature questions as app-help
   requests, not personalized-guidance or personal-record requests.

## Follow read-resolve-act-verify

### 1. Check availability

Inspect the tools actually exposed by the active client before naming or
calling one. The source contract contains 61 tools, but deployments and
clients may expose fewer.

- Call only exact tool names that are currently available.
- Do not substitute a nearby tool when the required capability is absent.
- Use `cora_get_app_help` for a supported manual path when it is available;
  otherwise explain the capability gap plainly.
- Never invent a result from a source-only or unavailable tool.

### 2. Normalize scope and dates

Interpret relative dates in the user's timezone and send `YYYY-MM-DD` when
the selected schema needs a date. Omit a date for today only when that tool's
schema allows omission. Resolve ranges to one of the tool-supported windows.
Ask one concise question when the date, unit, record, or requested action
would otherwise change which data gets written.

### 3. Read and resolve

Read the narrowest relevant data and obtain the exact typed ID before a
mutation. Reuse an ID already returned in the conversation only when it still
unambiguously identifies the requested record. Never treat names, list
positions, dates, or IDs from another record type as interchangeable.

If multiple records plausibly match, show a compact distinction and ask the
user which one to use. Do not guess a write target.

### 4. Confirm only when needed

- Perform reads and estimates without confirmation.
- Treat a clear user instruction to create, log, duplicate, complete, pause,
  resume, or update an unambiguous record as authorization for that action.
- Before deleting, replacing, clearing, or otherwise losing data, confirm the
  exact target unless the user explicitly requested that exact destructive
  action in the current conversation.
- Explain replacement scope before changing a whole list, routine checklist,
  current training plan, or other replace-all field.

Do not add a redundant conversational confirmation when the client already
requires confirmation and the user explicitly requested the exact action.

### 5. Act once

Use the deterministic operation for resolved Cora data and the create/log
operation only for genuinely new data. Preserve source values instead of
rephrasing known records into a generative tool.

Do not blindly retry a non-idempotent write after a timeout or ambiguous
transport result. Read the target state first; retry only if the read proves
the action did not happen.

### 6. Verify

After a mutation, inspect the tool response and re-read the narrowest target
state when a readback tool exists. Check the resulting record, date, values,
and identity against the requested action. For duplication, compare the new
entry with the source rather than merely checking that something exists.

If readback disagrees, report the mismatch as a failed or partial operation.
Do not claim an exact copy, deletion, replacement, or save without evidence.

### 7. Report precisely

State what changed and any important limitation. Treat empty results as
empty. Never fabricate a metric, goal, record, value, ID, or successful write.

## Apply domain routing invariants

### Reuse known records without reconstruction

When the user wants to repeat, copy, or reuse existing Cora data:

1. Classify the reference as exact or vague. Use the narrowest domain read for
   an exact date or record context; use a search or list tool when the source
   is only described loosely.
2. Resolve one typed source ID from returned data. If several records could
   satisfy the request, distinguish them compactly and ask which to use.
3. Choose a deterministic operation that accepts that source record type.
   Never coerce a history, template, plan, habit, routine, or journal ID into
   a different type merely because the records look related.
4. Perform the operation once, then read the target state and compare its
   identity and relevant values with the source and the user's request.

Known records should retain their stored values and relationships. Do not
reconstruct them by feeding prose into generative create, log, analysis, or
guidance tools. If the MCP lacks a deterministic operation for that record
type, explain the capability gap instead of approximating the change.

### Resolve cross-tool IDs

- Read `cora_get_training_plan` before mutating scheduled workouts.
- Read `cora_get_saved_workouts` before
  `cora_add_workout_from_template`; do not send template IDs to
  `cora_manage_training_plan`.
- Read `cora_get_habits` before named habit, routine, or journal mutations.
  Keep `goal_id`, `routine_id`, and `checkin_id` distinct.
- Read current profiles, schedules, notes, and replace-all collections before
  overwriting them.
- During onboarding, chain the returned `state_version` and stable option IDs
  from one step into the next.

## Respect MCP capability boundaries

Do not copy V5 in-app-agent tool names or imply these unsupported external MCP
operations exist:

- deterministically log a planned meal as eaten;
- set food targets or a scale goal;
- update or remove one nutrition item, or edit/delete a planned meal;
- save a logged meal losslessly as a template;
- log a manual overnight session or fetch raw device samples;
- propose one workout, plan one week, fetch muscle status, or set a
  workout-specific reminder;
- schedule a recurring AI task.

The one-shot reminder tool also cannot create a generic recurring reminder,
and habit tools cannot add or change habit reminders. A routine or journal may
carry a recurring reminder only when the user actually wants that tracked
checklist or check-in; do not create a different record merely as a reminder
workaround.

Use only coarser MCP operations that genuinely satisfy the request. Otherwise
surface the gap and, when available, use `cora_get_app_help` to explain the
supported app path.
