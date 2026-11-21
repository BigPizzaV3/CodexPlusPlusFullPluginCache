# YouTube submission preparation

Prepared on October 26, 2026. Original package identity
`app-6aa3b52a0da08191a4548fcfb89abdc5`, version `1.0.0`, display name
`Adzviser YouTube`, subtitle, and starter prompts are preserved. The original
download is unchanged. No portal entry was created, uploaded, submitted,
published, or deleted during preparation.

The owner confirmed that the entry is unpublished/rejected, that its registered
MCP URL is https://youtube.mcp.adzviser.com/widgets/http, and that the reviewer
login can access the workspace and account `YouTube Demo`.

## Package contents

The root and compatibility manifests have matching identity, listing, version,
publication, and review metadata. The concrete MCP URL is declared in `mcp.json`
and both skill dependencies. Source-specific skills cover field discovery,
date handling, report families, units, and interpretation limits.

Included: the supplied Adzviser icon, five positive Data Mode cases, three
negative cases, demo URL, all supported countries, website-only subscription
information, and user-facing release notes. Preview UI remains available on
explicit request; no review case requires a widget. No credentials or private
app bindings are included.

## Five positive prompts

1. How many YouTube views and hours of watch time did we get in the 30 days ending two days ago in YouTube Demo?
2. How many subscribers did we gain and lose in the 30 days ending two days ago in YouTube Demo? What was the net change?
3. Show our five most-viewed YouTube videos in the 30 days ending two days ago in YouTube Demo, with views and watch time.
4. Compare YouTube views and watch time for the 30 days ending two days ago with the preceding 30 days in YouTube Demo.
5. Show daily YouTube views and watch time for the 30 days ending two days ago in YouTube Demo.

Let D be the current user-local date. Recent means [D-31, D-2], inclusive;
preceding means [D-61, D-32]. Recalculate dates when the reviewer runs the cases.
No fixed dates or observed numeric answers are embedded in the review cases.
The local preparation date was October 26 in America/Los_Angeles, while tool
discovery reported October 27 UTC; the local date was used consistently.

## Direct-tool verification

Workspace and field discovery succeeded. All five exact underlying requests
returned `isError=false`, `directData=true`, `reportingMode=data`, and an empty
`note_of_assumption` through the authenticated connection available in this
session. Recent dates were September 25–October 24, 2026; comparison dates were
August 26–September 24. Responses contained header-first Combined or Video
tables under `reportingData.YouTube.data`.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Channel views and watch time | Passed | 139,046 Video views and 45,771 Estimated minutes watched, equivalent to 762.85 estimated hours. |
| Subscriber change | Passed | Five gained, two lost, net change +3. These are period changes, not the current subscriber count. |
| Top videos | Passed | 117 distinct video IDs with titles. The top five view counts were 31,010; 27,972; 19,904; 16,570; and 11,410. Each row includes watch time. The leading title was Explore the Modern Living House Plans. |
| Period comparison | Passed | Previous: 33,717 views and 10,873 estimated minutes. Recent: 139,046 views and 45,771 estimated minutes, matching the standalone report. Changes: +105,329 views (+312.39%) and +34,898 minutes (+320.96%). |
| Daily performance | Passed | All 30 dates returned rows. Daily views sum exactly to 139,046. Daily estimated watch time sums to 45,757 minutes, which differs from the independently returned period estimate by 14 minutes; this distinction is documented below and in the expectations. |

These figures are observations from this check, not future expected answers.
Keep the review workspace connected and its analytics available. Completeness
against YouTube Studio was not independently audited.

Fresh natural-language conversations through the saved submission: **Not run**.
Direct calls establish request execution and support inspection of the returned
values, not the entire saved-plugin routing or reviewer authentication flow.
No widget was opened during the data checks.

Three negative conversations: **Not run**. They cover publishing a video,
deleting low-view videos, and identifying individual viewers by name/email.
Each expects an explanation of the unsupported action without unnecessary tool
calls or fabricated completion.

## Report scope and precision

The 117 video rows sum to 138,700 views and 45,657 estimated minutes, below the
channel aggregate by 346 views and 114 minutes. The top-video case tests ranking
the returned videos, not replacing the channel total with their subtotal.
Google documents that deleted items can be absent from video-level reports while
their metrics remain in aggregate totals. That is a possible explanation here;
the exact source of this account's difference was not independently verified.
[YouTube Analytics data model](https://developers.google.com/youtube/analytics/data_model#aggregate_metrics_and_deleted_items).

The connector limits the video query to 200 results sorted by views, without
pagination in the inspected implementation. This query returned fewer than the
cap, and the five review rankings use views. Watch-time rankings of a capped
video list must be described as rankings of returned videos. Channel-level
statistics snapshots must not be repeated or summed as date-filtered activity.

The daily report's 45,757 estimated minutes are 14 minutes below the period
estimate of 45,771 (about 0.031%). The inspected adapter copies reported metric
values directly. Differing estimate precision or aggregation is plausible, but
the exact cause was not established from raw upstream responses. Do not call
the values exactly reconciled, silently adjust daily values, or present this
as a verified connector bug. Daily views and date coverage reconcile exactly.

Google documents that analytics data can arrive after a processing delay and
that reports include only days for which requested metrics are available.
Two days before today remains the requested end date; missing newer days must
be disclosed rather than fabricated. All 30 days were returned in this check.
[YouTube Analytics data freshness](https://developers.google.com/youtube/analytics/data_model#data-freshness-and-latency).

No connector implementation was changed during this preparation.

## Tool annotations and deployment

The local scoped connector sets explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_youtube | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

The catalog reads static definitions. Retrieval reads authorized channel
analytics and records Adzviser usage; repeated calls may record more usage,
explaining false read-only and idempotent hints. It does not edit or delete
videos. Preview compatibility paths can run reporting or save presentation
preferences. Workspace resolution can clear a stale account preference; mode
selection saves a presentation preference. Repeating the same preference change
is idempotent. These operations are confined to authorized accounts or local
definitions, so scoped open-world hints are false despite remote hosting.

**The shared annotation correction still needs deployment and a portal rescan.**
The public YouTube endpoint reported build `6bf20c8d-20261002201522` on October 26.
Earlier inspection of that deployed build's source established that it predates
the local scoped open-world correction; reporting and workspace definitions
still use true. The ZIP cannot change live server annotations. No deployment
was performed. Existing connector suites passed all 113 YouTube checks locally;
this does not establish deployment or the saved submission's scan.

Public health and both OAuth discovery endpoints responded successfully.
Anonymous MCP initialization returned the expected 401 challenge for this
resource. Fresh reviewer sign-in and the saved submission scan: **Not run**.
Authenticated queries do not verify the credentials saved for reviewers.

## Demo and listing checks

Demo: [Adzviser YouTube ChatGPT Plugin Demo](https://youtu.be/JHn9SkGFaaA).
YouTube identified an unlisted, non-private recording by Adzviser of approximately
173 seconds. An isolated signed-out browser played the beginning, middle, and
ending in separate runs. Inspected frames show development plugin setup,
connection, a natural-language analytics prompt, and a response at about 2:39
showing 22 likes and 137,460 video views for August 2026 in YouTube Demo.

The recording demonstrates an existing reporting workflow, not all five new
positive cases or their negative cases. An initial player error after roughly
one minute was handled with timestamped restarts; the final run reached the
video's end. Uninterrupted playback and every frame were not verified. Recorded
authentication does not prove current reviewer access. The supplied URL is
preserved in the review metadata.

The 256-pixel icon was visually checked earlier in this session and reused
unchanged. The four unchanged listing URLs were opened anonymously and inspected
earlier in this session: https://adzviser.com, https://adzviser.com/contact-us,
https://docs.adzviser.com/privacy, and https://docs.adzviser.com/terms. They provide
the expected publisher content. All supported countries and website-only billing
reuse the owner's confirmed preferences.

## Portal handoff

Use this archive for the existing YouTube entry. Its original package identity,
version, and confirmed endpoint are preserved. Inspect upload errors before
changing identity or creating another entry.

After an accepted upload and deployment of the shared annotation correction,
rescan tools and inspect saved booleans and imported review information.
Provide working reviewer credentials and exact sign-in instructions only in
the secure dashboard fields. Verify a fresh login reaches YouTube Demo without
additional setup or verification, then rehearse the cases through the saved
version and complete required attestations.

No specific YouTube rejection details were supplied. Archive validation cannot
guarantee approval or complete reviewer authentication, verification, or scans.
