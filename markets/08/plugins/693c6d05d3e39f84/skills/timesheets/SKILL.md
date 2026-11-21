---
name: timesheets
description: Review, submit, cancel, or resubmit your eHour timesheet, or check team submission status. Use for eHour approval and missing-submission questions.
---

# Review and submit eHour timesheets

Use the connected eHour tools and inspect their live schemas. If the connection
is unavailable, ask the user to connect eHour. Reuse IDs returned by the server;
do not invent approval, user, or team IDs.

## Review and submission

Use `getTimesheet` for the requested inclusive date range. Summarize recorded
hours by day or project as useful, and distinguish tracked time from approval
state. Missing entries do not establish the user's expected working hours.

“Review,” “check,” and “prepare” do not authorize submission or time changes.
`submitTimesheet` is for the caller's own timesheet and requires an explicit
submission request. It expands partial ranges to full weekly or monthly
approval periods according to tenant configuration. Inspect the approval
timeframes in `getTimesheet`; clarify if the actual period exceeds what the
user intended. Report the returned periods and status, not an assumed approval.

For an explicit cancellation, obtain `approvalId` from `getTimesheet.approvals`
and use `cancelTimesheetSubmission`. For an explicit resubmission, correct only
the requested entries, then use `resubmitTimesheet` on the rejected record.
These actions are self-only. Do not promise that this plugin can approve or
reject somebody else's timesheet; the inspected server has no such tools.

After an uncertain submission result, read current approval state before
retrying. Surface conflicts and locked periods; do not cancel another
submission merely to make a new one succeed.

## Who has submitted?

Use `listSubmissionStatus`, with the requested date range and team or user
filter. User and team filters cannot be combined. Resolve a team with
`listTeams` when needed. Do not fan out from `listUsers` to individual
timesheets: the submission-status tool already returns per-person status.

For an organization-wide request, query the visible teams and deduplicate
people appearing in multiple teams. Describe the result as coverage of the
accessible teams: users outside teams or outside the caller's management scope
may be missing. Do not claim full organizational coverage without evidence.

Keep not submitted, pending, rejected, and approved states distinct. A report
of tracked hours cannot prove submission status, and zero hours alone does not
prove a missing submission. Never disclose people outside the returned scope.
