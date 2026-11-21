---
name: weekly-content-batch
description: >
  Draft and schedule a week of social media content for a PostQuickAI content
  group. Use when the user says "plan my week", "batch this week's content",
  "weekly content", or references scheduling multiple posts at once.
---

# Weekly Content Batch

## Goal
Prepare 5–7 brand-aligned drafts, get approval, then schedule them across the week.

## Workflow

1. **Pick the brand.** Call `listContentGroups`. If multiple groups exist, ask the user which brand.

2. **Load brand context.** Call `getInstructions` and `getBrandContext` for that group. Use the returned voice, audience, tone, and topics.

3. **Check destinations.** Call `listAccounts`. Ask the user to choose among connected accounts if the destination is not clear.

4. **Collect topic seeds.** Ask for 5–7 topics, or propose topics based on the saved brand context. Wait for approval.

5. **Prepare each draft.** For each approved topic:
   - Call `generateCaption`, `generateCarouselCaption`, or `generateVideoCaption` for the requested format.
   - Call `createPost` to save text or carousel content as a draft. Use `createVideo` only when the user supplied a public video URL.
   - Keep the returned ID and content preview.
   - If a tool returns `LIMIT_EXCEEDED`, stop and say how many drafts were created.

6. **Preview the batch.** Show every draft, destination, date, time, and timezone. Do not schedule anything until the user confirms the full batch.

7. **Schedule the approved batch.** Call `bulkSchedule` once with the approved post, video or story IDs, destinations and timestamps. The batch either succeeds together or makes no schedule changes. Use `getCalendar` to check the saved campaign. Respect the user's requested spacing; ask if two items conflict.

8. **Return a summary.** Include date, time, timezone, platforms, content preview, and draft ID.

## Error handling

- `LIMIT_EXCEEDED` — stop; never retry silently.
- A missing content group or account — refresh with `listContentGroups` or `listAccounts`; never invent an ID.
- A failed or timed-out write — check each saved item and `getCalendar` before deciding whether another attempt is safe. Never blindly retry a write.

## Never do

- Never schedule before showing the full batch and receiving approval.
- Never exceed the requested post count.
- Never skip the saved brand instructions when they are available.
- For cancellation, show the affected future schedules and obtain approval before `cancelSchedule`. Cancellation cannot recall already published items or accepted publishing work.
