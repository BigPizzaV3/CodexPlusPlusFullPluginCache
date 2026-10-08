---
name: horizon-scan
description: Scan US federal, optionally selected US states, EU, and UK primary regulatory sources for new and upcoming changes since the user's last scan, scoped to their saved compliance profile, and return each finding with a source citation and a materiality score. Use when the user asks what regulatory or compliance changes affect their business, what is new since their last scan, what is coming up, or which consultations are open. Requires a compliance profile; if the user has none, run the compliance-profile skill first.
---

Read `../../references/runtime-safety.md` before using this workflow. Resolve relative paths from this skill directory. To use a sibling skill, read its `../<skill-name>/SKILL.md`; no special invocation tool is required.


Produce a deduplicated, source-cited list of regulatory developments relevant to one specific
business, with a materiality score on each.

**Read `../../references/citation-discipline.md` before producing any output. It governs everything
below, and where anything here appears to conflict with it, it wins.** The short version: every
claim needs a link fetched in this session, a verbatim supporting quote, and per-claim sourcing for
dates, deadlines, thresholds, and penalties. No link, no claim.

---

## 1. Get the profile

Ask the user for their saved compliance profile block. If they don't have one, run
`compliance-profile` first — do not scan against guesses about their business, because a scan scoped
to the wrong business is worse than no scan.

Read `../../references/profile-schema.md` to interpret it. Extract:

- `last_scan_date` → the start of the scan window. Today is the end.
- `operating_jurisdictions` → which source registry files to use
- `coverage.us_states` → optional selected states; absent means none
- `coverage.pending_state_baselines` → first/re-enabled state windows from the schema
- `coverage.pending_scope_baselines` → historical and standing-law checks for scope changes
- `domains_in_scope` → which domain sections apply
- `exposure_flags` → the applicability triggers
- `materiality_thresholds` → the reporting cut
- `reported_ledger` → what to suppress
- `watch_keywords` / `exclude_keywords` → extra searches and noise suppression

State the window and scope back to the user in one line before scanning, so a wrong profile is
caught before the work rather than after:

> Scanning 2026-07-11 → 2026-09-09 · US-Federal, EU, UK · privacy_ai, employment, esg,
> trade_sanctions, consumer_protection · reporting at medium and above.

## 2. Announce uncovered jurisdictions — before scanning, not after

Announce selected states (or “state coverage off”), their scan windows, and any profile
states not selected. Identify EU member-state implementation, local law, and unsupported
jurisdictions as excluded. For example:

> State research enabled: California and New York. Not searched: Texas (not selected),
> city/county law, and EU national implementation. Source coverage will be reported by state.

This goes first, not in a footnote. A user who believes a jurisdiction was searched when it was not
is the worst outcome this skill can produce.

## 3. Select sources

Load only the registry files you need:

- `US-Federal` → `../../references/sources-us-federal.md`
- Nonempty `coverage.us_states` → `../../references/sources-us-states.md`
- `EU` → `../../references/sources-eu.md`
- `UK` → `../../references/sources-uk.md`

Then read `../../references/cross-industry-domains.md` for the domains in scope, to get the
applicability triggers and the agency slugs and feeds to watch per domain.

## 4. Query primary sources first

Before ordinary delta queries, process pending scope baselines under `profile-schema.md`.
Announce their affected scope and historical window separately. Search older developments and
current standing obligations, including older rules with ongoing duties or transitions; do not
constrain that standing-law review by publication date. Use the relevant baseline start instead
of last_scan_date in historical queries below. Preserve pending entries on incomplete research.

Work the registry in tier order — `primary`, then `regulator`. Start from the official registers when available; use official-domain search as a
fallback to find primary documents, and disclose incomplete enumeration. Do not rely on commentary; the registers are structured, complete for their scope, and citable.

**US federal.** Query the Federal Register API once per relevant agency slug, plus once per
`watch_keyword` using `conditions[term]`. Always set
`conditions[publication_date][gte]=<last_scan_date>` and `[lte]=<today>`. Follow all result
pages, or report the unprocessed range as a coverage gap. Request the full field list from the registry
file. Check `count` before paging; a wide window across many agencies can return thousands.

**Selected US states.** Follow `sources-us-states.md` for each selected state and its
baseline window: discover official legislature, register/code, and relevant regulator
sources, search the profile domains, and record actual coverage for every source family.
Do not treat federal sources as state coverage. Keep state identifiers namespaced in the
ledger and return partial/deferred states explicitly.

**EU.** The OJ L feed covers only the last few days. For any window longer than that, also use
EUR-Lex search or the SPARQL endpoint. **If you cover only part of the window, the EU result is
partial and must be labelled as such** — a feed-only result presented as a full-window EU scan is
the most likely way this skill produces a false "nothing new."

**UK.** Use the dated `/new/uk/<date>` endpoints across the window, or the year feeds filtered by
`ukm:CreationDate`. Separate `UnitedKingdomDraftStatutoryInstrument` (stage `proposed`) from
`UnitedKingdomStatutoryInstrument` (made, but check commencement).

## 5. Filter

In this order:

1. **Ledger comparison.** Follow `profile-schema.md`: re-fetch pending/future ledgered
   instruments as well as new candidates. Suppress only after checking stage and material
   changes. Re-report verified changes as updates. Legacy string IDs have unknown prior
   stages; do not fabricate history or suppress a possible update without checking.
2. **Exclude keywords.** Drop title/summary matches on `exclude_keywords` — unless the item matches
   an `always_report` tag, which overrides exclusion.
3. **Applicability.** Apply the domain triggers against `exposure_flags`. Drop confirmed `not_applicable` items even when a liability keyword matches.
   Keep `unassessed` items separate as applicability questions, not confirmed duties.

## 6. Open the sources and score

For each surviving candidate, **fetch the actual document.** Feed metadata and API abstracts are
triage only — they are not sources for a finding. This is the step that costs time and the step
that makes the output trustworthy, so do not skip it to cover more items. Fewer fully sourced
findings beat more thinly sourced ones.

From the document, extract and quote:

- lifecycle stage, from the document's own words
- every date: comment deadline, entry into force, applies-from, staged milestones, first reporting
- any scope threshold that decides whether it binds this business
- penalty and liability exposure

Then score against `../../references/materiality-rubric.md` on all five axes, naming the profile
field that drove applicability.

**Where a date must be computed** — an EU act's "twentieth day following publication," say — show
the arithmetic, quote the provision it rests on, and label the result as derived rather than
presenting it as a date the instrument states.

**Where no date is published**, the value is `undated`. Never estimate. A proposed US rule has
`effective_on: null`; that is a fact to report, not a gap to fill.

## 7. Run the provenance self-check

Walk every finding against the checklist in `citation-discipline.md`:
`source_url` fetched this session and pointing at the document; `official_id` present;
`supporting_quote` verbatim; every date, deadline, threshold, and penalty traced to a quote;
lifecycle stage matching the source; nothing secondary-tier presented as a finding.

Move every failure to **Coverage gaps** or **Unverified leads**. Do not repair a weak finding by
softening its language — an unsourced claim hedged with "reportedly" is still an unsourced claim.

## 8. Output

```
## Horizon scan · <profile_name>
Window 2026-07-11 → 2026-09-09 · US-Federal, EU, UK · threshold: medium

**Not covered:** <uncovered jurisdictions, or "none">
**Provenance:** N findings, N fully sourced · N coverage gaps · N unverified leads

### Needs attention now
<always_report matches and items where effort exceeds lead time>

### Findings — <jurisdiction>
<ordered per the rubric: always_report, then impact, then timeline, then applicability>

Each finding:
**<Title>** · `<stage>` · <official_id>
<One line on what it does.>
- applicability: `binds_us` — <profile field and threshold, with quote>
- impact: `high` · effort: `policy_change` · timeline: `30-90` (to <which date>) · confidence: `high`
- <each date with its own quote and link>
- source: <link> (<publisher>, <tier>, retrieved <date>)

### Open consultations — you can still influence these
<items with a live comment deadline, soonest first, with the deadline quoted and the link to respond>

### State source coverage
<each selected state, source families/URLs, domains, window, and completeness; or “off”>

### Coverage gaps
<each failed source, what it would have covered, and the date attempted>

### Unverified leads
<secondary-tier signals with no primary source reached — explicitly not findings>

### Updated profile — save this
<the full profile block with new last_scan_date and extended reported_ledger>

---
Regulatory intelligence, not legal advice. Verify against the cited primary sources before acting.
```

Lead with **open consultations** in your summary remarks when any deadline is close. The chance to
shape a rule before it binds is often worth more to the user than notice after it has.

## 9. Emit the updated profile

For each verified finding, append the structured deadline and rule-detail snapshot required by
the schema. Include an explicit previous → current comparison for verified changes, retaining
prior sources. Separate newly relevant older rules from actual legal amendments. Unknown previous
values are labeled baseline unavailable. Clear completed scope baselines only after standing-law
and historical checks succeed; retain partial entries and explain their outstanding work.

Follow `profile-schema.md` for ledger records, legacy IDs, and pruning. Set `last_scan_date`
to today only after a complete scan of the profile's supported scope. On source failures,
partial paging, a narrowed request, or an interrupted scan, retain the previous boundary
and explain that the next scan must retry it. Save sourced findings in the ledger either way.
Change no business fields without the user's request.

Tell the user plainly that the scan is only incremental if they save this block. That is the whole
delta mechanism, and it fails silently if they don't.

---

## Notes on judgement

**A first scan is a baseline, not a delta.** With `last_scan_date` bootstrapped 90 days back across
five domains and three jurisdictions, expect a long list. Say so, and offer to narrow the window or
raise the threshold instead of returning something unmanageable.

**"Nothing new" is a legitimate result** — but only say it when the sources actually returned
nothing, and never when a source failed. A failed source produces a coverage gap, and the honest
sentence is "no changes found in the sources that responded, with N gaps," not "nothing new."

**Volume is not value.** The registers carry a great deal of sector-specific matter irrelevant to any
one business. A scan returning six things that matter is more useful than one returning sixty, and
padding a scan with `monitor_only` items to look thorough works directly against the user.

**Don't let a big-name regulation crowd out a small binding one.** A minor SI that actually binds
this business outranks a landmark regulation that doesn't. Score against the profile, not against
how much the instrument has been in the news.
