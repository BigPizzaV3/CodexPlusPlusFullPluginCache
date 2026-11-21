---
name: bulk-setup-audit
description: >
  This skill should be used when a CallRail agency asks to "export all my tracking numbers",
  "list every tracker across clients", "give me an account inventory", "check call recording compliance",
  "do we have recording notices", "audit our users and admins", "clean up tracker names and source rules",
  "onboard a new client", "set up a new company from a template", "create the same setup for every client",
  or needs a full account export or one-pass client setup that the CallRail UI can't do in one step.
---

# Bulk setup and audit

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

**Scope.** This skill covers the account's admin side: inventory, exports, compliance, configuration hygiene, users and new-client setup. Anything that affects a client's calls or reports (no tracking, forwarding loops, number swapping off, recording off, unused numbers, voicemail, call trends) belongs to agency-health-check, so this skill doesn't flag those. The inventory still shows the raw data (active trackers, website script active, calls in 28 days) for each client.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

Setup mode creates the new company in one account. If the user can reach several, ask which account it belongs in and confirm the account name back before any write. Creating companies, numbers and users needs a role in that account that's allowed to do it. If a write fails with a permission error, stop, say which account and what was and wasn't created.

Two modes. **Audit** builds a full inventory of each account and an admin cleanup list. **Setup** creates a new client company from an agency template in one pass. Ask which mode if the request is unclear.

## Rules for every connector response

- **Check for `_truncated`.** When a response is too large, the connector returns fewer records than requested and adds a `_truncated` object (field, showing, total, message). If it's present, re-request that range with a smaller `per_page` until it's gone. Never treat a truncated page as complete.
- **Page size 100 or less**, and page until `page` equals `total_pages`. Check the total collected against `total_records`.
- **Trackers: start with `per_page: 80`.** Long call flows can exceed result limits. Reduce the page size and restart pagination if needed; inline results are valid.
- **Large responses save to files.** Parse saved files with code (Python or similar) and do all counting there. Consume inline structured results directly. If a result cannot be read, narrow the query or request smaller pages; de-duplicate by id.

## Audit mode (read-only)

1. **Clients:** `list_companies` with `status: active` (paged per the rules above). Keep id, name, created date and `dni_active` (whether CallRail sees the website swap script running). Count disabled clients from `total_records` with `status: disabled` (`per_page: 1` is enough for the count).
2. **Trackers, account-wide:** `list_trackers` with `status: active`, **no `company_id`**, `fields=swap_targets`, `per_page: 80`. Never loop client by client: one large agency took 19 account-wide pages vs 916 per-client calls. Each tracker includes its company id.
3. **Call volume (for context):** `get_calls_summary` with `group_by: company_id`, `fields=total_calls`, last 28 days.
4. **Tags:** `list_tags` with `tag_level: account` for the shared tags. For company-level tags, report only the total from `total_records` (they are usually the same default tags copied into every client; one account had 12,572). Pull company tags only for a named client on request.
5. **Users:** check size first with `list_users` (`per_page: 1`): `total_records` gives the user count. Each user record includes every company that user can see, so on large accounts only one user fits per response. If users x active clients is over 20,000, skip the user detail, report the user count only, and say why. Otherwise page through users and record name, email domain, role, accepted, and number of companies.

### Findings to compute

**Admin companies:** clients whose names contain "template", "transfer" or "test" (whole words, case-insensitive). List them once as "admin or template companies". Include them in the recording-notice and shared-destination findings (a transfer company still records real callers, and a template's settings are copied into every new client), and leave them out of the other findings.

| Finding | Rule | Suggested check |
|---|---|---|
| Recording with no notice | `recording_enabled` true and no greeting: basic flow with empty `greeting_text` and no `greeting_recording_url`, or advanced flow with no `greeting` step | Add a recording notice. Matters most in all-party consent states (for example CA, FL, IL, MD, MA, PA, WA). Say "check with counsel," never "this is illegal" |
| Shared destination across clients | The same `destination_number` on trackers in 2 or more clients | Confirm it's intended (a brand-wide 800 line or a shared call center) and not a copy-paste error |
| Source rules that may never match | `landing_params` rule starts with "?" or "&"; or uses a different parameter key (for example `utm_source`) than most trackers in the account (for example `utm_campaign`) | Fix the rule. Also list trackers whose name doesn't match their `utm_campaign` value, as low priority |
| Trackers with no number | Active tracker with an empty `tracking_numbers` list | Disable or add a number |
| Duplicate tracker names | Same name twice inside one client, after trimming spaces and ignoring case. Also list names with leading or trailing spaces | Rename so reports are readable |
| Texting off on text-capable numbers | `sms_supported` true and `sms_enabled` false | Count only; mention if the agency sells texting |
| Admin sprawl (when users were audited) | Many admins, or admins on personal email domains | Downgrade anyone who only needs reports |

### Output

1. **Headline:** clients, trackers, tracking numbers, and the top 2 to 3 cleanup items with counts. Lead with compliance (recording with no notice) when it's found. End with one line: for client-impact checks (no tracking, unused numbers, swapping, voicemail), run agency-health-check.
2. **Findings table** (above), sorted by risk first (compliance, shared destinations), then tidiness. Show checks that found nothing as "0" so the reader knows they ran.
3. **Workbook** (use the available spreadsheet capability):
   - `Companies`: id, name, created, website script active, active trackers, tracking numbers, calls last 28 days.
   - `Trackers`: client, tracker, type, source rule, numbers, count, destination, SMS enabled, recording, greeting present, created. Skip campaign name; it is almost never set.
   - `Findings`, plus one sheet per finding list (for example `Shared destinations`).
   - `Not audited`: anything skipped and why (users, company tags, admin companies).
4. Never write anything in audit mode.

## Setup mode

1. **Template.** Use the appendix format. Ask for client name, time zone, destination number, area code, and which trackers, tags and users. Offer to copy the structure of an existing client the agency names (read its trackers and tags first).
2. **Plan before any write:**

| Step | Tool | Details | Cost or risk |

   Mark every tracker step "Buys a phone number (billed)". Session trackers buy `pool_size` numbers (minimum 4). Mark user steps "Sends an invite email to this person."
3. **Dry run** (default, or "test" / "preview"): stop after the plan.
4. **On explicit approval**, run in order:
   - `create_company`. New companies come with 4 default tags (Conversion, Existing Customer, Opportunity, Other). Skip any template tag that matches one of these (ignore case).
   - Trackers (`create_source_tracker` or `create_session_tracker` with the new `company_id`). Always pass `sms_enabled` and `recording_enabled` explicitly; texting turns on when omitted. When recording is on, always pass `greeting_text` with a recording notice.
   - `create_tag` (company level) for the remaining tags.
   - `create_user` (with `companies: [new id]`).
   - Stop at the first error and report what was and wasn't created.
5. **Verify:** read back with `list_trackers` (`company_id`) and `list_tags` (`company_id`) and confirm each item exists with the settings in the plan.
6. **Finish** with the new company id, tracking numbers, the swap script URL from the `create_company` response, and what still has to be done in the CallRail app (the connector can't set call flows beyond basic routing, website pool size changes, Multiscripts, integrations, form tracking or AI feature toggles). Also list how to undo the test if it was one (disable the company in the app, which releases its numbers).

### Guardrails

- Never create users with the `admin` role unless the user names it explicitly.
- One company per approval.
- Phone numbers must be E.164 (example: +14045551234). Confirm the destination number back to the user before writing.
- For tests, prefer 1 source tracker (1 number) over a session pool (4+ numbers).

## Appendix: setup template

```
client_name: Smile Dental Midtown
time_zone: America/New_York
destination_number: +14045551234
area_code: 404
recording_enabled: true
recording_notice: "This call may be recorded for quality assurance."
sms_enabled: true

session_trackers:
  - name: Website Pool
    pool_size: 4          # 4-50, each number is billed
    source: all
    swap_targets: [+14045551234]

source_trackers:
  - name: Google Business Profile
    source_type: google_my_business
  - name: Google Ads Call Extension
    source_type: google_ad_extension
  - name: Billboard I-85
    source_type: offline
    campaign_name: Q4 billboard

tags:                     # company level; defaults already exist
  - new-patient
  - booked
  - insurance-question

users:
  - first_name: Dana
    last_name: Lee
    email: dana@smiledental.com
    role: reporting        # admin, manager or reporting
```
