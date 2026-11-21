---
name: set-up-routines
description: Set up, change, pause or explain a recurring Folio delivery — a morning brief, a weekly digest, an RSS subscription that feeds it — so issues arrive on the user's device on a schedule.
---

Use this when the user wants something to happen repeatedly rather than once: "every morning, gather the local news into an editorial brief on my reMarkable", "send me a digest every Friday", "stop the daily one", "what's scheduled?".

Read before writing. Call `list_schedules` first: it returns existing routines with their cadence and next run, and the user often means "change that one", not "make another".

To create or change a routine, call `manage_schedule`:

- `action` is `create`, `update`, `pause` or `resume`. Everything but create needs the `id` from `list_schedules`.
- `cadence` is one of `daily`, `weekdays`, `weekly`, `biweekly`. Anything else needs settings this tool cannot reach; say so plainly and point the user at the Folio web app rather than guessing a near-miss.
- `time` is the user's local time as `"HH:MM"`, defaulting to 08:00. `weekday` is 0 for Sunday, for the weekly and biweekly cadences.
- `categories` narrows a routine to certain kinds of saved reading; `min_to_send` holds the issue back until enough has piled up; `max_items` caps it.

A routine only sends what the inbox actually has. If the user wants a topic to arrive on its own — local news, a newsletter, a blog — the source has to feed the inbox first: call `list_feeds` to see what is subscribed and `manage_feed` with `action: "subscribe"` and the feed URL to add one, setting `auto_add` so new items land in the inbox without being asked for. `list_sources` shows the other integrations already connected.

Confirm in one sentence in the user's own terms — what arrives, how often, on which device — not a field-by-field readback. Say when the first one lands.
