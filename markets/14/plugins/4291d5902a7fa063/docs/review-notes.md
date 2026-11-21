# Instagram Insights submission preparation

Prepared on 2026-10-26. Original package identity
`app-6aa3b2b62c008191b5aae60cd5faabb2`, version `1.0.0`, public name
`Adzviser Instagram Insights`, subtitle, publisher and starter prompts are preserved.
The owner confirmed the existing entry is unpublished/rejected, its registered
endpoint is https://instagram.mcp.adzviser.com/widgets/http, and the reviewer can
access the `Demo` Instagram Insights account in workspace `Demo`.

## Package

Portable and legacy manifests contain matching listing and review information.
The single MCP declaration and both skill dependencies use the confirmed endpoint.
The package includes the Adzviser PNG, five positive Data Mode cases, three
negative cases, all supported countries, website-only subscription details and
user-facing release notes. Explicit Preview UI support is retained, with no
widget test cases. No credentials or private app bindings are included.

The description uses current views and engagement metrics instead of advertising
retired impressions. Instructions distinguish account-period insights, current
profile snapshots and lifetime post metrics for a publication-date cohort.

## Five positive prompts

1. How many Instagram views did we have in Demo during the 30 days ending two days ago?
2. Show our Instagram likes, comments, shares, and saves in Demo for the 30 days ending two days ago.
3. Which five Instagram posts published in the 30 days ending two days ago have the most likes in Demo? Include links.
4. Compare Instagram views in Demo for the 30 days ending two days ago with the preceding 30 days.
5. Show daily Instagram views in Demo for the 30 days ending two days ago.

Let D be the current local date. Recent dates are [D-31, D-2], inclusive; the
preceding period is [D-61, D-32]. Recalculate at review time. These cover a total,
multiple metrics, a ranked post report, comparison and time series. Expected
values come from live rows, not the historical observations below.

## Actual direct-tool checks and a deployment prerequisite

Requests ran through the connected **Adzviser** app, using only Instagram
request keys. A separate authenticated Instagram test connection was not
available. Workspace and both catalogs were discovered successfully. This
does not verify authentication or routing through the saved Instagram plugin.

On October 26, the recent interval was September 25–October 24 and the earlier
interval was August 26–September 24. All five requests returned model-visible
Data Mode responses without a tool error or assumption note. However, successful
responses alone did not establish correct date coverage:

| Case | Status | Evidence |
| --- | --- | --- |
| Total views | Failed: final day omitted | Period total 1,255,158 versus daily sum 1,304,336. Difference 49,178 equals October 24's daily views. |
| Interactions | Blocked on date fix | Returned 34,473 likes, 551 comments, 6,790 shares and 2,765 saves, but uses the same incorrect multi-day profile boundaries. These are not validated full-period totals. |
| Most-liked posts | Failed date selection in additional live check | Original 30-day request returned nine posts with IDs, timestamps and permalinks; highest likes were 2,449, 685, 511, 17 and 8. A later single-day October 22 request returned a post published October 21, while an October 22–23 request returned the October 22 posts. |
| Views comparison | Failed date coverage | Returned 1,255,158 and 2,224,365, but both multi-day ranges use the incorrect end boundary. Do not treat them as validated inclusive-period totals. |
| Daily views | Passed direct daily-row checks | Thirty rows covering September 25–October 24, sum 1,304,336. Reconciliation with the period total failed as above. |

A diagnostic request ending October 25 returned 1,304,336, exactly the daily
sum through October 24. This confirmed the missing end day; it is not a change
to reviewer dates or a workaround in the test cases.

An additional live check on October 26 reproduced the problem with a different
window and two metrics. Daily October 20, 21 and 22 views were 36,416, 32,208
and 37,488 (sum 106,112); likes were 640, 622 and 622 (sum 1,884). The single
October 20–22 period report returned 68,624 views and 1,262 likes, exactly the
first two days. Extending the requested end to October 23 returned 106,112 and
1,884. The original 30-day views discrepancy also reproduced, and its likes
total increased by exactly October 24's 1,027 likes when the end was extended.

Live post selection provided separate timestamp evidence: requesting only
October 22 returned a post timestamped October 21 at 17:41:46 UTC. Requesting
October 22–23 returned two posts actually published October 22; October 22–24
also included the post published October 23. This supports a date-selection
problem independently of whether aggregate views should match daily sums.

The repository's synthetic demo adapters do not include Instagram. The inspected
Instagram path calls the provider using the connected account. Daily account
reports use different date handling from unsplit totals. That can explain why
some reporting workflows avoid the missing-day discrepancy, but customer usage
and the number of affected users were not measured. Local mocked regression
tests validate the proposed boundary conversion, not a deployed provider fix.

The local fix in Copter's `connectors/ig_insights/ig_insights_utils.py` converts
inclusive dates to UTC timestamps with an exclusive upper bound at midnight
after the requested end date. Profile windows remain at most 30 days with
contiguous boundaries. Post selection uses the same conversion, including
one-day requests instead of shifting their start into the previous day.

Five new regression tests reproduced the problems before the fix. All five
then passed, together with nine existing Meta metric-catalog tests (14 total).
They exercise period/daily reconciliation, the final fraction of a day, 30-day
chunking, year/leap-day boundaries, post selection and invalid reversed dates.
These are local tests with a simulated provider, not deployed verification.

**The Copter fix has not been deployed. Deploy it and rerun all five cases
before submitting for review.** The ZIP does not deploy backend code. No
Instagram MCP server source changes were required for this correction.

Fresh saved-plugin conversations, negative conversations, the saved submission
scan and reviewer sign-in: **Not run**. Owner-confirmed access is not an
independent sign-in test. Supply credentials only in secure portal fields.
Negative cases cover publishing a post, deleting a post and identifying viewers;
they should explain unsupported behavior without unnecessary tool calls.

## Tool annotations

Inspected local source definitions have explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_ig_profile | true | false | true | false |
| list_metrics_and_breakdowns_ig_post | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Both catalogs read static definitions. Retrieval accesses authorized external
reports and records usage, without modifying Instagram content. Preview
compatibility paths can run reports or save preferences. Workspace lookup can
clear a stale account preference; mode selection saves a presentation preference.
Shared reporting definitions use openWorldHint=true for external service access;
access remains restricted to authorized connections.

Anonymous initialize and tools/list requests to the dedicated endpoint returned
OAuth 401 challenges. Authenticated source queries succeeded through Adzviser
with the data-quality limitations above. Portal descriptors were not captured.
These notes do not override live annotations or prove reviewer acceptance.

## Demo and remaining handoff

Demo URL: https://youtu.be/O2hxwOgl7VM

Anonymous metadata identified “Adzviser Instagram Insights ChatGPT Plugin Demo”
by Adzviser, approximately 166 seconds, non-private and player status OK. An
isolated signed-out browser played the beginning, including a readable frame
showing plugin discovery around 48 seconds. Playback stopped around 60 seconds
and showed a YouTube error. Full playback, report coverage and absence of
sensitive content throughout remain unverified. Check the complete recording
before review; this browser failure alone does not establish a broken video.

The unchanged website, support, privacy and terms URLs were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. The supplied
256-pixel PNG was inspected and reused.

Use the ZIP with the existing entry, preserving its identity and registered
endpoint. No plugin was created, uploaded, deleted, submitted or published.
A ZIP cannot resolve an unrelated portal migration issue by itself. After an
accepted upload, inspect imported review details, authorize the MCP connection
if needed, inspect its scan and verify reviewer access. After the Copter
deployment, rerun the cases through the saved plugin and finish the recording
check before review. No particular rejection reason or approval is assumed.
