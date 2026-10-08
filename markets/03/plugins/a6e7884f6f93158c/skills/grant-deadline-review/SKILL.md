---
name: grant-deadline-review
description: Use when the user asks what grant work is due, what's overdue, or who owns what across the tasks and deadlines on the grants in their tracker.
---

# Grant deadline review

Answer questions about upcoming and overdue grant work. This skill is read-only.

## Ground rules

- **"My grants" is ambiguous.** Saved grants are already in the tracker; matches are new recommendations. Ask one short clarifying question rather than guessing.
- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** If a fact isn't in the record, say the record doesn't cover it.
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budgets, recording actual expenses.

## Resolving names before you present anything

Task records contain **only IDs** — no person name, no grant name. A readable answer needs three hops:

1. `list_tasks` returns `assignee_id`, `nominator_id`, and `saved_grant_id`.
2. Resolve people with `list_users`.
3. Resolve the grant by taking the task's saved grant through `list_saved_grants` to get its `grant_id`, then a single `list_grants` call for the name and funder.

If a lookup fails, say that row couldn't be loaded rather than inferring.

## Workflow

1. **For "what's due"**: pull open tasks in the requested window plus anything past due, sorted by date. **Call out overdue items first.**

2. **Disambiguate person references before filtering.** "Sarah's tasks" could mean assigned to, created by, completed by, or nominated (handed off) by her — these are four separate filters that compose with AND, so the wrong one returns wrong results. Ask: "Do you mean tasks assigned to Sarah, ones she created, ones she completed, or ones she handed off?"

3. **Filter by task kind with care.** Kinds are full proposal, report, general, letter of inquiry, and cultivation — but **older tasks may have no kind recorded at all**. If the user asks for a specific kind, say plainly that tasks without a recorded kind won't appear, and offer to show the unclassified ones too.

4. **Report unowned work** when relevant — tasks with no assignee are a common gap in a deadline review.

5. **Offer the follow-on action** — create, assign, reschedule, or complete a task — and hand off to the task management skill. Do not perform the write here.

## Guardrails

- This skill does not write. If the user asks to create, assign, or complete anything, hand off rather than acting.
- Never mark a task complete or assign work as a side effect of a status question.
- A task with a deadline earlier than its creation date is a data artifact, not necessarily overdue work — report it as recorded and don't editorialize.
