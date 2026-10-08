---
name: govly-sled-market-watch
description: Create an on-demand or scheduled, read-only Govly market watch that finds SLED public meetings and signals by customer keywords, searches open SLED opportunities in confirmed target places, and highlights evidence-backed connections. Use for state and local market monitoring, meeting intelligence, early demand signals, and topic-based opportunity alerts. Do not use for general saved-search scoring or federal recompete analysis.
---

# Govly SLED Market Watch

Monitor state and local public-sector signals and open opportunities without changing Govly records. Separate facts returned by Govly from inferred connections.

## Prepare the watch

Collect or recover these settings from the current chat:

- Topic groups: keywords, phrases, acronyms, products, programs, and exclusions.
- Signal scope: content types and lookback window. Default to public meetings when the user asks for meeting intelligence.
- Place scope: exact states, counties, cities, agencies, or confirmed Govly place IDs.
- Opportunity scope: posted or modified lookback, status, and maximum results to inspect.
- Reporting preference: daily or weekly cadence, changes-only behavior, and result cap.

For interactive use, ask one concise question when an unresolved setting would materially change the search. For a scheduled run, do not guess missing topics or geography; return a setup-needed message that names what is missing.

Read [references/templates.md](references/templates.md) when configuring a watch, creating a scheduled prompt, or formatting the report.

## Resolve the target geography

1. Use `search_places` for each named place. Prefer exact matches, then expected partial matches.
2. Treat semantic matches as suggestions, not confirmed geography. Ask the user to confirm them during an interactive run; skip ambiguous semantic matches during a scheduled run and report the gap.
3. Use `list_places` when the user wants to browse available places or when enumeration is more reliable than name search.
4. Preserve the selected Govly place IDs and the display names used in the report.
5. Remember that signal search does not accept a hard jurisdiction filter. Place scope for signals must be applied from returned evidence after the search. State this limitation when it affects coverage.

## Find public-sector signals

1. Call `search_signals` separately for each topic group so the report can identify what matched.
2. Put the substantive topic in `query`. Do not use signal categories as a substitute for keyword or topic search.
3. When the user asks for meetings, set `contentTypes` to `meeting`. Add other requested content types, such as hearing, law, policy, regulatory, event, news, or analysis, only when they fit the watch.
4. Apply the configured `dateRange` exactly.
5. Follow page-based pagination until no more results remain or the configured coverage cap is reached.
6. Post-filter returned signals to the confirmed place scope using explicit jurisdiction, agency, location, and source evidence. Keep a borderline result only when the report clearly labels the geographic uncertainty.
7. Deduplicate by canonical signal ID. Preserve all matching topic groups.
8. Call `show_signal` only for the highest-value signals whose details materially affect the report.

If a coverage cap truncates a query, label the signal section `Partial coverage` and name the truncated topic groups.

## Find open SLED opportunities

1. Call `search_opportunities` for each topic group with `searchType` set to `sled` and `status` set to `open` unless the user requests another status.
2. Pass confirmed target IDs through `placeIds`. Use `placeIdsNone` only when the user explicitly wants opportunities with no assigned place.
3. Apply the configured posted, modified, or response-date window rather than treating an unbounded search as a daily change feed.
4. Follow `meta.nextCursor` until it is null or the configured cap is reached.
5. Deduplicate opportunities by canonical opportunity ID and preserve every matching topic group.
6. Call `show_opportunity` only for the highest-value results or records needed to evaluate a potential signal connection.

Label incomplete pagination or capped searches `Partial coverage`.

## Detect changes

Compare current canonical IDs and material fields with the most recent successful report in the same chat when that context is available.

- Label a previously unseen record `New`.
- Label a record `Changed` only when a meaningful field changed, such as date, status, buyer, scope, location, deadline, or source details.
- Suppress unchanged records only when the configured watch requests changes-only output.
- Label the report `First run` when no reliable prior snapshot is available.

Do not claim durable cross-chat state.

## Evaluate possible connections

Connect a signal to an opportunity only when the returned evidence supports the relationship. Use these labels:

- `Strong connection`: the records share a specific agency or place, a materially matching topic or program, compatible timing, and at least one additional identifier or source detail.
- `Possible connection`: the records share a relevant agency, place, or topic, but lack a direct reference or enough detail.
- `Parallel activity`: the records concern the same broad market but do not support a direct relationship.

Never present timing or keyword overlap as proof that a meeting caused an opportunity. Quote or paraphrase the specific evidence used, and keep inference visibly separate from source facts.

## Produce the market watch

Lead with the market development, not the retrieval process. Include:

1. Run status: complete, partial coverage, first run, or setup needed.
2. Coverage: topic groups, date windows, confirmed places, signal results, and unique opportunities.
3. `Early signals`: meeting or signal, date, place or agency, matched topic, why it matters, and source.
4. `Open opportunities`: opportunity, buyer, place, deadline, matched topic, and one-sentence relevance.
5. `Potential connections`: evidence label, the connected records, supporting facts, uncertainty, and recommended monitoring action.
6. `Watch gaps`: ambiguous places, missing jurisdiction evidence, capped queries, or unavailable details.

If nothing qualifies, say so plainly and include the coverage summary. Do not manufacture a trend from sparse results.

## Preserve safety and scope

- Use only read tools during a scheduled run.
- Never call follow, inbox mutation, saved-search mutation, workspace mutation, comment, or opportunity mutation tools from this workflow.
- Treat the scheduling request as authorization to read and report, not authorization for future mutations.
- Do not send results to email, Slack, or another destination unless the user explicitly requests it and an authorized connector is available.
- Do not claim exhaustive jurisdiction coverage because `search_signals` cannot hard-filter by place.
- Do not report a first page as the complete result set.
