# Action-item and deadline rules

## When to create an action

Create an action item when the source supports an expected task, such as a participant saying “I'll do X,” a clear assignment (“Alex, please send X”), or an explicit team agreement to complete X. A wish, suggestion, hypothetical, question, or general concern is not automatically an action.

For each task, extract only supported fields:

| Field | Rule |
|---|---|
| Task | Describe the concrete deliverable or next step without expanding scope. |
| Owner | Use the named person only when they accepted or were clearly assigned the task; otherwise `UNASSIGNED`. |
| Supporting people | Include only explicitly involved participants. |
| Deadline | Preserve the exact phrase; use `NOT_SPECIFIED` if absent. |
| Resolved date | Add only when the meeting date and reference are unambiguous; retain the original phrase too. |
| Priority/status | Include only when stated; do not derive priority from urgency of tone alone. |
| Dependency | Include only a stated prerequisite or blocker. |
| Evidence | Add the source location or a brief excerpt when useful and available. |
| Confidence | `HIGH`, `MEDIUM`, or `LOW`, using the skill's confidence rules. |

## Owner detection

- “I’ll send the draft” belongs to that speaker if the speaker identity is reliable.
- “Can someone send the draft?” has no owner unless a person accepts it later.
- “Jordan should send it” is a proposal or expectation, not a confirmed assignment unless accepted or clearly agreed.
- If names are ambiguous or speakers cannot be mapped reliably, preserve the speaker label and mark the owner `UNASSIGNED` or `UNCLEAR`.
- Never assign an action to a manager, team lead, or department based only on their role.

## Deadline handling

Preserve original wording such as “by Friday,” “in two weeks,” or “after launch.” Resolve it only when the meeting date, locale/context if needed, and reference point make one date clear. When resolved, show both: `Original: by Friday; resolved: 2026-10-09`.

Do not calculate from the current date if the meeting date is missing. Do not guess year, time zone, whether “next Friday” means the coming Friday or the following one, or what event “after launch” refers to. Use `NOT_SPECIFIED` when absent and `UNCLEAR` when wording exists but cannot be resolved.

## Duplicate actions and changes

Merge repeats only when they clearly describe the same deliverable, owner, and intended deadline. Keep separate tasks when a deliverable or deadline differs. If an action changes later, use the latest clearly agreed version and mention the revision when useful. Do not silently drop a conflict that the source leaves unresolved.
