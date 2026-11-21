# Google Analytics submission preparation

Package: app-6aa0683f119c8191b279c9cc3ca2496e, version 1.0.0.
The original identity, display name, subtitle, descriptions, category and starter
prompts are preserved. The downloaded ZIP had no MCP declaration and referenced
the generic Adzviser endpoint in its skill dependencies. The Google Analytics
service at https://google-analytics.mcp.adzviser.com/ was verified publicly and
advertises /widgets/http for ChatGPT Data and UI reporting.

The saved portal entry's status and exact registered URL have been requested
from the publisher but are not yet confirmed. Do not treat public endpoint
availability as proof of the existing entry's saved connection configuration.

This preparation includes the supplied Adzviser icon, five Data Mode positive
cases, three negative cases, the demo video, all supported countries, website-only
subscription information and user-facing release notes. No server code was
changed or deployed, and no portal entry was created, deleted, submitted or
published. The preparation does not claim to resolve unspecified review findings.

## Existing-entry upload limitation

An unpublished/rejected Google Ads entry in the same preparation session rejected
a similar update with "Keep the existing MCP connection" and "Publish the existing
MCP app before updating its plugin ZIP." If this Google Analytics entry is in the
same state, it may encounter that restriction too. Its upload has not been tested.
ZIP validation cannot establish portal acceptance. The original internal name
is retained; this package is not a newly assigned plugin identity.

## Direct query evidence and limits

On 2026-10-07, five direct report requests succeeded through the authenticated
Google Analytics development connection available to this session, using Demo.
The connection exposes only the GA4 reporting tools and returned a Demo workspace
with a Google Analytics account. All reports returned isError=false,
reportingMode=data and directData=true. No widget was opened. This is distinct
from testing the uploaded package, saved portal connection or reviewer login.

| Case | Status | Observed result |
| --- | --- | --- |
| Weekly active users | Passed | September 28-October 4: 93 Active users from an ungrouped full-week query. |
| Sessions by channel | Retrieval passed; reconciliation discrepancy recorded | September 1-30: eight channel rows summing to 624 Sessions. The separate ungrouped monthly query returned 625, a difference of one. |
| Active users by device | Passed | September 28-October 4: desktop 59 and mobile 34 Active users. No tablet row was returned. Their sum happened to match the ungrouped result here; this does not establish that user counts are generally additive across devices. |
| Monthly session comparison | Passed | September 625 versus August 910 Sessions: decrease of 285, approximately 31.32%. |
| Daily sessions | Passed | All seven days from September 28 to October 4 returned, totalling 105 Sessions. Rows arrived sorted by value rather than date and were ordered chronologically for interpretation. |
| Fresh-conversation positive cases | Not run | Direct queries validate report execution and returned rows, not complete natural-language routing through the saved plugin. |
| Three negative conversations | Not run | Drafted against capabilities: changing key-event settings, deleting collected data and identifying individual visitors are unsupported. |
| Saved submission and reviewer login | Not run | Portal connection, imported cases, current scan and reviewer-access execution remain unverified. |

Channel rows were Cross-network 251, Organic Search 201, Direct 115, Organic
Shopping 31, Referral 12, Unassigned 11, AI Assistant 2 and Organic Social 1.
The one-session difference from the ungrouped result was not hidden or corrected
by inventing a balancing row. Its cause was not established. The cases distinguish
the sum of returned channel rows from a separate ungrouped count and require an
honest explanation when both are shown. Correctness against the GA4 interface
has not been independently verified.

Daily sessions in date order were 13, 17, 18, 23, 20, 2 and 12. The positive
cases use only Active users or Sessions and the required channel/device
dimension or time grouping. They request no personal identifiers, arbitrary
filters or unrelated data. GA4.data was a header-first row array with numeric
values represented as strings. All relative dates must be resolved again when
reviewers run the cases; observed values are not fixed expected answers.

The reviewer account needs access to Demo and its Google Analytics connection.
Enter credentials only in secure dashboard fields, outside this ZIP.

## Tool annotations and scope

The public endpoint identified itself as Adzviser Google Analytics, running build
6bf20c8d-20261002201522, and advertised the expected five UI-endpoint tools.
Local definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_ga4 | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

- Catalog discovery reads a bounded field catalog without changing analytics
  data or account state.
- Retrieval reads authorized reports and records Adzviser usage and external-tool-use
  state. Those writes explain false read-only and idempotent hints. It does not
  modify GA4 properties, events or collected records.
- Preview compatibility paths can retrieve reports or save presentation preferences,
  so its hints account for those effects. It does not modify GA4 configuration.
- Workspace discovery can clear a stale saved account-selection preference during
  resolution. Repetition has no additional preference effect.
- The app-only reporting-mode control saves a presentation preference without
  modifying analytics records; saving the same mode again is idempotent.

The shared server retains its conservative open-world classification for external
account/service reporting while access remains limited to authorized connected
properties. These notes do not claim that reviewers have accepted those values
and cannot override tool annotations or populate portal review fields. An
authenticated descriptor capture from the saved submission was not available.
No annotation or server-behavior changes were made during packaging.

## Demo, listing and remaining portal checks

Demo: https://youtu.be/QJIMoHtAnRE
Anonymous YouTube metadata returned "Adzviser Google Analytics ChatGPT Plugin Demo"
by Adzviser, a 148-second duration, non-private status and player status OK. Actual
visual playback, legibility, full scenario coverage and absence of secrets were
not independently inspected.

The existing publisher website, support, privacy and terms URLs are the same
ones fetched and inspected earlier on 2026-10-07 while preparing Meta Ads. The
supplied square Adzviser PNG is included as both listing and composer icon.
No new widget review cases or screenshots were added. All supported countries
and website-only Adzviser subscriptions follow the publisher's instructions.

Before uploading, confirm the registered endpoint matches the package and retain
the existing plugin identity. After an accepted upload, verify imported metadata,
complete connection/authentication and domain verification where required,
inspect the latest scan, enter reviewer access securely, and run the cases in
the saved version. Resolve actual review findings before resubmission. Local
archive validation does not establish portal acceptance or review approval.
