# Contact and audience analytics (Reteno only)

Use `count_segment_contacts` for people matching conditions, even when the user
does not mention segments. Examples: contacts with an email by profile language;
contacts in a country with a missing custom field; purchasers with at least two
events in the last month; contacts who opened but did not purchase; overlap of
two audiences. Capabilities depend on the selected organization's live definitions,
operators, event parameters, and feature context. Yespo is not supported.

## Plan and execute

1. Fix the selected organization, contact population, profile field/event identity,
   period and timezone, include/exclude logic, and denominator before calculating.
   Resolve business names through live definitions and event metadata. Profile
   language, a custom language field, device language, and activity language are
   different concepts; do not substitute one for another.
2. Read the Segment Designer operating manual. Stage one unbound `DYNAMIC`
   catalog with `list_segment_definitions(for_sdk=true)`, then build each condition
   set with the existing SDK. Reuse that catalog while valid. Run its trusted
   runner with `--mode count` and separate output/diagnostics files for each query.
   It prepares a request containing validated `finish().model` (include, exclude, parameters).
   Call that request through the selected host MCP connection using `count_segment_contacts(schema)`. Never create/update a segment to get statistics,
   hand-patch JSON, or call private recalculation endpoints.
3. Execute sequentially, with at least 11 seconds between calculation starts.
   The live tool limits **6 attempts per 60 seconds per organization**, including
   failures; its internal polling uses no additional allowance. Allow up to ten
   minutes per calculation. Reuse identical successful queries within this analysis
   (same organization, schema, period, and population); do not use stale results
   from earlier requests as fresh counts.
4. Budget at most **20 distinct calculations per user request**, including totals,
   denominators, unknown values, and overlap checks. Estimate work before starting.
   For larger requests, give the count/time estimate and ask one scope question.
   Prefer a narrower comparison or a supported grouped data source over scanning
   every possible value. During performance analysis, a few directly relevant
   audience counts are useful; do not launch a broad profile audit automatically.
5. Validate local diagnostics, then validate the actual MCP receipt using
   `python3 <plugin-root>/scripts/receipts.py count --response <receipt.json>`.
   The MCP success payload contains `totalCount` and `mediaChannels`; only completed
   calculations include `totalCount`. It must be a nonnegative integer. Zero is a
   completed measurement. Pending, timeout, rate limit, malformed response or failure
   means unavailable, never zero. Preserve error evidence and do not automatically
   retry an unknown/timed-out calculation; the backend job may still be running.
   Honor an explicit safe retry and Retry-After from MCP.

## Population and statistical meaning

- Count distinct contact records, not email addresses, devices, or event rows.
- Prefer active/nondeleted contacts as the default population **only when it can
  be represented by supported live definitions**. This MCP tool applies exactly
  the supplied schema and does not add the active `STATE = 1` filter used by
  `get_segment_contacts`. If the catalog lacks that filter, do not invent it or
  silently label the result active-only: disclose that active-only coverage cannot
  be verified and describe the exact matching population. For a specifically
  requested active-only metric, report that limitation instead of substituting.
- “Has email” means the supported email `IS_NOT_EMPTY` condition. It does not mean
  subscribed, deliverable, confirmed, or email-active. Add those filters only when
  requested and supported. `EMAIL IS_ACTIVE` is not a contact-state substitute.
- Fields are a current snapshot, even when an event criterion looks back in time.
  Do not claim historical profile distributions or historical audience membership.
- Use explicit event occurrence and period semantics. At least two purchases is
  an event aggregate threshold, not two contacts. No event and aggregate negation
  are different SDK intents. Preserve rolling versus calendar periods and timezone.
- Share = matching contacts / the explicitly counted base population. A zero
  denominator yields an undefined share. Do not divide by event or send counts.
  Intersections require combined conditions. Do not sum overlapping audiences as
  a unique total. Counts run sequentially can drift as the live database changes.
- Channel subtotals in `mediaChannels` can overlap. Never sum them into total contacts.

## Complete rankings and language breakdowns

A count endpoint is not a group-by or distinct-values endpoint. For an exact
global top-N, first establish a complete authoritative candidate set for the
chosen field from a supported source that proves coverage. Definition facets
describe condition categories, not observed field values. Autocomplete URLs,
common ISO lists, a contact sample, values seen in messages, and guessed country
or language lists do not prove complete profile coverage. Do not call private
autocomplete endpoints to fill the gap.

Count the base population, each mutually exclusive candidate bucket, and missing
values with the same conditions; reconcile their sum with the base count. Keep
unknown/missing separate, and report any unresolved remainder or live drift.
For “languages,” group locale variants by primary language (en-US/en-GB → English)
only when observed/authoritative values or supported exact prefix semantics prove
the mapping. “Locales” keeps variants separate. Do not guess a custom field's
encoding or double-count overlapping prefixes. Rank only after coverage is verified.

If full value discovery is unavailable, state the missing MCP capability: complete
distinct values or a grouped contact-count endpoint for the chosen field. Still
answer any independently supported totals/comparisons within budget, clearly label
coverage, and never present selected candidates as the global top-15. Do not ask
the user to choose favorite languages as a replacement for the requested ranking.

## Reporting

Return a concise summary/table: contact count, exact population and filters,
field/event meaning, event window/timezone when applicable, calculation time,
denominator for percentages, and material coverage limits. Keep schemas, modules,
and diagnostics under `output/segment-designer/`; attach files only if requested.
These counts support workflow audience diagnostics, not forecasts of actual sends,
event volume, conversion causality, or new Reteno Loop readiness gates.
