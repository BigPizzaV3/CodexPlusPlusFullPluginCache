# Margin Erosion Calculator

Answers: A job looked profitable when I quoted it. Where did the profit go?
Learn more: https://omnyra.ai/wiki/business/margin-erosion

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Quoted price | $ | none, ask for it | What the job was quoted at. |
| Amount billed | $ | none, ask for it | What was actually invoiced, after discounts and unbilled extras. |
| Amount received | $ | none, ask for it | What was actually collected. |
| Labor hours | hours | none, ask for it | Hours of labor the job took. |
| Labor cost an hour | $ an hour | $75 | What an hour of that labor costs the business, not what it is billed at. |
| Materials | $ | $0 | Materials the job used. Use 0 if there were none. |
| Subcontractors | $ | $0 | What subcontractors were paid on the job. Use 0 if there were none. |
| Overhead for this job | $ | $0 | The job's share of the business's overhead. Use 0 if it is not known, and say the result leaves overhead out. |

## Before you calculate

- Amount billed must be above 0.

## Formula

1. Direct costs = labor hours x labor cost an hour + materials + subcontractors
2. Gross margin = amount billed - direct costs, and as a percentage of the amount billed
3. Operating margin = gross margin - overhead for this job, and as a percentage of the amount billed
4. Cash margin = amount received - direct costs - overhead for this job, and as a percentage of the amount received
5. Margin expected at the quote = quoted price - direct costs - overhead for this job
6. Lost by not billing the full quote = quoted price - amount billed
7. Lost by not collecting the full bill = amount billed - amount received
8. Total erosion = margin expected at the quote - cash margin

## Rounding

Give dollars to the nearest whole dollar and percentages to one decimal place.

## Worked example

Inputs: Quoted price $50,000; Amount billed $50,000; Amount received $48,000; Labor hours 200; Labor cost an hour $75; Materials $15,000; Subcontractors $5,000; Overhead for this job $3,000.

1. Direct costs = 200 x $75 + $15,000 + $5,000 = $35,000
2. Gross margin = $50,000 - $35,000 = $15,000, which is 30.0% of the amount billed
3. Operating margin = $15,000 - $3,000 = $12,000, which is 24.0% of the amount billed
4. Cash margin = $48,000 - $35,000 - $3,000 = $10,000, which is 20.8% of the amount received
5. Margin expected at the quote = $50,000 - $35,000 - $3,000 = $12,000
6. Total erosion = $12,000 - $10,000 = $2,000

Result for these inputs:

- Direct costs: $35,000
- Gross margin: $15,000 (30.0%)
- Operating margin: $12,000 (24.0%)
- Cash margin: $10,000 (20.8%)
- Lost by not billing the full quote: $0
- Lost by not collecting the full bill: $2,000
- Total erosion: $2,000

Rule of thumb for this result: Margins holding.

## The Playbook's rule of thumb

- The gross margin is above 0 and the cash margin is below 0: **Positive gross, negative cash.** The price looks fine on paper, but after overhead and what was not collected the job lost money. This is the pattern that sinks businesses that look busy.
- The cash margin is above 0 and less than 30% of the gross margin: **Significant margin erosion.** Most of what the job earned on paper did not reach the bank. Find which step took it: discounts and unbilled extras, overhead, or slow and short payments.
- The cash margin is above 0 and at least 30% of the gross margin: **Margins holding.** The cash margin is tracking reasonably close to the gross margin. Keep watching, because erosion builds up slowly.
- Neither the gross margin nor the cash margin is above 0: **No margin to erode.** The job did not cover its direct costs, or it broke even on cash. The price or the direct costs are the problem before overhead or collections.

## Notes

- For several jobs, work each one on its own, then add up the margins and compare the totals to the bands.
- If the owner knows the month's overhead but not each job's share, split it by each job's share of the total amount billed: job overhead = job's amount billed / total amount billed x monthly overhead, rounded to the dollar.
- The Playbook's own calculator flags a job whose operating margin is under 10% or whose cash margin is under 5% as thin.
