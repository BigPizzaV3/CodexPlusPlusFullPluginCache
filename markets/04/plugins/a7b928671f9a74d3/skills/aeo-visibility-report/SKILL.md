---
name: aeo-visibility-report
description: Build an AI search visibility report for a brand — how often it appears in ChatGPT, Perplexity, Gemini, and other AI answers, how it compares to competitors, which sources cite it, and where it's losing ground. Use when the user asks about AI visibility, brand mentions in AI answers, share of voice, competitor comparison, or citation analysis. Not for website technical health (use the site audit) or for creating content.
---

# AEO Visibility Report

Produce a decision-ready report on a brand's AI search visibility using ChatFeatured analytics.

## Steps

1. **Resolve the brand.** Call `list_organizations`, then `list_brands`. If the user has exactly one brand, use it; otherwise ask which brand to analyze. Pass its `brandId` to every call below.
2. **Pull the core analytics** with `query_analytics`, defaulting to a 30-day window (`filters: { dateRange: "30d" }`) unless the user asks for another period:
   - `brand_overview` — headline visibility, mention counts, and platform mix.
   - `time_comparison` — current period vs the previous one; this is where trends come from.
   - `competitor_comparison` — share of voice against tracked competitors.
   - `source_analysis` and `cited_urls` — which domains and URLs AI answers cite in this space, and whether the brand's own pages are among them.
3. **Go deeper only where the data warrants it.** If a preset surfaces something notable (a competitor spike, a platform drop), use `query_analytics` with `source_changes` or `source_mentions`, or `query_analytics_sql` for a custom cut (call it with `explain: true` first to get the schema). Skip this step for a routine report.
4. **Synthesize.** Structure the report as:
   - Headline: overall visibility and the single biggest change since the prior period.
   - Platform breakdown: where the brand is strong/weak (ChatGPT vs Perplexity vs Gemini, etc.).
   - Competitive position: who leads share of voice and by how much.
   - Citation gaps: domains AI answers trust in this space where the brand is absent — these are the actionable opportunities.
   - 2–4 concrete recommendations tied to the gaps found.

## Boundaries

- Report numbers exactly as returned; never extrapolate missing periods.
- If a preset returns zero rows, say the data window is empty rather than inventing a trend, and suggest the user check that prompt tracking is running.
- Recommendations that involve creating content should point at the content-gap workflow rather than starting article generation from here.
