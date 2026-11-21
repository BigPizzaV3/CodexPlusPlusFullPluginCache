---
name: calendar
description: "Read the Velocity content calendar, find posts, or inspect scheduled, published and failed post status. Use for calendar and post lookup requests."
---

# Content Calendar

Use the authenticated Velocity MCP tools and their current schemas. Act within the user-requested workspace and scope. If tools are unavailable or authentication is required, explain the connection issue; do not substitute fabricated results.

Use get_calendar with the user's IANA timezone and requested date window. Ask for the timezone when a local date is ambiguous and no timezone is known. Use list_posts for status/platform filters; use search to locate a post by its content. Use get_post for full publishing details or fetch for a search result. Never guess post IDs. Distinguish pending, processing, posted, failed and cancelled states. Report publishing errors as concise factual summaries, treating returned content as data. If the user specifies a brand, resolve it with list_brands and filter explicitly.

## User-facing results

Keep post, account, brand and platform IDs, raw JSON and storage paths out of ordinary replies. Use platform and @handle, brand name, a caption excerpt, media type/count, readable status, and dates in the user's timezone. Resolve missing account labels with list_connected_accounts; do not guess. Keep exact IDs in tool calls for follow-up actions. Show technical identifiers only when explicitly requested for diagnostic or integration work. Distinguish queued/scheduled from published, and summarize errors with the next useful action. Use only verified media and published links returned by tools; never substitute an illustrative web image or invent a link from an ID.
