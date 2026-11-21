---
name: ai-estimates
description: This skill should be used when the user asks to "estimate a job", "write a quote", "make an invoice", "price this work", "what should I charge", or describes a trade job and wants a PDF. It drafts an estimate, quote, or invoice and has VanReceipts check every price and compute the total.
---

# AI estimates

Use this skill to turn a job description into an estimate, a quote, or an invoice PDF. VanReceipts checks every line and computes the total. Do the workflow below. Do not invent a total.

## Workflow

1. Take the currency from the prices the user writes ($ is USD unless they say CAD, AUD or similar; € is EUR; £ is GBP; or a currency they name) and pass it as an ISO code. If they give no currency, use USD. Never ask a separate question about currency, and do not mention countries. Identify the trade. Call `list_trades` when the trade is not obvious. The trade ids match the 18 trades on vanreceipts.app.
2. Call `get_trade_questions` once. Ask that whole list in one question round, then wait. Include the business name and the client name to print, and the labor rate and the markup on materials when the user has not given them. Do not call `build_document` in the same turn as the questions, and do not fill in names the user has not given.
3. After the reply, a question the user skipped or did not know becomes an assumption. Mark that line `assumption`. Do not ask a second round.
4. Build lines from the user's rates first. Then, only if the host can read the web and the user did not give a price, a supplier page. Then a VanReceipts benchmark, shown as a typical range with rate 0. Last, an assumption.
5. Call `render_document`. It checks every line, computes the total, and opens the editable panel with the PDF. If it returns an error, fix the lines and call it again. Do not add the figures yourself. Use `build_document` only to check lines without showing them.
6. The panel lets the user edit the lines and download the PDF. The panel shows the whole document, so reply in one short sentence and do not repeat the lines, the totals, or draw your own document card.

A photo of the job is context for the lines. VanReceipts does not generate images.

## Price sources

Every line needs exactly one source.

| Source | When | Required fields |
| --- | --- | --- |
| `contractor` | The user gave the rate, the cost, or the markup | none |
| `web` | The host read a current price on a supplier page | `url` (https) and `readOn` (YYYY-MM-DD) |
| `vanreceipts_data` | A published typical range from `get_price_benchmark` | `benchmarkId`, and rate 0 |
| `assumption` | The user skipped the question or the price is a guess | none |

`vanreceipts_data` is a benchmark. It is not the price, and it applies only when the document currency is USD. Put the amount that will be charged on a `contractor`, `web`, or `assumption` line.

The plugin works with no web search. Contractor rates and assumptions are enough.

## Document kinds

- **Estimate.** Needs a valid-until date. An allowance is allowed for an item the client has not picked. Say so on that line.
- **Quote.** A fixed offer. Needs the date the offer holds until, an acceptance line such as "Accepted by client", and deposit terms. No allowance. For USD, VanReceipts adds: "This is not legal advice. Rules vary by state." For any other currency, it adds: "This is not legal advice. Rules vary by location."
- **Invoice.** Needs a due date. No allowance.

Do not put a pay link, card number, or device location on the document. An address is printed only when the user typed it.

## What not to do

Do not compute the final subtotal, tax, or total. Do not present a benchmark as the customer's price. Do not ask the user to pay, and do not pitch a plan. One link is enough when a link is useful: https://vanreceipts.app

## More detail

Read `references/documents.md` when a quote, an allowance, or a benchmark line is unclear.
