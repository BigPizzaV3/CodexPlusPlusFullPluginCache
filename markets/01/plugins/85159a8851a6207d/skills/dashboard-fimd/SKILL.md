---
name: dashboard-fimd
description: >-
  Use this skill (licensed) to build a live, MSCI-branded HTML dashboard showing a factor index's methodology input via the IndexAI Insights MCP — the composite factor score (Quality/Momentum/Dividend) that drives selection and weighting, shown beside each holding's actual index weight. Trigger for "factor score behind the index", "FIMD", "quality score vs weight", "why is this holding weighted the way it is", "factor methodology input", for an index in the vetted FIMD list, even if the user never says MSCI. Produces a rendered .html artifact via the bundled assemble.py — renders only when the connector actually returns FIMD data for the entitled user, never fabricated.
---

# Factor Index Methodology Data (FIMD) Dashboard

Build a self-contained, MSCI-branded HTML dashboard showing, for a factor index's holdings, the **factor score** that the methodology uses to select and weight names, **beside each holding's index weight** — so a reader sees *why the weight is what it is*. FIMD is built on the `equity.sustainability_factor.input.security.*` namespace (per-security methodology inputs) and is **separately licensed** — render only when the connector actually returns data for the live probe; never fabricate values. See `references/recipes.md` §7 and `references/metric-audit.md` §7 for the exact mechanics.

## Output

Title the dashboard in plain words with the acronym in parentheses, e.g. *"Factor Index Methodology Data — the factor score behind index selection & weighting (FIMD)."* Layout, in order: availability strip → "rules that matter" panel (2-3 cited rules) → KPI row (parent-universe size, constituent count, factor-score headline, largest-holding weight) → "methodology inputs shown" chips → the Index holdings table (exactly four columns: Security · MSCI code · Weight % · Factor, factor column highlighted, sorted by weight desc, showing **every** constituent, not a top-N sample except the stated top-100 fallback for an unusually large parent) → a grounded commentary callout → index info (name+code, view, resolved calc date, rebalance effective date).

## Workflow

1. **Eligibility — code list + live probe.** The index must be in `data/fimd-indexes.txt` (the vetted FIMD eligibility list, 289 codes); if not, route to `dashboard-composition` or `dashboard-changes`. Then live-probe `fetch_index_data(codes:["<code>"], datapoints:["equity.sustainability_factor.input.security.msci_security_code"], date:"<as-of>")` — rows in `list_tables` (`pagination.total_rows`>0) means eligible; empty/error means tell the user it isn't available for that index/date (and, in Rebalance view, that Month-end may have data).
2. **Pick the view (default = Rebalance).** Control is a Month-end / Rebalance (T-9) toggle + a month picker (no range selector). Rebalance (T-9) resolves `next_rebalancing_date` if non-null else `last_rebalancing_date`, passes it as `date`, and the server resolves the T-9 pro-forma calc date; if the probe returns "No Data" (upcoming review not yet published), say so and offer Month-end. Month-end uses bare ids and auto-snaps to the 2nd business day.
3. **Which factor to show (methodology-driven, never assumed).** Read the methodology stack (`search_index_methodology_stack`) to confirm the composite factor the index uses. Infer the family from the index name as a starting point — Quality → `quality_score`; Momentum → `momentum_score`/`composite_momentum_score`; High Dividend Yield → `composite_dividend_score` — then discover the exact id with `search_index_datapoints` at build time and confirm it populates. Label the Factor column for the family (e.g. "Quality Score"). Never surface the descriptor inputs (ROE, Debt/Equity, Earnings Variability, momentum z-scores) as table columns — the single composite score sits beside weight; descriptors belong only in the rules panel.
4. **Build the holdings×weight×factor join.** Pull the index's constituents by weight (`equity_index.constituents.closing_weight` + `identifiers.security_name` + `description.msci_security_code`, `order_by:closing_weight desc`, `page_size:2000`); pull the FIMD factor map for the parent universe (`msci_security_code` + the single composite score id, matching bare/`.rebalancing` form); **join by `msci_security_code`** client-side; render descending by weight. The methodology input is index-scoped — it cannot be fetched by security code (returns "No Data available for the given input index …") — so the join must read the index map, a single call at load.
5. Render **all** constituents for a small-to-medium parent (standing rule 9 — a table claiming to show holdings in full must actually contain all of them); only for an unusually large parent, default to the top 100 by weight, page the rest, and say so on the dashboard face.
6. Show 2-3 cited "rules that matter" from the methodology stack (e.g. for Quality: score = average z of ROE, Debt/Equity, Earnings Variability, winsorized 5th/95th pct; Debt/Equity and Earnings Variability enter with a negative z; selection ranks the parent by score and weights market-cap-based among the selected names).
7. Add a grounded commentary callout (standing rule 10) — e.g. whether the highest-weighted holding also carries a high factor score, or whether weight and score diverge.
8. Validate (`references/metric-audit.md` § Validation): availability probe returns rows before rendering; weights sum to a plausible total (≤100); the composite score is within a plausible range (z-composite roughly [−5,5], flag outside); Rebalance-view calc date matches the server T-9 (else "No Data" → offer Month-end); Month-end `note` confirms the 2nd-business-day snap.

## Interpretation

- A blank Factor cell for a holding means unrated/not-mapped — show "n/a", never zero-fill.
- Weight is market-cap-based **among the factor-selected names**, not the whole parent universe — note this so weight-vs-score reads correctly.

## Handoff

- General composition/holdings of the same index without the factor join → `dashboard-composition`.
- Returns or risk analytics for the same index → `dashboard-performance-risk`.
- What changed at the index's last rebalance → `dashboard-changes`.
- The eligibility rule behind why a name is/isn't in the factor-selected set → `dashboard-methodology`.

## Guardrails

- Licensed data — render only when the connector actually returns it for this entitled user; never fabricate a factor score or weight.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}`, `data/fimd-indexes.txt` (the eligibility list), and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
