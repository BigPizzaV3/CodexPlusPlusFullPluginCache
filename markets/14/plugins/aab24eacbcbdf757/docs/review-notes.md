# X Ads submission preparation

Prepared on October 26, 2026. Original package identity
`app-6aa3b5dca7bc8191b4db37504d521a64`, version `1.0.0`, public name
`Adzviser X Ads`, subtitle, and starter prompts are preserved. The original
download is unchanged in Downloads. No portal entry was created, uploaded,
submitted, published, or deleted during this preparation.

The owner confirmed that this entry is unpublished/rejected and that its
registered MCP endpoint is https://x-ads.mcp.adzviser.com/widgets/http.
The owner confirmed reviewer access to the workspace and account `X Ads Demo`.

## Package contents

The root manifest and compatibility manifest have matching identity, version,
listing, publication, and review metadata. The endpoint is declared in `mcp.json`
and both skill dependencies. Skills are specialized to X Ads field discovery,
date handling, campaign-row aggregation, currencies, and reporting boundaries.

Included: the supplied Adzviser icon, five positive Data Mode cases, three
negative cases, demo URL, all supported countries, website-only subscription
information, and user-facing release notes. Preview UI remains available on
explicit request; no review case requires a widget. No credentials or private
app bindings are packaged.

## Historical period selection

September 25–October 24 returned zero Cost, Impressions, Clicks, and URL clicks.
A wider July 27–October 24 check also returned zeros. July 1–26 returned just
one impression and no spend or clicks. The owner then explicitly requested
an older period. January–June returned real spend, impressions, and clicks.

The five cases therefore intentionally use fixed historical dates in 2026,
not a rolling recent interval. This preserves the selected active period even
if the reviewer runs them later. These are fixed request dates, **not hardcoded
answers**. Every result must be retrieved live. The skills still resolve relative
dates normally when a user asks a relative-date question.

## Five positive prompts

1. How much did we spend on X Ads from April 1 through June 30, 2026 in X Ads Demo?
2. How many impressions and clicks did we get from April 1 through June 30, 2026 in X Ads Demo?
3. Show X Ads spend, impressions, and clicks by campaign from April 1 through June 30, 2026 in X Ads Demo. Show only campaigns with activity.
4. Compare X Ads spend, impressions, and clicks for April–June 2026 with January–March 2026 in X Ads Demo.
5. Show daily X Ads spend, impressions, and clicks for April 2026 in X Ads Demo.

## Direct-tool verification

Workspace and field discovery succeeded. The five exact underlying requests
were executed through the authenticated X Ads connection available in this
session. All returned `isError=false`, `directData=true`, and
`reportingMode=data`, with the requested workspace, fields, and date ranges.
The response note says successful X Ads API reads may be reused for up to
60 seconds. X Ads returns header-first tables under `reportingData.XAds.data`.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Spend | Passed | April–June: USD 132.98, summed across eight returned campaign rows. |
| Impressions and clicks | Passed | April–June: 153,216 Impressions and 169 Clicks. Clicks was not relabeled as URL clicks or conversions. |
| Campaign performance | Passed | Three campaigns with activity: April 2026, USD 100.00 / 95,074 impressions / 71 clicks; May 2026, USD 12.24 / 17,323 / 25; June 2026, USD 20.74 / 40,819 / 73. Their sums exactly match the standalone spend and traffic reports. Five other returned campaigns have zero requested metrics. |
| Period comparison | Passed | January–March: USD 200.92, 108,024 impressions, 54 clicks. April–June: USD 132.98, 153,216 impressions, 169 clicks, matching the standalone reports. Both periods have activity. |
| Daily performance | Passed | April returned 240 campaign rows covering all 30 dates. After aggregation: 95,074 impressions, 71 clicks, and USD 99.98 from rounded daily Cost values. Twenty-nine dates have impressions; April 30 is an explicit zero day. |

Daily Cost is rounded to two decimals per returned row. The daily amounts sum
to USD 99.98 while the April campaign's separately aggregated period amount
is USD 100.00. The two-cent difference is consistent with the source code's
row-level rounding. Counts reconcile exactly. The case and skills explicitly
require preserving the returned daily values and explaining rounding rather
than altering figures to force equality.

These figures are observations from this check, not required outputs or fallback
answers. The manifest expectations contain no observed totals. Keep the review
workspace connected and historical data accessible. Completeness against the
X Ads console was not independently audited. The implementation currently uses
the ALL_ON_TWITTER placement scope and excludes deleted entities from its entity
listing; results must not be presented as verified coverage of every placement
or deleted campaign. No connector code was changed during this preparation.

Fresh natural-language conversations through the saved submission: **Not run**.
Direct calls establish query execution and numerical consistency, not the
entire saved-plugin routing or reviewer authentication flow. No widget was
opened during these data checks.

Three negative conversations: **Not run**. They cover pausing campaigns,
publishing a promoted post/changing its budget, and identifying individual
clickers. Each expects an explanation of the unsupported request without
unnecessary tool calls or fabricated action completion.

## Tool annotations and deployment

The local scoped connector sets explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_x_ads | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

The catalog reads static field definitions. Retrieval reads the authorized
advertising account and records Adzviser usage; some report paths also create
upstream analytics jobs. Repeated retrieval can record more usage, explaining
the false read-only and idempotent hints. It does not edit or delete ads.
Preview compatibility paths can run reporting or save presentation preferences.
Workspace resolution can clear a stale account preference; mode selection saves
a presentation preference. Repeating the same preference operation is idempotent.
These tools act within authorized accounts or local definitions, so scoped
open-world hints are false. Remote hosting does not make their scope open-ended.

**The shared annotation correction still needs deployment and a portal rescan.**
The public X Ads endpoint reported build `6bf20c8d-20261002201522` on October 26.
Earlier inspection of that deployed build's source established that it predates
the local scoped open-world correction: reporting and workspace definitions
still use true. A ZIP cannot change server annotations. No deployment was
performed. The two existing connector suites passed 113 X Ads checks locally;
that does not establish production deployment or the submission's saved scan.

Public health and both OAuth discovery endpoints responded successfully.
Anonymous MCP initialization returned the expected 401 authentication challenge
for this resource. Fresh reviewer sign-in and the saved submission's scan:
**Not run**. Working authenticated queries do not establish the validity of
credentials entered separately for reviewers.

## Demo and listing checks

Demo: [Adzviser X Ads ChatGPT Plugin Demo](https://youtu.be/quY1w4PvCM4).
YouTube identified a non-private, unlisted recording by Adzviser, approximately
202 seconds long. An isolated signed-out browser played the beginning, middle,
and ending in separate runs. Inspected frames show plugin setup, an OAuth
return, a natural-language spend query in X Ads Demo, and reporting answers.
The initial recent-week answer is zero. Near 3:16, the year-to-date answer is
USD 333.90 for January 1–September 13, 2026. This is consistent with the two
active historical quarters found during this preparation.

The recording demonstrates an existing reporting workflow, not all five new
cases or the negative cases. An initial YouTube player error after roughly
one minute was handled with timestamped restarts; the final run reached the
video's end. Uninterrupted playback and every frame were not verified. OAuth
callback query parameters are briefly visible in the recorded browser address
bar. Historic authentication in the video does not establish current reviewer
access. The supplied demo URL was preserved.

The 256-pixel icon was visually checked earlier in this session and reused
unchanged. The four unchanged listing URLs were opened anonymously and inspected
earlier in this session: https://adzviser.com, https://adzviser.com/contact-us,
https://docs.adzviser.com/privacy, and https://docs.adzviser.com/terms. They provide
the expected publisher content. All supported countries and website-only billing
reuse the owner's confirmed preferences.

## Portal handoff

Use this archive for the existing X Ads entry. Its original package identity,
version, and confirmed endpoint are preserved. Inspect any upload error before
changing the identity or creating another entry.

After an accepted upload and deployment of the shared annotation correction,
rescan tools and inspect the saved booleans and imported review information.
Provide working reviewer credentials and exact sign-in instructions only in
the secure dashboard fields. Verify a fresh login reaches X Ads Demo without
additional setup or verification, then rehearse the cases through the saved
version and complete the required attestations.

No specific X Ads rejection details were supplied. Archive validation cannot
guarantee approval or complete reviewer authentication, verification, or scans.
