---
name: home-loan-decision
description: Help an Indian home buyer decide whether they can afford a home loan, what rate they will likely get, which bank and government schemes fit, and what the loan will really cost. Use when someone is planning to buy a flat or house, asks "can I afford a ₹X home loan", "how much home loan can I get", or "which bank for my home loan".
---

# Home loan decision

Explicit instructions from the user override this workflow. Skip steps they don't want.

## Answer first, then refine
Start computing as soon as you know the **loan amount** (or property price) and **monthly take-home**. Do not open with a list of questions. Fill every gap with a stated assumption:
- Tenure 20 years · existing EMIs ₹0 · living expenses ≈ 35% of take-home
- Rate: the median from `get_current_interest_rates`
- Salaried private-sector employee · CIBIL 750 · ready property

Say the assumptions in one line. The cards have sliders, so the user can adjust amount, rate and tenure themselves. After the result, ask at most **one** question — the one that would change the verdict most (usually existing EMIs or expenses).

Never ask for PAN, Aadhaar, account numbers or documents with them.

## Steps
1. `get_current_interest_rates` (loanType `home`) — never guess a rate.
2. `check_loan_affordability` with the user's numbers (and the assumptions above) at the median advertised rate. If the verdict is `tight` or `unaffordable`, lead with that and the recommended loan amount before anything else.
3. `predict_my_interest_rate` — the rate this borrower will likely get, and the bank that fits best.
4. `calculate_loan_cost` at the predicted rate — EMI, total interest, APR, tax benefit, saving habits.
5. `find_government_schemes` (purpose Home). For state schemes, check the user's state first.
6. `list_loan_red_flags` (Home, severity high) — pick the 3 most relevant to their situation (e.g. under-construction → pre-EMI trap).

## Answer format
1. **Verdict in one line** — affordable / stretch / not yet, with the safe loan amount.
2. A short table: EMI, FOIR, likely rate, total interest, APR.
3. Best-fit banks (max 3) and why.
4. Schemes that match, with the official portal link.
5. Three things to check before signing.
6. One line: these are estimates, not a loan offer; link to the relevant `openOnSite` page.

## Don't
- Don't present advertised minimum rates as what the user will get.
- Don't recommend a specific lender as "the best"; say "best fit for this profile" and show the alternatives.
