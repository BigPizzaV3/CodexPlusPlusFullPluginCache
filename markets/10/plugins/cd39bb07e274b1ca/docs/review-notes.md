# Shopify submission preparation

Package: app-6aa0684226208191b41f6cf373ea6cce, version 1.0.0.
The original identity, display name, subtitle, descriptions, category and starter
prompts are preserved. The publisher confirmed that the existing entry is
unpublished/rejected and that its registered MCP endpoint is:
https://shopify.mcp.adzviser.com/widgets/http

The original ZIP had no MCP declaration and referenced the generic Adzviser
endpoint in its skill dependencies. This package explicitly declares the confirmed
Shopify endpoint and scopes both skills to shopify_request. It includes the
Adzviser icon, five Data Mode positive cases, three negative cases, the supplied
video, all supported countries, website-only subscription information and
user-facing release notes. No server code was changed or deployed, and no portal
entry was created, deleted, submitted or published.

## Existing-entry upload limitation

An unpublished/rejected Google Ads entry in the same preparation session rejected
a similar update with "Keep the existing MCP connection" and "Publish the existing
MCP app before updating its plugin ZIP." Shopify may encounter the same restriction.
Its upload has not been tested. ZIP validation cannot establish that the portal
will accept an update to this older entry. The original internal name is retained
for the existing entry; this archive is not a newly assigned plugin identity.

The Shopify rejection details were not supplied. This preparation does not claim
to resolve particular reviewer findings. The original entry's saved connection,
tool scan, review information and current resubmission controls remain unverified.

## Direct query evidence and limits

On 2026-10-07, the five final report requests succeeded through the authenticated
general Adzviser connection, using only shopify_request and the Demo workspace.
This was not a separately installed Shopify test connection or the saved portal
draft. All responses had isError=false, reportingMode=data and directData=true.
No widget was opened. Relative dates below are evidence for that day; review
cases resolve dates again when run.

| Case | Status | Observed evidence |
| --- | --- | --- |
| Monthly sales and orders | Passed, with source-data limitations | September 1-30: USD-labelled rows had Total sales 137,429.09 and 170 Orders. A separate missing-currency row had Total sales -3,531.70 and zero Orders. These were not combined into a USD total. |
| Top products by Items | Passed, with missing identifiers | 222 product groups, 293 reported Items in total. The identifiable leaders had 7, 5, 4, 4 and 4 Items, with ties. An unidentified product group accounted for 16 Items and was kept separate. The final request retrieved Items and product identifiers only. |
| Sales by channel | Passed, with missing labels | Point of Sale: USD 135,036.76 and 164 Orders; Online Store: USD 1,997.33 and 5 Orders; unknown channel: USD 395.00 and 1 Order. A separate unknown-channel/unknown-currency adjustment was -3,531.70. Known-currency channel figures reconciled to the monthly report. |
| Net-sales comparison | Passed, with missing currency | September USD 128,542.63 versus August USD 179,857.68: decrease USD 51,315.05, approximately 28.53%. Currency-unspecified rows of -3,416.22 and -3,971.90 were kept separate. |
| Daily sales and orders | Passed, with missing currency | September 28-October 4 returned all seven days for USD: Total sales 47,559.37 and 38 Orders. Additional currency-unspecified adjustments summed to -2,905.46. The daily query took longer than the other reports; it was allowed to finish without duplicate retrieval. |
| Fresh-conversation positive cases | Not run | Direct queries validate report execution and returned rows, not natural-language routing through the uploaded plugin. |
| Negative conversations | Not run | Drafted against capabilities: issuing refunds/cancelling orders, deleting products, and sending marketing emails are unsupported. |
| Dedicated Shopify connection and saved submission | Not run | Public server identity was checked, but authenticated execution used the general Adzviser connection. Portal OAuth, scanning and reviewer-login execution remain to be verified. |

These successful requests do not establish the correctness or completeness of
the underlying store data against Shopify Admin. Missing currency means the
complete store-wide monetary total cannot be labelled confidently. Missing
product/channel identifiers also limit attribution. The skills and expectations
require those limitations to be disclosed rather than guessed away. Product-level
and account-level monetary rollups are not assumed interchangeable.

The final positive requests use only Total sales, Orders, Items or Net sales,
plus Currency, Product ID/Product title or Channel as needed. No customer names,
email addresses, phone numbers, addresses or order notes were requested. Derived
sales requests returned additional component columns automatically; only relevant
values should be included in the answer. Shopify.data was a header-first row array.

The reviewer account needs access to Demo and its Shopify connection. Enter
credentials in secure dashboard fields, not in this ZIP.

## Tool annotations and scope

The public Shopify endpoint identified itself as running build
6bf20c8d-20261002201522 and advertised the expected tools. Local definitions use
explicit boolean annotations:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_shopify | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

- Catalog discovery reads a bounded field catalog without changing store state.
- Retrieval reads reporting data and records Adzviser usage and external-tool-use
  state. Those side effects explain its false read-only and idempotent hints;
  it does not edit products, orders, customers or payments.
- Preview compatibility paths can run reports or persist presentation preferences,
  so its hints cover those side effects. It does not change Shopify records.
- Workspace discovery can clear a stale saved account-selection preference during
  resolution. Repeating it has no additional preference effect.
- The app-only reporting-mode control saves a presentation preference without
  modifying source records; saving the same mode repeatedly is idempotent.

The shared server retains its conservative open-world classification for external
account/service reporting while actual Shopify access is limited to authorized
connected stores. These notes do not claim that reviewers have accepted those
values and do not override server annotations or populate portal review fields.
An authenticated descriptor capture from the saved Shopify submission was not
available. No annotation or server-behavior changes were made during packaging.

## Demo, listing and remaining portal checks

Demo: https://youtu.be/eHS1xu8Rhfc
Anonymous YouTube metadata returned "Adzviser Shopify ChatGPT Plugin Demo" by
Adzviser, a 186-second duration, non-private status and player status OK. Actual
visual playback, legibility, full scenario coverage and absence of secrets were
not independently inspected.

The existing publisher website, support, privacy and terms URLs are the same
ones fetched and inspected earlier on 2026-10-07 while preparing Meta Ads. The
supplied Adzviser PNG is bundled as both listing and composer icon. No new UI
review cases or screenshots were added. Website-only Adzviser subscriptions and
all supported countries follow the publisher's established instructions.

After an accepted upload, verify the imported metadata and cases, complete
connection/authentication and domain verification where required, inspect the
current tool scan, enter reviewer access securely, and run the cases against the
saved version. Resolve the actual rejection findings before resubmission. Local
archive validation does not establish portal acceptance or review approval.
