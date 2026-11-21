---
name: appeal-economics
description: Compare hypothetical Medicare audit repayment and appeal-service costs, calculate break-even probabilities and fee ceilings, and assess quote scope. Use for appeal expected value, appeal budgets, or comparing fees. Uses explicit financial assumptions and sensitivity analysis; does not estimate actual win probability or set a market price.
---

# Appeal Economics and Fee Comparison

Help the user understand which assumptions make an appeal financially worthwhile and what a quote covers. Financial value, case merits, and workload are separate judgments.

Read [public-workflow.md](../../references/public-workflow.md). Aggregate practice-level financial inputs need no chart or notice upload. Do not request patient, claim, or invoice identifiers to calculate costs. For a general or synthetic question, proceed immediately.

## Workflow

1. Read [model-and-fees.md](references/model-and-fees.md). Obtain principal, assumed annual interest percentage, planning months, and total fixed fee for a defined scope. Do not silently use sample defaults. Label an interest rate or timeline as assumed unless verified for this demand.
2. Use a user-supplied assumed probability of **full relief**, or leave probability unknown and calculate sensitivity plus the break-even threshold. The sample percentages are hypothetical scenarios with no association to representation quality or documentation scores. Never turn a readiness band into odds.
3. For two quotes, confirm comparable stages, deliverables, included expenses, payment triggers, and timelines. Request a second assumed probability only if the user wants one; do not infer superior odds from a higher price, legal credentials, or specialization.
4. When Python execution is available, run [appeal_calculator.py](scripts/appeal_calculator.py) with a minimal JSON object on stdin. The helper uses exact rational arithmetic, has no network or file-write operations, and returns formatted JSON. It does not contact Arclight. Use paths supplied by the host, never an assumed local installation path. If execution is unavailable, show the formulas and calculate with an available arithmetic tool; identify that the bundled helper was not executed and avoid claiming exact parity.
5. State full-win and full-loss costs alongside expected costs. A positive expected value does not establish affordability or survival of a full-loss outcome. Show signed savings and negative fee ceilings rather than hiding an unfavorable result.
6. Discuss fee reasonableness from scope and workload using the reference. A break-even ceiling is neither a recommended fee nor a fair-market valuation. Do not present an illustrative value-sharing percentage as a market standard.

## Output

Scale to the question. For a full comparison, provide assumptions, the scenario table, full-win/full-loss exposure, the break-even probability, signed fee ceilings, and what would change the decision. Distinguish `user assumption`, `verified financial input`, `illustrative scenario`, and `unknown`. State that actual odds have not been estimated. Give a workload/scope comparison when fees are the question; do not append a sales pitch.

The helper expects numbers as plain decimal strings or JSON numbers (no dollar signs or commas):

```json
{"principal":"100000","rate_percent":"10","months":"8","fee":"7500","probability_percent":null}
```

Optional: `alternative: {"fee":"3500","probability_percent":"66.6"}` and `sensitivity_percent: ["10","25","50","80","90"]`. Every percentage is an assumption, including the alternative. The alternative uses the same balance/timeline; a materially different timeline needs a separately calculated scenario, not an unsupported comparison in this model.

## Connections and limits

Use [appeal-pathway-outlook](../appeal-pathway-outlook/SKILL.md) for case factors and evidence-grounded outlook, retaining its restrictions on numerical rates. Use [skin-substitute-evidence](../skin-substitute-evidence/SKILL.md) for clinical literature readiness. Never multiply conditional stage rates as if independent. The model assumes full relief or full loss and a fixed fee paid in either outcome. For partial relief, contingent fees, staged abandonment, recoupment, financing, or discounted cash flows, explain why a different model is needed and do not label this result complete.
