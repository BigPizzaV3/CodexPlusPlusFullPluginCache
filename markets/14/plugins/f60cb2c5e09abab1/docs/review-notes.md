# Omnisend submission preparation

Prepared on 2026-10-26. Original package identity
`app-6aa60a0b2a5481919e5ad341dec33bab`, version `1.0.0`, public name
`Adzviser Omnisend`, subtitle and publisher are preserved.

Pending owner confirmation: the existing submission is unpublished/rejected and
its registered endpoint is exactly https://omnisend.mcp.adzviser.com/widgets/http.
That endpoint matches the local connector profile and responds with an OAuth
challenge. Workspace discovery found `Omnisend Demo`, connected account `ILASHSG`;
reviewer access to this workspace is also awaiting owner confirmation.

## Package and listing corrections

The downloaded archive contained generic skills without a concrete MCP
declaration. The new portable and compatibility manifests share identity,
version, listing and review information. Both skill dependencies use the
dedicated Omnisend endpoint.

The original listing promised automation and attributed-revenue reporting, and
its third starter prompt requested automation revenue. Neither capability exists
in the current returned catalog or connector implementation. The listing now
describes campaign reporting, and the third starter prompt asks for campaign
open and click rates. The first two starter prompts are preserved.

The package includes the supplied Adzviser PNG, five positive Data Mode cases,
three negative cases, supplied demo URL, all supported countries, website-only
subscriptions and user-facing release notes. Optional Preview UI remains
available, with no widget test cases. No credentials or private app bindings
are packaged.

## Five positive prompts

1. How many Omnisend campaigns started in the 30 days ending two days ago in Omnisend Demo, and how many messages did they send?
2. Show open and click rates for each Omnisend campaign started in the 30 days ending two days ago in Omnisend Demo.
3. How many bounces, complaints, and unsubscribes did our Omnisend campaigns started in the 30 days ending two days ago have in Omnisend Demo?
4. Compare campaign counts and sends in Omnisend Demo for the 30 days ending two days ago with the preceding 30 days.
5. Show opens and clicks on mobile, desktop, and tablet for Omnisend campaigns started in the 30 days ending two days ago in Omnisend Demo.

Let D be the current local date. Recent dates are [D-31, D-2], inclusive;
the preceding interval is [D-61, D-32]. Recalculate when testing. No case
hardcodes expected report values, campaign IDs or calendar dates.
Run the cases one at a time rather than submitting parallel reporting requests.

## Actual direct-tool verification

All five report variants eventually passed through the authenticated tools
available in this session (namespace `Adzviser Omnisend Test`). That is the
existing connection used for tests, not a new portal plugin. Workspace and
field discovery passed. No duplicate submission was created.

The initial parallel engagement, delivery and device requests failed with HTTP
500 responses. Copter Cloud Run logs at approximately 23:44–23:45 UTC on
October 26 showed upstream HTTP 429 Too Many Requests from Omnisend's campaign
listing endpoint during pagination. The connector calls raise_for_status and
does not handle this throttle response before it becomes a generic server error.
Each of those three unchanged requests passed when retried sequentially.
This is a real reliability limitation under rate limiting, not a malformed
metric request or proof of zero campaign activity. No server changes or
deployments were made; this ZIP does not fix backend rate-limit handling.

The successful responses had isError=false, reportingMode=data, directData=true,
the requested workspace and source, and empty note_of_assumption. On October 26,
the recent dates were September 25–October 24; earlier dates were August 26–
September 24.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Campaign count and sends | Passed direct request | 5 campaigns and 8,466 sends. |
| Campaign engagement rates | Passed on sequential retry | 5 distinct campaigns, all start dates inside the interval; 1,684 opens and 14 clicks in total. Per-campaign rates match counts divided by sends, rounded to four decimal places. |
| Delivery and unsubscribes | Passed on sequential retry | 83 bounces, 0 complaints, 11 unsubscribes from the selected campaigns; 8,466 sends. |
| Period comparison | Passed direct request | Recent 5 campaigns / 8,466 sends; preceding 9 campaigns / 12,131 sends. Differences -4 campaigns and -3,665 sends. |
| Device engagement | Passed on sequential retry | Opens: mobile 30, desktop 317, tablet 0; overall 1,684. Clicks: mobile 10, desktop 1, tablet 0; overall 14. |

Reported devices account for 347 of 1,684 opens and 11 of 14 clicks. The remaining
1,337 opens and 3 clicks are not represented in those three device counts. The
cause was not independently established; the test requires disclosing coverage
rather than inventing a device assignment or forcing totals to match.

These are observations from preparation, not expected answers for future review.
Engagement can change after campaigns start. Completeness and exact event
semantics against Omnisend's own dashboard were not independently verified.

Saved-plugin positive conversations, three negative conversations, saved portal
scan and reviewer sign-in: **Not run**. Direct tool calls do not prove routing
through a new saved plugin. Negative cases cover sending a campaign, changing
subscriptions, and unsupported automation-revenue reporting. Credentials belong
only in secure dashboard fields.

## Reporting semantics and annotations

Implementation selects campaigns by the date part of startDate. Counts describe
the campaigns' accumulated results at retrieval, not all engagement events
occurring inside the selected dates. Rates are fractions calculated from count
totals and sends, rounded to four decimal places. Device fields can have partial
coverage. A/B variants must remain separate from campaign totals.

The connector reads Omnisend v3 campaigns. Its currently linked
[campaign documentation](https://api-docs.omnisend.com/reference/campaigns)
describes broader provider capabilities; that does not expand the reporting
plugin's actual tools. In particular, no automation or revenue fields are in
the returned catalog. The catalog tool's short description still mentions an
Automation Name example; the packaged skills require the actual returned fields
instead. Server descriptors were not changed for this ZIP task.

Inspected local definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_omnisend | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads static definitions. Retrieval accesses authorized reports
and records usage; it does not send campaigns or edit contacts. Preview compatibility
paths can run reports or save preferences. Workspace lookup can clear stale account
preferences; mode selection saves a presentation preference. Reporting's external
service access uses openWorldHint=true, with authorization still limiting accounts.
Anonymous initialize and tools/list calls returned OAuth 401 challenges.
Saved portal descriptors were not captured or compared; notes do not override
the deployed annotations or guarantee approval.

## Demo and handoff

Demo: https://youtu.be/X6kQfjOfB3A

Anonymous metadata identified “Adzviser Omnisend ChatGPT Plugin Demo” by
Adzviser, approximately 153 seconds, non-private and player status OK. An
isolated signed-out browser played the opening. The inspected frame around
47 seconds showed the custom-plugin connection dialog. Playback stopped around
60 seconds with a YouTube error. Full playback, result coverage and absence of
sensitive content throughout remain unverified. Check the entire recording
before review; this browser failure alone does not prove the hosted video is broken.

The unchanged website, support, privacy and terms pages were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. The supplied
256-pixel Adzviser PNG was inspected and reused.

Confirm the existing entry's status and exact registered endpoint, and reviewer
workspace access, before uploading. Package identity and version are preserved.
No portal upload, submission, publication or deletion was performed. After an
accepted upload, inspect imported review information, connect and scan the MCP,
verify reviewer sign-in, and run the cases sequentially through the saved version.
Full recording verification and portal attestations remain necessary before review.
