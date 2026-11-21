# Pipedrive resubmission preparation

The source and ZIP are prepared for upload to the existing rejected Pipedrive
entry. Internal package identity app-6aa60a9d9b408191a84fd2eecf0a58c1 and version
1.0.0 are preserved. The publisher confirmed the existing MCP endpoint:
https://pipedrive.mcp.adzviser.com/widgets/http

The .codex-plugin/plugin.json manifest references .mcp.json. Both skill dependency
files use the same pipedrive server key and endpoint. The subsequent rejection
identified naming/affiliation and tool-annotation issues. On October 26 the
publisher asked to leave the public name unchanged; that naming finding remains
outside this correction.

## Review cases

Five positive cases use Pipedrive Demo in Data Mode: monthly created-deal count
and value, current status, current pipeline/stage IDs, month comparison and daily
creation trends. Three negative cases request unsupported status changes,
record deletion and HubSpot data. The reviewer account must have access to
Pipedrive Demo and its connected Demo account. No reviewer credentials or
personal account email addresses are included in this package.

The listing and the first starter prompt were corrected to describe creation-date
reporting. The original closing-date prompt implied a different record cohort.
Both skills distinguish creation dates from current status and handle separate
Deals/Leads tables, identifiers and multiple currencies.

## Direct query verification

The discovery response reported 2026-10-02 as its date reference (the session
context said 2026-10-01). Both resolve last month to September 1-30, the preceding
month to August 1-31, and last week to September 21-27. Future runs must resolve
the relative dates again. Figures below are observed evidence, not fixed test
answers. Requests used the available Pipedrive development connection, not the
saved resubmission or a dedicated reviewer login.

| Query | Status | Observed evidence |
| --- | --- | --- |
| Monthly summary | Passed | 18,356 USD deals worth USD 213,100; 35 INR deals worth INR 1,000. Values kept separate. |
| Current status | Passed | USD: 17,816 open, 518 lost, 22 won; INR: 35 open. Counts and values reconcile with the summary by currency. |
| Pipeline/stage | Passed | 22 returned pipeline/stage/currency groups. Counts and values reconcile with the summary by currency. |
| Month comparison | Passed | August: 6,711 USD deals worth USD 219,299; 7 INR deals worth INR 0. September matches the summary. INR value has a zero baseline, so no finite percentage change. |
| Daily creation | Passed | 11 date/currency rows for September 21-27. USD: 8,633 deals, value 61,500; INR: 35 deals, value 1,000. Missing currency/day combinations are not fabricated. |
| Exploratory lead query | Passed, empty | No September leads returned. This was not selected as one of the five positive cases. |
| Fresh-chat positive/negative cases | Not run | Direct queries do not prove natural-language routing or user-visible answers. |
| Existing submission, OAuth and reviewer login | Not run | The saved submission and reviewer access still need verification. |

## Annotation correction and deployment status: October 26

The public endpoint reports build `6bf20c8d-20261002201522`. Cloud Run serves
revision `mcp-00319-qoy` at 100% traffic. The source archive for its successful
Cloud Build `b50107d2-3217-4266-8e82-9394221c319a` was inspected: reporting tools
still explicitly set openWorldHint=true, and workspace discovery inherits true.
The deployed source therefore lacks the prepared correction. This verifies a
current mismatch; it does not identify the exact annotation cited by the reviewer,
whose rejected scan has not been captured.

The corrected local descriptors use the following explicit booleans:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_pipedrive | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

- Catalog discovery reads static definitions without changing state.
- Retrieval reads authorized Pipedrive records and records reporting usage;
  repeated retrievals may record additional usage. It does not edit or delete
  CRM records, so it is non-destructive but not strictly read-only or idempotent.
- Preview compatibility paths can retrieve reports or persist presentation
  preferences. Its annotations cover those possible effects as well as preview.
- Workspace discovery can clear stale account preferences. This normalization
  changes state but repeating it has no additional effect, so it is idempotent.
- Mode selection saves an app presentation preference. Repeating the same value
  has no additional effect. It does not modify CRM records.
- All five tools are bounded to the catalog, app preferences, or connected,
  authorized accounts. They do not accept arbitrary external entities or publish
  content. Remote hosting alone does not make them open-world.

The local TypeScript build and 224 targeted AdRoll/Pipedrive connector and UI
tests passed. These tests mock external authentication/reporting and do not
establish reviewer login or a successful saved portal scan. The correction has
not been deployed by this preparation. Deploy the corrected MCP server, rescan
the existing submission, and inspect the resulting annotations before review.
The ZIP contains justifications; it cannot change the live tools' annotations.
See [OpenAI's review requirements](https://developers.openai.com/plugins/deploy/app-review#review-and-approval-faqs).

## Demo, icon and publication

Demo URL: https://youtu.be/8kqbK7vaYpw
Anonymous YouTube checks identified Adzviser Pipedrive ChatGPT Plugin Demo by
Adzviser, non-private status, player status OK and a 206-second duration.
Visual playback, complete case coverage and absence of secrets in the recording
have not been independently reviewed.

The supplied Adzviser PNG is reused. Website and support content, and the actual
privacy/terms publisher text, were fetched and inspected. All supported countries
and website-only Adzviser subscriptions follow the publisher's prior instructions.
Release notes describe user-facing functionality. The original ZIP remains in
Downloads. No portal entry was created, deleted, uploaded or submitted.
## Upload and verify the resubmission

Upload adzviser-pipedrive-1.0.0.zip as the updated draft of the existing Pipedrive
entry, whose package name is app-6aa60a9d9b408191a84fd2eecf0a58c1. Check the imported
listing, five positive cases, three negative cases, demo and country availability.
This archive retains the existing identity; it does not create a renamed plugin.

Verify the saved MCP URL against the confirmed endpoint above. Complete OAuth
or reconnect when requested, run the current tool scan, and resolve its findings.
Enter reviewer credentials only through secure portal fields. Confirm the
reviewer can access Pipedrive Demo and run the cases against the saved draft.

The five direct queries passed in the available development connection. Full
conversational cases, reviewer sign-in, and the existing portal submission have
not been exercised. The server annotation correction still requires deployment
and a new portal scan. The naming finding is intentionally unchanged at the
publisher's request. Local packaging and query checks do not guarantee approval.
