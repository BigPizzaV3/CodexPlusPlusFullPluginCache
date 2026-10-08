---
name: dashboard-methodology
description: >-
  Use this skill to build a live, MSCI-branded HTML dashboard combining a live eligibility screen for a named security against a reference MSCI index/Inclusion Module with 2-3 cited construction rules (capping, buffer zones, country classification) pulled from the actual methodology document via the IndexAI Insights MCP — never from memory. Trigger for "why isn't this stock in the index", "is this eligible for MSCI EM", "capping rule", "buffer zone", "country classification rule", "what would it take to be included", even if the user never says MSCI. Produces a rendered .html artifact via the bundled assemble.py, plus the mandatory Index Inclusion Module disclaimer — never a text-only answer, never a from-memory methodology claim.
---

# Index Methodology Dashboard

Build a self-contained, MSCI-branded HTML dashboard combining a live quantitative eligibility screen with cited rule text — two sources that answer two different questions and must never be blended: the screen answers "does it pass today's checks", the cited methodology text answers "why does the rule exist and where do capping/buffer bands kick in." See `references/recipes.md` §5 and `references/metric-audit.md` §5 for the exact fields and the mandatory disclaimer text.

## Output

Eligibility strip (pass/fail + every component flag, colour-coded) → "why" panel narrating each failing flag with its own input values/cutoffs → "rules that matter" panel (2-3 cited capping/buffer/country-classification rules, methodology name shown) → buffer/migration caveat stated plainly → standard disclaimer footer **plus** the Index Inclusion Module disclaimer block. If the user asks a pure eligibility question, you may omit the rules panel; if a pure rules question with no security, omit the eligibility strip.

## Workflow

1. Resolve the security's MSCI code via `search_index_securities`; resolve the reference index/Inclusion Module entity (e.g. `IIM GLOBAL`, `IIM AMERICAS`, `IIM EMEA`, `IIM APAC`) with an optional country filter.
2. Pull `security.index_inclusion_monitor.index_eligible_fg` and **every** component flag (`size_segment_fg`, `minimum_free_float_market_capitalization_fg`, `minimum_foreign_inclusion_factor_flag`, `foreign_room_flag`, `atvr_12m_fg`, `atvr_3m_fg`, `fot_12m_fg`, `fot_3m_fg`, `china_a_share_with_connect_line`).
3. If `index_eligible_fg` is FALSE or blank, read every component flag and attribute the result to **all** flags that fail or are "Not Met" — never just the first one found. Never recompute the roll-up yourself; read the field directly (FALSE beats blank in its own precedence logic, which is easy to get subtly wrong by re-deriving).
4. For a rules question, call `search_index_methodology_stack(indexCode, query)` and cite the methodology name + returned snippet. If nothing returns, prefix the answer with the tool's own mandated "⚠️ Note: ... not the official MSCI methodology document" fallback — never answer from training data unlabeled.
5. Attach the mandatory Index Inclusion Module disclaimer verbatim via `assemble()`'s `extra_disclaimers` parameter whenever step 2/3 data is shown — this is carried in the datapoint's own `constraints.notes`, not injected automatically by the fetch tool, and must never be paraphrased, trimmed, or merged with the standard footer.
6. Add one grounded interpretive callout per major section (standing rule 10).

## Caveats to always state alongside the eligibility flag

- Size-segment cutoffs shown are interim daily-maintenance cutoffs, not the final Index Review cutoffs.
- Free float, foreign room, and liquidity reflect the latest data as of the prior month-end, not the actual review price-cutoff date.
- **Buffer/migration rules (size-migration 2/3 and 1.5x, Small Cap entry) are NOT reflected in this snapshot** — those live only in the cited methodology text, never in `index_eligible_fg`.
- AUM figures elsewhere in the Inclusion Module are indicative only, not actual fund flows.

## Interpretation

- `index_eligible_fg` is a reference indicator, not a final index-inclusion decision.
- Never conflate the eligibility screen's pass/fail with the methodology text's explanation — state both, in their own panels, never merged into one claim.

## Handoff

- What's currently inside the index (holdings, weights) → `dashboard-composition`.
- Returns or risk analytics → `dashboard-performance-risk`.
- What changed at a past review (the actual addition/deletion event) → `dashboard-changes`.
- Comparing eligibility context across indexes → `dashboard-comparator`.

## Guardrails

- Never cite a rule from memory unlabeled — always via `search_index_methodology_stack`, with the methodology name shown, or the mandated fallback note.
- Every dashboard must build through `assets/assemble.py`. This package bundles everything needed to do so: `assets/{dashboard-shell.html, assemble.py, disclaimer-footer.html, disclaimer-notice.txt, refresh-snippet.html, logos/}` and `references/{brand.md, recipes.md, metric-audit.md, mcp-queries.md}`. Full build mechanics, the shared shell/brand/disclaimer stack, and the as-of/range control are documented in `references/recipes.md`'s "Shared conventions" section (self-contained in this package) — apply them exactly as written; do not re-derive or simplify them.
