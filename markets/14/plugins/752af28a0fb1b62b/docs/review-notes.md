# Campaign Manager 360 submission preparation

Prepared on October 26, 2026. Original package identity
`app-6aa60c5c879c8191a01d0d7896e3c591`, version `1.0.0`, public name
`Adzviser Campaign Manager 360`, subtitle, and starter prompts are preserved.
The original downloaded archive remains in Downloads. No portal entry was
created, uploaded, submitted, published, or deleted during preparation.

The owner confirmed that this submission is unpublished/rejected and that its
registered endpoint is https://cm360.mcp.adzviser.com/widgets/http. The owner
also confirmed reviewer access to the `CM360` workspace and its connected
`TP - BetFred - IPR - DCM - UK` account.

## Package contents

The portable root manifest and legacy compatibility manifest have matching
identity, version, listing, publication, and review metadata. The concrete MCP
endpoint is declared in `mcp.json` and both skill dependencies. Generic skills
were specialized to Campaign Manager 360 with exact field discovery, scoped
requests, date handling, report interpretation, and unsupported-action limits.

The package includes the supplied Adzviser 256-pixel PNG, five positive Data Mode
cases, three negative cases, the demo URL, all supported countries, website-only
subscription information, and release notes written for users. Preview UI remains
available when explicitly requested; none of the review cases requires a widget.
Credentials and private app bindings are not included.

## Five positive prompts

1. How many CM360 impressions and clicks did we have in the 30 days ending two days ago in CM360, and what was the click-through rate?
2. Show our top 10 CM360 campaigns by impressions, with clicks, for the 30 days ending two days ago in CM360.
3. Show our top 10 CM360 placements by impressions, with clicks, for the 30 days ending two days ago in CM360.
4. Compare CM360 impressions and clicks for the 30 days ending two days ago with the preceding 30 days in CM360.
5. Show daily CM360 impressions and clicks for the 30 days ending two days ago in CM360.

Let D be the current date in the user's timezone. The recent interval is
[D-31, D-2], inclusive; the preceding interval is [D-61, D-32]. Dates must be
resolved again at review time. Cases contain no fixed dates or numeric answers.
The local preparation date was October 26 in America/Los_Angeles; field discovery
reported October 27 UTC. The local date was used consistently for these checks.

## Actual verification

Workspace and field discovery succeeded. All five underlying reporting queries
passed through the authenticated CM360 connection available in this session.
The recent interval was September 25–October 24, 2026; comparison used
August 26–September 24. All responses had `isError=false`, `directData=true`,
`reportingMode=data`, and an empty `note_of_assumption`.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Overall delivery and calculated CTR | Passed | 404,798,326 impressions and 753,463 clicks. Calculated CTR was approximately 0.18613%. |
| Campaign ranking | Passed | 170 campaign rows. Their impressions and clicks summed exactly to the overall report. Sorting the returned set produced the top ten; different IDs were kept separate. |
| Placement ranking | Passed | 579 placement rows. Their impressions and clicks summed exactly to the overall report. The ranking uses placement IDs to distinguish repeated names. |
| Period comparison | Passed | Previous period: 443,107,075 impressions and 896,931 clicks. Recent changes were -38,308,749 impressions (-8.65%) and -143,468 clicks (-16.00%). The recent-period row matched the standalone report. |
| Daily delivery | Passed | All 30 dates from September 25 through October 24 returned rows. Daily impressions and clicks summed exactly to the overall report. |

These are dated observations, not fixed expected answers. Future data can change.
Keep the approved review workspace connected and populated during review.
Source completeness against the Campaign Manager 360 console was not independently
audited. No widget was opened by these reporting checks.

Fresh natural-language conversations through the saved submission: **Not run**.
Direct tool checks establish query execution, field validity, date coverage, and
numeric consistency; they do not establish every step in a fresh saved-plugin chat.

The three negative conversations are **Not run**. They cover pausing campaigns,
uploading/assigning creatives, and identifying individual ad clickers. Each case
expects an explanation of the unsupported action without unnecessary tool calls
or a false claim of completion.

## Tool annotations and deployment

The local connector definitions explicitly set all four boolean hints:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_cm360 | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

The metric catalog reads field definitions without modifying account data.
Reporting can create and run an upstream CM360 report, download its results,
attempt to delete that generated report, and record Adzviser usage. Repeated
requests can repeat those side effects, explaining false read-only and
idempotent hints. Cleanup concerns the newly generated report, not a pre-existing
user report. Retrieval does not change campaign delivery or creative assignments.
Preview compatibility paths can run reports or save presentation preferences.
Workspace resolution can clear a stale account preference; mode selection saves
a presentation preference. Repeating the same preference operation is idempotent.
All are confined to the user's authorized account or local definitions, so their
corrected scoped open-world hints are false. Hosting on an external server alone
does not make the account boundary open-ended.

**The shared annotation correction still needs deployment and a portal rescan.**
On October 26 the CM360 endpoint reported build `6bf20c8d-20261002201522`.
Earlier inspection of the deployed build's source established that it predates
the local scoped open-world correction: its report and workspace definitions
still use true. This archive cannot change annotations served by that build.
Do not describe the correction as deployed or verified in the submission scan.
No server deployment was performed during this preparation.

The two existing connector test suites passed all 113 CM360-specific checks
against the local code, including scoped descriptors and data/preview routing.
These tests do not establish the state of the production deployment.

The public endpoint and OAuth discovery responded successfully. Anonymous MCP
initialization returned an expected 401 challenge identifying the same resource.
This establishes public discovery, not successful reviewer sign-in. The saved
submission's tool scan and a fresh reviewer OAuth flow remain **Not run**.

## Demo and listing checks

Demo: [Adzviser CM360 ChatGPT Plugin Demo](https://youtu.be/RJUibbvGXIg).
YouTube identified an approximately 172-second, non-private recording by Adzviser.
An isolated signed-out browser played the beginning, middle, and ending in
separate runs. Inspected frames show plugin setup, the Complete Authorization via
MCP step, a natural-language request for last month's clicks and impressions, and
a successful numerical response for the same connected account at about 2:40.
The ending run reached the video's end. The recording demonstrates the main
totals workflow; it does not demonstrate all five new cases or the negative cases.

The first two playback runs encountered YouTube player errors after approximately
one minute of streaming. Timestamped restarts verified the middle and ending.
Uninterrupted playback and every frame were not verified; no password or token
was visible in the inspected frames. This recording check does not verify the
reviewer's saved credentials or establish that current authentication will work.

The supplied icon was visually inspected. Website, support, privacy, and terms
URLs were opened anonymously and identified the correct publisher and expected
content: [Adzviser](https://adzviser.com), [contact](https://adzviser.com/contact-us),
[privacy notice](https://docs.adzviser.com/privacy), and
[terms](https://docs.adzviser.com/terms). Country targeting and website-only
subscriptions follow the owner's established instructions.

## Portal handoff

Use the archive for the existing CM360 entry with the preserved package ID and
confirmed endpoint. A valid archive does not itself resolve legacy portal
migration restrictions; do not change the identity or create a duplicate entry
without first inspecting any actual upload error.

After an accepted upload and deployment of the shared annotation correction,
rescan the tools, inspect the saved boolean annotations, and check imported
review metadata. Provide working reviewer credentials and detailed sign-in steps
only in the secure dashboard fields. Confirm a fresh reviewer sign-in reaches
the intended workspace without additional setup or verification, then run the
cases through the saved version and complete the portal attestations. Owner
confirmation of workspace access does not replace this authentication check.

No particular CM360 rejection details were supplied. This work does not guarantee
review approval or claim that previously rejected findings have all been resolved.
