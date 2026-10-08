# Workflow: Funding Activity Within a Confirmed Universe

Goal: analyze company count, capital deployment, round-size trends, concentration, stage mix, and formation within a user-confirmed company universe. Use the result to inform market timing without claiming a whole-market census.

## Establish the universe

This is a stop gate. If no universe below has been supplied or explicitly confirmed, ask the user to choose one before calling any Crunchbase tool. Do not build, test, or analyze a proxy universe in the same turn.

Use one of:

- Company names or domains supplied by the user
- An existing saved Crunchbase list selected by the user
- A candidate set produced by a landscape and explicitly confirmed by the user

Resolve and show canonical linked organizations before analysis. State the inclusion rule, adjacent exclusions, geography or stage constraints, and confirmed denominator. A one-off analysis does not require a saved-list write.

If the supplied universe repeats the same exact name, domain, permalink, or resolved UUID, deduplicate it and proceed with the unique denominator. Do not ask whether an exact repeat was intended to represent a different company.

## Retrieve the evidence

1. For a saved list, keep this market-analysis workflow primary and use live-confirmed `in_list` predicates directly on organization and funding-round searches. Load `saved-lists.md` only for list lookup and membership; do not route the analysis through pipeline monitoring.
2. For an unsaved universe, use confirmed organization permalinks with the live-supported multi-identifier operator.
3. Query organization fields needed for the census and formation buckets.
4. Query all funding rounds in the trailing 24 calendar months, ordered by announcement date and paginated to the returned count.
5. If the user requests equity-only capital, apply the live-confirmed equity predicate and state that definition.
6. Obtain organization profile URLs for all companies shown in round tables.

The 24-month `cb_search_query` is required even when organization profiles return funding-round cards. Do not substitute profile cards for the date-bounded, count-audited round search.

## Calculate

Use `calculation-spec.md` or `scripts/derive_metrics.py` for:

- Current and prior 12-month round counts
- Numeric capital totals and `—` amount counts
- Median numeric round size
- Funding-type mix
- Top-three capital concentration
- Formation by year within the confirmed universe

Show three to five largest numeric rounds in the 24-month window with lead investors.

## Interpret

Describe evidence that supports both greater and lower capital intensity. Give a conditional conclusion with a confidence level and the strongest counterinterpretation. Frame the practical question as whether the user's mandate still supports taking meetings within this universe.

## Output

- **Confirmed universe:** definition, denominator, and unresolved inputs
- **Headline metrics:** timeframes and amount-count denominators
- **Period comparison:** current versus prior 12 months
- **Concentration and stage mix**
- **Formation within the confirmed universe**
- **Notable rounds:** linked companies, round type, amount, date, leads
- **Conditional interpretation:** evidence, confidence, and counterinterpretation
- **Questions for follow-up**

Save or update the universe only when explicitly requested, following `saved-lists.md`.
