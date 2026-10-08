# Invoice review rules

## Aging date

Use the live current date as the as-of date. Calculate days overdue as `as-of date - due date` in calendar days.

An invoice is overdue only when its status is `Unpaid` and its due date is before the as-of date. An unpaid invoice due on the as-of date is not overdue.

## Aging buckets

Assign each `Unpaid` invoice to exactly one bucket:

- `Not due`: due date is on or after the as-of date.
- `1-30 days overdue`: 1 through 30 calendar days overdue.
- `31-60 days overdue`: 31 through 60 calendar days overdue.
- `61-90 days overdue`: 61 through 90 calendar days overdue.
- `91+ days overdue`: 91 or more calendar days overdue.

When `Processing` invoices are in the requested population, show them in a separate status group. Do not place them in an aging bucket.

## Customer concentration

Group invoices by exact customer ID. Do not join by customer name or email address.

For each customer and currency, calculate unpaid invoice count, open invoice face value, overdue invoice count, overdue face value, oldest due date, and maximum days overdue.

Calculate customer share with the same-currency open invoice face value as the denominator. Do not combine currencies.

## Priority queue

Order unpaid invoices with this deterministic score:

1. More days overdue.
2. Larger face value within the same currency.
3. Earlier due date.
4. Invoice ID as the stable tie-breaker.

Report these review signals:

- any invoice 91 or more days overdue;
- any customer with more than 25% of same-currency open invoice face value;
- any missing due date, customer ID, amount, currency code, or invoice ID;
- any duplicate invoice ID;
- any invoice with a negative amount;
- any retrieved `Processing` invoice that the user should check in Mercury.

These signals define a review queue. They do not prove collectability, revenue recognition, credit risk, or customer intent.

## Reconciliation

For an open-invoice or aging review, check these equalities for each currency:

- retrieved unpaid invoice count equals the sum of the five aging-bucket counts;
- retrieved open invoice face value equals the sum of the five aging-bucket face values;
- customer open invoice face value equals retrieved open invoice face value when customer concentration is in scope.

For a full status review, also check these equalities for each currency:

- all invoice face value equals `Unpaid + Paid + Cancelled + Processing` face value;
- each invoice appears in exactly one status group.

If a required field is missing, place the invoice in a data-exception table. Do not force it into an unsupported bucket.

## Unsupported measures

Do not calculate or claim these measures unless the live MCP adds the required fields:

- remaining accounts-receivable balance;
- partial-payment amount;
- days sales outstanding;
- collection rate;
- payment time;
- recognized revenue;
- expected loss or collectability.
