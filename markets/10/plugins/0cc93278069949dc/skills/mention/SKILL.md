---
name: mention
description: Use the mention.ma MCP to analyze and manage a brand's visibility across AI platforms. Select the correct Mention tool, resolve brands and record identifiers, combine related reads, and handle state-changing or credit-consuming operations safely.
---

# Mention MCP

Use the Mention MCP as the source of truth for the authenticated user's brands, AI visibility, citations, sentiment, prompts, GEO opportunities, consensus analyses, shopping visibility, URL monitoring, and research.

## Resolve context first

1. Most tools require `brandId`. If a valid `brandId` is not already available from the conversation or a previous tool result, call `mention_list_brands` first.
2. When the user names a brand, match it against the returned brands. If exactly one brand matches, use its ID. If several brands could match, ask the user to choose instead of guessing.
3. Call `mention_get_brand` when the task needs the full brand profile, competitors, aliases, industry, country, language, or configuration.
4. Reuse identifiers returned by tools, such as `promptId`, `opportunityId`, `runId`, `queryId`, and `watchId`. Never invent an identifier.
5. For paginated tools, use `limit` between 1 and 100. Continue with the returned cursor only when more results are needed for the request.

## Choose the tool from the user's intent

### Brands and account

- List available brands or resolve a brand name: `mention_list_brands`.
- Read one brand's profile and settings: `mention_get_brand`.
- Change a brand profile, competitors, aliases, features, country, language, industry, descriptions, account type, or self-improvement settings: `mention_update_brand`.
- Check the plan, subscription status, or remaining feature credits: `mention_get_billing_status`.

### Visibility and AI responses

- Current or period visibility score, share of voice, or average position: `mention_get_visibility_snapshot`.
- Change over time, historical trend, growth, decline, or evolution: `mention_get_visibility_trend`.
- Compare AI platforms for `visibilityScore`, `shareOfVoice`, or `citationShare`: `mention_get_platform_matrix`.
- Citation share, top citing domains, or top citing pages: `mention_get_citation_report`.
- Stored prompt executions, individual AI responses, or the prompts behind visibility results: `mention_list_prompt_executions`.
- Positive, neutral, or negative brand sentiment: `mention_get_sentiment`.

For a general visibility overview, normally combine the snapshot with the platform matrix. Add citations, sentiment, or prompt executions only when the user asks for them or when they are necessary to explain the result.

### Tracked prompts

- List prompts, prompt distribution, enabled prompts, or suggestions: `mention_list_prompts`.
- Create prompts: `mention_create_prompts` with a `prompts` array.
- Edit one prompt: `mention_update_prompt` with `promptId` and all three replacement fields (`text`, `promptType`, `intent`).
- Enable or disable one prompt: `mention_set_prompt_enabled` with `promptId` and `enabled`.

Each created prompt needs text of at least 12 characters, a `promptType` of `organic`, `brandSpecific`, or `competitorComparison`, and an intent of `branded`, `informational`, `navigational`, `commercial`, or `transactional`.

### GEO opportunities

- List opportunities, filter by `new`, `inProgress`, `done`, or `dismissed`, or retrieve one known opportunity: `mention_list_opportunities`.
- Change an opportunity's workflow status: `mention_update_opportunity` with its `opportunityId` and the new status.

If the user asks to update an opportunity but provides no valid ID, list the relevant opportunities first and resolve the intended record.

### Multi-platform consensus

- List earlier consensus runs: `mention_list_consensus_runs`.
- Read one run: `mention_get_consensus_run` with `runId`.
- Start a new run: `mention_start_consensus` with `promptText` and between 2 and 12 supported `platformSlugs`.

Starting a consensus run consumes credits. If the user only asks to see existing results, use the read tool and do not start a new run. A new run can remain pending, so report its status and use `mention_get_consensus_run` later rather than claiming immediate completion.

### Shopping visibility

- List shopping queries: `mention_list_shopping_queries`.
- List available shopping run dates: `mention_list_shopping_run_dates` with `queryId`.
- Read results for a query or run date: `mention_get_shopping_results` with `queryId` and an optional `runDate`.
- Add a shopping query: `mention_add_shopping_query` with `query`.

Adding a shopping query requires available credits. Check `mention_get_billing_status` when credit availability is unknown and the user wants to add one.

### URL monitoring

- List watches: `mention_list_url_watches`.
- Read one watch: `mention_get_url_watch` with `watchId`.
- Read watch runs: `mention_list_url_watch_runs` with `watchId`.
- Read detected changes: `mention_list_url_watch_changes` with `watchId`.
- Create a watch: `mention_create_url_watch` with a valid `url` and a frequency of `24h`, `2d`, `5d`, or `7d`. Creation always starts an active watch.
- Pause, resume, or change a watch: `mention_update_url_watch` with `watchId` and `frequency` or `status` (`active` or `paused`). This does not change the URL.

Active watches follow Mention's normal credit rules. Do not create or activate one when the user only asked to inspect monitoring results.

### Keyword and domain research

- List cached AnswerThePublic research: `mention_list_question_research`.
- Read one cached question research result: `mention_get_question_research` with `answerId`.
- List cached domain overviews: `mention_list_domain_overviews`.
- Read a cached keyword gap: `mention_get_keyword_gap` with the required `competitorDomain` and optional `languageUi` and `countryIsoCode`.
- Request fresh question research: `mention_start_question_research` with `keyword`, `language`, and `location`.
- Run a domain overview: `mention_run_domain_overview` with `domain`; it uses the brand's stored country and language.
- Request a keyword gap: `mention_run_keyword_gap` with `competitorDomain` and optional `languageUi` and `countryIsoCode`.

Fresh research consumes credits. Use the cached read tools when the user asks for existing results, and call a research start/run tool only when the user requests a new analysis.

## Date handling

- Use ISO-formatted dates for `dateStart` and `dateEnd`.
- When the user says “current”, omit dates unless the comparison needs a defined period.
- When the user gives a relative range such as “last 30 days”, convert it to exact dates and state the interpreted range in the answer.
- `mention_get_visibility_trend` requires `dateStart`, `dateEnd`, and a `buckets` array. Build non-overlapping chronological buckets whose `startIso` and `endIso` cover the requested range. Use daily buckets for short ranges and weekly or monthly buckets for longer ranges unless the user requests another granularity.
- Apply `promptIds` only when the user asks to limit analysis to specific tracked prompts.

## Mutation and credit rules

- Read-only questions must not trigger manage, update, add, start, or fresh-research tools.
- If a requested write lacks a required identifier, retrieve the possible records and ask the user to select when the target is ambiguous.
- Before a credit-consuming action, check billing when the available balance is unknown, explain which workflow will consume credits, and obtain any confirmation required by the active environment.
- Never silently enable automation, overwrite profile data, or change workflow status as a side effect of an analysis request.
- After a write, report the record affected, the operation performed, and the returned status. Do not claim success when the tool returns an error or a pending state.

## Response quality

- Name the analyzed brand and exact date range.
- Separate stored Mention data from your own interpretation.
- When comparing platforms, state the metric used rather than mixing visibility score, share of voice, and citation share.
- Summarize the important result first, then support it with the relevant metrics, citations, prompts, or records.
- If the available data is empty or partial, say so and suggest the smallest useful next tool call.
- Do not invoke Mention for unrelated requests such as weather, general creative writing, financial transactions, or topics with no connection to the user's Mention workspace.

## Error handling

- Authentication error: ask the user to connect or reconnect mention.ma; do not request OAuth tokens in chat.
- Ownership or not-found error: refresh brands or list the relevant records instead of retrying an invented ID.
- Insufficient credits: report the limitation and stop; do not repeatedly retry the paid operation.
- Pending workflow: return the run or workflow ID and status, then read it again only when the user asks or when the environment supports an appropriate wait.
- Pagination: continue only until the requested answer is supported, rather than fetching the entire workspace by default.

