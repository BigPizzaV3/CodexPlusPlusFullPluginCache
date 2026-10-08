# Recompete watch templates

Read this file when configuring the watch, creating a schedule, or formatting the final report.

## Customer configuration

```yaml
market: federal
award_scope:
  saved_searches:
    selection: [] # exact Govly award saved-search IDs or names
  fallback:
    keywords: []
    buyer_names: []
    incumbent_names: []
    naics: []
    psc: []
    minimum_award_amount: null
expiration:
  use: period_of_performance_potential_end_date
  lookahead_days: 365
opportunities:
  status: open
  posted_or_modified_lookback_days: 90
reporting:
  maximum_awards_per_search: 200
  maximum_awards_to_investigate: 15
  maximum_opportunities_per_award: 50
  changes_only: true
```

Treat this as a template, not a Govly default. Prefer exact saved-search IDs and use the customer's actual capture priorities.

## Scheduled prompt

```text
Every Monday at 8:00 AM local time, use the Govly Recompete Watch skill.

Run the configured award saved searches and identify awards whose period of
performance ends within the configured window. Investigate the strongest
candidates and search for new or materially changed open successor
opportunities. Grade every relationship using the skill's evidence labels.

If no supported successor is found, state that bounded result without claiming
that no recompete exists. Do not modify Govly records, saved searches, inbox
items, follows, or workspaces.
```

## Report format

```md
# Recompete watch — YYYY-MM-DD

Status: Complete | Partial coverage | First run | Setup needed
Coverage: X award searches; DATE–DATE expiration window; Y awards; Z opportunity queries

## Awards approaching end

| Status | End date | Award | Buyer | Incumbent | Value | Evidence completeness | Why watch |
|---|---|---|---|---|---:|---|---|

## Successor opportunities

### Evidence label — opportunity
- Linked award:
- Deadline:
- Supporting facts:
- Uncertainty:
- Recommended capture action:

## No supported successor yet
- Award:
- Searches performed:
- Next monitoring trigger:

## Watch gaps
- Missing period-of-performance dates:
- Partial queries:
- Ambiguous or unavailable records:
```
