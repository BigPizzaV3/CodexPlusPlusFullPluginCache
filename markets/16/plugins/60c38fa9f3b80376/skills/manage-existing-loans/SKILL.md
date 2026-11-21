---
name: manage-existing-loans
description: Help someone with loans they already have — what an RBI repo rate change does to their EMI, whether to transfer a loan to a cheaper lender or ask their bank to cut the rate, whether to prepay, and how to clear several loans or credit card balances faster. Use for "RBI hiked rates, what happens to my EMI", "should I do a balance transfer", "write to my bank to reduce my rate", "prepay or invest", "how do I get out of these loans".
---

# Manage existing loans

Explicit instructions from the user override this workflow.

## Rate change ("RBI changed the repo rate")
1. `get_rbi_policy_rates` to state the current repo rate and the next MPC date.
2. Ask the loan's benchmark if unknown (most bank home loans since Oct 2019 are repo-linked / EBLR; older ones MCLR).
3. `calculate_repo_rate_impact` with the user's outstanding, rate, remaining months and the change in bps. Show both options — higher EMI vs longer tenure — and note banks extend tenure by default; RBI lets the borrower choose.

## Cheaper rate available
1. `get_current_interest_rates` for the loan type.
2. `build_rate_negotiation_brief` — then draft a short, polite letter or email to the current lender using its facts (gap, savings, leverage, the specific ask). Asking the current lender to reprice comes first.
3. If the user has a competing offer, `analyze_refinancing` with that offer's rate and fees and give the verdict (switch / negotiate first / stay).

## Prepay or not
`simulate_prepayment` for the user's amount. Compare the interest saved (the "return") with what the money would earn safely, and mention keeping an emergency fund first. If they have several loans, prepay the highest-rate one.

## Several loans or card balances
`plan_debt_payoff` with each loan and any extra monthly amount. Recommend avalanche (highest rate first) unless the user wants quick wins (snowball). If they ask about consolidation, include `consolidationRate` and compare total interest. This is a self-managed repayment plan — never suggest settlement, skipping payments or "debt relief" services, which damage the credit report.

## Answer format
Lead with the number that answers the question, then a small table, then one concrete next step. Close with a one-line estimate disclaimer.
