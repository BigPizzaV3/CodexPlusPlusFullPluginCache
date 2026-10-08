---
name: index-changes
description: >-
  Use this skill for what changed in an MSCI index at a review or corporate event: additions and deletions, proforma constituents, FIF/number-of-shares changes, index turnover, and corporate actions. Trigger for "what changed in the May review", "which companies were added or removed", "when was this stock deleted", "index turnover for this rebalance", "upcoming index changes", even if the user never says MSCI.
---

# MSCI index changes and review outcomes

Report what an index review or corporate event actually changed. Review **outcomes** live in the change datasets; review **rules** live in methodology. Do not answer one from the other.

## Output

Lead with the change list or figure. Identify the index as `<name> (<msci_index_code>)`, state the rebalance date used and how it was resolved, and distinguish announcement date from effective date whenever both are returned.

## Workflow

1. Resolve the index with `search_index_indexes`.
2. Discover the change datapoints with `search_index_datapoints`. Typical concepts: additions, deletions, proforma constituents, FIF changes, number-of-shares changes, corporate events, turnover.
3. **Resolve the rebalance date in two steps. Never pass today, a guessed month-end, or a first-of-month date to a rebalancing-aware datapoint.**
   - Fetch `master_description` rebalancing fields — last rebalancing date, next rebalancing date, and future-days where available — using a probe date: the user's explicit date, or the month-end of the month the user named, or the latest business date if unspecified.
   - Prefer the returned next rebalancing date when it is not null or empty. Otherwise fall back to the returned last rebalancing date.
   - Pass that returned value as `date`. Do not construct it.
4. Set `rebalance_target` deliberately:
   - `previous` — the most recent completed review. Pass the returned last rebalancing date as `date`.
   - `upcoming` — the current announcement window. `date` is ignored; the server uses its own reference date. If the date falls outside MSCI's live review window the change datapoints come back empty with an `outsideRebalWindow.message` — relay it verbatim rather than reporting "no changes".
   - `proforma_start_date` — returns the earliest calc date at which proforma data exists, as `{ start_proforma_date, rebalanceDate }`. The `datapoints` array must contain at least one proforma-constituent id, and must not carry `master_description` ids.
     This mode alone rejects a forward `date` — passing a future next-rebalancing date fails with `Calculation Date(calc_date) can not be in future`. Pass the latest business date and let the server resolve the proforma window. The step 3 preference for the next rebalancing date applies to the change datasets, not here.
5. Read `constraints.notes` on every selected datapoint before fetching, including required `info_points` and any mandatory disclaimer.
6. Fetch with `fetch_index_data`. Use `order_by` / `order_direction` and pagination for long add/delete lists, and state rows shown versus available.
7. **Resolve the security names — required.** Additions and deletions return bare `msci_security_code` values with no names, so a raw answer is a list of numbers. Make a **second** `fetch_index_data` whose `codes` are those security codes, batched, with `security.description.security_name` (and country where useful), reusing the same date. Do not mix index codes and security codes in one call. Never present unresolved codes as the answer.
8. **Turnover.** `equity_index.performance.total_index_turnover` is range-only (`supports_single_day=false`), so it must go through `fetch_index_timeseries`, not `fetch_index_data`. Set `start_date` and `end_date` both to the review effective date to isolate that review — over a wider window the value is a single aggregate summed across the range, with a blank date cell, which is expected. The value returns as a **fraction**, so multiply by 100 to present a percentage. It is MSCI's **one-way** turnover; MSCI's printed review report shows **two-way**, which is twice that figure — state which convention you are showing. If no published turnover field is available and you derive one from add/delete weights, say it was derived and give the basis.

## Historical change questions

For "when was this security added or deleted", resolve the security with `search_index_securities`, then work from the change datasets across the relevant review dates. Do not infer an effective date from a price or weight series.

## Interpretation

- Announcement date and effective date are different facts. Report whichever the data returns, labelled.
- Proforma data is pre-announcement and estimated. It can be discarded and re-announced if constraints are breached between announcement and effective date.
- A change list reflects the index and review requested. Do not generalise it to a parent, child, or sibling index.
- Corporate-event driven changes are not review changes; keep them distinguishable when both appear.

## Handoff

- Why the rule produced the change, or review frequency → `methodology`.
- Passive flow, days-to-trade, or estimated demand from a change → `index-flows`.
- Current holdings and weights outside a review context → `composition`.
- Whether a security clears the screens → `eligibility`.

## Guardrails

- Never invent or arithmetically derive a rebalance date. Use the value the app returns.
- No returned changes is not the same as no changes. Report it as unavailable or outside the returned window.
- Proforma is an estimate, not an announcement, and not a prediction that a security will be added or deleted.
- Reproduce any mandatory disclaimer from `constraints.notes` verbatim.
- Do not present a single page of a long add/delete list as the complete review outcome.
