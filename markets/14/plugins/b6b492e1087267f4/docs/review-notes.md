# Mailchimp submission preparation

Prepared on 2026-10-26. Original identity
`app-6aa3b674f8008191bb3319b027b5e104`, version `1.0.0`, public name
`Adzviser Mailchimp`, subtitle, publisher and three starter prompts are preserved.
The owner confirmed the existing entry is unpublished/rejected and its registered
MCP endpoint is https://mailchimp.mcp.adzviser.com/widgets/http.
The reviewer has owner-confirmed access to workspace `Mailchimp Demo` and its
`Respect Victoria` Mailchimp account.

## Package

The original archive contained generic skills without a concrete MCP declaration.
The portable MCP declaration and both skill dependencies now use the confirmed
endpoint. Portable and legacy manifests have matching identity, version, listing,
publication and review information.

The package contains the supplied Adzviser PNG, five positive Data Mode cases,
three negative cases, the supplied demo URL, all supported countries,
website-only subscription information and user-facing release notes.
Explicit Preview UI functionality remains available, with no widget test cases.
There are no credentials or private app bindings in the package.

The description avoids unsupported segment breakdown promises and date-filtered
audience-growth claims. Instructions distinguish campaigns selected by send
date, their accumulated engagement, and current audience snapshots.

## Five positive prompts

1. How many emails did we send through Mailchimp in Mailchimp Demo during the 30 days ending two days ago?
2. Show the open and click rates for Mailchimp campaigns sent in the 30 days ending two days ago in Mailchimp Demo.
3. How many hard bounces, soft bounces, and unsubscribes did our Mailchimp campaigns sent in the 30 days ending two days ago have in Mailchimp Demo?
4. Compare the number of Mailchimp emails sent in the 30 days ending two days ago with the preceding 30 days in Mailchimp Demo.
5. What is the current member count of each Mailchimp audience in Mailchimp Demo?

Let D be the current local date. Recent dates are [D-31, D-2], inclusive; the
preceding period is [D-61, D-32]. Recalculate when testing. The fifth case uses
the required date pair in its input but explicitly treats list statistics as
current snapshots, unaffected by those dates. No case hardcodes expected
report values, campaign IDs, audience IDs or calendar dates.

## Actual direct-tool verification

All five source requests passed through the authenticated Mailchimp tools
available in this session (tool namespace `Adzviser Mailchimp Test`).
This refers to the connected tools used for testing, not a newly created portal
plugin. No private plugin or duplicate submission was created.

Workspace and catalog discovery passed. On October 26, recent dates were
September 25–October 24 and earlier dates were August 26–September 24. Each
response had isError=false, reportingMode=data, directData=true, the requested
source and workspace, and an empty note_of_assumption. No widget, contact-level
fields or unrelated source was requested.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Emails sent | Passed direct request | One campaign sent October 7; 3,430 emails. |
| Campaign rates | Passed direct request | Same campaign: 2,295 unique opens, 67.93960923623446% open rate, 175 unique subscriber clicks, 5.180580224985198% click rate. |
| Bounces and unsubscribes | Passed direct request | 21 hard bounces, 31 soft bounces and 6 unsubscribes. Total bounces 52. |
| Send-volume comparison | Passed direct request | Recent 3,430 across one campaign; earlier 11,416 across five campaigns. Difference -7,986, approximately -69.95%. All returned send dates belong to their requested periods. |
| Audience sizes | Passed direct request | Three lists returned with IDs and names, with member counts 662, 3,509 and 12. These are current per-list counts, not date-filtered growth or a unique cross-list total. |

The campaign rate denominators also reconcile for this fixture: 3,430 sends
minus 52 bounces equals 3,378; 2,295/3,378 and 175/3,378 match the returned open
and click percentages after scaling. The connector already scales its rate
fields to percentages, so the assistant must not multiply them again.

These are observations from the preparation date, not expected answers for
later review. Campaign activity and list membership can change. Direct-tool
checks do not prove natural-language routing through a new saved-plugin
conversation. Campaign completeness against Mailchimp's own UI was not
independently verified.

Saved-plugin positive conversations, three negative conversations, saved
submission scan and reviewer sign-in: **Not run**. Negative cases cover sending
campaigns, deleting audiences and unsubscribing contacts. They should explain
unsupported actions without unnecessary tool calls or fabricated success.
Keep reviewer credentials only in secure dashboard fields.

## Tool annotations

Inspected local definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_mailchimp | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads static field definitions. Retrieval accesses authorized
external reports and records usage; it does not send campaigns or modify
contacts. Preview compatibility paths can run reports or save preferences.
Workspace lookup can clear a stale account preference; mode selection saves a
presentation preference. Shared reporting uses openWorldHint=true for external
service access, while actual access remains scoped to authorized connections.

No Mailchimp backend changes or deployments were made. Anonymous initialize and
tools/list requests to the dedicated endpoint returned OAuth 401 challenges.
Authenticated reporting worked through the Mailchimp connection described
above. Saved portal descriptors were not captured or compared; these notes do
not override live annotations or guarantee approval.

## Demo and handoff

Demo: https://youtu.be/SsAgK6mLv0c

Anonymous metadata identified “Adzviser Mailchimp ChatGPT Plugin Demo” by
Adzviser, approximately 183 seconds, non-private status and player status OK.
An isolated signed-out browser played the beginning, including a readable
plugin-discovery frame around 48 seconds. Playback stopped around 60 seconds
and displayed a YouTube error. Full playback, report-result coverage and absence
of sensitive content throughout remain unverified. Check the complete recording
before review; the browser failure alone does not prove a broken video.

The unchanged website, support, privacy and terms pages were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. They identify
Adzviser and provide the expected website, contact and legal information.
The supplied 256-pixel PNG was inspected and reused.

Use this ZIP with the existing Mailchimp entry. Its identity, version and
confirmed endpoint are preserved. No portal entry was uploaded, submitted,
published or deleted. A ZIP cannot itself fix a portal migration issue.
After accepted upload, check imported review information, authorize the MCP
connection if required, inspect the scan, verify reviewer sign-in and run the
cases through the saved version. Complete recording verification and required
portal attestations before review. No specific rejection reason was supplied.
