# HubSpot submission preparation

Prepared on 2026-10-26. The package ID
`app-6aa608e54d808191922a3a433d6afa04`, version `1.0.0`, public name
`Adzviser HubSpot`, subtitle `Talk to your HubSpot CRM data`, and publisher
`Adzviser LLC` are preserved. The owner confirmed that the existing entry is
unpublished/rejected and that its registered MCP endpoint is:
https://hubspot.mcp.adzviser.com/widgets/http

The owner confirmed reviewer access to workspace `HubSpot Demo`, containing the
`HubSpot Demo` account. The original ZIP remains in Downloads. No duplicate
plugin was created, and no portal entry was uploaded, submitted or deleted.

## Package contents and listing

The original archive contained generic Adzviser skills without an MCP declaration.
The prepared package declares the confirmed endpoint in `mcp.json` and both
skill dependencies. Portable and legacy compatibility manifests have matching
identity, version, listing, publication and review metadata.

The listing and starter prompts now describe records created during a period.
The original close-date and pipeline language was ambiguous: the CRM connector
filters contacts, companies, deals and tickets using their creation date, with
UTC day boundaries. Current stage and amount values for those records are not
historical snapshots or all deals closed during the period. The package explains
this distinction and retains separate currencies for monetary reports.

The ZIP contains the Adzviser 256-pixel PNG, five positive Data Mode cases, three
negative cases, the supplied demo URL, all supported countries, website-only
subscription details and user-facing release notes. Positive prompts also appear
in `review.prompts`. Existing explicit Preview UI functionality is retained, but
no widget test cases were added. There are no credentials or private app bindings.

## Five positive prompts

1. How many HubSpot contacts did we create in the 30 days ending two days ago in HubSpot Demo?
2. How many HubSpot deals did we create in the 30 days ending two days ago in HubSpot Demo, and what is their total amount by currency?
3. Break down HubSpot deals created in the 30 days ending two days ago by pipeline and current stage in HubSpot Demo.
4. Compare HubSpot contacts created in the 30 days ending two days ago with the preceding 30 days in HubSpot Demo.
5. Show daily HubSpot contacts created in the 30 days ending two days ago in HubSpot Demo.

Let D be the current date in the user's timezone. The recent interval is
[D-31, D-2], inclusive; the previous interval is [D-61, D-32]. Resolve these dates
again when reviewing. The following values are one live verification, not fixed
expected answers. The examples cover a contact total, a deal total with currency,
a pipeline/stage grouping, a comparison and a daily time series.

## Actual direct-tool verification

All five authenticated report requests succeeded on October 26, 2026. Workspace
and field discovery passed. The recent interval was September 25–October 24;
the earlier interval was August 26–September 24. All responses had
`isError=false`, `reportingMode=data`, `directData=true` and empty
`note_of_assumption`. Only necessary fields were requested. No widget was opened.

| Case | Result | Observed evidence |
| --- | --- | --- |
| Contacts created | Passed | 8,191 contacts. |
| Deal count and amount by currency | Passed | 2,430 deals; current total amount USD 7,856,188.17. This is not recognized revenue or only closed-won deals. |
| Deals by pipeline and stage | Passed | Seventeen rows across three pipeline IDs. Counts sum to 2,430. Identically named stages in different pipelines remain separate. |
| Contact comparison | Passed | Recent 8,191 versus earlier 10,879; decrease 2,688, approximately 24.71%. |
| Daily contacts | Passed | Thirty rows covering every date from September 25 through October 24, summing to 8,191. |

The stage report includes both Closed Won and Closed Won - Pending. These remain
distinct. Pipeline IDs were returned without names; the cases do not invent
labels. Counts and amounts were read by table header, and contact and deal tables
were not treated as joined populations. No missing days were filled with zeros.

Fresh-conversation routing through the uploaded plugin: **Not run**. Direct tool
execution verifies report requests and returned values, not every natural-language
step in a new saved-plugin conversation. Source completeness against HubSpot's
own UI was not independently checked. Keep this workspace and its data available
during review; moving date ranges can return different values later.

Three negative conversations: **Not run**. They cover creating a contact, moving
deals to Closed Won, and sending a promotional email. The reporting plugin
cannot perform these actions. Expected behavior is an accurate explanation
without unnecessary data retrieval or a false claim that an action occurred.

Saved portal scan and reviewer sign-in: **Not run**. The owner confirmed workspace
access. Reviewer credentials and sign-in instructions belong only in the secure
dashboard fields, never in this package.

## Tool annotations

The local source definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_hubspot | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

HubSpot catalog discovery reads static field definitions and does not run account
resolution. Reporting retrieves authorized HubSpot data and records Adzviser
usage; it does not modify CRM records or send email. Preview compatibility paths
can run reports or save presentation preferences. Workspace lookup can clear a
stale account preference, and mode selection saves a presentation preference.
Reporting uses the shared external-service classification `openWorldHint=true`;
actual access remains scoped to authorized connections.

No HubSpot server source changes or deployments were made for this package.
Anonymous initialize and tools/list calls returned OAuth 401 challenges at the
confirmed endpoint. Authenticated reports worked through the connected tools.
The saved portal descriptors were not captured or compared. These notes do not
override live annotations or prove reviewer acceptance.

## Demo and listing checks

Demo: https://youtu.be/WiIRrd-fdY0

Anonymous metadata identified “Adzviser HubSpot ChatGPT Plugin Demo” by Adzviser,
approximately 164 seconds, non-private status and player status OK. An isolated
signed-out browser played the beginning. Inspected frames around 7 and 48 seconds
show ChatGPT and plugin discovery. Playback then displayed a YouTube error.
Full playback, report-result coverage and absence of sensitive content throughout
the recording remain **unverified**. Check the complete recording before review;
this browser error alone does not establish that the video is broken for reviewers.

The unchanged website, support, privacy and terms URLs were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. They identify
Adzviser and provide the expected site, contact form and legal pages. The supplied
icon was inspected and reused. Country targeting and website-only subscription
details follow the owner's established instructions.

## Portal handoff

Use this ZIP with the existing HubSpot entry. Its identity and confirmed endpoint
are preserved. The legacy entry's exact resubmission behavior has not been tested;
a valid ZIP cannot by itself fix a portal migration issue. Do not change package
identity or create a duplicate submission to work around one.

After an accepted upload, check imported review information, authorize the MCP
connection if required, inspect its current scan, verify reviewer access and run
the cases through the saved version. Complete required portal attestations.
Specific rejection details were not provided, so this work does not claim to
resolve particular reviewer findings or guarantee approval.
