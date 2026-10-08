# Compliance profile schema

The profile is the plugin's only memory. It is a portable YAML block the user keeps — in a project
file or notes — and supplies at the start of every scan. It does two jobs:

1. **Scopes the scan** to one specific business, so results are relevant rather than generic.
2. **Carries scan state** — `last_scan_date` and `reported_ledger` — so each scan reports only what
   is new since the last one. Without this the plugin is a search box, not a horizon scanner.

Treat the profile as a reviewable artifact: counsel should be able to read it, disagree with it, and
version it. Never silently change a field the user set. When a scan implies a profile change (a new
jurisdiction appears in the business's operations, say), surface it as a question rather than editing.

---

## Schema

```yaml
profile_version: 1
profile_name: "Northwind SaaS Ltd — group"
last_scan_date: 2026-09-09        # ISO date. Scan window starts here.
coverage:
  us_states: []                  # Optional: e.g. [US-CA, US-NY, US-TX]
  pending_state_baselines: {}    # US-XX: ISO start date for first/re-enabled scan
  pending_scope_baselines: []    # Outstanding research caused by changes in business scope

business:
  legal_entities:
    - name: "Northwind SaaS Ltd"
      jurisdiction_of_incorporation: UK
    - name: "Northwind Inc."
      jurisdiction_of_incorporation: US-DE
  operating_jurisdictions: [US-Federal, EU, EU-DE, UK]   # see vocabulary below
  sector:
    description: "B2C subscription software"
    naics: "513210"
    sic: "7372"
  public_company: false
  listing_venues: []
  headcount_by_jurisdiction: {UK: 120, EU: 40, US: 900}
  revenue_band: "50-250m USD"

domains_in_scope: [privacy_ai, employment, esg, trade_sanctions, consumer_protection]

exposure_flags:
  personal_data: [customer, employee]        # customer | employee | health | biometric | children | financial | location | none
  ai_systems: [in_product, in_hiring]        # in_product | in_hiring | in_credit_decisions | internal_only | none
  regulated_products: []                     # e.g. medical_device, food, cosmetics, financial_product
  exports_controlled_items: false
  sanctioned_country_touchpoints: []
  consumer_facing: true
  processes_payments: true
  supply_chain_tiers_mapped: 2
  physical_sites: [UK, US]
  unionised_workforce: false

# Questions that must survive when the profile is saved without surrounding prose.
unresolved_profile_fields: []  # e.g. [{field: exposure_flags.personal_data, question: "Biometric data processed?"}]

materiality_thresholds:
  report_at_or_above: medium                 # critical | high | medium | low
  always_report: [criminal_liability, personal_liability, licence_condition]

watch_keywords: ["subscription auto-renewal", "automated decision-making"]
exclude_keywords: ["airworthiness", "fisheries quota"]

reported_ledger:
  federal_register: []
  celex: []
  uk_si: []
  us_states: []
  other: []
```

---

## Field notes

### `operating_jurisdictions` vocabulary

Use these exact tokens so the source registry can be selected mechanically:

- `US-Federal`
- `US-<state>` — e.g. `US-CA`, `US-NY`. Record the business footprint here;
  search only states selected in `coverage.us_states`. Unselected states are exclusions.
- `EU` — Union-level law
- `EU-<country>` — e.g. `EU-DE`, `EU-IE`, for national implementation. **Accepted but out of v1
  coverage**; same disclosure rule.
- `UK` — includes UK-wide instruments. `UK-SCT`, `UK-WLS`, `UK-NIR` for devolved matters.

Anything outside this list is recorded verbatim and reported as uncovered. Never quietly drop a
jurisdiction the user cares about; an unsearched jurisdiction the user thinks was searched is the
worst failure this tool can have.

### Optional state selection

`coverage.us_states` defaults to `[]`, including when an older profile omits `coverage`.
It is a selection list, separate from the business footprint. Offer “Federal only” or
“Federal plus selected states” during setup. Accept full state names or postal codes in
conversation, normalize unambiguous choices to `US-XX`, and echo the selection. Users can
add/remove states later without rebuilding the profile. Never auto-enable state coverage
from incorporation, headcount, or `operating_jurisdictions` alone. An explicit request to
monitor a named state authorizes selecting it; generic “we operate there” does not.

Accepted codes (50 states): AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD
MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY.
Reject ambiguous/invalid selections with a concise clarification; preserve the last valid
selection. DC, territories, and local ordinances are outside this option. “All 50 states”
expands to the explicit list only when requested; explain that coverage may require batches.
No state selection implicitly enables or disables `US-Federal` or other jurisdictions.

For each newly added or re-enabled state, set `coverage.pending_state_baselines.US-XX`
to 90 days before the selection date (or the user's explicit baseline start). For new
profiles use `last_scan_date`. If a selected state lacks historical state ledger records
and a baseline field, establish and disclose this same baseline before scanning.
Search from the earlier of that baseline and `last_scan_date`, through today. Keep the
baseline until all required source families and domains for that state/window are complete;
then remove it. Preserve it on partial or deferred runs, even if other states complete.
Removing a state removes its pending baseline but preserves historical ledger records;
re-adding it always establishes a new baseline. Never reset the global date or ledger
merely to change selections. Existing profiles remain `profile_version: 1` (additive fields).

State ledger records also require jurisdiction, instrument_type, and session, as described
in `sources-us-states.md`. Group findings and source coverage by state. State selection
requests research; it does not promise complete enumeration or establish applicability.

### `exposure_flags`

These drive the applicability triggers in `cross-industry-domains.md`. They are the mechanism that
makes the scan industry-specific, so it is worth getting them right rather than assuming defaults.
Ask when unclear; a wrong flag produces confidently irrelevant results.
Persist each unresolved category or field in `unresolved_profile_fields` as an object with
`field` (a schema path) and `question` (the exact missing fact). For example, retain confirmed
`personal_data: [customer, employee]` and add a question about biometric data. This does not
assert biometric data is present or absent. A null whole field remains appropriate when
nothing is known. Remove only questions the user has answered. Legacy profiles with no
question list must not be treated as evidence that unlisted exposures are confirmed absent.

### `materiality_thresholds`

- `report_at_or_above` filters by impact level from `materiality-rubric.md`.
- `always_report` tags bypass the threshold entirely: `criminal_liability`, `personal_liability`
  (director/officer), `licence_condition`, `reporting_obligation`, `data_breach_duty`.
- Neither ever bypasses the provenance gate in `citation-discipline.md`. A `critical` item with no
  resolvable source is a coverage gap, not a headline.

### `watch_keywords` / `exclude_keywords`

`watch_keywords` add targeted searches beyond the domain defaults. `exclude_keywords` suppress known
noise — high-volume registers like the Federal Register carry a great deal of sector-specific matter
irrelevant to any one business. Exclusions apply to titles and summaries only, never to a document
that already matched an `always_report` tag.

### `reported_ledger`

Each sourced record also stores `snapshots`, an append-only list of observations. Each snapshot
has `observed_on`, `stage`, `deadlines`, `rule_details`, and `sources`. Each deadline has a stable
`key` (obligation, cohort and milestone type), `value` (ISO date/time or null), `status`
(dated, undated, withdrawn or unknown), and source references. Rule details separately record
scope thresholds, duties, exemptions and penalties with provision identifiers and source references.
Each source has URL, publisher, retrieval date, provision locator and a short supporting excerpt
within the host quote budget. Preserve qualifiers, time zones, derived-date calculations and cohorts.
Missing information is unknown, never evidence that a duty or deadline was removed.

Before suppression, compare the newest verified observation with the last saved snapshot by
deadline key and provision. Report changed fields as previous value → current value with both
observations' dates and sources. Append the new snapshot without overwriting earlier evidence.
If retrieval fails, preserve history and report a comparison gap. Legacy IDs or records without
snapshots have unknown prior details: establish a baseline, never invent an old deadline.
Reassess applicability after profile changes even if the legal text is unchanged; label these
items newly relevant to the business, not newly enacted. Keep active duties and incomplete
snapshots under review even when no future deadline is known. Do not prune their records.

Store records keyed by identifier type. Each record has `official_id`, `stage`,
`last_reported_on` (ISO date), and `source_url` from a reported finding. This is an additive
v1 extension; accept legacy string IDs, preserving them until their source is rechecked.
Never invent a prior stage or report date for a legacy string.

- Re-fetch ledgered instruments with upcoming or pending milestones, even when they were
  published before the scan window. Compare current stage and material amendments to the
  saved stage before suppressing an unchanged finding.
- Re-report a verified stage change or material amendment as an update. For legacy IDs,
  say prior stage is unknown and establish a sourced baseline before future suppression.
- Prune only records whose known `last_reported_on` is over 24 months old and which have
  no pending or future milestones. Retain legacy strings of unknown age. Note pruning.
- Do not advance `last_scan_date` on a partial, narrowed, interrupted, or failed scan.
  Retain the old boundary so unsearched periods/domains are retried; record verified
  findings in the ledger to suppress duplicates on retry. Advance only after completing
  the whole requested window across all supported jurisdictions and domains in the profile.
  Permanent out-of-scope jurisdictions stay explicit gaps; they do not prevent advancing
  a completed scan of the supported scope.

---

## Bootstrapping a new profile

When there is no prior profile:

- Set `last_scan_date` to **90 days before today** and say so in the output, so the user knows the
  first scan's window.
- Start `reported_ledger` empty.
- Default `domains_in_scope` to all five cross-industry domains, then narrow with the user.
- Default `report_at_or_above` to `medium`.

A first scan over a 90-day window across five domains and three jurisdictions returns a lot. Say up
front that the first run is a baseline and later runs are deltas, and offer to narrow the window or
raise the threshold rather than dumping an unmanageable list.

---

## Updating an existing profile

Accept a partial update without re-interviewing. Common cases: a new operating jurisdiction, a new
product line, a headcount crossing a threshold, a domain added or dropped.

On update: change the requested fields and add pending scope research as described below; keep `last_scan_date` and `reported_ledger` intact,
and re-emit the whole block so the user has one current artifact to save. Call out when a change
alters what will be in scope — for example, adding `biometric` to `personal_data` engages materially
different obligations, and the user should know the next scan will look different because of it.

### Baselines after a scope change

Adding or re-enabling a country, activity, product, domain or exposure, or crossing a relevant
threshold, creates an entry in `coverage.pending_scope_baselines`. Missing fields in older
profiles mean an empty list. Each entry carries `id`, `changed_on`, `field`, `before`, `after`,
`jurisdictions`, `domains`, `lookback_start`, `standing_law_required: true`, and `status: pending`.
Use a user-specified lookback, otherwise 90 days before the change. Preserve earlier outstanding
entries; do not reset the global date or delete history. Pure removals do not require new research.

The next scan searches the affected scope from the earlier of lookback_start and last_scan_date,
AND reviews currently applicable standing rules and outstanding transition obligations regardless
of publication date. A 90-day publication search alone cannot close this baseline. Report older
rules as newly relevant. Disclose any limit or narrowed request and retain the pending entry until
both historical discovery and standing-law review are complete for its stated scope. Unsupported
countries remain explicitly uncovered with status unsupported; they do not expand source coverage.
State selection still requires explicit authorization. Coordinate overlapping state and scope
baselines using the earliest boundary, and clear each only when its completion criteria are met.
