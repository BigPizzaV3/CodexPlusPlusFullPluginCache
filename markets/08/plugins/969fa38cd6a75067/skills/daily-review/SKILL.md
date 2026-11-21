---
name: daily-review
description: "Review a user's recorded day, week, or selected period in Orendro with consistent visuals, clear data gaps, and one practical next step. Use for daily summaries, weekly reviews, progress checks, or deciding what remains unrecorded."
---

Read [shared rules](references/shared-rules.md) before operating.

1. Resolve the requested period in the user's local timezone. Use supported
   range/relative-day arguments. If the time window is materially ambiguous,
   ask one clarification; otherwise use the explicit or stored local day.
2. Retrieve only context relevant to the requested review. Use confirmed saved
   goals and preferences when accessible. An empty bounded memory search does
   not prove the user has no preferences.
3. For a whole-day or multi-domain review, call daily_summary_get for that range.
   Reuse its structured result. For a focused question, use the narrow relevant
   domain tool instead of retrieving every domain.
4. If the host supports the card, pass the daily_summary_get structured result
   unchanged to render_daily_summary_card. Do not fabricate or edit fields to
   make a card appear. Use a concise text equivalent when rendering is absent
   or unsuitable for a notification.
5. Describe recorded values and their completeness. A missing food entry is not
   proof of a missed meal. A failed or denied read is not an empty day. Clearly
   distinguish estimates from confirmed values and limits from minimum goals.
6. Add one or two useful observations beyond the card. Keep them tied to the
   available records; do not repeat every tile in prose or make causal claims
   from a short history.
7. For period comparisons, use comparable windows and measures. Disclose partial
   current days, missing dates, and changing targets. Fetch extra data only
   when needed to support the specific comparison.
8. Offer one relevant next action, such as adding a missing record, reviewing
   an expiring grocery item, or adjusting a chosen routine. Do not change a
   goal, plan, or schedule just because a review suggests an improvement.
9. When this workflow runs inside a scheduled task, obey the saved notification
   condition and use the host's actual quiet-result mechanism when available.
   Report access problems according to the agreed failure rule.

Output: local date/window, one supported card or compact text summary, a brief
interpretation, and at most one next-action question. If there are no useful
records, offer a first action instead of interpreting zeros as actual behavior.
