---
name: income-and-asset-guidelines
description: Look up how Fannie Mae, Freddie Mac, FHA, VA or USDA treat a type of borrower income or asset, and return the regulator's exact text with its citation and effective date. Use when a user asks what a guide requires for income or assets, for example bonus, overtime or commission income, restricted stock units (RSU), retirement, IRA or pension distributions, social security and gross-up, rental income, self-employment, capital gains, trust, alimony or child support, foster care, temporary leave, a new job offer, paystub or W-2 documentation, variable income, gift funds, gift letters, gift of equity, large deposits, reserves, earnest money, or sale of personal property.
---

# Income and asset guidelines

Answers underwriting questions about qualifying income and assets with the agency's own words.

## Inputs
- The income or asset type the user asked about.
- The agency or loan program, if they named one (Fannie Mae, Freddie Mac, FHA, VA, USDA).

If the user didn't name an agency and the rule differs by agency, ask which one, or answer for each agency the user is likely to need and label each answer.

## Map: where each agency puts the rule (checked 2026-10-12)
FHA: TOTAL Scorecard loans use II.A.4.c (income) and II.A.4.d (assets); manually underwritten loans use II.A.5.b and II.A.5.c, usually with the same subsection letters. Freddie Mac citations are Freddie Mac Guide sections (write "Freddie Mac Guide 5303.1"). VA is M26-7 Chapter 4. USDA is HB-1-3555 9.3; USDA's Income and Documentation Matrix (Attachment 9-A, covering income types, assets and reserves) is filed under HB-1-3555 9.11.

| Topic | Fannie Mae | Freddie Mac | FHA 4000.1 | VA M26-7 | USDA HB-1-3555 |
|---|---|---|---|---|---|
| Bonus, overtime, tips | B3-3.3-02 | 5303.1 "overtime" | II.A.4.c.v "Overtime, Bonus" | Ch. 4 Topic 2 (h) "overtime" | 9.3 "overtime" |
| Commission | B3-3.3-02 | 5303.1 "commission" | II.A.4.c.ix "commission" | Ch. 4 Topic 2 (i) "commission" | |
| Restricted stock units (RSU) | B3-3.3-07 | 5303.1 "restricted stock" | | | 9.11 "Restricted Stock Units" |
| Pension, annuity, retirement income | B3-3.4-03 | 5305.1 (l)-(m) "pension" | II.A.4.c.xii(H) "Retirement Income" | | 9.11 "Pensions" |
| Social Security | B3-3.4-15 | 5305.1 "Social Security" | II.A.4.c.xii(A) "Social Security" | Ch. 4 Topic 2 "Social Security" | 9.3 "Social Security" |
| Non-taxable income, gross-up | B3-3.1-01 "nontaxable" | 5305.1 (r) "tax-exempt" | II.A.4.c "gross" | | 9.3 "gross" |
| Rental income | B3-3.8-01; subject property B3-3.8-02 | 5306.1 "rental income" | II.A.4.c.xii(I) "Rental Income" | Ch. 4 Topic 2 (n) "rental" | 9.11 "rental income" |
| Self-employment | B3-3.5-01 | 5304.1 "self-employed" | II.A.4.c.x "Self-Employment" | Ch. 4 Topic 2 "self-employed" | 9.3 "self-employ" |
| Capital gains | B3-3.4-05 | 5305.1 "capital gains" | II.A.4.c.xii(K) "Capital Gain" | | |
| Trust income | B3-3.4-16 | 5305.1 (q) "trust" | II.A.4.c.xii(M) "Trust" | | |
| Alimony, child support | B3-3.4-02 | 5305.1 "alimony" | II.A.4.c.xii(B) "Alimony" | Ch. 4 Topic 2 (p) "alimony" | 9.3 "alimony" |
| Foster care | B3-3.4-07 | 5305.1 "foster" | | | 9.11 "Foster" |
| Temporary leave | B3-3.3-09 | 5303.3 "temporary leave" | II.A.4.c.xi(C) "Temporary Reduction" | | 9.11 "pre-leave" |
| Job offer, income starting later | B3-3.3-03 | 5303.2 "commencing" | | Ch. 4 Topic 2 (f) "offer" | |
| Paystubs, W-2s, verification of employment | B3-3.2-01 | 5302.2 "paystub" | II.A.4.c.ii(C) "pay stub" | Ch. 4 Topic 2 (e) "pay stub" | 9.3 "pay stub" |
| Gift funds | B3-4.3-04 | 5501.4 (a) "gift" | II.A.4.d.iii(F) "Gift" | Ch. 4 Topic 4 (d) "gift" | 9.11 "gift" |
| Gift of equity | B3-4.3-05 | 5501.4 (a) "gift of equity" | II.A.4.d.iii(F)(4) "Gifts of Equity" | | |
| Large deposits | B3-4.2-02 | 5501.1 (f)(i) "large deposit" | II.A.4.d.iii(A)(2) "individual deposits" | Ch. 4 Topic 4 "deposit" | |
| Reserves | B3-4.1-01 | 5501.2 "reserves" | II.A.5.c.i(C) "Reserves" (manual) | Ch. 4 Topic 4 (a) "reserves" | 9.11 "Assets and Reserves" |
| Earnest money | B3-4.3-09 | 5501.3 (l) "earnest money" | II.A.4.d.i(A) "Earnest Money" | | 9.11 "earnest money" |
| Retirement accounts as assets | B3-4.3-03 | 5501.3 (a) "retirement" | II.A.4.d.iii(C) "Retirement" | | |
| Sale of personal property | B3-4.3-18 | | II.A.4.d.iii(N) "Sale of Personal Property" | | 9.11 "Personal Property" |

## How to use the map
1. Find the user's topic in the map. For each agency that applies, call `lookup_citation` with the citation in the map, then `find_in_section` with the terms shown in quotes. These are the agency's own words, and they may differ from the user's ("individual deposits" is FHA's term for large deposits).
2. The subsection shown (for example II.A.4.c.v) is where the answer usually sits; cite the subsection the passage actually comes from.
3. A blank cell, a topic not in the map, a `not_found` or an `ambiguous` result: fall back to `search_regs` (step 1 of Steps below). Never treat a blank cell as "the agency has no rule".

## Steps (topic not in the map)
1. Call `search_regs` with the topic in the regulator's own vocabulary. Write "restricted stock units", not "RSU"; write "large deposits", not "big deposit"; write "debt-to-income", not "DTI". Set `family` when the user named an agency (fnma, fhlmc, hud for FHA, va, usda).
2. Pick the section whose title fits the question. If no title fits, search again with different regulator terms before concluding anything.
3. Read the passages that answer the question with `find_in_section`, using 1 to 6 short terms from the question (for example "vesting", "200-day moving average", "12 months"). For the whole section, page through `get_obligation` until `next_offset` is null.
4. If a general rule and a special program's rule both appear (HomeReady, Home Possible, 203(k) and others), give the general rule unless the user asked about that program.

## Output
- Quote each relevant passage verbatim, with its `canonical_citation` and a link to `page_url`.
- State any `currency` warning: two versions in force, a pending revision, superseded text, or a later letter that changes it. Say which version you quoted.
- Put any summary after the quotes, labeled "Summary".
- Mention the research-only `notice` once per conversation, in one short line.

## Do not
- Do not paraphrase in place of the quote, or answer from memory. If the corpus doesn't address the question, say so.
- Do not calculate a borrower's qualifying income for them. Quote the calculation method the guide gives.
- Explicit user instructions take priority over this skill.
