---
name: competitor-battlecard
description: Use when the user asks about a specific competitor, such as "why is X ahead of us", "how does AI talk about X versus us", a battlecard, competitive positioning, or where a rival wins in AI answers.
---
# Competitor battlecard
1. list_workspaces. Then get_competitor_comparison to confirm the competitor is tracked and to get the ranking.
2. get_competitor_visibility_gap with that competitor_name: the questions where they lead, which models favor them, and the sources cited there.
3. get_sentiment_breakdown with brand_name set to the competitor, and again for the own brand, to compare how each is described.
4. get_ai_answers with brand_name set to the competitor: read a page of answers where they appear and quote 2–3 short, representative excerpts with model and date.
Output a battlecard:
- where they win and where we win;
- how AI describes each;
- the sources behind their visibility;
- three counter-moves.
If the competitor leads nowhere, say so plainly.

