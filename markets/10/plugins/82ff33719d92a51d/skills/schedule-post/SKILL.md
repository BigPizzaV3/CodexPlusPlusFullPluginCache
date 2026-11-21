---
name: schedule-post
description: >
  Schedule a single social media post to one or more platforms for a specific time.
  Use when the user says "schedule a post", "post tomorrow", "post at 3pm", or
  references scheduling one specific post. For batch scheduling of multiple posts,
  use weekly-content-batch instead.
---

# Schedule a Post

## Goal
Create one draft and schedule it for a specific time on one or more platforms.

## Workflow

1. **Identify the brand (content group).** Reuse the known content group from the conversation. If it is unknown, call `listContentGroups`; ask which one when multiple groups match.

2. **Check destinations.** Reuse destinations already confirmed in the conversation. Otherwise call `listAccounts` for the selected content group. Use only connected accounts.

3. **Prepare or retrieve the draft.**
   - For new content, preserve user-supplied text or draft text in the conversation. Call `generateCaption` only when the user specifically asks to use PostQuickAI's caption generator. Call `createPost` to save the approved text as a draft.
   - For an existing draft, reuse its known ID or call `listPosts` to locate it. Call `getPost` and read back its current content before scheduling.

4. **Resolve the time.**
   - Convert natural language such as "tomorrow at 9am" to an ISO 8601 timestamp in the user's timezone.
   - The time must be at least 5 minutes in the future.
   - Ask when the date, time, or timezone is ambiguous.

5. **Confirm.** Show the complete content, connected destination accounts, and exact scheduled time. Get approval before calling `schedulePost`.

6. **Schedule.** Call `schedulePost` once for the approved draft ID and time. Return the post ID and scheduled time. Use `getCalendar` when the user wants to check surrounding schedules. If asked to cancel, inspect the saved item and obtain approval for `cancelSchedule`; do not claim already accepted publishing can be recalled.

## Error handling

- `LIMIT_EXCEEDED` — stop and explain that the action is currently unavailable; do not promise completion.
- A missing content group or account — call `listContentGroups` or `listAccounts` again; never invent an ID.
- A past scheduled time — ask the user for a new future time.

## Never do

- Never schedule before the user confirms the content, destinations, and time.
- Never target an account that is not connected to the signed-in PostQuickAI account.
- Never claim delivery until the saved post reports publishing results.
