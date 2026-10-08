---
name: wasted-spend-review
description: Find and explain likely wasted Google Ads spend through Adszy MCP. Use for search-term reviews, negative-keyword candidates, irrelevant-query analysis, zero-conversion spend, or requests to reduce PPC waste.
---

# Wasted Spend Review

Build a read-only candidate list grounded in search-term and keyword evidence.

## Workflow

1. Resolve the account with `list_ad_accounts` when needed.
2. Call `get_negative_keyword_candidates` for the requested window.
3. Use `get_search_terms` to verify the highest-spend terms and `get_keywords` only when keyword context is needed.
4. Rank candidates by:
   - clear intent mismatch;
   - spend with zero conversions;
   - high engagement with no conversion;
   - low-spend terms that need human review.
5. Return term, evidence, why it may be waste, confidence, and recommended review action.

## Guardrails

- Never claim a negative keyword was added or applied.
- Do not treat every zero-conversion term as irrelevant; consider spend, clicks, window length, conversion lag, and business intent.
- Keep strict mismatches separate from judgement calls.
- State the analysis dates and currency.
- Describe savings as avoidable historical spend, not guaranteed future savings.
- If the user asks to make changes, explain that Adszy MCP is read-only and provide a review list instead.
