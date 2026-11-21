# Merchant Center submission preparation

Prepared on 2026-10-26. The original internal identity
`app-6aa3b9397a048191be1511994353757e`, version `1.0.0`, public name
`Adzviser Merchant Center`, subtitle, publisher and starter prompts are preserved.
The owner confirmed the entry is unpublished/rejected and its registered endpoint
is https://merchant-center.mcp.adzviser.com/widgets/http. The reviewer has
owner-confirmed access to workspace `Merchant Center Demo`, account `Yuka.ua`.

## Package

The downloaded archive contained generic skills without a concrete MCP
declaration. Portable and compatibility manifests now share the original
identity, version, listing and review information. The MCP declaration and both
skill dependencies use the confirmed Merchant Center endpoint.

Included: the supplied Adzviser icon, five positive Data Mode cases, three
negative cases, demo URL, all supported countries, website-only subscriptions,
and user-facing release notes. The optional Preview UI skill remains available;
no widget tests are required by these cases. No credentials or private app
bindings are packaged. The listing distinguishes historical performance from
current product details and issues.

## Five positive prompts

1. How many impressions and clicks did we get in Merchant Center Demo during the 30 days ending two days ago, and what was our CTR?
2. Which 10 products got the most clicks in Merchant Center Demo during the 30 days ending two days ago?
3. Show clicks and impressions by customer country in Merchant Center Demo for the 30 days ending two days ago.
4. How many clicks and impressions came from ads versus organic listings in Merchant Center Demo during the 30 days ending two days ago?
5. Compare clicks and impressions in Merchant Center Demo for the 30 days ending two days ago with the preceding 30 days.

Let D be the current local date. The recent interval is [D-31, D-2], inclusive;
the preceding interval is [D-61, D-32]. Recalculate at review time. No test case
hardcodes calendar dates, expected totals, product IDs or country codes.

## Direct-tool verification

All five report queries passed through the authenticated Merchant Center tools
available in this session (namespace `Adzviser Merchant Center Test`). This is
the existing connection used for testing, not a newly created portal plugin.
Workspace and catalog discovery passed. Every response had isError=false,
reportingMode=data, directData=true, the requested workspace and source, and an
empty note_of_assumption. No UI widgets or unrelated fields were requested.

On October 26, the recent interval was September 25–October 24 and the preceding
interval was August 26–September 24.

| Case | Status | Preparation evidence |
| --- | --- | --- |
| Traffic totals and CTR | Passed direct request | 467,971 impressions, 3,546 clicks, fractional CTR 0.007577392616209124, displayed as approximately 0.76%. Clicks / impressions reconciles. |
| Top products | Passed direct request | 917 performance rows; 878 distinct nonblank product IDs after grouping title variants. The leading product had 262 clicks; the next two had 176 and 123. One blank-ID row had 1 click and 12,011 impressions and is excluded from named-product rankings. |
| Customer countries | Passed direct request | Five returned codes: CZ, DE, MD, PL and UA. All 3,546 clicks were attributed to UA in this snapshot. Returned country rows contained 467,822 impressions. |
| Ads versus organic | Passed direct request | ADS: 3,294 clicks and 425,485 impressions. ORGANIC: 252 clicks and 42,486 impressions. Both measures reconcile with account totals. |
| Period comparison | Passed direct request | Recent 3,546 clicks / 467,971 impressions; preceding 2,964 / 402,943. Changes +582 clicks (+19.64%) and +65,028 impressions (+16.14%). |

Numeric strings were converted for arithmetic; product IDs remained text.
Product rows with repeated IDs were grouped before ranking, without merging
different IDs that happen to share titles. CTR was converted from ratio to
percentage once.

Product-segmented impressions summed to 464,340, below the unsegmented 467,971.
Country-segmented impressions summed to 467,822, also below the account total.
Their click totals both matched 3,546. The cause of the impression differences
was not independently established; they must not be filled with invented rows
or described as a proven connector defect. The cases report the returned scope
and do not require all segmented impressions to reconcile with account totals.

These numbers document the preparation run; they are not expected answers for
future review. Data and reporting coverage can change. Completeness against
Merchant Center's own dashboard was not independently verified.

Saved-plugin positive conversations, three negative conversations, the saved
submission scan and reviewer sign-in: **Not run**. Direct queries do not prove
natural-language routing through a new saved version. Negative cases cover
price changes, deleting products, and ad-budget changes; they should explain
unsupported actions without tool calls or fabricated success. Credentials belong
only in secure dashboard fields.

## Interpretation and tool annotations

The source implementation returns historical performance in ProductPerformance
or Combined, and current catalog information in ProductDetails&Issues. Current
product details are not filtered to the requested dates. Multiple issue rows can
refer to one product; Status contains reporting contexts rather than a simple
approval boolean. Skills describe those limits and keep reports separate.

Google's [performance report documentation](https://developers.google.com/merchant/api/guides/reports/performance-reports)
explains segmentation. The [ProductPerformanceView reference](https://developers.google.com/merchant/api/reference/rest/reports_v1/accounts.reports#ProductPerformanceView)
defines CTR as clicks divided by impressions and explains that product dimensions
reflect the time of an impression. No claim of complete historical feed diagnostics
is made.

Inspected local definitions contain explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_merchant_center | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads static field definitions. Retrieval accesses authorized
external reports and records usage; it does not modify products or campaigns.
Preview compatibility paths can run reports or save preferences. Workspace
lookup can clear a stale account preference. Mode selection saves a presentation
preference. Shared reporting uses openWorldHint=true for external service access,
while account access stays scoped to authorized connections.

No Merchant Center server changes or deployments were made. Anonymous initialize
and tools/list requests returned OAuth 401 challenges. Authenticated reports
worked through the existing connection. Saved portal descriptors were not captured
or compared; these notes neither override live annotations nor guarantee approval.

## Demo and handoff

Demo: https://youtu.be/gbv-Vxd8LR0

Anonymous metadata identified “Adzviser Merchant Center ChatGPT Plugin Demo” by
Adzviser, approximately 169 seconds, non-private, with player status OK.
An isolated signed-out browser played the opening; the inspected frame around
46 seconds showed plugin discovery. Playback stalled around 60 seconds, followed
by a YouTube error. Full playback, result coverage and absence of sensitive
content throughout remain unverified. Check the complete recording before review;
the browser failure alone does not prove the hosted video is broken.

The unchanged website, support, privacy and terms pages were opened anonymously
and inspected earlier on October 26 during Salesforce preparation. The supplied
256-pixel Adzviser PNG was inspected and reused.

Use this ZIP with the existing Merchant Center entry. Its identity, version and
confirmed endpoint are preserved. No portal entry was uploaded, submitted,
published or deleted. A ZIP cannot itself resolve a portal migration issue.
After accepted upload, check imported review information, authorize the MCP
connection if needed, inspect the scan, verify reviewer sign-in, and run the cases
through the saved version. Complete video verification and portal attestations
before review. No specific rejection reason was supplied for this submission.
