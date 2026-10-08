# Habits, routines, journals, and reminders tool map

Read `cora_get_habits` before mutating an existing named habit, routine, or
journal. Keep their IDs and event semantics separate.

## Habits

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_get_habits` | List active habits, routines, journals, and all three ID types. | Use as the canonical named-record lookup. |
| `cora_get_habit_progress` | One habit's streak and completion history. | Accepts a habit `goal_id`, not a routine/journal ID. |
| `cora_create_habit` | Create one measurable or manual-checkoff habit. | Pick a supported metric; do not model a checklist or question as a habit. |
| `cora_log_habit_event` | Mark a manual/binary habit done. | Do not manually log an automatically measured habit; re-read progress. |
| `cora_pause_habit` | Pause streak tracking. | Resolve exact `goal_id`, then re-read habits. |
| `cora_resume_habit` | Resume a paused habit. | Resolve exact `goal_id`, then re-read habits. |
| `cora_delete_habit` | Permanently delete one habit. | Confirm exact title/ID unless explicitly requested; verify absence. |

## Journals and check-ins

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_create_journal` | Create a recurring user-entered check-in question. | Define input kind and matching options/scale when needed. |
| `cora_update_journal` | Patch an existing journal definition. | Resolve `checkin_id`; only supplied fields change. |
| `cora_delete_journal` | Permanently delete one journal. | Confirm exact title/ID unless explicitly requested; verify absence. |
| `cora_log_checkin_event` | Record a value for a journal/check-in. | Match the value to its input kind and use `checkin_id`. |

Use a journal for a recurring question such as mood or soreness. Do not turn a
numeric check-in into a binary habit event.

## Routines

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_create_routine` | Create a scheduled ordered checklist with one to eight steps. | Do not model its steps as separate habits unless the user asks. |
| `cora_update_routine` | Patch routine metadata or replace its checklist. | Supplying `steps` replaces every step; read/explain scope first. |
| `cora_delete_routine` | Permanently delete one routine. | Confirm exact title/ID unless explicitly requested; verify absence. |
| `cora_complete_routine` | Mark one routine complete for a local day. | Resolve `routine_id`; completion is idempotent for that day. |

## One-shot reminders

| Tool | Choose it for | Resolve or verify |
|---|---|---|
| `cora_set_reminder` | Schedule one static push message at one local date/time. | Notifications must be enabled; it is not recurring and does not run AI. |
| `cora_list_reminders` | List pending one-shot reminders and their IDs. | Requires reminder permission even though it is a read. |
| `cora_cancel_reminder` | Cancel one pending reminder. | Resolve `reminder_id`; confirm exact cancellation unless explicitly requested. |

For “remind me once tomorrow at 3,” use the one-shot reminder flow. For a
generic “every day” reminder, surface the capability gap; do not pretend a
one-shot reminder recurs and do not create a habit merely as a workaround.
When the user actually wants a recurring checklist or check-in, a routine or
journal can include reminder settings. Habit reminder creation or mutation and
recurring AI tasks are not exposed through this MCP.
