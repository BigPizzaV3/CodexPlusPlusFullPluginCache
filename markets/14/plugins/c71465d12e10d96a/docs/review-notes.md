# Spotify Ads submission preparation

## Package

- Internal name: `app-6aa60b3243908191afabf0d9e3a16d0c`; version: **1.0.0**.
- Display name: **Adzviser Spotify Ads**. Publisher: Adzviser LLC.
- Confirmed existing unpublished/rejected entry and registered endpoint:
  `https://spotify-ads.mcp.adzviser.com/widgets/http`.
- Confirmed reviewer workspace: **Spotify Ads Demo**, containing **ABL Digital Media**.
- All supported countries. Subscriptions are purchased on Adzviser's website;
  this plugin does not offer checkout or purchases.
- Reviewer credentials must be supplied in secure portal fields, never this ZIP.

The package preserves the original identity and version and adds the supplied
Adzviser icon, a concrete MCP declaration, source-specific skills, five positive
Data Mode cases, three negative cases, the supplied video and user-facing release
notes. The listing describes supported reporting features and removes ambiguous
claims about frequency and cost per result. The original downloaded ZIP is intact.

## Five positive cases

1. Account spend, impressions and clicks.
2. Campaign spend, impressions, clicks and completed plays.
3. Ad set spend, impressions and clicks, including currency.
4. Top five ads by clicks, with impressions and campaign context.
5. Monthly spend, impressions and clicks, checked against account totals.

Use a fresh Data Mode conversation for each. Let D be today's local date,
E=D-2, and Y=January 1 of E's calendar year. Request [Y,E], inclusive. Recalculate
dates when reviewing, and explicitly name the year around the January boundary.
No numerical answer is hardcoded into the cases. The user confirmed there was
no recent activity, so year-to-date reporting is used to include historical data.
If a later review has no eligible activity, report that honestly and refresh the
test fixture before using it to demonstrate nonzero reporting.

Three negative cases cover campaign/budget edits, ad creation and publishing,
and access to an unconnected competitor's private account. They should explain
the unsupported action without calling tools to simulate it. No UI-widget case
is included.

## Direct-query evidence and current status

Checked on **October 26, 2026, America/Los_Angeles**. Workspace and catalog
discovery succeeded. All five report requests returned model-visible SpotifyAds
rows with `directData=true`, `reportingMode=data` and no field assumptions.
The requested year-to-date window was **January 1–October 24, 2026**.

| Case | Observed production response | Status |
| --- | --- | --- |
| Account totals | One row: Spend 3,022.205813; Impressions 374,809; Clicks 975. Currency absent. | Blocked for final verification by the date-range defect below. |
| Campaign performance | Four campaigns; additive totals match the account report; 348,278 completed plays. | Blocked for final verification by the date-range defect. |
| Ad set performance | Eight ad sets; totals match the account report; all currency cells blank. | Blocked by date-range and currency defects. |
| Ad ranking | Nine ads; summed impressions/clicks match the account report. | Blocked for final verification by the date-range defect. |
| Monthly performance | Ten periods; totals 3,038.191888 spend, 377,073 impressions and 979 clicks disagree with the full-period report. | Failed reconciliation; recheck after deployment. |

These observations describe the current production responses, **not correct
expected answers**. Do not copy them into a review answer. Reports for
September 25–October 24 returned explicit zeros, which agrees with the user's
confirmation of no activity in that period.

### Confirmed date defect and local correction

A diagnostic daily request for **March 31 only** returned rows for March 31
and **April 1**. The connector adds a day to Spotify's `report_end`, although
[Spotify's v3 aggregate-report reference](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAggregateReport)
specifies an inclusive end date for both DAY and LIFETIME. This also makes
adjacent chunks overlap and can distort totals even when the final extra day
has no activity.

The local Copter fix sends the requested chunk end date unchanged. Regression
tests independently model Spotify's inclusive provider behavior and check
single-day boundaries, leap-year multi-chunk coverage without duplicates, and
reconciliation of adjacent monthly reports. All failed before the correction
and pass afterward. Corrected live account totals remain unverified until deployed.

### Currency correction

The connector reads a top-level ad set currency, while the
[Spotify v3 ad set response](https://developer.spotify.com/documentation/ads-api/reference/v3.0/getAdSetsByAdAccountId)
places it under `budget.currency`. The local fix reads that field when the
legacy top-level value is absent. Tests cover v3 data, legacy data and missing
currency, without rescaling Spend or substituting a guessed currency. Live
currency values must be checked after deployment.

### MCP annotation correction

The local MCP source now marks account-bound connector reporting and workspace
discovery as `openWorldHint=false`. Public-source reporting retains true.
This is a shared correction for source-specific connector profiles; it does not
change tool permissions or reporting inputs. See [tool annotations](tool-annotations.md)
for the five tools' flags and reasons. The two relevant MCP suites passed
**3,215 tests**. The four Spotify connector regression tests passed.

**Neither Copter nor MCP has been deployed as part of this preparation.**
The ZIP does not contain or deploy either backend fix. Deployment, a fresh MCP
scan and re-running the five cases are required before treating this as ready
for review. Packaged notes cannot override annotations served by the MCP server.

## Listing, demo and remaining checks

All four listing links were opened anonymously and inspected on October 26:
Adzviser's website identifies its reporting service; the support page provides
a contact form; the privacy page describes authorized source reporting,
credentials and destination transfers; the terms apply to the service and its
integrations. This verifies the intended destinations, not a legal audit.
The supplied 256×256 PNG is included and inspected.

Demo: https://youtu.be/zprNuYqXTIU

YouTube identified “Adzviser Spotify Ads ChatGPT Plugin Demo” by Adzviser,
199 seconds long, non-private with player status OK. An isolated signed-out
browser played the opening and an inspected frame showed the ChatGPT plugin
directory. Playback then hit a YouTube player error after the sampled frame at
approximately 48 seconds. Full playback, test coverage and absence of sensitive
content throughout the video are **not verified**. This browser failure does
not establish that the supplied video is broken; check the full recording.

The confirmed MCP endpoint returned an OAuth challenge to anonymous requests.
Authenticated direct report calls succeeded through the existing connection.
That does not test a new reviewer's login, consent or callback flow.

Fresh reviewer OAuth, saved-version positive and negative conversations,
imported review metadata, final tool scan, required attestations and full demo
playback: **Not run / incomplete**. Verify reviewer access through the complete
sign-in and authorization flow using the credentials supplied in secure portal
fields. No upload, submission, publication, account change or deletion was performed.
