# eBay review preparation

This package is a separate new-plugin candidate, with internal name adzviser-ebay
and version 1.0.0. Its public display name remains Adzviser eBay. It is not a
version update for app-6aa610f6b3c8819181fffd9c236538ed.

The original unpublished portal entry showed an unavailable endpoint, no MCP key
and a disabled scan after a ZIP update. The original source and archive are kept
separately. This fresh candidate allows a new MCP connection to be configured;
it is a workaround to verify, not proof of the original entry's root cause.

The confirmed endpoint is https://ebay.mcp.adzviser.com/widgets/http.
The .codex-plugin/plugin.json manifest references .mcp.json. Both skill dependency
files use the same ebay server key and exact endpoint. Local validation does not
establish a portal connection or constitute review approval.

## Review cases and access

The manifest contains five Data Mode positive cases and three negative cases.
The positives cover a monthly summary, month comparison, top sold items, daily
sales, and marketplace fees. The negatives cover refunds, listing edits and an
unsupported Shopify source. No reviewer widget interaction is required.

The selected workspace is eBay Demo, with the connected account labelled Demo.
The dedicated reviewer login must have access to this workspace and its eBay
connection. No dedicated reviewer login or saved submission draft was exercised.
No reviewer credentials or account email addresses are included in the package.

## Direct reporting evidence

Reference date: 2026-10-01, America/Los_Angeles. Last month was September 1-30,
2026; the month before was August 1-31; last week was September 21-27. The cases
resolve dates when executed. Recorded values are evidence, not fixed expected
answers. Queries used the eBay connection available in this session; its runtime
label does not identify a particular saved portal draft.

| Check | Result | Evidence and limitations |
| --- | --- | --- |
| Monthly order query | Passed | GBP: 2,210 orders, 2,435 units, 25,137.57 Order Total. EUR: one order, one unit, 41.70 Order Total. Currency amounts are kept separate. |
| Two-month comparison query | Passed | August returned GBP 29,082.82 and 2,714 orders. September returned GBP and EUR. No EUR baseline row was returned, so a EUR percentage change is unavailable. |
| Sold-item query | Passed | 674 item/SKU groups and 2,436 units returned. The leading group had 47 units and GBP 300.80 product revenue. Product and order totals are distinct measures. |
| Daily query | Passed | Seven September 21-27 rows, all GBP: 516 orders and 5,882.82 total order value. September 22 had the highest value, GBP 1,032.29. |
| Marketplace fee query | Passed | September returned GBP 4,196.57 and EUR 7.57. Transaction Fees is an alias for the same amount and is not added again. |
| Full conversational review cases | Not run | Direct queries do not prove fresh-chat routing, date interpretation, calculations, user-visible answers, or handling of negative prompts. |
| Portal scan and reviewer sign-in | Not run | These must be verified against the saved submission. |

The live discovery tool returned 76 metrics and 68 breakdowns. The listing was
corrected to remove unsupported listing-view and category/marketplace breakdown
claims. The two bundled skills distinguish historical orders from current
listing/inventory/seller-standard snapshots and avoid mixing currencies.

The five relevant local tool descriptors contain explicit boolean readOnlyHint,
destructiveHint, openWorldHint and idempotentHint values. Discovery reads the
field catalog; reporting tools can create jobs and usage records; list_workspace
can clear stale selection state; the app-only mode tool changes a preference.
These internal effects do not make eBay listing edits or refunds available.
No hosted tool code was changed, and local annotations are not a portal scan.

## Demo and publication details

Demo: https://youtu.be/YEeZe5IBLGA

Anonymous YouTube checks returned Adzviser eBay ChatGPT Plugin Demo by Adzviser,
player status OK, non-private status and a 185-second duration. The recording's
visual quality, case coverage and absence of exposed secrets were not independently
reviewed in video playback.

The package reuses the supplied 256 x 256 Adzviser PNG. The website, support form,
privacy notice and terms were fetched and their publisher content inspected.
All supported countries and subscriptions purchased separately on the Adzviser
website carry forward the publisher's previous instructions. Release notes are
written for plugin users. The original download remains in Downloads.
## Upload and verification

Start from the Plugins list and choose Upload new or existing plugin. Upload
adzviser-ebay-new-plugin-1.0.0.zip with the verified Adzviser developer identity.
This package is for a new entry: do not upload it as a new version of the original
app-6aa610f6b3c8819181fffd9c236538ed entry, whose package name must stay unchanged.

Verify the imported package name is adzviser-ebay and its version is 1.0.0. Check
the listing, review cases and demo URL. In MCPs, select ebay and check the endpoint
above, then use Connect to complete domain verification and OAuth authorization.
Wait for tool discovery and review its findings. Keep the original entry until
the new connection is confirmed to work. This local package has not been uploaded.

Provide reviewer credentials only in the portal's secure fields. The reviewer
account needs access to eBay Demo and its connected eBay account. Run the saved
submission's conversational cases and reviewer sign-in before submitting for
review; the direct query evidence above does not replace those checks.
