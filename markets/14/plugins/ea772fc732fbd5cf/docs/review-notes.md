# LinkedIn Ads submission preparation

Prepared on 2026-10-26. The package ID
`app-6aa3b7e0ca108191a4926f22391a49d2`, version `1.0.0`, public name
`Adzviser LinkedIn Ads`, subtitle `Talk to your LinkedIn Ads data`, publisher
`Adzviser LLC`, and three original starter prompts are preserved.

The owner confirmed that the existing entry is unpublished/rejected and that
its registered MCP URL is https://linkedin-ads.mcp.adzviser.com/widgets/http.
The owner also confirmed that `Matterport` is the intended test workspace and
the reviewer login has access to its `Matterport` LinkedIn Ads account.
The original downloaded archive remains in Downloads. No duplicate plugin was
created and no portal entry was uploaded, submitted, published or deleted.

## Package contents

The original archive contained generic Adzviser skills without an MCP declaration.
The prepared package declares the confirmed LinkedIn Ads endpoint in `mcp.json`
and both skill dependencies. Portable and legacy compatibility manifests have
matching identity, version, listing, publication and review metadata.

The ZIP contains the Adzviser 256-pixel PNG, five positive Data Mode cases, three
negative cases, the supplied demo URL, all supported countries, website-only
subscription information and user-facing release notes. Positive prompts also
appear in `review.prompts`. Existing explicit Preview UI functionality is retained,
but no widget review cases were added. There are no credentials or private app
bindings. The skills request only LinkedIn Ads data, even when the workspace
contains other sources.

## Five positive prompts

1. What was our LinkedIn Ads spend in USD for the 30 days ending two days ago in Matterport?
2. Show LinkedIn Ads impressions, clicks, and click-through rate for the 30 days ending two days ago in Matterport.
3. Show LinkedIn Ads spend in USD by campaign for the 30 days ending two days ago in Matterport.
4. Compare LinkedIn Ads spend in USD for the 30 days ending two days ago with the preceding 30 days in Matterport.
5. Show daily LinkedIn Ads spend in USD for the 30 days ending two days ago in Matterport.

Let D be the current date in the user's timezone. The recent interval is
[D-31, D-2], inclusive, and the previous interval is [D-61, D-32]. Recalculate
these dates at review time. These cases cover a spend total, a calculated rate,
a campaign grouping, a period comparison and a daily time series. Values below
are preparation evidence, not fixed expected answers for future reviews.

## Actual direct-tool verification

All five requests passed on October 26, 2026 through the connected **Adzviser**
app, using only `assorted_requests.linkedin_ads_request`. A separate authenticated
LinkedIn Ads test connection was not available in this session. These results
verify the source queries through Adzviser, not authentication or routing through
the dedicated submission endpoint or the saved LinkedIn Ads plugin.

Workspace and field discovery passed. The recent interval was September 25–
October 24; the preceding interval was August 26–September 24. All responses had
`isError=false`, `reportingMode=data`, `directData=true` and empty
`note_of_assumption`. No widget or unrelated data source was requested.

| Case | Result | Observed evidence |
| --- | --- | --- |
| Spend in USD | Passed through Adzviser | USD 7,510.1900000000005, displayed as USD 7,510.19. |
| Impressions, clicks and CTR | Passed through Adzviser | 272,732 impressions and 8,572 clicks; calculated CTR approximately 3.1430%. |
| Campaign spend | Passed through Adzviser | Three campaign rows: USD 4,983.38, USD 1,826.81 and USD 700.00. Their unrounded sum matches total spend. |
| Period comparison | Passed through Adzviser | Recent USD 7,510.19 versus earlier USD 12,917.30921252498; decrease USD 5,407.11921252498, approximately 41.86%. |
| Daily spend | Passed through Adzviser | Thirty daily rows covering every date from September 25 through October 24. Their sum, USD 7,510.190000000002, matches the ungrouped total within floating-point precision. |

The catalog's canonical Campaign ID and Campaign name map to the API's campaign
group level. Ad set fields map to the API campaign level, and Ad fields map to
creatives. The cases preserve these distinctions. `Total spent (USD)` is used
explicitly; local-currency spend, CPC and CPM are not relabeled as USD.

Fresh-conversation routing through the uploaded plugin: **Not run**. Direct-tool
checks do not prove every natural-language step of a new saved-plugin conversation.
Source completeness against LinkedIn Campaign Manager was not independently
checked. Keep the workspace and its reporting data available during review;
moving intervals can return different values later.

Three negative conversations: **Not run**. They cover pausing campaigns,
increasing ad-set budgets, and identifying individual ad clickers. Expected
behavior is an accurate explanation without unnecessary tool calls or a false
claim that the action was performed.

Saved submission scan and reviewer sign-in: **Not run**. Access was confirmed by
the owner. Credentials and sign-in instructions belong only in secure dashboard
fields, never in this package.

## Tool annotations

The local source definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_linkedin_ads | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

LinkedIn Ads catalog discovery reads static field definitions without account
resolution. Retrieval requests authorized advertising reports and records
Adzviser usage; it does not change campaigns, budgets or ads. Preview compatibility
paths can run reports or save preferences. Workspace lookup can clear a stale
account preference, and mode selection saves a presentation preference.
Reporting uses the shared external-service classification `openWorldHint=true`;
actual access remains scoped to authorized connections.

No LinkedIn Ads server source changes or deployments were made for this package.
Anonymous initialize and tools/list calls to the dedicated endpoint returned
OAuth 401 challenges. Authenticated reporting succeeded through Adzviser as
described above. The saved portal descriptors were not captured or compared.
These notes do not override live annotations or guarantee reviewer acceptance.

## Demo and listing checks

Demo: https://youtu.be/qxuqnoAqZOw

Anonymous metadata identified “Adzviser LinkedIn Ads ChatGPT Plugin Demo” by
Adzviser, approximately 162 seconds, non-private status and player status OK.
An isolated signed-out browser played the beginning, including a frame at
approximately 48 seconds showing plugin discovery in ChatGPT. Playback then
displayed a YouTube error. Full playback, report-result coverage and absence of
sensitive content throughout remain **unverified**. Check the complete recording
before review; the browser failure alone does not establish that the video is
broken for reviewers.

The unchanged publisher website, support, privacy and terms URLs were opened
anonymously and inspected earlier on October 26 during Salesforce preparation.
They identify Adzviser and provide the expected site, contact form and legal
pages. The supplied icon was inspected and reused. Country targeting and
website-only subscription details follow the owner's established instructions.

## Portal handoff

Use this ZIP with the existing LinkedIn Ads entry. Its identity and confirmed
endpoint are preserved. The legacy entry's exact resubmission behavior has not
been tested; a valid ZIP cannot itself fix a portal migration issue. Do not change
package identity or create a duplicate submission to work around one.

After an accepted upload, check imported review information, authorize the
LinkedIn Ads MCP connection if required, inspect its current scan, verify reviewer
access and run these cases through the saved plugin version. Complete required
portal attestations. Specific rejection details were not provided, so this work
does not claim to resolve particular reviewer findings or guarantee approval.
