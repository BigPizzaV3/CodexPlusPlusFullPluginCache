---
name: spam-sweep
description: >
  This skill should be used when a CallRail user or agency asks to "find spam calls",
  "clean up spam", "why are we getting so many robocalls", "mark these as spam",
  "explain spam calls to my client", "block a robocaller that keeps calling", "who keeps calling my clients",
  or wants a spam review across one or many companies with a client-friendly explanation.
---

# Spam sweep and client explainer

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

Find likely spam calls, separate them from callers that only look like spam (hidden caller ID, vendors, price shoppers, customers who can't get through, broken routing), optionally mark spam after approval, and write a plain-language explanation the agency can send its client.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

## Inputs

1. Accounts: see "Which accounts this covers" above. A caller that hits clients in several accounts can be reported once in the headline, but marking spam happens account by account.
2. Scope: one company, a list, or all companies. Date range default `last_7_days`; baseline is the 28 days before.
3. Mode: dry run (default) or write mode.
4. The agency's own name (used to spot its test calls). Ask once if it isn't obvious from the account name.

## Rules for every connector response

- Check for `_truncated`; if present, re-request with a smaller `per_page`.
- **Page size:** `per_page: 100` on standard accounts. On Premium accounts use `per_page: 50`: every call carries a long `lead_explanation`, and 100-call pages get cut in half.
- Large responses save to files. Parse them with code and do all grouping and counting there.
- Consume the last page whether it is inline or file-backed; do not substitute an ascending first page for the last page. If truncation forces a smaller page size, restart pagination at page 1 with that size and de-duplicate by call id.
- `list_calls` has no duration filter. Use `get_calls_summary` with `max_duration` to size short calls.

## Step 1: size it (2 to 3 calls)

- `get_calls_summary` for the window (total only). This sets the approach.
- `get_calls_summary` with `group_by: company_id` and `max_duration: 10`, for the window and the baseline. Compare each client's short calls this week to its weekly baseline. Clients with 3x or more (and 10+ short calls) are **spike clients**.
- If short calls account-wide are within 20% of baseline, say "no account-wide spam wave" in the headline.

## Step 2: pull calls

- **Up to 2,000 calls in scope:** `list_calls` for the scope, `fields=company_id,source,tags,lead_status`.
- **More than 2,000:** pull every missed call account-wide (`answer_status: missed`) plus all calls for spike clients. Spam is mostly missed or very short; this kept one 22,596-call week down to 2,504 missed calls.
- **Known spam names, 30 days:** for each name on the spam list, run `list_calls` with `search` (for example `search: "spam risk"`) and `date_range: last_30_days`, account-wide. This catches spam that answered calls hide, and it's cheap: one bank's robocalls (260 calls across 7 clients) came back in 3 pages. `search` matches inside words, so confirm matches in code (see name matching).
- **Bank and collections names, 30 days:** run `list_calls` with `search` for "bank", "collections", "credit union", "recovery" and "financial", `date_range: last_30_days`, account-wide. Confirm matches with whole-word matching. These feed the recycled-number check in Step 5.
- Premium accounts: add `call_summary` to `fields` for spike clients only.

## Step 3: classify callers before scoring

Group calls in code **two ways**:
- by `customer_phone_number`
- by **normalized caller name plus tracking number**

Normalize names by lowercasing and removing spaces and punctuation, so "ACMECARD SVCS", "AcmeCard Svcs" and "Acme Card Svcs" all match. Robocallers rotate numbers and fake the client's local area code. In testing, one bank used 56 different numbers on one client, and grouping by number alone missed all of it.

Put each caller into one of these buckets first. Only the last bucket gets scored.

| Bucket | How to spot it | What to do |
|---|---|---|
| **Already handled** | Call already has lead status `not_a_lead` or a tag the agency uses to reject calls (for example "Not Qualified", "Spam") | Count it and leave it alone. Don't double count it as new spam |
| **Hidden caller ID** | Number `+1266696687` (spells ANONYMOUS on a keypad), names "Private", "Unavailable", "Anonymous", "Restricted", or blank name with no location | Many different people sharing one label. Never treat as one caller or score on volume. Count only |
| **Agency test calls** | Caller name contains the agency's name, or the caller is a known agency staff number | Exclude. List the count |
| **Vendors and business callers** | Toll-free or business caller name that calls several clients and is mostly answered with normal length (60s+ average). Examples from auto repair: warranty companies (names like "XYZ WARRANTY"), car dealers, parts suppliers | Not spam, not a new customer. Suggest a "vendor" tag or lead status `not_a_lead`. Ask the agency which vendors are normal for the industry and keep the list in the conversation. Use this bucket only at clients in the vendor's own industry (a warranty company calling an auto shop). At other clients (a warranty company calling a dentist), score the caller as a sales pitch |
| **Price shoppers** | Same number calls several clients **in the same metro or state** (area codes or customer_state match the clients' market) | Real customer comparing shops. Not spam |
| **Customer couldn't get through** | A named person (not a carrier label) with 3+ missed calls to one client in 24 hours | Not spam. Report as a follow-up list for the client |
| **Calls dropping on one tracker** | 5+ different named callers on one tracking number in the window, all missed, all about the same short length (within 3 seconds of each other) | A routing problem, not spam. Report the tracker and suggest running the account-health-watchdog skill on that client |
| **Score these** | Everyone else | Score below |

## Step 4: score the rest

| Signal | Points |
|---|---|
| Same specific caller name (not a generic carrier label like "WIRELESS CALLER") on one tracker from 10+ different numbers, every call under 20 seconds. Callers that own their numbers register one name for all of them | 5 |
| Caller name matches the known spam list (whole words after normalizing) | 3 |
| **Same caller name hits one tracker on 3+ different days**, every call under 20 seconds, from rotating numbers | 3 |
| Same number hit 3+ clients **in different states or markets** in the window | 3 |
| Transcript or call summary has a pitch phrase **said by the customer** (Premium only, see appendix) | 2 |
| Same number called one client 5+ times in 24 hours and every call was under 10 seconds | 2 |
| Answered and under 10 seconds, or voicemail under 5 seconds | 1 |
| Already tagged spam-like (tag contains "spam" or "robo") | 2 |

High confidence: 5 or more. Medium: 3 to 4. Ignore below 3. Never score on duration alone.

**Name matching:** confirm every `search` hit in code with whole-word matching after normalizing ("scam" returns surnames that contain "scam"; "credit" returns any business with "credit" in its name). Generic carrier labels ("WIRELESS CALLER", city-and-state labels like "SPRINGFIELD IL") are never a signal.

**Transcript phrases (Premium):** run `search_transcripts` with `speaker: customer` for each phrase group in the appendix, same range. Drop any phrase that describes the client's own services (a credit union says "business loan"; an auto shop gets real warranty calls). Robocalls are usually too short to transcribe, so a clean transcript search does not mean there's no spam. If the tool returns "Premium Conversation Intelligence plan is required", skip this signal and say so once.

**Bursts:** 5+ calls under 20 seconds to the same tracker within 72 hours from different numbers, not explained by a bucket above. Report as "worth a listen" (no points).

## Step 5: likely recycled numbers

When a bank, collections or debt caller name keeps hitting **one** tracking number (3+ different days in 30), the tracking number most likely belonged to one of that company's customers before. Say so as likely, not certain, and suggest:
- Replace that tracking number in the CallRail app.
- Or have the client ask the caller to remove the number.
- Tell the client's staff to stop answering those calls. Flag it when staff are picking up (in testing, one client's staff answered 91 of 122).

## Output

1. **Headline:** calls checked, short calls vs baseline, high and medium spam counts. When nothing scores high, say "No high-confidence spam this week" plainly. That's a valid result.
2. **Spam table** (if any): confidence, client, caller name, tracker, calls (window and 30 days), numbers used, answered, reasons.
3. **Likely recycled numbers:** client, tracker, caller, calls in 30 days, how many staff answered, suggested fix.
4. **Looks like spam, isn't:** one line per bucket with counts and examples (already handled, hidden caller ID, vendors, price shoppers, test calls, calls dropping on one tracker).
5. **Follow-up list:** customers who couldn't get through, by client.
6. **Reporting note:** if vendor calls are credited to a marketing source, say how many and which source (in testing, warranty company calls counted as calls from the AI search channel).
7. **Client explainer** (separate block, ready to paste, under 200 words, no jargon, no CallRail branding unless asked): what the client is seeing, why (numbers are public on Google Business Profile and ads, autodialers cycle numbers and fake local area codes, caller ID is often hidden), what was found and done, and what the client can do (call back the follow-up list, don't answer the named spam caller, report repeat callers). If there was no real spam, say so and explain the short calls.

## Marking spam

- Marking spam with `update_call` (`spam: true`) **removes the call from billing and reports**. Say this every time.
- Dry run: stop after the output and say nothing was changed.
- Write mode: only high-confidence calls by default. List the exact call ids and count, and wait for explicit approval in chat for that batch. Medium-confidence calls need a separate approval.
- Never mark spam on a call in an excluded bucket, a call with lead status `good_lead`, or a call with a value set. Vendor calls get a tag or `not_a_lead` only after a separate approval.

## Limits

The connector can't block numbers or caller names, or replace a tracking number. Point the user to the block list and number settings in the CallRail app.

## Appendix: spam signals

**Caller names (whole words after normalizing):** spam risk, scam likely, potential spam, telemarketer, robocall, card services, v-number. Count "unknown caller" or "toll free caller" only alongside another signal. Business-funding callers (names with "fund" or "funding" calling a non-finance client) count as medium.

**Transcript phrase groups (customer speaker only):**
- Listing scams: "google listing", "verify your business", "business profile", "google maps listing", "suspended listing"
- Robocall openers: "press 1", "press one", "this is not a sales call", "final notice", "do not hang up"
- Financial: "extended warranty", "credit card services", "lower your interest", "merchant services", "business loan", "pre-approved"
- Vendor pitches: "seo services", "rank on the first page", "website redesign", "lead generation services"

Drop any group that matches the client's own business (auto repair: "extended warranty"; banks and credit unions: the financial group).

Agencies can add their own phrases and vendor names. Keep additions in the conversation.
