---
name: find-opportunities
description: Find evidence-backed business opportunities for a market, audience, problem, or category using Trend Seeker. Use for opportunity discovery and niche exploration, not for validating one already-defined idea.
---

# Find business opportunities

Use the Trend Seeker MCP tools to find opportunities that match the user's request.

## Research

1. Extract the market, audience, problem, constraints, and desired number of results from the request.
2. Use `list_idea_categories` only when category discovery would materially improve the query.
3. Use `search_business_ideas` for a specific market, audience, problem, or keyword. Use `list_business_ideas` when the user wants to browse recent or highly ranked opportunities without a specific query.
4. Inspect the best candidates with `get_business_idea` when the search result doesn't contain enough detail.
5. Call `get_supporting_evidence` for each finalist. Prefer candidates with dated evidence from more than one source when the data supports that distinction.

Keep the result set focused. Don't broaden the query merely to fill a requested count. If nothing relevant is returned, say so and suggest a more general query.

## Report

For each opportunity, provide:

- The title and target user.
- The concrete problem.
- Why it appears timely, if the returned data supports that claim.
- The relevant Trend Seeker scores or confidence tier, with their scale.
- One or two dated evidence points with direct source links.
- The largest unresolved assumption.

End with a short comparison explaining why the leading candidates fit the user's constraints. Treat scores as research signals, not forecasts or guarantees. Clearly separate retrieved facts from your interpretation. Never invent market size, revenue, growth, source links, or missing fields.

Use other external research tools only when the user asks for broader research beyond Trend Seeker.
