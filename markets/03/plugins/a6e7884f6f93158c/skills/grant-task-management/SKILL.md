---
name: grant-task-management
description: Use when the user wants to create, assign, reschedule, or complete tasks and deadlines on the grants in their tracker, or wants a prep checklist built out from a grant deadline.
---

# Grant task management

Create and change task records on the user's tracked grants.

## Ground rules

- **"My grants" is ambiguous.** Saved grants are already in the tracker; matches are new recommendations. Ask one short clarifying question rather than guessing.
- **Confirm before any write.** Restate exactly what will change and wait for a yes.
- **No internal identifiers in output.** Never show an ID, cursor, or API field name.
- **Never invent grant data.** If a fact isn't in the record, say the record doesn't cover it.
- **Out of scope** — say so plainly and point to the Instrumentl app: creating or configuring projects, writing or storing proposal narrative, building or restructuring budgets, recording actual expenses.

## Workflow

1. **Identify the saved grant** the task belongs to. Every task attaches to a saved grant — there is no free-floating task. Find it by grant name or project name through `list_saved_grants`, and resolve the display name through `list_grants` so your confirmation names the grant in plain language.

2. **Resolve any named teammate to a user record** via `list_users` before assigning. Search matches first name, last name, or email. Do not try to find people through the task people-filters — those only surface users already on a task, not everyone on the account. If a name matches more than one person, ask which.

3. **Pick the task kind**: full proposal, report, general, letter of inquiry, or cultivation. If the user's intent doesn't clearly map to one, ask rather than defaulting.

4. **Set the deadline** as a date and time. Never invent a date the user didn't state — ask.

5. **For a prep checklist from a deadline**, propose the full list of tasks with their dates first, get **one** confirmation, then create them in a **single batch**.

6. **Report what actually happened.** Rows are processed independently and a failed row does not roll back the others, so the response may be partially successful. Always report failures explicitly and in plain language:
   - the saved grant wasn't found or belongs to another account
   - an assignee isn't a member of this account
   - the caller lacks permission for that row
   - the row failed validation

## Tasks cannot be deleted

There is no delete operation. A task can only be created, updated, or marked complete. If the user asks to delete or remove a task, say plainly that deletion happens in the Instrumentl app.

**Do not mark a task complete as a substitute and describe it as removed.** A completed task still exists, and because completed tasks are hidden from the default tracker view, the user can easily believe it's gone when it isn't. If marking it done is what they actually want, confirm that first and say clearly that the task remains on the grant.

## Guardrails

- **Never assign work to a teammate without confirming** — restate who is getting what, by when.
- **Never mark a task complete on the user's behalf unless they explicitly said so.** Completing is a write like any other; reopening a completed task is also a write and needs the same confirmation.
- Never reschedule or reassign in bulk without listing every affected task first.
- If the user has a calendar connected in ChatGPT, you may offer to suggest blocking prep time. Frame it as available only when their other tools are connected — don't promise it, and don't imply Instrumentl writes to their calendar.
