---
name: agency-report-pack
description: >
  This skill should be used when a CallRail agency asks for "monthly client reports",
  "a report for each client", "roll-up across all my clients", "portfolio report",
  "month over month by client", "compare this period to last period", "report grouped by industry or rep",
  "results by source for my clients", "send call reports to my clients", or wants shareable, branded
  CallRail results reporting that the in-app custom reports can't share or schedule.
---

# Agency report pack

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

Build a monthly roll-up across every client in the CallRail accounts the user can access and produce branded, client-ready results reports with period-over-period comparison.

**Scope.** This skill reports results: calls, forms and sources, this period vs last. It doesn't flag problems or check setup. For "which clients need attention", setup checks or a health report per client, use agency-health-check. For what changed this week (drops, outages, campaigns that ended), use account-health-watchdog.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

## Inputs

Use these defaults and state them in the output; ask only if the user's request contradicts them:

1. **Accounts.** See "Which accounts this covers" above. Build one roll-up per account. If the user wants one combined headline across accounts, give it separately, above the per-account roll-ups, and label it as combined.
2. **Period.** Last full month vs the month before. Any custom range compares to the same-length period immediately before.
3. **Clients.** All active companies. Optional grouping (industry, rep, region) supplied by the user.
4. **Report depth.**
   - 50 or fewer active clients: roll-up plus a full report for every client.
   - More than 50: roll-up plus full reports for the clients the user names, or the 20 biggest by current-period calls if they don't name any. Offer full reports for everyone on request.
5. **Branding.** The agency's name at the top. No CallRail mention in client-facing text unless asked.

## Step 1: roll-up (2 to 4 calls)

1. `get_calls_summary` with `group_by: company_id` (never `company`: client names are not unique, and duplicates would merge two clients), `fields=total_calls,answered_calls,missed_calls,first_time_callers,leads`, for the current and prior period.
2. `get_forms_summary` with `group_by: company`, `fields=total_forms,first_forms,leads`, both periods. Join to clients by name only where the name is unique; otherwise report forms at the account level.
3. Map company ids to names with `list_companies` (`status: active`, **`per_page: 100`**, page until `total_pages`). Never request more than 100 per page. Oversized responses come back with fewer records plus a `_truncated` object, while `total_pages` assumes the requested size, so clients get skipped. Check every response for `_truncated` and re-request with a smaller `per_page` if present. Check the collected count against `total_records`. Exclude disabled clients.
   Companies whose names contain "template", "transfer" or "test" (whole words, case-insensitive) are not clients. Leave them out of the roll-up and totals, and list them with their call counts in the agency notes.
4. **Large results:** for accounts with hundreds of clients, these responses are often too large to read in one pass and get saved to a file. Parse the file with code (Python or similar) and do all math there. Never estimate totals by reading part of the data. If a response comes back inline but is too long to process reliably (forms summaries often do), narrow it or request smaller pages; do not force file output.

## Step 2: seasonal labels

When a client's name clearly points to a seasonal business (festival, fair, county fair, pool, ski, snow removal, tax prep, Halloween, Christmas) and a big change lines up with that season, label its roll-up row "likely seasonal" so the change isn't read as a problem. Match whole words only, never inside other words ("rv" inside "Services", "fair" inside "Fairclaim").

## Step 3: data sanity checks

Before reporting a change, check for setup effects instead of real demand:

- **Tracking just turned on:** if forms or calls go from near zero to a large number (prior period under 10% of current and current over 100), report "tracking appears to have started during this period; no comparison" instead of a percentage.
- **New clients:** prior 0 and current 10+: list as "new this period," not as growth.
- Never print a percentage change over 500%; say "not comparable" and explain.

## Step 4: client reports

For each client in scope (see Report depth):

- `get_calls_summary` with `company_id`, `group_by: source`, both periods.
- `get_forms_summary` with `company_id`, `group_by: source`, current period.
- **Highlights:** `list_calls` with `lead_status: good_lead`, `fields=source,call_summary`, `per_page: 3`. If none (common, since few accounts set lead status), use the 3 longest answered calls instead, and only if `call_summary` is available (Premium). Otherwise skip the section and say why in the agency notes, not the client report.
- **AI search sources:** group sources whose names point to AI assistants or AI search (names that mention ChatGPT, Perplexity, Gemini, Copilot, "AI search" or "LLM") into one "AI search" line, and show it even when small. Agencies want to see this channel grow.

Client report format (short enough to paste into an email):
- **Headline (1 to 2 sentences):** main number, direction, and the main takeaway. Example: "960 calls in September, up 21% from August, almost all from Google Ads. Missed calls rose 51%, so the answer rate slipped from 89% to 86%."
- Table: source, calls, change, forms.
- 2 to 3 plain-language takeaways.
- Highlights if available.

## Step 5: output

1. **Agency headline first:** total calls, forms and change across all clients, number of clients, biggest gainers and the share of calls by top sources (including AI search).
2. **Roll-up table:** one row per client with calls, change, answered, first-time callers, forms, sorted by call volume. Optional grouping by industry, rep or region.
3. Client reports (per Report depth).
4. Workbook (use the available spreadsheet capability): `Roll-up` (all clients), one sheet per full client report.
5. Agency notes: data issues found (tracking start dates, duplicate names, missing summaries, admin and template companies left out).
6. **One line at the end:** for which clients need attention and why, run agency-health-check.

State the date range and time zone on every report.

## Delivery

- Default: chat summary plus files.
- Email: drafts only, one per client, to the contact the user supplies. Never send.
- Slack: draft only; send only with explicit approval.
- Recurring: you may offer a monthly run. If the user requests it, use the available scheduling or Automations capability as described in the runtime guidance.

## Guardrails

- Read-only. Never call write tools.
- Never include transcript text in client reports.
- Client reports describe only that client. Never compare a client with the agency's other clients or mention them.
- Describe changes as results, not diagnoses. Leave causes and fixes to agency-health-check.
