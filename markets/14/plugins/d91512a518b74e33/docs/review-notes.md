# Salesforce submission preparation

Prepared on 2026-10-26. The source and ZIP preserve package
`app-6aa3b356b39481918ea5e0a30248baca`, version `1.0.0`, public name
`Adzviser Salesforce`, and subtitle `Talk to your Salesforce data`.

The owner confirmed the existing entry is unpublished/rejected and uses
https://salesforce.mcp.adzviser.com/widgets/http. The owner also confirmed that
the reviewer login can access the `Salesforce Demo` workspace and account.
The original downloaded ZIP remains unchanged in Downloads.

## Package changes

The supplied archive had two generic Adzviser skills and no MCP configuration.
The prepared package declares the confirmed Salesforce endpoint in `mcp.json`
and both skill dependencies. A portable root manifest and the retained legacy
manifest have matching identity, listing, publication and review fields.
There are no private app bindings or credentials in the upload.

The package includes the supplied Adzviser 256-pixel PNG, all supported countries,
website-only subscription information, the supplied demo link, five positive
Data Mode cases, three negative cases, and user-facing release notes. The five
positive prompts are also in `review.prompts` for plugin metadata review.
Existing explicit Preview UI functionality is retained; no widget cases were added.

The listing and starter prompts now describe record counts, stages, statuses and
comparisons. The connector filters Salesforce records by CreatedDate using UTC
calendar-day boundaries. It does not filter by opportunity close date or return
historical stage snapshots. Skills and expectations explain this distinction.

## Five positive prompts

1. How many Salesforce opportunities were created in the 30 days ending two days ago in Salesforce Demo?
2. Break down Salesforce opportunities created in the 30 days ending two days ago by their current stage in Salesforce Demo.
3. How many Salesforce leads were created in the 30 days ending two days ago, broken down by current status, in Salesforce Demo?
4. Compare the number of Salesforce opportunities created in the 30 days ending two days ago with the preceding 30 days in Salesforce Demo.
5. Show how many Salesforce opportunities were created each day during the seven days ending two days ago in Salesforce Demo.

Let D be the current date in the user's timezone. Recent 30 days: [D-31, D-2].
Previous 30 days: [D-61, D-32]. Recent seven days: [D-8, D-2]. All endpoints are
inclusive. Recalculate these dates when running the cases; the numbers below are
verification evidence, not fixed expected answers for future review.

## Actual verification

On October 26, 2026 in America/Los_Angeles, the recent interval was September
25–October 24, the comparison interval was August 26–September 24, and the daily
interval was October 18–24. The authenticated Salesforce tools available in this
session returned successful Data Mode responses for all five requests. No widget
was opened. Workspace and field discovery passed. Requests included only counts
and the necessary stage/status breakdowns; no contact details were requested.

| Direct reporting case | Result | Observed evidence |
| --- | --- | --- |
| Opportunity count | Passed | 238 opportunities for September 25–October 24. |
| Opportunities by current stage | Passed | Eight returned stage groups summed to 238, matching the overall count. |
| Leads by current status | Passed | 247 leads with status New Opportunity and 65 with status New Lead; total 312. These are lead-status labels, not opportunity counts. |
| Opportunity comparison | Passed | 238 recent opportunities versus 310 earlier; decrease of 72, approximately 23.23%. |
| Daily opportunity counts | Passed, with an omitted date | October 18: 6; October 19: 9; October 20: 15; October 21: 2; October 22: 16; October 23: 3. Sum 51. October 24 had no returned row and was not filled with a fabricated zero. A separate ungrouped query for October 18–24 also returned 51. |

Stage counts were Unlikely/unsuitable 13, New Opportunity 83, Open Opportunity
56, Withdrawn 59, Warm prospect 17, Reserved 8, Long Term 1 and Referrer/associate 1.
All reporting responses had `isError=false`, `reportingMode=data`, `directData=true`,
and empty `note_of_assumption`. Consistent totals do not independently establish
source completeness against Salesforce Admin.

Fresh-conversation routing through the saved plugin: **Not run**. The direct tool
checks validate query execution and returned data, not every natural-language
step in the uploaded version.

Three negative conversations: **Not run**. Cases cover marking opportunities
Closed Won, deleting duplicate leads, and emailing leads. These actions are not
supported by this reporting plugin. Expected behavior is an accurate limitation
without substitute reporting/preference calls or a fabricated success.

Saved portal scan, reviewer sign-in, and secure access instructions: **Not run**.
Owner-confirmed workspace access does not replace testing the reviewer login.
Use the secure dashboard fields for credentials and sign-in instructions.

## Tool annotation reference

The local server definitions have explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_salesforce | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads field definitions. Reporting reads connected Salesforce
records and records Adzviser usage. Preview compatibility paths can retrieve
reports or save presentation preferences. Workspace resolution can clear a stale
saved account-selection preference. Reporting-mode selection saves a presentation
preference and is idempotent for the same mode. None of these tools modifies
Salesforce opportunity or lead records, deletes records, or sends emails.

The shared external-service reporting classification uses openWorldHint=true;
actual access remains limited to connected authorized accounts. These are local
source checks, not a descriptor capture from the saved submission. Anonymous
initialize and tools/list calls to the confirmed URL returned OAuth 401 challenges
as expected. Documentation does not override tool annotations or prove acceptance
by reviewers. No server code or deployment was changed during this preparation.

## Demo and public listing URLs

Demo: https://youtu.be/EyuXGMvA6m8

Anonymous YouTube metadata returned “Adzviser Salesforce ChatGPT plugin Demo” by
Adzviser, approximately 163 seconds, non-private status and player status OK.
An isolated signed-out browser played the early portion; inspected frames at
approximately 7, 27 and 47 seconds show plugin discovery and connection setup.
Playback subsequently showed a player error. A second attempt to seek to later
sections remained buffering. Full playback, report-result coverage and absence
of sensitive content throughout the entire recording remain **unverified**.
Check the full recording before submission; metadata alone is not that check.

The website, support, privacy and terms URLs were opened anonymously and their
Adzviser content inspected on October 26. The contact page contains a support
form; the legal pages identify Adzviser LLC and cover the service. No legal text
or policy commitments were invented for this package.

## Handoff

Upload the ZIP to the existing Salesforce entry. The internal package ID and
confirmed endpoint are preserved. The imported legacy entry's exact resubmission
behavior is unverified; a valid ZIP alone cannot resolve a portal migration error.
Do not create another plugin or change its identity to work around an upload issue.

After an accepted upload, check imported review information, connect/authorize
the MCP server if required, inspect its current scan, verify reviewer access,
run the cases through the saved version, and complete the portal's attestations.
The original rejection details were not supplied. These preparation checks do
not establish that particular reviewer findings have been resolved, nor guarantee
approval. No portal entry was created, deleted, submitted or published here.
