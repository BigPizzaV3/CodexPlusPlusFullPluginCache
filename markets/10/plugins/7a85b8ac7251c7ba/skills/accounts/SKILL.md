---
name: accounts
description: "Inspect connected social accounts and brands in Velocity, including accounts needing reconnection. Use for account or brand questions, not for connecting new social accounts."
---

# Accounts & Brands

Use the authenticated Velocity MCP tools and their current schemas. Act within the user-requested workspace and scope. If tools are unavailable or authentication is required, explain the connection issue; do not substitute fabricated results.

Call list_connected_accounts for platform, handle, status and social_connection_id. Call list_brands when the user asks about brands or needs to select one. Use IDs returned by tools; do not infer them from handles. Explain needs_reconnect and direct the user to reconnect in Velocity; these tools do not connect accounts. Report which workspace or brand filter was used. Unfiltered account results may include multiple brands.

## User-facing results

Keep post, account, brand and platform IDs, raw JSON and storage paths out of ordinary replies. Use platform and @handle, brand name, a caption excerpt, media type/count, readable status, and dates in the user's timezone. Resolve missing account labels with list_connected_accounts; do not guess. Keep exact IDs in tool calls for follow-up actions. Show technical identifiers only when explicitly requested for diagnostic or integration work. Distinguish queued/scheduled from published, and summarize errors with the next useful action. Use only verified media and published links returned by tools; never substitute an illustrative web image or invent a link from an ID.
