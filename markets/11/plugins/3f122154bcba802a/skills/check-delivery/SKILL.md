---
name: check-delivery
description: Inspect Postroom queue and delivery receipts and cancel queued posts. Use for status checks, blocked or uncertain outcomes and cancellation requests.
---
Call yet_queue, then yet_post_status for relevant IDs. Report actual states and confirmed provider receipts. Never fabricate publication or analytics.
Use yet_analytics for available cached metrics and disclose their freshness. Relay provider errors; do not blindly retry uncertain writes.
Identify the exact queued post before calling yet_cancel. Ask for cancellation approval unless the user already explicitly requested that cancellation. Do not delete live posts, cancel unrelated posts or expose other workspaces or credentials.
