---
name: competitor-intelligence-brief
description: Turn Linkeddit competitor monitors, briefs, switching signals, and page snapshots into an evidence-backed competitive update or battlecard when users ask about competitor moves or market changes.
---

# Competitor intelligence brief

Use `list_competitor_monitors` to resolve the competitors and monitor IDs available to this account. A tracked competitor is not access to that company's private account. Use the current connected tool schemas and avoid inventing missing IDs or records.

For one competitor, retrieve `get_competitor_brief`. For a weekly overview, start with `get_weekly_brief`, using the requested week if supplied. Add `get_switching_signals` or `get_competitor_changes` only when they help answer the request. Respect the actual returned window, generation date, limits, and missing data; a latest brief may be older than the requested period.

Distinguish competitor announcements, buyer complaints, observed changes, and your interpretation. For page comparisons, compare snapshots of the same URL at different timestamps. A changed hash establishes a page changed; it does not prove a specific price or feature changed. Summary snippets may be truncated; request the tool's raw mode where available before making precise comparisons.

Deduplicate repeated reports of the same event. A single complaint or switching signal is evidence of that instance, not a market-wide trend or confirmed purchase. Report conflicting evidence and the number and independence of sources where known.

Produce the requested brief or battlecard with dated evidence links, implications for the user's product, and suggested responses. Separate verified product facts from positioning ideas. If no current brief exists, say so rather than inventing one. Do not create monitors, contact prospects, or publish comparisons as a side effect of producing a brief.
