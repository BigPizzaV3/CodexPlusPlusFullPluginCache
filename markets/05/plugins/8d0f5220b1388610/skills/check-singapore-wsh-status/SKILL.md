---
name: check-singapore-wsh-status
description: Check a Singapore company's publicly available WSH status against official bizSAFE, MOM Business Under Surveillance, and MOM demerit-point sources. Use for supplier, contractor, or company WSH screening; do not present the result as legal clearance or a complete compliance audit.
---

# Check Singapore WSH Status

## Recommended execution mode

Use ChatGPT Work for the best and most reliable results. This check requires multi-step live web research and may require opening or inspecting official Excel and PDF files. If the current surface is ordinary Chat and Work is available, recommend switching to Work before beginning. If Work is unavailable or the user chooses to continue in Chat, proceed with the available tools and clearly mark any source that could not be verified.

Verify these three items for one or more Singapore entities:

1. Current bizSAFE Enterprise recognition specifically at Level 3, Level 4, or Star.
2. Current listing under MOM's Business Under Surveillance (BUS) Programme.
3. Appearance in MOM's current list of companies with demerit points, including points and debarment details when shown.

## Identify the entity

Prefer the UEN. If it is absent, ask for the exact ACRA-registered name only when the supplied name could identify multiple entities. Never silently choose among ambiguous matches.

Match by UEN whenever the source provides one. A matching UEN is authoritative for entity matching. For name-only checks, normalize case, spacing, punctuation, `PTE LTD`/`PTE. LTD.`, and `PRIVATE LIMITED`, but do not ignore substantive words, branch designations, or joint-venture names.

## Verify current official sources

Use live web access because all three statuses can change. Read [official-sources.md](references/official-sources.md) before checking. Prefer the source itself over search-result snippets or third-party directories.

For bizSAFE, use the WSH Council's bizSAFE Self-Help Excel. Record the matched UEN/name, level, status, and certificate expiry date. Report a positive result only if the level is 3, 4, or Star and the record is current/valid. If a row exists but is expired, suspended, or at another level, state that precisely.

For BUS, search the current MOM BUS PDF by UEN first and legal name second. Use CheckSafe as a corroborating source when a company record is available. If the two official sources conflict, report the conflict and their respective dates; do not resolve it by guessing.

For demerit points, search MOM's current demerit PDF by UEN first and legal name second. Record points, debarment phase/period, and the listing date. CheckSafe may corroborate the result but does not replace the dedicated list.

## Interpret absence carefully

Use these outcome labels:

- `Confirmed`: exact UEN match, or an unambiguous exact legal-name match when no UEN is available.
- `No match found in current public source`: the current source was successfully checked and no matching row was found.
- `Could not verify`: the source was inaccessible, stale without a usable current replacement, the workbook/PDF could not be searched reliably, or identity remained ambiguous.

Never translate absence into “certified safe,” “compliant,” “no enforcement history,” or “no demerit points ever.” CheckSafe generally displays up to three years of records and may omit companies without covered records. Dedicated lists are point-in-time publications.

## Report

Lead with the entity checked and identity confidence. Then give a table with:

| Check | Result | Details | Source date | Evidence |
|---|---|---|---|---|
| bizSAFE L3/L4/Star | Confirmed / No match found / Could not verify | Level, status, expiry | Date shown or access date | Direct official link |
| BUS Programme | Confirmed / No match found / Could not verify | Matched UEN/name | “Accurate as at” date | Direct official link |
| Demerit points | Confirmed / No match found / Could not verify | Points and debarment details | “Accurate as at” date | Direct official link |

Close with a short limitation: this is a public-record screening snapshot, not legal advice, certification, or a complete WSH compliance assessment. Mention any identity ambiguity, inaccessible source, conflicting official record, or stale date prominently.

Do not reproduce entire MOM lists. Quote or transcribe only the row needed for the requested company and link to the official source.
