---
name: track-time
description: Log, correct, or move time entries and start or stop timers in eHour. Use when the user asks to record or reassign work in their connected eHour account.
---

# Track time in eHour

Use the connected eHour MCP tools. Names below are the server's canonical names;
the host may namespace them. Inspect the live tool schemas before calling them.
If the connection or required tool is missing, ask the user to connect eHour.
Do not substitute a local file or claim that time was saved.

## Log or correct time

1. Establish the date, duration, and assignment. Use ISO dates and decimal hours
   (90 minutes is 1.5 hours). Resolve relative dates using known user context;
   ask when the date or timezone is ambiguous. Do not infer hours from meetings
   or other activity unless the user requested that workflow.
2. Resolve the assignment with `getAssignments` for the current user, or
   `listAssignments` for an explicitly requested other user. `trackTime` also
   accepts project code or name, narrowed by task and client. Reuse returned
   prefixed IDs; a project ID is not an assignment ID. Ask the user to choose
   when the server returns disambiguation candidates. Keep prefixed IDs internal
   and refer to projects by name, code, and task in user-facing replies unless
   the user explicitly asks for technical identifiers.
3. Use `addTime` for an explicit increment or reduction such as “add another
   hour” or “subtract 30 minutes.” It appends one signed adjustment and preserves
   existing detail rows, comments, tags, sources, and time windows. Generate a
   UUID `operationId` once for each logical adjustment and reuse that same UUID
   if the call must be retried; do not generate a new ID for a retry. Use
   `trackTime` when the user specifies the desired assignment total for the day.
   Clarify “log two hours” when replacement versus addition is unclear.
4. Read `getTimesheet` before replacing an existing total with `trackTime`.
   Omitted comments can affect existing comments; preserve the intended comment
   and ask if merging multiple comments is unclear. `hours: 0` deletes the
   assignment's time for that date, including its entry details; use it only
   when deletion is explicitly intended. Never use zero as a placeholder.
5. Report the returned result, date, assignment, and hours. A tool error is not
   success. After a timeout or uncertain write, reuse `addTime`'s operation ID
   for the retry. Read the timesheet before retrying other write tools.

Act on behalf of another person only when explicitly requested. Pass that same
user identity to both reads and writes. The server decides management access;
do not switch identities or use another API to work around a denial.

`trackTime` can collapse detailed time rows and discard their tags or start/stop windows.
A daily total does not prove that there are no such details.
If preserving detailed entries is required, explain this limitation and use the eHour interface instead of claiming the tool will preserve them.
Before replacing known detailed entries, make the loss of detail clear and obtain the user's agreement.

## Move time between assignments

Use `moveTimeEntries` to move existing entries between two assignments for the
same user. Resolve both assignments and prefer an explicit inclusive date
range. If the intended scope is unclear, ask which dates to move before calling;
"move my hours from A to B" does not by itself mean all recorded history.

Omitting either date leaves that side unbounded. Omitting both moves every
recorded entry from the source assignment. Before an unbounded move, explain
that scope, identify the source and target assignments and whose entries will
move, and obtain the user's confirmation. Preserve an explicit request to move
all entries; do not invent a cutoff or silently move only a recent period.

Report the returned entry count, hours, and effective dates. Do not fetch the
entire timesheet history just to prepare the move or invent preview totals.
The move is atomic: surface locked dates and other errors without silently
splitting the operation to move only the entries that succeed.

## Timers

Only one timer can run for a user. `startTimer` returns an `action` of `started`,
`already_running`, or `assignment_attached`; use that value instead of claiming
that every call started a new timer. It can store an optional comment. Do not
silently stop an existing timer to switch projects.

For a simple request such as "start my timer", call `startTimer` immediately
with no assignment arguments. Do not first call `getTimerStatus` or
`getAssignments`: `startTimer` safely returns the existing timer without
resetting it, and the server permits a newly started timer to remain unassigned.
When the user supplies a project code, project name, or assignment ID, pass it
directly to `startTimer`; the server resolves it. Call `getAssignments` only
after resolution fails or remains ambiguous. Use `getTimerStatus` only when the
user asks for timer status or elapsed time, or to recover from an uncertain
write result.

Use `updateTimer` to correct the running timer's project, task, or comment
without resetting its start time. Omitted assignment and comment fields are
preserved; an explicitly empty comment clears the comment. A task name supplied
without a project is resolved within the running timer's current project.

`stopTimer` records elapsed time. A timer may have no assignment; resolve one
before stopping in that case. An omitted stop comment reuses the timer's stored
comment. Ask for any required comment. Use the duration
returned by the tool, not a guessed elapsed time. After an uncertain stop, check
both timer status and the relevant timesheet before retrying.

`discardTimer` cancels the running timer and permanently discards its elapsed
time without creating a timesheet entry. Use it only when the user explicitly
asks to cancel, discard, or stop without saving. Do not substitute it for
`stopTimer`. Report the discarded project and duration returned by the tool.

Locked dates, budget limits, required tags/comments, and missing permissions
must be resolved through supported eHour behavior. Do not fabricate a tag,
unlock a date, or change a budget to make the time entry succeed.
