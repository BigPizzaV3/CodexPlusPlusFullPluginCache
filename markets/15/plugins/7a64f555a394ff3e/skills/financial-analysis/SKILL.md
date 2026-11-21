---
name: financial-analysis
description: Analyze a company's annual financials across fiscal years (revenue, result, equity, balance sheet total) and its rule-based financial indicators. Use for "financials", "revenue development", "is the company healthy", "Jahresabschluss", "Umsatz", "Bilanz", "Kennzahlen".
---

Use this skill when the user asks about the financial situation or development of one company.

## Workflow

1. Resolve the company with `search_company` (ask when several results fit).
2. Call `get_company` with `sections: ["financials"]`. Add `financial_indicators` when the user asks for an assessment, health, trend or comparison.
3. Present a compact table per fiscal year with the figures that are on record (revenue, result after tax or profit/loss, equity, balance sheet total) and the currency. Leave a cell empty and say "not reported" when a value is missing. Many small companies only file a short balance sheet without revenue; explain that instead of treating it as zero.
4. Describe the development in two or three sentences: direction, notable jumps, equity ratio if both equity and balance sheet total are present.
5. When you show financial indicators, use the neutral quadrant names as returned (ideal, volatile, stable, strained, weak) and state that they are analytical scores based on fixed rules, not a credit rating or a lending recommendation.

## Boundaries

- Only use figures returned by the tools. Do not estimate, extrapolate or fill missing years.
- Do not give investment, lending or credit decisions. Offer the facts and indicators instead.
- If financials are marked `not_loaded`, say they have not been collected yet.
- Answer in the user's language. Explicit user instructions take priority over this skill.
