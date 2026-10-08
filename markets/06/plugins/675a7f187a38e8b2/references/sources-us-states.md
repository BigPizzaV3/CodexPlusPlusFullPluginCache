# Optional US state research

For recurring scans, use only states explicitly selected in `coverage.us_states`.
For an explicit one-off named state instrument assessment or calendar request, research
that instrument even if monitoring is off; preserve the saved state selection. This is an on-demand
official-source research workflow, not a maintained feed or a guarantee of complete
50-state monitoring. An empty or absent selection disables state scans.

## Resolve official sources for each selected state

Start at [USAGov's state government directory](https://www.usa.gov/state-governments)
(directory inspected 2026-09-09). Follow the state's official links to establish the
identity of its legislature, administrative register/code publisher, and relevant agencies.
Do not guess a `.gov` hostname: some official legislatures use other domains. If direct
navigation fails, search by state name and agency and verify the publisher through an
official government link. A directory entry is discovery evidence, not a legal citation.

For every selected state, cover these source families for the profile's domains:

1. Legislature: bill status/history, enacted session laws, and codified statutes.
2. Administrative register and code: proposed and adopted regulations, notices, hearings,
   comment periods, emergency rules, and effective-date provisions.
3. Relevant regulators: attorney general/consumer protection, privacy regulator if one
   exists, labor/civil rights/workplace safety, environment, and sector regulators as
   appropriate. Do not assume a state has an agency dedicated to every domain.

Reuse the five domains and exposure flags in `cross-industry-domains.md` as search topics.
For employment, seek workforce location and state-specific headcount; for privacy and
consumer matters, seek relevant customers/residents and statutory scope. Incorporation
alone does not establish applicability. Quote the actual threshold and actor definitions;
do not import federal thresholds or another state's applicability rules.

## Search the selected window

Use each official site's date/status filters and page through the results. Search domain
terms and watch keywords across legislation, rulemaking, and regulator updates. Inspect
amendments and status changes during the window, not just newly introduced bills. Re-fetch
ledgered items with pending or future milestones. A codified text without change history
cannot establish when a change happened; locate the session law or rulemaking notice.

Use official-domain web search when APIs or indexed archives are unavailable, but label
that source family's coverage partial: search results do not enumerate every development.
Do not convert a source-discovery failure into “no relevant laws.” Large selections may
require multiple batches; list every deferred state and preserve its pending window.

Open the official instrument and status record. Distinguish introduced/passed bills from
enacted law, and adoption from commencement. Trace amendments, repeals, and relevant
official court orders affecting operation when encountered; this is not comprehensive
litigation monitoring. Record unresolved operative status as a gap, not a settled duty.

## Identify findings without collisions

Keep the publisher's exact `official_id`. Add `jurisdiction: US-XX` and `instrument_type`
(bill, statute, regulation, guidance, or order) to each state finding. Store state ledger
records under `reported_ledger.us_states`, with the standard source/stage/report-date fields
plus `session` (official session or year when available). Match on jurisdiction, type,
session, and identifier together: “HB 123” in two states or sessions is not one item.
Cross-link a bill and resulting enacted law when the official history establishes the
relationship; do not assume their identifiers are identical.

## Report actual coverage

For each selected state, list source family, official URL, date range examined, domains,
and status: `complete`, `partial`, `failed`, or `not_applicable` with the reason.
“Complete” means the declared sources were enumerated for the window, not that every
possible state obligation has been found. A missing family, truncated results, discovery
failure, or search-only review makes that state's scan partial.

Carry this coverage record and gaps into briefs and calendars. Unselected states are
not searched; identify unselected states mentioned in the profile as exclusions. Municipal,
county, tribal, territorial, and DC law are outside this option. Do not silently treat
New York State selection as New York City coverage.

Follow `profile-schema.md` for newly selected state baselines and cursor updates. If any
selected state's required sources remain partial/failed, do not advance the full-profile
scan boundary. Keep verified findings so retries can suppress unchanged duplicates.
