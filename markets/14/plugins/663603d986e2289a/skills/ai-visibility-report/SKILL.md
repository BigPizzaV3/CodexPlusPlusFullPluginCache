---
name: ai-visibility-report
description: Use when the user wants a summary or report of their brand's AI visibility, such as a weekly or monthly report, an executive summary, a client report, "how are we doing in AI search", or a status update for a meeting.
---
# AI visibility report
Build a concise, client-ready report from Refora data.
1. list_workspaces. If there are several workspaces and the user didn't name one, ask, or offer a short overview of each.
2. get_visibility_score for the period: overall visibility, change in points, strongest and weakest model.
3. get_visibility_trend with resolution=week, for the direction over time.
4. get_share_of_voice and get_competitor_comparison, for position against competitors.
5. get_sentiment_breakdown, for tone. get_citation_sources, for the top sources and the own site's share of citations.
Output, in this order:
- headline (one sentence);
- 3–5 key numbers with period and comparison;
- what changed and the likely reasons, labelled as hypotheses;
- competitors;
- how AI describes the brand;
- top cited sources;
- 3 prioritized next steps.
State the date window and how many AI answers the numbers are based on.

