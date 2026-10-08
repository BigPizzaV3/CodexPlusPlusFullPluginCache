---
name: magister-marketing-plan
description: Work a brand's Magister marketing plan — find the highest-priority task, read its brief, record progress, add or edit tasks, and change roadmap strategy. Use when the user asks what to work on next, what their marketing plan says, how a task is going, or wants to add, update, complete, or reprioritize marketing work.
---

# Working a Magister marketing plan

A Magister **project** is one brand or client. Each project has one live
**marketing plan** built from that brand's audit evidence, organized into moves
across acquisition, activation, retention, referral, and revenue, and broken
into **plan items** — the individual pieces of work.

## Always resolve the project first

Every plan tool needs a `project_id`. Get it from `list_projects`. Never guess
one, never reuse an id from an earlier conversation, and never construct one.

If `list_projects` returns exactly one project, use it without asking. If it
returns several, ask which brand the user means before doing anything else.

## Answering "what should I work on?"

Call `get_next_plan_item`. It returns the single most actionable item **plus a
self-contained `brief_markdown`** that already explains the work, the reasoning,
and the acceptance criteria.

Present that brief. Do not re-derive the task from the plan, do not summarize it
into something shorter unless asked, and do not invent steps it does not
contain. If the user wants the wider picture instead, `get_marketing_plan`
returns the whole plan with its sections and items, and `get_plan_item` returns
one item in full including its recent timeline.

## Recording progress

- `update_plan_item_status` — mark an item running, completed, reopened,
  blocked, or skipped. Status changes are reversible, so no confirmation is
  needed beyond the user's request.
- `add_plan_item_note` — append a progress note to an item's timeline. Use this
  for findings and context that should survive the conversation.

Record status honestly. If work partly succeeded, say so in a note rather than
marking the item completed.

## Changing the plan itself

- `create_plan_item` adds a new item; `update_plan_item` edits an existing one's
  title, description, task instruction, expected impact, phase, due date, or
  priority. Both are ordinary edits.
- `set_plan_preferences` and `recompile_marketing_plan` are different in kind.
  **A recompile replaces the live plan's sections and items with a newly
  generated version.** Any hand-authored item the user added can disappear from
  the active plan.

Before calling either one, tell the user plainly that the current plan will be
regenerated and wait for them to confirm. `recompile_marketing_plan` also
**spends the organization's credits**, so say that too.

Changing only notes or non-roadmap preferences does not trigger a recompile.
When `set_plan_preferences` does start one, it returns a compile run — poll it
with `get_compile_run` rather than calling recompile again.

## Background work

A recompile runs in the background. Poll `get_compile_run` until it reports a
terminal state. Never start a second recompile because the first has not
finished, and never report a new plan before the run completes.

## Useful context tools

- `get_brand` — the audited brand profile: positioning, audience, voice, and
  messaging pillars. Read this before drafting anything in the brand's voice.
- `get_audit_health` — the overall health score and per-channel breakdown from
  the last completed audit. It needs the audit plan id that `get_marketing_plan`
  supplies.
- `list_recent_activity` and `list_agent_artifacts` — what has recently been
  worked on and shipped for the project.

## Do not infer

- Never state a score, status, due date, or priority the tools did not return.
- Never claim an item is done because you drafted something; only a status write
  makes that true.
- If a tool reports the organization is out of credits, tell the user they need
  to upgrade and stop. Do not retry it and do not substitute another metered
  tool.
