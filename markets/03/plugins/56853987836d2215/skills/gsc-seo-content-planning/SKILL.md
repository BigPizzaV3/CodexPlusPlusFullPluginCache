---
name: gsc-seo-content-planning
description: Analyze authorized Google Search Console performance data and turn it into evidence-based SEO keyword, content, and article plans. Use for GSC analytics, search queries, clicks, impressions, CTR, average position, rising or falling keywords, striking-distance opportunities, low-CTR pages, keyword cannibalization, content briefs, editorial calendars, and SEO prioritization. Do not use for Google Ads search volume, paid keyword research, live rank tracking, publishing content, or modifying Search Console.
---

# GSC SEO Content Planning

Use the SMEPost GSC MCP tools to turn the user's own finalized Search Console data into an actionable, read-only SEO plan. Respond in the user's language.

## Workflow

1. Establish scope.
   - Call `list_gsc_orgs` when the user has not already selected an authorized organization.
   - If more than one organization is available and the intended one is unclear, ask the user to choose by organization name.
   - Never expose organization IDs in user-facing prose; use IDs only as tool inputs.
2. Select the property.
   - Call `list_gsc_properties` for the chosen organization.
   - If multiple properties could match the request, ask the user to choose the exact property URL.
   - If exactly one property is available, continue with it.
3. Load planning data.
   - Call `get_gsc_seo_planning_data` with the authorized organization ID and selected property URL.
   - Apply `country`, `device`, or `minImpressions` only when the user requests a segment or a threshold. Read [references/tool-contract.md](references/tool-contract.md) before using filters or handling an error.
4. Check the returned boundaries before analysis.
   - Treat `effectiveRange`, `comparisonRange`, `access`, `filters`, and `limitations` as authoritative.
   - State when comparison data is unavailable or the effective range is shorter than the requested range.
   - Do not describe GSC impressions as total search volume or infer keyword difficulty, conversions, revenue, demographics, or competitor performance.
5. Build the requested deliverable.
   - Ground every priority in returned metrics or opportunity lists.
   - Distinguish observations from recommendations.
   - For a detailed article roadmap, keyword cluster, or editorial calendar, follow [references/planning-method.md](references/planning-method.md).

## Default response

When the user does not request a specific format, return:

1. **Scope and data quality** — property, effective period, comparison period, filters, access mode, and material limitations.
2. **Performance summary** — clicks, impressions, CTR, average position, and available period-over-period changes.
3. **Prioritized opportunities** — three to seven items ordered by likely impact and confidence, each with the query/page evidence and a concrete next action.
4. **Content plan** — identify whether to refresh an existing page, consolidate competing pages, improve title/meta copy, strengthen internal linking, or create a new article.
5. **Next measurement** — specify which GSC metrics and pages to review after the change.

Keep the answer compact unless the user asks for a full roadmap. Use percentages for CTR and explain that a positive `positionChange` means ranking improvement. Preserve exact query and page values from the tool output.

## Safety and failure handling

- Keep the workflow read-only. Never claim to edit a page, publish an article, change Search Console, or connect an integration.
- If the server returns `GSC_NOT_CONNECTED`, explain that GSC must be connected in SMEPost, provide the returned integrations link, and say whether a manager must act.
- If authentication or organization access fails, ask the user to reconnect or authorize the correct organization; do not attempt to bypass membership checks.
- If the result is empty, say that no usable rows were returned for the effective range and filters. Suggest widening or removing an optional segment, but do not manufacture keywords.
- If data is partial, unavailable, or rate-limited, report the limitation and stop short of unsupported conclusions.
