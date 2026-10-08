---
name: govly-recompete-watch
description: Create an on-demand or scheduled, read-only Govly watch for awards approaching their period-of-performance end, inspect related records, and identify evidence-backed successor or recompete opportunities. Use for recompete pipeline monitoring, incumbent and buyer tracking, expiring-award review, and successor-opportunity discovery. Do not use for general saved-search scoring or SLED meeting intelligence.
---

# Govly Recompete Watch

Identify awards that may create future recompete demand and search for successor opportunities. A likely recompete is an analytical conclusion, not a source fact, unless a returned record explicitly says so.

## Prepare the watch

Collect or recover these settings from the current chat:

- Market scope: federal, SLED, international, or a specified combination.
- Award scope: exact saved award-search IDs or names when available; otherwise target buyers, incumbents, keywords, NAICS, PSC, and minimum value.
- Expiration window: period-of-performance end or potential end dates to monitor.
- Opportunity scope: status, buyer or topic terms, posted or modified window, and result cap.
- Reporting preference: daily or weekly cadence, changes-only behavior, and finalist cap.

Prefer configured award saved searches for repeatable monitoring, especially when they already encode a period-of-performance end window. For interactive use, ask one concise question when a missing setting materially changes the search. For a scheduled run, do not invent a market, expiration window, or award scope; return a setup-needed message naming the missing settings.

Read [references/templates.md](references/templates.md) when configuring the watch, creating a scheduled prompt, or formatting the report.

## Build the expiring-award set

### Use configured award saved searches

1. Call `list_award_saved_searches` and follow pagination until no more results remain.
2. Match configured IDs exactly. Match names exactly when possible; ask about ambiguity during an interactive run and skip ambiguous names during a scheduled run.
3. Call `execute_award_saved_search` for each selected search so the watch uses live results rather than a cached list.
4. Follow every returned cursor until it is null or the configured coverage cap is reached.

### Fall back to direct award search

If no suitable award saved search is configured:

1. Call `search_awards` using the customer's market, buyer, recipient, keyword, NAICS, PSC, amount, and other supported filters.
2. Do not use the award `dateRange` as a period-of-performance expiration filter. It filters award action dates.
3. Follow `meta.nextCursor` until it is null or the coverage cap is reached.
4. Filter the returned award `dates` client-side against the configured `period_of_performance_end_date` or `period_of_performance_potential_end_date` window.
5. Report when missing period-of-performance dates prevent an award from being evaluated.

Deduplicate by canonical award ID while preserving the source searches or criteria that matched. Label capped or incomplete pulls `Partial coverage`.

## Investigate the strongest candidates

1. Prioritize awards using timing, value, target-buyer fit, scope fit, and evidence completeness. Do not turn these priorities into a precise probability unless the customer supplies a validated model.
2. Call `show_award` for the strongest candidates, up to the configured detail cap.
3. Inspect related opportunities returned by the award detail before running broader searches.
4. Search for open successor opportunities with `search_opportunities` using combinations of the award's contract or reference number, buyer, program or scope terms, and classifications.
5. Use the same market as the monitored award unless the user explicitly asks for cross-market analysis.
6. Apply a bounded posted or modified window when the watch is intended to report new activity.
7. Follow `meta.nextCursor` until it is null or the configured cap is reached.
8. Call `show_opportunity` only when its details materially affect the evidence grade.

Deduplicate successor opportunities by canonical opportunity ID. Preserve all awards they may relate to.

## Grade recompete evidence

Use the strongest label supported by returned evidence:

- `Confirmed successor`: an opportunity or explicit relationship cites the predecessor award, contract number, incumbent effort, or recompete directly.
- `Strong candidate`: the buyer and scope materially match, timing aligns with the award end window, and multiple additional facts support succession.
- `Possible candidate`: buyer, topic, classification, or timing overlaps, but the record lacks enough evidence for a strong relationship.
- `No open successor found`: the bounded search found no supported match. This does not mean no recompete exists or will occur.

Never infer a guaranteed recompete from an award end date alone. Keep source facts, analytical interpretation, and missing evidence separate.

## Detect changes

Compare canonical IDs and material fields with the most recent successful report in the same chat when that context is available.

- Label a newly monitored award or opportunity `New`.
- Label a record `Changed` when period-of-performance dates, value, buyer, status, deadline, scope, or relationship evidence materially changes.
- Suppress unchanged records only when the configured watch requests changes-only output.
- Label the report `First run` when no reliable prior snapshot is available.

Do not claim durable cross-chat state.

## Produce the recompete watch

Lead with the highest-priority market developments. Include:

1. Run status: complete, partial coverage, first run, or setup needed.
2. Coverage: award searches or filters, market, expiration window, candidate awards, and opportunity queries.
3. `Awards approaching end`: award, buyer, incumbent or recipient, value, end date, evidence completeness, and why it merits attention.
4. `Successor opportunities`: evidence label, opportunity, deadline, linked award, supporting facts, and uncertainty.
5. `No supported successor yet`: priority awards with no open match and the bounded searches performed.
6. `Watch gaps`: missing dates, incomplete pagination, capped searches, ambiguous saved searches, or unavailable details.

If no award falls in scope or no successor is found, say so plainly and include the coverage summary. Do not pad the report with unsupported matches.

## Preserve safety and scope

- Use only read tools during a scheduled run.
- Never call follow, inbox mutation, saved-search mutation, workspace mutation, comment, or opportunity mutation tools from this workflow.
- Treat the scheduling request as authorization to read and report, not authorization for future mutations.
- Do not send results to email, Slack, or another destination unless the user explicitly requests it and an authorized connector is available.
- Do not describe a candidate as confirmed without a direct source relationship.
- Do not report a first page as the complete result set.
