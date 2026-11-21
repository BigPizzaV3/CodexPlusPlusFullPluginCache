---
name: edit-posts
description: "Edit captions and media, reschedule, or cancel existing Velocity posts. Use for changes to existing posts rather than new-post creation."
---

# Edit & Cancel Posts

Use the authenticated Velocity MCP tools and their current schemas. Act within the user-requested workspace and scope. If tools are unavailable or authentication is required, explain the connection issue; do not substitute fabricated results.

Find the exact post with list_posts or search and read get_post before changing it. Check list_connected_accounts before writes. update_post changes caption or media for pending or failed posts; preserve all unrequested fields. reschedule_post changes the schedule; use the user's timezone, asking only if unknown. attach_media adds supplied media according to its schema; preserve existing media unless replacement was requested. Confirm cancellation unless the user already authorized cancellation of the specific post. cancel_post deletes the post; do not promise recovery or a cancelled row. Read back after a write; after cancellation, verify absence. Report the resulting status/time and summarize errors.

## User-facing results

Keep post, account, brand and platform IDs, raw JSON and storage paths out of ordinary replies. Use platform and @handle, brand name, a caption excerpt, media type/count, readable status, and dates in the user's timezone. Resolve missing account labels with list_connected_accounts; do not guess. Keep exact IDs in tool calls for follow-up actions. Show technical identifiers only when explicitly requested for diagnostic or integration work. Distinguish queued/scheduled from published, and summarize errors with the next useful action. Use only verified media and published links returned by tools; never substitute an illustrative web image or invent a link from an ID.
