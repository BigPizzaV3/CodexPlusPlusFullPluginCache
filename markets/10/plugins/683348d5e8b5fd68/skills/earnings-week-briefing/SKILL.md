---
name: earnings-week-briefing
description: Briefing on the week's earnings from the published weekly preview: who reports on which day and session, which names carry the largest options-implied moves next to their own history, and a closer look at up to three reporters. Use when the user asks who reports this week or next week, what is on the earnings calendar, or which upcoming earnings have the biggest expected moves.
---

Use this skill when the user asks about the week's earnings as a group rather than one ticker.

1. Call `get_weekly_earnings_preview` (pass `day` only when the user names a date). State the period
   from `period_start` and `period_end`; the preview may already show next week, so never call it
   "this week" from the page name alone. Say it is a curated public preview, not the complete calendar
   (`coverage`), and repeat any `warnings` that apply.
2. Present the rows grouped by `date`, then `session` (BMO = before the open, AMC = after the close),
   with `implied_move_pct`, `average_move_pct` and `last_report_move_pct`. When asked which moves are
   largest, rank by `implied_move_pct` and also by the ratio of implied to average, and say which ranking
   you used.
3. For up to three names the user picks (or the three highest implied-to-average ratios when they ask
   for the most notable), call `get_stock_earnings_snapshot` and summarise each in two or three lines:
   date and session, implied versus average and median, last report.
4. When the user asks why implied moves differ or what happens to options after the report, call
   `search_earnings_wiki` with the concept ("implied move", "IV crush", "IV rush"), `limit` 1 or 2,
   and ground the answer in the returned excerpt.
5. End with the sources: the preview `source_url` and each snapshot `source_url` exactly as returned
   (keep the query string), plus their `as_of` dates.

Numbers come only from the tool results of this conversation. The weekly table's last-report column
is not the same measure as a snapshot's `close_pct`; do not mix them. If the user asks for the complete
calendar, the scanner or the simulator, relay the `platform_tools` sentence from the result once, as a
plain statement of where those tools live; otherwise leave it out. No trade recommendations.
