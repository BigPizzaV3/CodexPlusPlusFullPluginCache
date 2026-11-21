---
name: social-calendar-review
description: Use when the user wants to review the content calendar of one or more brands: which posts are scheduled, drafted, waiting for client approval, published or failed in a period.
---

Review a brand's social media calendar. Read-only unless the user asks for a change. Reply in the user's language.

1. Call `list_brands` and confirm the brand and the period (by default the next 14 days).
2. Call `list_posts` for the brand and period. Group the posts by day and show network, status (draft, scheduled, pending_approval, published, failed) and the first line of the caption.
3. Point out gaps (days without posts), drafts that will never publish because they have no date, posts waiting for client approval and failed posts.
4. Offer next steps: give a draft a date with `update_post`, or prepare new posts with the publish-social-post skill. Never reschedule or retry a failed post on your own: ask the user first.

Rules:
- Make MCP calls one at a time.
- A post without `scheduled_at` is a draft and is never published until someone gives it a date.
