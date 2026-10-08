---
name: grant-tracker-update
description: Use when the user reports an outcome or change on a grant they're tracking — a submission, an award, a decline, a new amount, a change of owner, or award period dates — and it needs to be recorded in Instrumentl.
---

# Grant tracker update

Record changes to a saved grant in the user's tracker.

## Ground rules

- **"My grants" is ambiguous.** Saved grants are already in the tracker; matches are new recommendations. Ask one short clarifying question rather than guessing.
- **Confirm before any write.** Restate exactly what will change and wait for a yes.
- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** Never guess a dollar amount or a date the user didn't state.
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budgets, recording actual expenses.

## Money format

Amounts on a saved grant — requested and awarded — are **dollars**, not cents. Send `25000` for $25,000. This differs from budget and expense figures elsewhere in Instrumentl; don't carry a cents conversion over from those.

## Workflow

1. **Find the saved grant.** Search by grant name or project name through `list_saved_grants`. Because a saved-grant record carries only IDs, resolve the grant's display name through `list_grants` before you restate anything back to the user. If the same grant is tracked across more than one project, **ask which project's record** they mean — they are separate records and updating the wrong one is silent.

2. **Map what the user said to the right fields**: pipeline status, amount requested, amount awarded, owner, award notification date, award period start and end, notes, or fiscal year. Resolve a named owner to a user record via `list_users` first.

3. **Restate what will change and get confirmation.** Only the fields you pass are touched; everything else is left alone.
   - **Status, amount requested, and amount awarded are readable beforehand** — state the before-and-after for these.
   - **Notes, owner, fiscal year, notification date, and award period dates are not readable beforehand.** Do not assert a current value for them. Say what the new value will be, and if the prior value matters, ask the user rather than guessing.
   - A null amount means unknown, not zero. Don't describe filling one in as "changing it from $0."

4. **Warn before setting status to researching.** That clears the requested amount and submission goals, matching the app's behavior. Say so explicitly and get a second confirmation before proceeding.

   **The awarded amount only persists on an awarded grant.** If the status is not awarded (active or closed), a saved awarded amount is silently cleared — so when recording an award, set the status and the amount in the same update, and warn that moving a grant out of an awarded status drops its awarded amount.

5. **Award period dates must be consistent** — the start date has to fall on or before the end date. If the user gives dates that don't, ask rather than reordering them.

6. **Apply and confirm.** The update response comes back with the grant name, funder, project, and owner already filled in — use those to confirm in plain language. No follow-up lookup is needed after a write.

7. **Offer the natural next step** — for example a report deadline task on a newly awarded grant. Hand off to the task management skill rather than creating it here.

## Guardrails

- **"Remove this grant" means hide, not delete.** Hiding marks the grant as no longer saved. Explain that everything attached to it — submission goals, tasks, expenses — is preserved and that it can be restored from the Instrumentl app (not from here). Confirm before hiding.
- Never guess a dollar amount or a date the user didn't state.
- Moving a grant to a different project is a real change with downstream effects on reporting — confirm it explicitly rather than treating it as a minor edit.
- If the user wants to record an outcome on an opportunity that isn't in the tracker yet, that's a save, not an update — hand off to the match triage skill.
