# Trade Desk submission preparation

Prepared on 2026-10-26. Package `app-6aa3bb5095d08191bc985a64cb7a3d98`, version
`1.0.0`, public name `Adzviser The Trade Desk`, and subtitle `Talk to your TTD data`
are preserved. The owner confirmed that the existing entry is unpublished/rejected
and its registered MCP endpoint is:
https://ttd.mcp.adzviser.com/widgets/http

The owner confirmed that `Schaumburg Honda` is the intended test workspace and
that the reviewer login will have access to it. Its connected Trade Desk account
is also named `Schaumburg Honda`. The original download remains in Downloads.
No duplicate plugin was created or existing portal entry deleted.

## Package contents

The original archive contained generic Adzviser skills without an MCP declaration.
This package declares the confirmed endpoint in `mcp.json` and both skill
dependencies. The portable manifest and legacy compatibility manifest have
matching identity, version, listing, publication and review metadata. The three
original starter prompts are preserved. Instructions require workspace-scoped
field discovery, distinguish cost measures, and explain reporting boundaries.

The ZIP includes the Adzviser 256-pixel PNG, five positive Data Mode cases, three
negative cases, the supplied demo URL, all supported countries, website-only
subscription information and user-facing release notes. Positive prompts also
appear in `review.prompts`. There are no private app bindings or credentials.
Existing explicit Preview UI functionality is retained, but no widget review
cases were added.

## Five positive prompts

1. What was our Trade Desk advertiser cost in USD for the 30 days ending two days ago in Schaumburg Honda?
2. Show Trade Desk impressions, clicks, and click-through rate for the 30 days ending two days ago in Schaumburg Honda.
3. Show Trade Desk advertiser cost in USD by campaign for the 30 days ending two days ago in Schaumburg Honda.
4. Compare Trade Desk advertiser cost in USD for the 30 days ending two days ago with the preceding 30 days in Schaumburg Honda.
5. Show daily Trade Desk advertiser cost in USD for the 30 days ending two days ago in Schaumburg Honda.

Let D be the current date in the user's timezone. The recent interval is
[D-31, D-2], inclusive, and the previous interval is [D-61, D-32]. Resolve dates
again at review time. These examples cover totals, a calculated rate, campaign
grouping, a period comparison and a daily time series. Historical values below
are preparation evidence, not fixed expected answers for future reviews.

## Actual direct-tool verification

All five authenticated report requests returned data on October 26, 2026.
Workspace discovery and the catalog with `workspace_name=Schaumburg Honda` also
passed. The recent interval was September 25–October 24; the preceding interval
was August 26–September 24. Responses had `isError=false`, `reportingMode=data`,
`directData=true` and empty `note_of_assumption`. No widget was opened.

| Case | Result | Observed evidence |
| --- | --- | --- |
| Advertiser cost in USD | Passed | USD 4,147.812895854396, displayed as USD 4,147.81. |
| Impressions, clicks and CTR | Passed | 137,861 impressions, 631 clicks; calculated CTR approximately 0.4577%. |
| Campaign advertiser cost | Passed | Two campaigns returned USD 2,926.248258906077 and USD 1,221.5646369483204. Their sum matches the ungrouped cost within floating-point precision. |
| Period comparison | Passed | Recent USD 4,147.812895854396 versus earlier USD 4,763.780661547409. Decrease USD 615.9677656930135, approximately 12.93%. |
| Daily advertiser cost | Passed | Thirty daily rows covering every date from September 25 through October 24. Sum USD 4,147.812895854397 matches the ungrouped cost within floating-point precision. |

The campaign report placed ID and name before the cost column. Verification
matched headers instead of assuming a metric column position. No omitted days
were filled with invented zeros. Keep this workspace and its reporting data
available during review; moving intervals can return different values later.

Fresh-conversation routing through the uploaded plugin: **Not run**. Direct
requests verify query execution and calculations, not every natural-language
step of a new conversation. Source completeness against Trade Desk's own UI
was not independently checked.

Three negative conversations: **Not run**. They cover pausing campaigns,
increasing ad-group budgets and identifying individual ad clickers. Expected
behavior is an accurate explanation without unnecessary tool calls or claims
that the requested action was performed.

Saved submission scan and reviewer sign-in: **Not run**. Reviewer access was
confirmed by the owner. Credentials and sign-in instructions belong only in the
secure dashboard fields, never in this package.

## Tool annotations and local correction

The local source definitions contain these explicit booleans after one correction:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_trade_desk | false | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Workspace-scoped catalog discovery calls Copter's account resolver. If a saved
account preference refers to a revoked membership, that resolver clears and
saves the stale preference. Catalog discovery therefore cannot promise read-only
behavior for every supported call. Its `readOnlyHint` was changed from true to
false, with an explanatory source comment. It still reports a bounded catalog,
does not alter advertising campaigns, and repeated cleanup has the same effect.
This is a specific observed source path, not a claim about an earlier rejection.

The correction is local in:
`mcp/packages/mcp-server/src/tools/trade-desk/list-metrics-and-breakdowns-trade-desk.ts`.
It is not executable server code inside this ZIP. Deploy the MCP server and
rescan the saved submission to apply and inspect the changed live descriptor.
No deployment was performed. Existing connector-profile and reporting-tool
suites passed: 2 suites, 3,209 tests. No unrelated server changes were made here.

Reporting reads cached date partitions and records usage; missing partitions
can require background upstream report refresh. It does not change campaign
delivery, bids, budgets or creatives. Preview compatibility paths can run reports
or save presentation preferences. Workspace lookup can clear a stale account
preference; mode selection saves a presentation preference. Reporting's shared
external-service classification uses `openWorldHint=true`; actual access remains
scoped to authorized connections. These notes do not override live annotations.

Anonymous initialize and tools/list requests to the confirmed endpoint returned
OAuth 401 challenges. Authenticated reporting worked through the connected tools.
The descriptors saved in the submission portal were not captured or compared.

## Demo and listing checks

Demo: https://youtu.be/vOH2kjmZ2Pk

Anonymous YouTube metadata identified “Adzviser TTD ChatGPT Plugin Demo” by
Adzviser, approximately 169 seconds, non-private status and player status OK.
An isolated signed-out browser played the beginning. Inspected frames around
7 and 47 seconds show ChatGPT and plugin discovery. Playback failed around the
one-minute mark in that browser. Full playback, report-result coverage, and
absence of sensitive content throughout remain **unverified**. Check the full
recording before submitting; the automated browser failure alone does not prove
that the recording is broken for reviewers.

The unchanged publisher website, support, privacy and terms URLs were opened
anonymously and inspected earlier on October 26 during Salesforce preparation.
They identify Adzviser and provide the expected site, contact form and legal
pages. The supplied icon was inspected and reused. Country targeting and
website-only subscription details follow the owner's established instructions.

## Portal handoff

Use the ZIP with the existing Trade Desk entry. Its package ID and confirmed
endpoint are preserved. The legacy entry's resubmission behavior has not been
tested. A valid ZIP cannot itself resolve a portal migration error; do not change
the identity or create a duplicate entry to work around one.

After an accepted upload and the annotation deployment, check imported metadata
and cases, authorize the MCP connection if required, inspect the current tool
scan, verify reviewer access and run the cases through the saved version.
Complete required attestations in the portal. Specific rejection details were
not provided, so this work does not claim to resolve particular reviewer
findings or guarantee approval. No entry was uploaded, submitted or published.
