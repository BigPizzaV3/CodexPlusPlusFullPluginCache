---
name: grant-pipeline-review
description: Use when the user asks where their grant pipeline stands — a status rollup, what's stalled, totals requested or awarded, or prep for a board or leadership update.
---

# Grant pipeline review

Report on the state of the user's tracked grants. This skill is read-only.

## Ground rules

- **"My grants" is ambiguous.** Saved grants are already in the tracker; matches are new recommendations. Ask one short clarifying question rather than guessing.
- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** If a fact isn't in the record, say the record doesn't cover it.
- **Money formats differ by source.** Budget figures are integer cents (divide by 100). Expense amounts are decimal dollar strings (use as-is).
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budgets, recording actual expenses.

## Resolving names before you present anything

Saved-grant records contain **only IDs** — no grant name, no funder, no deadline. You must resolve them or the output is unusable:

1. Call `list_saved_grants` with the user's scope.
2. Collect the `grant_id` values from the results.
3. Resolve them in a **single** `list_grants` call passing all of them at once, which returns each grant's name, funder, and next deadline.
4. Resolve owner and assignee references through `list_users`.

If a row fails to resolve, say that row couldn't be loaded. Never infer a grant's name or deadline from surrounding context.

## Workflow

1. **Pull saved grants**, scoped to a project or fiscal year if the user named one.

2. **Group by pipeline status** — researching, planned, started, LOI in progress, submitted, LOI submitted, awarded, closed, declined, abandoned. Report counts and dollar totals (requested, awarded) per group. Amounts on a saved grant are already in dollars; do not convert them.

3. **Surface what's stuck**: grants sitting in researching or started well past the grant's next deadline, and grants with no owner. The deadline comes from the resolved grant record, not the saved grant.

4. **If they're prepping for a meeting**, lead with the three things that changed or need a decision, not the full table.

5. **Offer the follow-on action** — update a status, assign an owner, add a task — and hand off to the tracker update or task management skill. Do not perform the write here.

## Guardrails

- Say explicitly that totals are calculated live from their records in this conversation, not pulled from a saved Instrumentl report.
- This skill does not write. If the user asks to change something, hand off rather than acting.
- A saved grant with a null requested or awarded amount is unknown, not zero. Exclude it from totals and note how many rows were excluded.
