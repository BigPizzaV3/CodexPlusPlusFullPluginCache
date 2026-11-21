---
name: analytics
description: "Read available Velocity analytics, engagement snapshots and best-time-to-post data. Use for social performance questions and timing recommendations grounded in workspace data."
---

# Social Analytics

Use the authenticated Velocity MCP tools and their current schemas. Act within the user-requested workspace and scope. If tools are unavailable or authentication is required, explain the connection issue; do not substitute fabricated results.

Use list_brands to resolve a requested brand; inspect list_connected_accounts when the user names a handle/platform. Call get_analytics with the applicable brand and schema-supported filters. Distinguish empty or unavailable metrics from zero performance. Report the data period and timezone when provided, and separate observed metrics from recommendations. Best-time-to-post data is guidance, not a guarantee. Do not invent trends from missing snapshots or imply live platform coverage beyond returned data. This workflow does not schedule or modify posts.

## User-facing results

Keep post, account, brand and platform IDs, raw JSON and storage paths out of ordinary replies. Use platform and @handle, brand name, a caption excerpt, media type/count, readable status, and dates in the user's timezone. Resolve missing account labels with list_connected_accounts; do not guess. Keep exact IDs in tool calls for follow-up actions. Show technical identifiers only when explicitly requested for diagnostic or integration work. Distinguish queued/scheduled from published, and summarize errors with the next useful action. Use only verified media and published links returned by tools; never substitute an illustrative web image or invent a link from an ID.
