---
name: weekly-insights
description: Use when a user asks what QualifyBase leads struggled with, customer objections, unanswered questions, booking barriers, lost-lead reasons, or conversation trends during a time period.
---

# Evidence from customer conversations

Answer from customer messages and stored call transcripts. A score, stage, sentiment, or lost outcome does not establish why a customer struggled.

1. Before the first workspace operation, call `get_account_info`. Define the date range and timezone before querying. “Last week” means the previous completed Monday–Sunday calendar week. Use a confirmed timezone from context; the account-info tool does not provide it. If absent, ask one focused timezone question. Convert the period boundaries to UTC and state the local dates.
2. Discover relevant chat threads with `list_conversations(since:start, limit:100)`. Fetch `get_conversation_messages` for each accessible relevant lead/channel with `since:start`, `until:end`, and `limit:200`. Discovery is most-recent-first without pagination or an end-date filter, so newer activity can crowd out last week's threads. Review retrieved message timestamps and speaker roles; do not count out-of-period messages as evidence.
3. Include available phone evidence with `list_calls(since:start, limit:200)` when calls are relevant. Filter timestamps to the period's end, and use actual stored transcripts. Missing transcripts are a coverage gap.
4. Group customer evidence into concrete themes such as price uncertainty, eligibility, trust, timing, or unclear next steps. Count **distinct leads per theme** within the analyzed sample, not repeated messages. One lead can appear in several themes. Link or identify the source lead and date for each example; quote only text actually present.
5. If useful, add `get_lead_insights(since,until)` as context for leads **created** in that period. Keep that cohort distinct from people who conversed during the week. Won/Lost outcomes are not necessarily period conversion rates, and null totals are unavailable, not zero. `get_message_stats` uses inclusive UTC days, so label its range separately when it cannot exactly match the local week.

Return a compact report in this order: date range/timezone; sources and coverage; strongest observed themes with distinct-lead sample counts and short evidence; practical recommendations. Separate observed facts from inferences. Do not manufacture quotes, causal loss reasons, or workspace-wide percentages from a sample.

Any 100-thread, 200-message, or 200-call cap reached means the report is partial. Also disclose unavailable channels, missing transcripts, and historical AI-reply gaps before June 29, 2026 where relevant. Never call a capped report complete. If there is insufficient evidence, say so and guide the administrator to [AI Reporting](https://www.qualifybase.com/assistant) for the workspace reporting view. Recommendations do not authorize prompt edits, lead writes, outreach, or bookings.
