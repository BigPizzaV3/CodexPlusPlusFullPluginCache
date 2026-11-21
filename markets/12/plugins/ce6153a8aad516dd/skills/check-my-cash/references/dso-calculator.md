# DSO Calculator

Answers: How long do my customers take to pay me?
Learn more: https://omnyra.ai/wiki/business/days-to-get-paid

## Inputs

| Input | Unit | Default | What it means |
|---|---|---|---|
| Accounts receivable balance | $ | $0 | What customers owe right now on invoices already sent. Use 0 if nothing is owed. |
| Average monthly revenue | $ a month | none, ask for it | Average sales a month, over the last few months. |
| Invoice terms | choose one | Net 30 | How many days customers are given to pay. One of: Due on Receipt; Net 7; Net 14; Net 15; Net 30; Net 45; Net 60. |

## Before you calculate

- Average monthly revenue must be above 0.

## Formula

1. Days to collect (DSO) = accounts receivable balance / average monthly revenue x 30
2. Days over terms = days to collect - invoice terms
3. Receivables if everyone paid on terms = invoice terms / 30 x average monthly revenue
4. Cash tied up beyond terms = accounts receivable balance - receivables if everyone paid on terms, or 0 if that is negative
5. Cash freed by collecting 10 days faster = average monthly revenue / 30 x 10

## Rounding

Give days to the nearest whole day and dollars to the nearest whole dollar.

## Worked example

Inputs: Accounts receivable balance $75,000; Average monthly revenue $50,000; Invoice terms Net 30.

1. Days to collect = $75,000 / $50,000 x 30 = 45 days
2. Days over terms = 45 - 30 = 15
3. Receivables if everyone paid on terms = 30 / 30 x $50,000 = $50,000
4. Cash tied up beyond terms = $75,000 - $50,000 = $25,000
5. Cash freed by collecting 10 days faster = $50,000 / 30 x 10 = $16,667

Result for these inputs:

- Days to collect (DSO): 45 days
- Days over terms: 15 days
- Cash tied up in receivables: $75,000
- Cash tied up beyond terms: $25,000
- Cash freed by collecting 10 days faster: $16,667

Rule of thumb for this result: Healthy.

## The Playbook's rule of thumb

- Days to collect is 45 or under: **Healthy.** Collections are in good shape. Keep watching, because the figure creeps up slowly.
- Days to collect is over 45 and up to 60: **Warning.** Collections are running slow. Terms may be too lenient or follow-up inconsistent. Tightening by even 10 days frees real cash.
- Days to collect is over 60: **Critical.** The business is financing its customers for two months or more, which strains cash. Review how invoices are chased, consider a discount for early payment, and look hard at the slowest payers.

## Notes

- The calculation treats every month as 30 days.
