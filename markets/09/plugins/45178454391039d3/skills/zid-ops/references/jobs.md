# Scheduled jobs

A job runs a store task without someone in the chat: a daily fulfillment batch,
a morning sales brief, a stock sync, an accounting export.

## Pick the trigger

| Trigger | Fits | Needs |
| --- | --- | --- |
| Schedule | Reports, reconciliations, stock syncs, exports, follow-ups | Any runner below and the personal MCP URL |
| Store event | Acting the moment an order is created or changes status, a cart is abandoned or a customer signs up | A Zid OAuth app subscribed to webhooks (the `zid-api` skill); the MCP tools cannot subscribe |

Stock levels and shipment progress run best on a schedule.

## Pick the runner

- **n8n**: Schedule Trigger (or Webhook node for events) → AI Agent with an MCP
  Client Tool on the personal URL ([mcp.md](mcp.md)) → a message node for the result.
- **Make**: the same shape with Make's scheduler and an MCP-capable module.
- **A script under cron or a cloud scheduler**: the MCP SDK with the URL from an
  environment variable, or the Merchant API with an app's tokens (the `zid-api` skill).
- **An agent client with scheduled runs**: give it the task's skill and the time.

## Design rules

1. **Write scope first.** Settle with the merchant, before the job runs, which
   changes it makes and to which records (for example: add a tracking number to
   orders the courier picked up). A call that answers `confirmation_required`
   needs a person: the job sends them the plan and applies it only after they
   approve, so schedule approval-gated changes where someone is there to answer.
2. **One writer per field.** Do not schedule a job that writes what a connector
   app already writes (`zid_account.list_installed_apps`).
3. **Run twice, change once.** Keep a record of what each run handled (order id
   and the status it set). Repeating a manage call repeats the change, so check
   the record or read the order before writing.
4. **Overlap windows.** Read a little more than the interval (a daily job reads
   the last 26 hours) and drop what the record shows as done.
5. **Dates.** Tools take `YYYY-MM-DD`; report periods resolve in Asia/Riyadh.
6. **Report every run.** Send counts of what was read, changed, skipped and
   failed. A run that sends nothing is a failure to look into.
7. **Limits.** Page through every list; on a `429`, wait the seconds given and
   continue one call at a time.

## Job recipes

| Job | Schedule | Steps from |
| --- | --- | --- |
| Fulfillment batch and courier reconciliation | Daily, before the courier's pickup | `order-fulfillment` |
| Sales brief and P&L | Daily, early morning | `sales-report` |
| Stock sync from the ERP or POS | Hourly to daily | `stock-sync` |
| Sales and payouts to accounting | Daily or monthly | `accounting-export` |
| Abandoned-cart follow-up | Daily | `abandoned-carts` |
| Review and question replies | Daily | `reviews-and-questions` |
| Customer sync to CRM or email tool | Daily | `customer-sync` |
