---
name: sales-report
description: Report a Zid store's sales and profit for any period. Use for a daily brief, a period comparison, a profit and loss estimate, best sellers, a breakdown by channel, city or payment method, or a report across several stores.
---

# Sales report

Answers "how did the store do" with numbers the merchant can check, and says
where each number came from.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Read only. This skill changes nothing in the store.
- Every figure names its source (report or orders) and period. Estimates are
  labelled as estimates, with what they leave out.
- Amounts are in the store currency; dates are `YYYY-MM-DD`, and report periods
  resolve in Asia/Riyadh.

## 1. Settle the question

Period, comparison (previous period, same weekday last week, same month last
year), and the figures wanted: sales and orders, profit, products, channels,
customers. For a daily brief, default to yesterday against the same weekday a
week earlier.

## 2. Read the numbers

| Figure | Read |
| --- | --- |
| Headline totals: sales, orders, sessions, conversion | `zid_reports.sales_summary` with `period` (`yesterday`, `last_7_days`, `this_month`, `last_month` …) or `date_from` and `date_to`; `compare` true adds the previous period |
| Revenue, discounts, shipping, tax, cost of goods, margin, returns | `zid_reports.sales_report`; `components` breaks it down by `periods`, `channel`, `location`, `products`, `category`, `coupons`, `city`, `payment_methods` and more; `peak` finds the busiest weekday or hour |
| Best sellers | `zid_reports.top_products`, or `zid_reports.products_performance` for one row per product |
| Today, as it happens | `zid_reports.live_sales` |
| How current the data is | `zid_reports.data_freshness` |

**When the store has no analytics access**, the reports answer that analytics is
not available. Then:

1. `zid_orders.list_orders` with `dateFrom` and `dateTo`, `perPage` 100, every page.
2. Leave out `cancelled` orders and orders whose payment failed; count the rest.
3. Total the order amounts, discounts, shipping and VAT, and say the figures were
   computed from orders. `zid_reports.live_sales` still works for today.

## 3. Profit and loss

Reports give gross margin as a percentage, not profit. Build profit as:

| Line | Source |
| --- | --- |
| Net sales | `zid_reports.sales_report` (or the order totals), after discounts and returns, without VAT |
| − Cost of goods | `cogs` in `zid_reports.sales_report`; it needs a cost on each product. Name the best sellers without a cost and leave them out of the estimate |
| − Payment fees | `zid_payments.get_account_statement` for ZidPay, or the rates in `zid_payments.get_fee_plan` × card sales |
| − Shipping costs | `zid_shipping.list_shipping_charges` for Zid Ship labels and fees; other carriers from the merchant's invoice |
| − Other costs | Ads, salaries, rent: only what the merchant provides |
| = Profit (estimate) | Show each line, so the merchant can correct one |

## 4. Several stores

Each store has its own connection. Report each store separately, then a total
row, converting currencies only at the merchant's exchange rate.

## Output

- **Daily brief**: sales, orders, average order value and conversion against the
  comparison, with the change in percent; top 5 products; one line on anything
  unusual (a sales drop over 20%, a product that stopped selling, a spike in
  returns); and orders waiting in `new` for more than a day.
- **Period report**: the table of figures with sources, the breakdown asked for,
  then two or three observations backed by the numbers.
- **P&L**: the line table above with the estimate flagged and the missing costs listed.

Done when every figure names its source and period, and every comparison shows both values.

To send the brief every morning, use the `zid-ops` skill for scheduled jobs.
