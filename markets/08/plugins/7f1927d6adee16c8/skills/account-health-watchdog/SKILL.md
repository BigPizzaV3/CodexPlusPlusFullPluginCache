---
name: account-health-watchdog
description: >
  This skill should be used when a CallRail agency or admin wants a weekly early-warning digest of what
  changed across every client in the CallRail accounts the user can access: "did any client stop getting calls", "alert me when calls drop",
  "monitor my clients every week", "what changed this week", "did a campaign end", "were there any outages",
  "is my Google Ads number still working", or a Monday digest of call drops, missed-call spikes, recovered
  outages and campaigns that ended.
---

# Account health watchdog

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

Scan every active client in a CallRail account for what changed in the last 7 days (calls that stopped or dropped, misses that spiked, campaigns that ended, outages) and produce one prioritized weekly digest.

**Scope.** This skill only looks at week-over-week change in calls and forms, and is built to run fast every Monday. It doesn't check setup (forwarding numbers, number swapping, recording, voicemail) or build client reports. For those, or for a full monthly review of each client, use agency-health-check. For account inventory and cleanup, use bulk-setup-audit.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

## Inputs

1. **Accounts.** See "Which accounts this covers" above. Steps 1 to 5 run once per account.
2. **Window.** Default `last_7_days`. Baseline: the 28 days before the window, scaled to a weekly average.
3. **Thresholds** (confirmed defaults; the user can change them):
   - No calls: baseline 5+ calls a week, 0 this week.
   - Calls down: baseline 5+ calls a week, this week at or below half.
   - Missed calls up: 10+ calls in both periods, missed share up 15 points or more.
   - Zero answered: 10+ calls this week, none answered.
   - Forms down: baseline 5+ forms a week, this week at or below half.

## Step 1: get the full client list (watch the paging)

- `list_companies` with `status: active` and **`per_page: 100`**, paging until `page` equals `total_pages`. Never ask for more than 100 per page. When a response is too large, the connector returns fewer records than requested and adds a `_truncated` object (showing vs total); `total_pages` is still based on the requested size, so whole blocks of clients get skipped unless you catch it. Check every response for `_truncated` and, if present, re-request that page with a smaller `per_page`.
- **Last page:** consume inline structured results directly, or parse an accessible result file. Do not change page sizes to force file output. If a page size must change because of truncation, restart pagination at page 1 with the smaller size and de-duplicate by client id.
- Check the count you collected against `total_records`. If they don't match, stop and say so.
- Keep each client's id, name, created date and `dni_active`.
- Exclude disabled clients entirely. A client disabled during the baseline would otherwise look like "calls stopped."
- Clients created after the baseline starts have only part of a baseline. List them as "new, partial baseline" and don't flag drops for them.

## Step 2: pull the numbers (2 to 4 calls, process in code)

- `get_calls_summary` with `group_by: company_id`, `fields=total_calls,answered_calls,missed_calls,leads`, for the window and for the baseline.
- `get_forms_summary` with `group_by: company`, `fields=total_forms`, for both periods. Forms can only be grouped by name, so join to clients by name only where the name is unique among active clients. If the account has 0 forms in both periods, say "form tracking not in use" once and skip all form checks.
- **Large results:** for big accounts these responses are often too large to read and are saved to a file. Parse every saved file with code (Python or similar) and do all math there. If an inline response is too large to process reliably, narrow the scope or request smaller pages; do not add fields just to force a file. Never estimate by reading part of the data.

## Step 3: flag and group

Apply the thresholds to active clients only, then sort each flag into one group:

| Group | Rule | Priority |
|---|---|---|
| **Likely campaign ended** | No calls (or near zero) this week, the daily trend shows calls stopped on the 1st of the month (or within a day of it), trackers are still active, **and only paid sources stopped** (Google Ads, Microsoft Ads, LSA, Meta, call extensions, PPC or campaign trackers) | Flagged on its own list. Check: campaign status, budget, contract end date |
| **High** | No calls this week (not month-start); **all sources stopped, including unpaid ones** like Google Business Profile, organic or direct (points to call forwarding, the number itself, or the client leaving, not a campaign); zero answered; missed share now 60% or more | Act today |
| **Outage, recovered** | Calls stopped for 3 or more business days in a row inside the window (or bridging baseline and window), then came back. Weekends with zero calls don't count | Medium. Report the dates, the business days lost, and estimated calls lost (baseline daily average x business days). Agencies should tell the client |
| **Medium** | Calls down 50%+; missed calls up 15+ points; forms down 50%+ | Look this week |
| **Likely seasonal** | Would be High or Medium, the client name clearly points to a seasonal business, **and** the change fits the time of year: a drop going into the off-season, or a rise going into the season. A drop during the season keeps its normal priority | Low |

To tell paid from unpaid, compare `get_calls_summary` by source for the baseline and the window: if the sources that went to zero include any unpaid source (Google Business Profile, organic search, direct, referral, "SEO" trackers), it's High, not campaign ended.

To find recovered outages, run `get_calls_timeseries` (`interval: day`) for every client flagged as down 50%+ and for any client whose window total is under 60% of baseline. Look for runs of 3+ zero-call business days followed by calls.

How to confirm "likely campaign ended": for each client with no calls (or 90%+ drop), run `get_calls_timeseries` (`interval: day`, from 21 days before the window to its end). If the last calls fall on the last day of a month and nothing follows from the 1st, it qualifies. Also run `list_trackers` for the client: if every tracker is still active (especially paid search, call extension or campaign trackers), say "tracking looks intact; the campaign likely ended or paused." If trackers were disabled, say that instead.

**Seasonal matching uses whole words only.** Match these as complete words in the client name (case-insensitive): festival, fair, county fair, pool, pools, ski, golf, marine, boat, boats, yacht, outboard, car wash, landscape, landscapes, landscaping, lawn, greenhouse, Harley, RV, snow, Christmas, Halloween, tax. Never match inside other words ("rv" inside "Services," "fair" inside "Fairclaim"). When unsure, don't label it seasonal. Let the agency mute any client from future digests and keep the muted list in the conversation.

## Step 4: dig into the top flags

For every High flag (and up to 10 Medium flags with the largest drops):

- **Missed-call spikes and zero answered:** `get_calls_summary` with `company_id`, `group_by: source`, this week. Name the source where the misses are happening (in testing, all 26 missed calls for one client were from Google Ads while Facebook calls were answered). That points to that tracker's routing or hours.
- **Drops:** `get_calls_summary` by source for both periods to name which source fell.
- **One-day spikes:** if `get_calls_timeseries` shows one day with 3x or more the daily average and most of those calls missed, say it looks like a robocall burst or a phone outage that day, and suggest running the spam-sweep skill on that client for that date.
- **Trackers:** `list_trackers` (`company_id`, `status: active`) to name the numbers involved.

## Step 5: market clusters

Many agencies put the market or rep in the client name (examples: "TX_Austin_Riverside Dental", "ZZ | 101 | SpringfieldIL"). Detect a consistent prefix pattern. If 3 or more flags share the same market or group, call it out as a cluster at the top of the digest. Clusters often mean one shared cause (a rep, a station, a campaign).

## Output

1. **Headline:** clients checked, number flagged by group, and the single most urgent item.
2. **Likely campaign ended** list: client, calls per week before, the date calls stopped, tracker status, what to check.
3. **High**, then **Outage, recovered**, then **Medium**, then **Likely seasonal**: client, what changed, since when, likely cause, what to check.
4. **Clusters**, if any.
5. **Counts:** active clients checked, new clients with a partial baseline (listed by name), clients with calls this week, small clients under threshold that went quiet (count only), disabled clients excluded.
6. **Limits (one line):** the CallRail MCP can't read integration errors, DNI alerts, account closure events or audit logs, so this digest infers problems from call and form volume.
7. **Next step (one line):** for flagged clients that need a setup check or a client-ready report, suggest running agency-health-check on those clients by name.

Save the full flag list to a file when there are more than 20 flags.

## Delivery

Chat by default. Slack or email: drafts only. You may offer a weekly run on Monday morning. If the user requests it, use the available scheduling or Automations capability as described in the runtime guidance.

## Guardrails

Read-only. Never call write tools. Present causes as likely, not certain.
