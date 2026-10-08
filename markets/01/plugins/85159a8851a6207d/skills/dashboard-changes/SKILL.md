---
name: dashboard-changes
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard summarizing an MSCI index's last N index reviews (rebalances) via the IndexAI Insights MCP: constituent counts before/after, additions, deletions, FIF changes, official index turnover, addition/deletion turnover, and significant constituent weight changes. Trigger for "last N reviews", "what changed at rebalance", "index turnover", "additions and deletions", "which stocks were added/removed", even if the user never says MSCI. This is a read-only historical review SUMMARY, not a proforma trade/order list. Produces a rendered, refreshable .html artifact via the bundled assemble.py — never a text-only answer.
---

# Index Changes Dashboard

Build a self-contained, MSCI-branded HTML dashboard of an index's last *N* reviews — a review-summary of read-only facts + simple arithmetic, explicitly NOT a proforma trade/order list or an estimate of post-event weights. See `references/recipes.md` §4 and `references/metric-audit.md` §4 for the full deterministic build and validation rules — follow that build **exactly and in order**; this is the most procedural of the seven dashboards.

## Output

KPI row (index, reviews analyzed, last review effective date, latest turnover) → Review summary table (one row per review: effective date, N pre/post, additions, deletions, index turnover %, addition/deletion TO %, FIF changes) → per-review significant weight-changes tab (cutoff default 1pp, adjustable, expandable to the full list) → index information table. Present with `present_files`, stating index, N, currency/variant used for turnover.

## Workflow

1. Resolve the index code via `search_index_indexes` — never hardcode a code.
2. Resolve *N* review effective dates recursively: `equity_index.master_description.last_rebalancing_date` at the latest resolved business date → R1; repeat at `date = R1 − 1 business day` → R2; continue until *N* dates are collected.
3. Per effective date T (T₋₁ = the business day before T), make these as **separate** `fetch_index_data` calls: PRE composition at T₋₁ (`closing_weight`, `identifiers.security_name`, `description.msci_security_code`, `page_size:2000`) plus `nb_of_securities` at T₋₁ = N(Pre-review); REVIEW changes at T with `rebalance_target:"previous"` (`review_change_counts.*`, `additions.msci_security_code`, `deletions.msci_security_code`, `proforma_constituents.initial_weight`); POST count `nb_of_securities` at T = N(Post-review); a **second** call resolving added/deleted names via `security.description.security_name` (never mix index and security codes in one call); official turnover via `fetch_index_timeseries(..., equity_index.performance.total_index_turnover)` at start=end=T.
4. Compute: normalize weights (PRE is percent as-is, PROFORMA `initial_weight` is decimal → ×100); assert N(Post-review) = N(Pre-review) − Deletions + Additions (flag if not); weight-change table over the union of PRE/POST securities (`Δw = w_post − w_pre`, missing side = 0); Addition TO% = Σ post weight over additions; Deletion TO% = Σ pre weight over deletions; Index turnover% = official `total_index_turnover` × 100 (never recompute — the `Σ|Δw|/2` proxy is a cross-check only); significant weight changes = union rows with `|Δw| ≥` the cutoff (default 1pp), sorted by `|Δw|` desc, tagged added/deleted/reweighted.
5. Validate every build: assert `rebalanceDate == T` on each review-change call; assert the N(Post) identity per review; pre/post weights each sum to ≈100 (±1); one-way turnover ≥ Addition TO — flag any violation on the dashboard face.
6. Add one grounded interpretive callout per major section (standing rule 10).

## Labels & conventions

Use "Effective date" for a review's date and "Last review effective date" for the most recent one — do not mix in other phrasing. Use Pre-review/Post-review (not MSCI's own report labels "Current"/"Proforma", which are announcement-time labels that mislead in a historical view — note the mapping if asked). State plainly that the shown turnover is MSCI's official **one-way** figure; the printed review report shows **two-way** (= 2× one-way); double it if the user wants that figure, or show both.

## Interpretation

- Reason for deletion (security-level, from IRCR content) is **deferred** — not captured by IndexAI Insights today. Show the column marked "coming with the IRCR dataset"; never fabricate a reason.
- FIF-changes count is kept but its usefulness is an open question — surface it, be ready to see it dropped later.
- Historical reviews are immutable; on refresh, only re-check whether a *newer* review has occurred (via `last_rebalancing_date`) and banner if so — do not re-pull all per-review data on every refresh.

## Handoff

- What's currently inside the index (holdings, weights) as of today → `dashboard-composition`.
- Returns or risk analytics → `dashboard-performance-risk`.
- Why a specific addition/deletion happened on eligibility grounds → `dashboard-methodology`.
- Comparing review activity across indexes → `dashboard-comparator`.

## Guardrails

- This is a review SUMMARY, never a proforma trade/order list — estimated post-event weights and trade lists are out of scope regardless of how the user phrases the ask.
- Never recompute the N(Post) identity or index turnover from your own arithmetic when an official field exists — use the official field, cross-check only.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
