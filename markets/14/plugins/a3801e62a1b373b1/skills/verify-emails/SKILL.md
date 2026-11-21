---
name: verify-emails
description: Verify email addresses with SMTPing before sending, importing or storing them. Use when the user asks to verify, validate, check or clean one email address or a list (pasted text, CSV, CRM export), wants to know which contacts are safe to email, asks about bounces, disposable, spamtrap, spambot or complainer addresses, or asks for their SMTPing credit balance.
---

# Verify email addresses with SMTPing

Verify addresses with the SMTPing tools and turn the results into a clear decision for the user: send, remove, or review.

## Tools

- `verify_email`: one address.
- `verify_list`: several addresses as one bulk job (up to 100,000 unique addresses). Lists of 10 or fewer return results directly; larger lists return a `job_id`.
- `get_bulk_job`: progress and results of a bulk job.
- `check_threat`: one address against one threat list (spamtrap, disposable, spambot or complainer).
- `get_credits`: remaining credit balance and plan.

## Before verifying

- Deduplicate the list (lowercase, trim). Skip values that are not email addresses and tell the user how many you skipped.
- Each verified address uses one credit. Before verifying more than 100 addresses, state the number of unique addresses and ask for confirmation.
- For a single address, prefer `verify_email`. Use `check_threat` only when the user asks about one specific list.

## Bulk jobs

1. Call `verify_list` once with the deduplicated list.
2. If it returns a `job_id`, call `get_bulk_job` until the status is `Succeeded`, `Failed` or `Cancelled`.
3. Large jobs can take minutes. If the user does not want to wait, give them the `job_id` so they can ask for the results later.

## Reading the results

Report by band:

| band | statuses | what to tell the user |
| --- | --- | --- |
| safe | valid, alias | Send. |
| avoid | invalid, spamtrap, disposable, blacklisted, complainer, spambot, inbox_full | Remove before sending. |
| judgement | catch_all, unknown, role and anything else | Review. Send only to engaged or high-value contacts, in small batches. |

Explain the risky ones in one line each when they appear:

- **spamtrap**: address used to catch senders with poor list hygiene. One hit can damage domain reputation. Always remove.
- **complainer**: known to mark mail as spam. Remove.
- **disposable**: throwaway inbox, usually gone within hours. Remove from marketing lists, block at signup.
- **catch_all**: the domain accepts every address, so the mailbox cannot be confirmed. Judgement call.
- **role** (info@, sales@): shared inbox, higher complaint rate. Fine for B2B replies, avoid for bulk marketing.

## Output

- One address: the status, the band, and one sentence on what to do.
- A list: totals per band, the count per status, then the addresses to remove. Offer a table with columns email, status, band when the list is longer than about 20 rows.
- Never claim an address is "guaranteed deliverable". Verification lowers bounce risk; it does not guarantee inbox placement.

## Errors

- Not enough credits: tell the user and stop; do not retry.
- Temporary errors: retry once, then report the problem.

## Limits

- Only verify addresses the user has a legitimate reason to process. Verification is list hygiene, not a way to find or identify people.
- Do not send email, find addresses or edit contacts. SMTPing only checks addresses.

Verdict guide: https://smtping.com/13-verdict-types-guide
