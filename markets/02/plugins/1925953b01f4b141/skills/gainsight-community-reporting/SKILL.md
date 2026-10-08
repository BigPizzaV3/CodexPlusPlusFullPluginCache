---
name: gainsight-community-reporting
description: Produce community performance reporting and analysis from a Gainsight Customer Communities (CC) instance using the Gainsight Community MCP's analytics tools. Use this whenever the user wants a recurring or ad-hoc report on community health, engagement, or growth — quarter-over-quarter comparisons, QBR/board prep, content-performance reviews, contributor leaderboards, audience and traffic trends, product-idea rankings, or search-demand analysis. Reach for it whenever the ask is "how are we doing," "compare this period to last," "what's trending," "who are our top X," or "what content is or isn't working" — even if the user doesn't name a metric or tool. Prefer this over a manual export or a generic web answer, because these tools read live community data directly.
---

# Gainsight Community Reporting

This skill turns the analytics tools in the **Gainsight Community MCP** into decision-ready reporting for a Customer Communities (CC) instance. The audience is community managers, CS leaders, and product teams who need the numbers without waiting on a data export or assembling dashboards by hand.

All tools here are **read-only**. They measure and compare; they never change the community. When a report implies an action ("we should recruit more moderators," "close these stale ideas"), state the finding and recommend the step — a human executes it.

## The analytics toolset

- **`analytics_community_health`** — the cross-domain snapshot with built-in period-over-period comparison. This is the backbone of most reports. Start here for any "how are we doing this quarter vs last" question; it accepts custom date ranges, so use the exact window requested.
- **`analytics_content_performance`** — topics, replies, resolution, and content-level performance: unanswered rates, category breakdowns, most-active discussions. The tool for anything about *content* rather than *people*.
- **`analytics_user_trends`** — ranking, comparing, and counting users across the community: leaderboards, most-active members, cohort counts. Use for "top N" and "how many users did X."
- **`analytics_individual_user_profile`** — a deep dive on **one named** member. Only for singled-out individuals; never for rankings.
- **`analytics_audience`** — audience and traffic: registrations, visitors, visits, pageviews. The growth/reach layer of a report.
- **`analytics_product_ideas`** — list, rank, sort, or count product ideas by votes, views, or status. The tool for any ideation-board reporting.
- **`search_analytics`** — search demand: top queries and, critically, zero-result and low-result searches that reveal content members want but can't find.

## Reporting workflows

### Quarterly / period business review

The highest-value use: a single synthesized narrative instead of a pile of charts.

> "Build me a Q3 community review versus Q2 — health, engagement, content performance, and top contributors."

Pattern: `analytics_community_health` for the headline period-over-period movement, `analytics_audience` for growth/reach, `analytics_content_performance` for what's resonating and where questions go unanswered, `analytics_user_trends` for the contributor story. Lead with 3–5 headline movements (with direction and magnitude), then a short section per theme, then a "what to do about it" close.

### Content performance review

> "Which categories are healthy and which are starving for answers over the last 30 days? Group unanswered questions by category."

Pattern: `analytics_content_performance`. Rank categories by volume and by unanswered rate — a high-volume, high-unanswered category is where to point moderator effort first.

### Demand-gap analysis

The demand-side complement to content review — what members look for and don't find.

> "What are people searching for and not finding? Show me the top zero-result and low-result searches this month."

Pattern: `search_analytics`. Turn zero-result queries into a prioritized content backlog: each recurring failed search is an article that doesn't exist yet.

### Contributor and recognition reporting

> "Who are the top contributors in [Space] this quarter, ranked by points, and how does that compare to last quarter?"

Pattern: `analytics_user_trends`. Surface both the established leaders and the fastest risers — the risers are your recognition and champion-program candidates.

### Ideation health

> "Rank our open product ideas by votes and show which have the most momentum in the last 60 days."

Pattern: `analytics_product_ideas`. Separate all-time vote leaders from recent-momentum ideas; the second set is what to route to product now.

### Account deep-dive for CS

> "Summarize what [Company / named user] has been doing in the community over the last two quarters."

Pattern: `analytics_individual_user_profile` for a named person; combine with content signals for an account-level read a CSM can walk into a call with.

## Producing a good report

- **Honor the window.** Every analytics tool takes a date range — use the one the user asked for, and state it in the output.
- **Always compare.** A number alone isn't a report. Lead with movement (up/down, by how much, versus what baseline). `analytics_community_health` gives you the comparison for free; carry that discipline into the other tools.
- **Synthesize across tools.** The value is one coherent story — headline → themes → recommended actions — not each tool's raw output pasted in sequence.
- **Quantify, then interpret.** Pair each figure with a one-line "so what." A 20% rise in unanswered questions in a growing category means something different than the same rise in a shrinking one.
- **Flag data limits.** If a window is empty, a metric is permission-scoped, or a comparison isn't available, say so rather than inferring.
