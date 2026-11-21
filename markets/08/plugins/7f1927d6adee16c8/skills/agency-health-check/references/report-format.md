# Report format

## Who reads what

Each company in CallRail is a separate client of the agency. When the run covers several accounts, each account gets its own JSON input, spreadsheet and PDFs. There are 2 audiences:

- **The agency (internal):** the chat overview and the Overview tab. They're for triage: which clients need work, and what.
- **The agency's client (external):** the client report, meaning that company's spreadsheet tab and its 1-page PDF. The agency forwards these as-is. So they use plain language, no CallRail IDs, no internal jargon, and never mention other clients.

Never mix 2 companies' findings in one list.

## Status labels

Always show the symbol and the words together, never color alone:

- ✕ **Needs action now** (code `action`)
- ! **Keep an eye on** (code `watch`)
- ✓ **Healthy**

## Input JSON for the build scripts

```json
{
  "account_name": "Example Agency",
  "run_date": "2026-10-08",
  "current_period": {"start": "2026-09-08", "end": "2026-10-07"},
  "prior_period": {"start": "2026-08-09", "end": "2026-09-07"},
  "scope": null,
  "disabled_companies": 41,
  "website_tiers_available": {"tier1": true, "tier2": false},
  "agency_name": "",
  "account_patterns": [
    {"title": "You're not marking leads in CallRail", "detail": "14 leads across 98,000 calls this month.", "opportunity": "Marked leads show clients which calls became real opportunities.", "next_step": "Turn on automatic lead qualification, or pilot it with 1 client this month."}
  ],
  "widespread_problems": ["8 of 12 clients missed more than 30% of calls."],
  "companies": [
    {
      "company_id": "COM...",
      "name": "Maple Street Tile",
      "summary": "Calls are down and many go unanswered. 2 fixes would make the biggest difference.",
      "snapshot": {
        "calls": {"current": 12, "prior": 30},
        "new_callers": {"current": 8, "prior": 21},
        "answered_pct": {"current": 58, "prior": 81},
        "leads": {"current": 2, "prior": 6},
        "forms": {"current": 1, "prior": 4}
      },
      "working": ["Form submissions are still coming in (1 this month).", "Number swapping is turned on and the CallRail snippet is on maplestreettile.example."],
      "findings": [
        {"level": "action", "area": "Call volume", "issue": "Calls down 60% (30 to 12).", "impact": "18 fewer calls than the month before.", "fix": "Check for paused campaigns...", "owner": "Agency"},
        {"level": "watch", "area": "Call handling", "issue": "42% of calls missed (5 of 12).", "impact": "5 callers didn't reach anyone.", "fix": "Review business hours...", "owner": "Agency + client"}
      ],
      "checks": [
        {"area": "Setup", "name": "Tracking numbers active", "result": "pass"},
        {"area": "Call volume", "name": "Call volume trend", "result": "action"},
        {"area": "Call handling", "name": "Short or spam calls", "result": "not_enough_data"},
        {"area": "Website", "name": "Number swaps for visitors", "result": "not_checked", "note": "No browser available"}
      ],
      "website_url": "https://maplestreettile.example/",
      "not_checked": ["Website: number swapping needs a browser to confirm"]
    }
  ]
}
```

Field rules:

- `account_patterns`: account-wide opportunities (see "Account-wide patterns" in scoring-rules.md). Internal only; they appear at the top of the chat overview and the Overview tab, never in client reports.
- `widespread_problems`: one-line notes on problems most clients share. Internal only.
- `scope`: `null` for a full-account run. For a subset, text like "6 checked companies".
- `agency_name`: optional. If the user tells you their agency name, it appears as "Prepared by" on client reports.
- `name`: the client-facing name. Agencies often add internal prefixes and suffixes (like "ZZ | 12 | " or "_5550100"). Strip those so the client sees a clean name ("Springfield-MainSt"), and keep the original in `company_id` lookups. If you can't tell what's internal, use the name as-is.
- `summary`: one plain sentence for the top of the client report. For Healthy companies, say so with the main reason ("Calls are steady and almost every call is answered.").
- `snapshot`: use `null` for any value you don't have. `answered_pct` = answered / total × 100, rounded. Leave `forms` null if form tracking is off.
- `working`: 2 to 3 wins with real numbers, for every company, not just Healthy ones (see below). Leading with what's working gives the client context for the problems that follow.
- `findings`: only `action` and `watch`. Every one needs `issue`, `impact`, `fix`, `owner`. The scripts work out the company's status from these.
- `checks`: one entry per check in the checklist below. `result` is `pass`, `action`, `watch`, `not_enough_data`, `not_checked`, or `not_applicable`. Add a short `note` for `not_checked`.
- `not_checked`: short strings for things that couldn't be checked; these also go in the Not Checked tab.

### The checklist (same order every time)

| Area | Check |
|---|---|
| Setup | Tracking numbers active |
| Setup | Website number swapping turned on (DNI) |
| Setup | Forwarding numbers valid |
| Setup | No duplicate tracking for the same source |
| Setup | No test or leftover numbers |
| Setup | Call recording on |
| Setup | Voicemail or backup when no one answers |
| Call volume | Calls coming in |
| Call volume | Call volume trend |
| Call volume | Each channel still getting calls |
| Call volume | New callers |
| Call handling | Calls answered |
| Call handling | Voicemail rate |
| Call handling | Leads being marked |
| Call handling | Short or spam calls |
| Forms | Forms coming in |
| Website | Swap target number on the website |
| Website | CallRail snippet on the website |
| Website | Number swaps for visitors |

Website checks are `not_applicable` for companies with no website tracking numbers. Checks covered by an account-wide pattern are `not_applicable` with note "Not in use".

### What's working (every company)

Pick the 2 or 3 strongest that are true, with real numbers:

- Calls steady or up: "Calls up {pct}% ({prior} to {current})." or "Calls steady at {current} (last month: {prior})."
- High answer rate (10+ calls, 80%+ answered): "{pct}% of calls answered."
- Answer rate improving (10+ calls both periods, up 5+ points): "Answered calls up from {prior}% to {current}%."
- Leads coming in: "{leads} calls marked as leads."
- New callers up: "{n} new callers, up from {prior}."
- Forms coming in: "{forms} form submissions this month."
- Website confirmed: "Number swapping confirmed on {domain}." (browser) or "The business number CallRail swaps is on {domain}." (page text)
- Setup complete (only if every Setup check passed): "Tracking setup passed every check."

If nothing applies (very low volume), write: "{current} calls this month ({prior} last month), too few to judge trends yet."

## Build the files

1. `python scripts/build_report.py <input.json> <output.xlsx>` creates:
   - **Overview** (internal): every company with status, the top issue, the owner of the top fix, calls with a trend arrow, and a link to its tab.
   - **1 client report tab per company that needs attention**: header, summary, snapshot with ▲▼ arrows, What's working, What needs attention (issue, why it matters, how to fix, who), What we checked.
   - **Not Checked** (internal).
2. `python scripts/build_client_pdfs.py <input.json> <output_folder>` creates a 1-page PDF client report per company that needs attention, with the same content as its tab. File name: `{Company} - CallRail health check - {run_date}.pdf`.

Healthy companies get no tab or PDF by default. If the user asks for reports to send to every client, or names the companies they want reports for, add `--all` to both commands.

## Chat overview (internal, for the agency)

```
## Health check: {account_name}
{current start} to {current end}, compared to the prior 30 days
✕ {n} need action now · ! {n} to keep an eye on · ✓ {n} healthy, across {scope or "N active companies"}

### Across your account
- **{pattern title}.** {detail} {opportunity} Next step: {next_step}
- {widespread problem line}
(skip this section if nothing fired)

### ✕ {Company name}: needs action now
- **{Issue}** {Fix in one sentence.} *(Owner: {owner})*
- ...

### ! {Company name}: keep an eye on
- **{Issue}** {Fix.} *(Owner: {owner})*

(one section per company that needs attention, action first, bigger clients first, up to 15)

### {N} more need attention
{names, or "see the Overview tab" if more than 20}

### ✓ Healthy ({n})
{2 to 3 sentences naming the strongest examples with numbers.}

### Not checked
- {Company}: {reason} (group as "{count} companies: {reason}" if more than 5)

Files: {spreadsheet name} (Overview + a client-ready tab per company) and {n} client PDFs ready to send.
```

Writing notes:

- Plain language. "Tracking numbers", not "trackers". "Number swapping", not "DNI", in client-facing text (you can add "(DNI)" once).
- One bullet per finding: the issue in bold, then the fix.
- End with one line on what limited the website check, if anything: no URLs found ("Send me the website URLs and I'll run the website check"), or no browser ("Number swapping wasn't tested in a browser, so website results only confirm the business number is on each page. Use an available browser tool or check in a private browser window to test swapping.").
- Single-company runs use the same format with 1 to 5 sections and no account totals.
