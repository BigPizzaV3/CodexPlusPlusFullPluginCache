---
name: client-reporting
description: Marketing reports with Opus Growth - a designed PDF across all connected platforms, a live Looker Studio (Data Studio) dashboard, a shareable white-label Google Ads page, agency roll-ups across many accounts, and the raw numbers for a custom report. Use when the user asks for a report, a monthly or weekly summary for a client or boss, a dashboard, or a link to share.
---

# Reports

Follow the `opus-growth` skill for dates. Pick the format first; they are different products.

| The user wants | Tool |
|---|---|
| A finished, designed report to download or send (all connected platforms) | `marketing_report_pdf` |
| A live dashboard that updates itself, in their own Google account | `looker_studio_report` (settings: `looker_studio_settings`) |
| A link to a web page showing one Google Ads account | `google_ads_shareable_report_link` |
| One report across many Google Ads accounts (agency) | `google_ads_portfolio_report` |
| Numbers to build their own report | `google_ads_client_report_data`, `get_report` |

## Doing it well

- Confirm the period and the account(s), especially for agencies. Default: last full calendar
  month vs the month before, or last 7 full days for a weekly report.
- The PDF's `download_url` is the deliverable: give the link and a three-line summary from the
  response's headline values. Do not re-type the whole report in the chat.
- For a client report, lead with the client's goal metric (leads, sales, ROAS), then spend, then
  diagnosis. CTR and CPC belong in the appendix.
- Each platform credits its own conversions; a cross-platform total of conversions is a sum of
  claims, not unique customers. Say so in the report when platforms overlap.
- Recent days are incomplete (conversion lag). A report run on the 1st for the previous month is
  fine; one run mid-week for "this week" is partial.
- Never put another client's data or account names into a report.

## Agencies

`google_ads_portfolio_report` covers all or selected connected Google Ads accounts in one table.
For other platforms run `get_report` per account and combine, keeping currencies separate.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
