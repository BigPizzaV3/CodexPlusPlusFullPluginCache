---
name: agency-health-check
description: >
  Run a CallRail health check across every client in the CallRail accounts the user can access (or named clients) and build a
  client-ready report per client (spreadsheet tab and 1-page PDF) showing what's working, what needs action,
  why it matters, how to fix it and who owns it. Checks forwarding numbers, number swapping and the website
  snippet, unused or test numbers, recording, voicemail coverage, 30-day call and channel trends, new callers,
  missed and voicemail rates, lead marking, short calls and forms. Use for "run a health check",
  "client review", "prep for my client check-ins", "which clients need attention", "is DNI working",
  "is the swap script on this client's site", "which numbers are we paying for but not using",
  "which clients have no tracking", or a client-ready tracking report, even if they don't say "health check".
---

# Agency health check

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

**Scope.** This is the full per-client review, run monthly or before client check-ins. Hand off to the other toolkit skills for:
- **What changed this week** (sudden drops, campaigns that ended, outages, missed-call spikes): account-health-watchdog.
- **Account inventory, exports, recording-notice compliance, user and tag cleanup, or setting up a new client:** bulk-setup-audit.
- **Reviewing and marking spam calls:** spam-sweep. This skill only counts short calls.

You're helping an agency account manager (usually a CSM) find which of their client companies in CallRail need attention this week, and exactly what to do about each one.

Each company is a different client of the agency, and the agency keeps them separate. So report every company on its own: its own section in chat, its own tab in the spreadsheet. Never blend 2 companies' problems into one list or count problems across companies.

There are 2 audiences. The agency wants a fast internal triage in chat: which clients need work and what. Each client gets a report the agency can forward as-is: what's working, what needs attention, why it matters in the client's terms, how to fix it, who fixes it, and the full list of what was checked. Status always uses words and a symbol (✕ Needs action now, ! Keep an eye on, ✓ Healthy), never color alone. Every flag you raise should say what's wrong, why it matters to their client, and the fix. If you can't check something, say so plainly. A "Not checked" is more useful than a guess.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

For the reports: build one spreadsheet (and one set of client PDFs) per account, and name the account in the file name and the chat overview.

## What you need

- The CallRail connector (tools like `get_account`, `list_companies`, `get_calls_summary`, `list_trackers`).
- A web fetch tool for the swap-target check. Optional but recommended.
- An available browser tool to confirm the snippet and the swap. Optional, but it's the only way to see `<script>` tags and live number swaps, so recommend it when it's missing.
- Code execution to build the spreadsheet (`scripts/build_report.py`, needs openpyxl) and client PDFs (`scripts/build_client_pdfs.py`, needs reportlab). If code execution isn't available, give each company's section in chat instead.

## Two modes

- **Account mode** (default): the user wants every company checked. Follow all steps below.
- **Named-companies mode**: the user names specific companies ("check Smile Dental", "run it for these 6 clients"). Find each with `list_companies` using `search`. If several names are close, use the exact match and name the others in your reply (ask first only if there's no exact match). Then run steps 3 to 8 filtered by `company_id`, with no batch limits, and set `scope` to "{n} checked companies". For step 4, still make the account-wide calls and keep only the named companies' rows (fewer calls than one per company). For the forwarding-number loop check, use the account's full tracker list if you have it; otherwise compare within the named companies and say so. Use the same report format.

## Handling large tool results

The CallRail connector cuts off responses that are too big. It doesn't error. It returns fewer records than you asked for and adds a marker near the end of the result like `"showing": 63, "total": 250` or a "Response exceeded size limit" message. If you miss it, you silently lose companies.

- Use `per_page: 100` for `list_companies` and `per_page: 80` for `list_trackers` (reduce the size and restart pagination if long call flows cause truncation; inline results are valid).
- On every page, compare the records you got to `per_page` and look for a `_truncated` object or a size marker. If the page was cut, re-request that range with a smaller `per_page`. Overlapping pages are fine; de-duplicate by id.
- Check that your final company count matches `total_records` from the first page.

As you page, write only the fields you need into a compact working file (one line or JSON object per company/tracker, with the ID on the same line as each value). Don't keep full raw responses around. Tracker records carry large call-flow objects, and reading values back from separate lists is how IDs and values get mismatched.

If a result is saved to an inaccessible file, use the available result-reading tools or request smaller pages. Keep each ID together with its values. Never reconstruct inaccessible data, hand-copy long lists, or claim a complete audit from partial results.

## Workflow (account mode)

Steps 2 through 4 use account-wide calls on purpose. Agencies can have well over 1,000 companies, and checking companies one at a time will time out.

### Step 1: Pick the account and set the window

1. Call `get_account` and pick the accounts as described in "Which accounts this covers". Run steps 2 to 8 once per account, passing that `account_id` on every call.
2. Default window: last 30 days, compared to the 30 days before that. Compute explicit dates from today (current period = the 30 full days ending yesterday; prior period = the 30 days before that). Use `start_date`/`end_date`, not `date_range`, so the two periods line up. If the user asks for a different window (like 7 days), use it and say so in the summary.

### Step 2: Build the company list

1. Call `list_companies` with `status: active`, paging as described above. Keep: `id`, `name`, `created_at`, `dni_active`, `script_url`, `form_capture`, `lead_scoring_enabled`.
2. Skip disabled companies. Get their count from one `list_companies` call with `status: disabled, per_page: 1` (read `total_records`) and report it in the summary.
3. Companies created less than 30 days before the current period ends are "New". Score them on Setup and Website only (skip Activity, Trend, Lead handling, and Forms) and add "Activity: new company, not scored yet" to its `not_checked` list.

### Step 3: Pull trackers for the whole account

Call `list_trackers` with `status: active`, `fields: swap_targets`, paging as described above. Don't filter by company; one pass over the account is faster. Per tracker keep only: `id`, `name`, `company.id`, `type` (source or session), `source` (type plus any settings), `tracking_numbers`, `destination_number`, `swap_targets`, `created_at`, and from `call_flow` just 3 facts: its `type` (basic/advanced), whether recording is on, and whether any step has `type: voicemail`. Also note `inbound_recording_enabled` from `get_account`.

A **website tracker** is any active tracker that swaps numbers on a site: every session tracker, plus any source tracker with 1+ swap targets whose `source.type` isn't `offline` (for example `landing_params`, `google_paid`, `search`, `referrer`, `direct`, `all`). Source trackers keyed on UTM parameters are common at agencies and use the same snippet, so don't skip them.

Group by company. For each company, record: active tracker count, website tracker count, the tracking numbers and swap targets from its website trackers, and whether any website tracker has source type "all".

Ignore trackers whose company isn't in the active list (they belong to disabled companies).

### Step 4: Pull activity for the whole account

Make these account-wide calls:

1. `get_calls_summary`, current period, `group_by: company_id`, `fields: total_calls,missed_calls,answered_calls,leads,first_time_callers`
2. `get_calls_summary`, prior period, same settings
3. `get_calls_summary`, current period, `group_by: company_id`, `answer_status: voicemail`, `fields: total_calls` (voicemail count)
4. `get_calls_summary`, current period, `group_by: company_id`, `max_duration: 10`, `fields: total_calls` (calls under 10 seconds)
5. `get_forms_summary`, current period, `group_by: company`, `fields: total_forms,leads`
6. `get_forms_summary`, prior period, same settings
7. `get_calls_summary`, last 7 days of the current period, `group_by: company_id`, `fields: total_calls` (for the "Stopped recently" check)

Companies with zero calls are left out of the grouped results. Before scoring, list by name every active company missing from the call results; each one has 0 calls. A company can have forms and still be missing from the call results. Do the same for the 7-day results.

Trend is only scored for companies with 1+ active tracker.

`get_forms_summary` groups by company name, so match on name. If 2 active companies share a name and that name has forms, mark both "Unclear". If the shared name has no forms, both are 0.

### Step 5: Per-number call counts (in batches)

The "Each channel still getting calls" check needs call counts per tracking number, which no account-wide call returns. For each source tracker, call `list_calls` with `tracker_id`, the period dates, and `per_page: 1`, and read `total_records`. Do this for the current and prior period (2 small calls per tracker).

This is the slowest data step, so run it in the same batches as the website check (step 7): 40 companies at a time, biggest clients first. Skip companies that already have a "Went dark" or "Dormant" finding. Companies not reached get "Each channel still getting calls" marked `not_checked`.

### Step 6: Score each company

Read `references/scoring-rules.md` and apply it. It has every check, threshold, and volume guard, plus starting wording for the issue, why it matters, the fix, and who owns it.

After scoring every company, check for **account-wide patterns** (also in `scoring-rules.md`). When most clients share the same gap, like no leads marked or form tracking off, raise it once at the top of the agency's overview as an opportunity and drop it from each company's findings. Client reports never mention these.

A company's status is its worst finding: any `action` makes it ✕ Needs action now, otherwise any `watch` makes it ! Keep an eye on, otherwise ✓ Healthy.

### Step 7: Website check (snippet + number swap)

Read `references/website-check.md` and follow it. In short:

- **Who:** every active company with 1+ website tracker (see step 3). Everyone else is "Not needed" and isn't mentioned in the report.
- **URL:** from form submissions across the account (1 pass), then ask the user for the rest.
- **Tier 1 (web fetch):** is the swap target number on the page? Does the page even have a phone number?
- **Tier 2 (browser):** is this company's `swap.js` loaded (and not another company's)? Does a tracking number show up?

Large accounts: run the website check in batches of 40, highest prior-period call volume first. After each batch, save results and tell the user how many are left. Continue within the authorized scope and available runtime. If blocked or interrupted, mark unchecked companies in the Not Checked tab with "Website: not reached yet" and preserve progress for continuation.

### Step 8: Build the reports

Read `references/report-format.md` first. It has the JSON structure, the checklist, the "what's working" rules, and the chat template.

1. Put every company's results into one JSON file: snapshot numbers, 2 to 3 "what's working" lines, findings (each with issue, impact, fix, owner), and the full checklist.
2. Run `python scripts/build_report.py <input.json> <output.xlsx>`. It creates an internal Overview tab, a client-ready tab for each company that needs attention, and a Not Checked tab.
3. Run `python scripts/build_client_pdfs.py <input.json> <folder>`. It creates a 1-page PDF per company that needs attention. Add `--all` to both commands if the user wants reports for Healthy clients too.
4. Share the spreadsheet and PDFs with the user.
5. Write the chat overview: "Across your account" opportunities first (if any), then one section per company that needs attention (up to 15), then a short Healthy paragraph.

If the user tells you their agency's name, put it in `agency_name` so client reports say "Prepared by {agency}".

## Things to avoid

- Don't flag percentage changes on low-volume companies. Going from 2 calls to 1 is noise. The volume guards in the scoring rules handle this.
- Don't say numbers are swapping unless Tier 2 saw a tracking number on the page. Word Tier 1 results as what they are.
- Don't report on integrations (Google Ads, GA4, CRMs). The connector can't see integration status yet, so anything you said would be a guess.
- Don't change anything in the account. This skill is read-only. Never call `update_company`, `update_call`, `send_text_message`, or any create/delete tool.
- Don't put caller names, caller phone numbers, form contents, or call content in the report. Form submissions come back with personal details; take the URL and nothing else. Tracking numbers and swap targets are fine because they belong to the business.
