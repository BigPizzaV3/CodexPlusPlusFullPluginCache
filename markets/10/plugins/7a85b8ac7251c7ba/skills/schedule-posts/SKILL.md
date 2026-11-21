---
name: schedule-posts
description: "Create and schedule new social posts in Velocity for selected connected accounts. Use for new-post scheduling or explicit immediate publishing requests."
---

# Schedule Posts

Use the authenticated Velocity MCP tools and their current schemas. Act within the user-requested workspace and scope. If tools are unavailable or authentication is required, explain the connection issue; do not substitute fabricated results.

Call list_connected_accounts to resolve the exact social_connection_id; use list_brands for a named brand. Do not write to an account marked needs_reconnect. Preserve the user's caption, hashtags and line breaks unless editing was requested. create_post requires social_connection_id and content. Provide scheduled_at as ISO 8601 with an offset, or local YYYY-MM-DDTHH:mm with an IANA timezone. Ask when timezone or target is ambiguous. Set publish_now true only for an explicit immediate-publishing request. One post targets one account; create separate posts only for the user's chosen targets. upload_media can prepare user-supplied media; pass returned URLs in media_urls. Read back with get_post and report persisted status and local scheduled time.

## User-facing results

Keep post, account, brand and platform IDs, raw JSON and storage paths out of ordinary replies. Use platform and @handle, brand name, a caption excerpt, media type/count, readable status, and dates in the user's timezone. Resolve missing account labels with list_connected_accounts; do not guess. Keep exact IDs in tool calls for follow-up actions. Show technical identifiers only when explicitly requested for diagnostic or integration work. Distinguish queued/scheduled from published, and summarize errors with the next useful action. Use only verified media and published links returned by tools; never substitute an illustrative web image or invent a link from an ID.
