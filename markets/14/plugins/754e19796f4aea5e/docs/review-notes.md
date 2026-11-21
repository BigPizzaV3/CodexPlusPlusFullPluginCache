# Display & Video 360 submission preparation

Prepared on 2026-10-26. Package `app-6aa607baa59c8191a2568b87978075c9`, version
`1.0.0`, public name `Adzviser Display & Video 360`, and subtitle
`Talk to your DV360 data` are preserved. The owner confirmed that the existing
entry is unpublished/rejected and its registered MCP endpoint is:
https://dv360.mcp.adzviser.com/widgets/http

The owner confirmed reviewer access to workspace `DV360 Demo` and its `Demo`
Display & Video 360 account. The original downloaded ZIP remains in Downloads.
No duplicate plugin was created, and no server code or deployment was changed.

## Package contents

The original archive contained generic Adzviser skills without an MCP declaration.
The prepared package declares the confirmed DV360 endpoint in `mcp.json` and both
skill dependencies. The portable manifest and legacy compatibility manifest have
matching identity, version, listing, publication and review metadata. Original
starter prompts are retained. The listing describes reporting capabilities;
instructions distinguish media cost, total media cost, billable cost and revenue.

The ZIP includes the Adzviser 256-pixel PNG, five positive Data Mode cases, three
negative cases, the supplied demo URL, all supported countries, website-only
subscription information and user-facing release notes. The positive prompts
also appear in `review.prompts` for plugin metadata review. There are no private
app bindings, credentials, or unrelated files. Existing explicit Preview UI
functionality is retained, but no widget review cases were added.

## Five positive prompts

1. What was our DV360 media cost in USD for the 30 days ending two days ago in DV360 Demo?
2. Show DV360 impressions, clicks, and click-through rate for the 30 days ending two days ago in DV360 Demo.
3. Show DV360 media cost in USD by campaign for the 30 days ending two days ago in DV360 Demo.
4. Compare DV360 media cost in USD for the 30 days ending two days ago with the preceding 30 days in DV360 Demo.
5. Show daily DV360 media cost in USD for the 30 days ending two days ago in DV360 Demo.

Let D be the current date in the user's timezone. The recent interval is
[D-31, D-2], inclusive, and the previous interval is [D-61, D-32]. Resolve these
dates again at review time. The following numbers record one live verification;
they are not fixed expected answers for future reviews.

## Actual direct-tool verification

The authenticated DV360 tools available in this session returned data for all
five requests on October 26, 2026. Workspace and field discovery passed. The recent
interval was September 25–October 24, with August 26–September 24 for comparison.
All responses had `isError=false`, `reportingMode=data`, `directData=true` and empty
`note_of_assumption`. Only required reporting fields were requested. No widget was opened.

| Case | Result | Observed evidence |
| --- | --- | --- |
| Media cost in USD | Passed | USD 3,744.866238, displayed as USD 3,744.87. This is Media cost (USD), not total fees or sales revenue. |
| Impressions, clicks and CTR | Passed | 6,496,284 impressions, 88,736 clicks; calculated CTR approximately 1.3660%. |
| Campaign media cost | Passed | One returned campaign, ID 57238540, with USD 3,744.866238. The campaign subtotal matched the overall media cost. |
| Period comparison | Passed | Recent USD 3,744.866238 versus earlier USD 6,304.781964. Decrease USD 2,559.915726, approximately 40.60%. |
| Daily media cost | Passed, with narrower returned date coverage | Thirteen rows covering September 25–October 7 summed to USD 3,744.866239; the difference from the ungrouped report is USD 0.000001, below displayed currency precision. Both display USD 3,744.87. |

No daily rows were returned for October 8–24. Those dates were not filled with
invented zeros. The response alone does not establish why the rows are absent,
and the package does not claim every requested day had activity or cached data.
Reviewers should use the actual returned dates and values. Keep the demo account
and its reporting data available during review; moving intervals can return a
different amount of data later.

Fresh-conversation routing through the saved plugin: **Not run**. Direct requests
verify query execution and returned rows, not every natural-language step in a
new uploaded-plugin conversation. Source completeness against DV360's own UI was
not independently checked.

Three negative conversations: **Not run**. Cases cover pausing line items,
increasing insertion-order budgets, and identifying individual ad clickers.
These are unsupported. Expected behavior is an accurate explanation without
unnecessary tool calls or a claim that the requested action was performed.

Saved submission scan and reviewer sign-in: **Not run**. Workspace access was
confirmed by the owner. Credentials and sign-in instructions belong only in the
secure dashboard fields, never in this package.

## Tool annotations

The local source definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_dv360 | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads field definitions. DV360 retrieval creates and runs a
transient Bid Manager reporting query, downloads its report, attempts to delete
that transient query afterward, and records Adzviser usage. These reporting side
effects explain the false read-only and idempotent hints. They do not change
campaign delivery, bids, budgets or creatives. Preview compatibility paths can
run reports or save presentation preferences. Workspace resolution can clear a
stale saved account preference; mode selection saves a presentation preference.

The shared external-service classification uses openWorldHint=true for reporting;
actual account access remains scoped to authorized connections. These are local
source checks, not a descriptor capture from the saved portal scan. Anonymous
initialize and tools/list calls to the confirmed endpoint returned OAuth 401
challenges. Notes do not override live annotations or prove reviewer acceptance.

## Demo and listing checks

Demo: https://youtu.be/gBNXuMRPG0Q

Anonymous YouTube metadata identified “Adzviser DV360 ChatGPT Plugin Demo” by
Adzviser, approximately 162 seconds, non-private status and player status OK.
An isolated signed-out browser played the beginning. Inspected frames at about
8, 48 and 60 seconds show ChatGPT, plugin discovery and DV360 connection setup.
Playback later stalled and displayed a player error. Full playback, report-result
coverage and absence of sensitive content throughout the recording remain
**unverified**. Check the full recording before submitting.

The unchanged publisher website, support, privacy and terms URLs were opened
anonymously and inspected earlier on October 26 during Salesforce preparation.
They identify Adzviser and provide the expected site, contact form and legal pages.
The supplied icon was inspected and reused. Country targeting and website-only
subscription details follow the owner's established instructions.

## Portal handoff

Use the ZIP with the existing Display & Video 360 entry. Its package ID and
confirmed endpoint are preserved. The legacy entry's exact resubmission behavior
has not been tested. A valid ZIP cannot by itself resolve a portal migration error;
do not change the identity or create a duplicate entry to work around one.

After an accepted upload, check imported metadata and review cases, authorize
the MCP connection if required, inspect the current tool scan, verify reviewer
access and run the cases through the saved version. Complete the required
attestations in the portal. Specific rejection details were not provided, so
this work does not claim to resolve particular reviewer findings or guarantee
approval. No portal entry was uploaded, submitted, published or deleted here.
