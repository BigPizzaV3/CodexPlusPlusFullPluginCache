# Amazon Ads submission preparation

Updated on 2026-10-08. All five positive reporting requests passed through the
authenticated Amazon Ads connection. The ZIP now uses the current workspace,
`Amazon Ads Demo`. Saved-plugin conversations and reviewer sign-in remain
unverified; successful direct requests do not establish full review readiness.

## Identity and connection

- Original package: `app-6aa067f0047481919ec3f768fee69f3c`
- Version: `1.0.0`
- Public name: `Adzviser Amazon Ads`
- MCP key: `amazon-ads`
- Confirmed registered URL: `https://amazon-ads.mcp.adzviser.com/widgets/http`
- The owner confirmed this is an unpublished/rejected entry. The owner has since
  replaced the underlying account and renamed the workspace to `Amazon Ads Demo`,
  containing the `Demo` Amazon Ads account. Live discovery confirms this workspace.
  Check that the secure reviewer-access instructions use the current workspace.

The supplied download had no MCP configuration file. Its two skill dependencies
pointed to the generic Adzviser endpoint. This package uses the confirmed Amazon
Ads endpoint in `mcp.json` and both skill dependencies, with source-specific
instructions. The original package ID, version, display name and listing description
are preserved. Starter prompts now explicitly end their reporting periods two
days before the current date, as requested. The original download remains in Downloads.

The root Agent Plugins manifest and the legacy `.codex-plugin/plugin.json`
overlay carry matching identity, listing and review metadata. The overlay points
to the same MCP configuration. Neither contains private app bindings. The ZIP's
single enclosing folder matches the original package ID.

## Review cases and actual results

The five positive cases use Data Mode only. Each recent reporting period ends
two calendar days before the current date in the user's timezone. Let that
current date be D: the seven-day range is [D-8, D-2], inclusive, and its preceding
comparison period is [D-15, D-9]. Recalculate these dates at review time.

For October 8, 2026 in America/Los_Angeles, the cutoff is October 6. The live
requests used September 30–October 6, with September 23–29 as the comparison
period. No request included October 7 or October 8. All five returned reporting
rows in Data Mode with no error or missing-coverage assumptions.

| Check | Result | Evidence |
| --- | --- | --- |
| Workspace discovery | Passed | The authenticated connection listed Amazon Ads Demo with a Demo Amazon Ads account. |
| Field discovery | Passed | Catalog returned Spend, Impressions, Clicks, Currency, Campaign ID and Campaign name. |
| Seven-day spend by currency | Passed | Spend with Currency returned USD 161.43 for September 30–October 6. |
| Seven-day impressions, clicks and calculated CTR | Passed | 53,910 impressions and 535 clicks; calculated CTR = 535 / 53,910 × 100 = 0.9924%. |
| Seven-day campaign spend | Passed | Seven distinct campaign IDs with names and USD spend. Their sum is USD 161.43, matching the overall result. |
| Two-period spend comparison | Passed | September 30–October 6: USD 161.43; September 23–29: USD 150.33. Increase: USD 11.10, or 7.38%. |
| Daily spend | Passed | Seven dates returned with time_granularity=Date; the daily sum is USD 161.43, matching the overall result. |
| Fresh-conversation positive routing | Not run | Direct tool requests exercise retrieval, not complete conversations through the saved plugin. |
| Three negative conversations | Not run | Drafted from supported capabilities: pausing campaigns, changing budgets and identifying individual clickers are unsupported. |
| Saved submission and reviewer login | Not run | A reviewer sign-in and saved-version scan were not performed here. Verify access to the renamed workspace using the reviewer's login. |

Daily spend returned: September 30 USD 23.13; October 1 USD 18.82; October 2
USD 23.83; October 3 USD 18.93; October 4 USD 30.38; October 5 USD 22.24;
October 6 USD 24.10. These numbers are evidence from this check, not fixed
expected answers for a future review. Recalculate dates and use the actual
returned rows when the reviewer runs the cases.

The former workspace's missing-report failures are not present in these checks
of the replacement account. This does not prove permanent cache availability or
that pending backend fixes have been deployed. If a future request reports data
still being prepared, treat that run as blocked rather than reporting zero
activity or a successful test.

After importing this ZIP, verify the five prompts through the saved submission
with the reviewer account. Also run the three negative conversations without
performing unsupported mutations. Credentials belong only in secure portal
fields, never in this package.

## Tool annotation reference

The local server definitions contain these explicit booleans:

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_amazon_ads | true | false | true | false |
| retrieve_reporting_data | false | false | false | true |
| preview_and_retrieve_reporting_data | false | false | false | true |
| list_workspace | false | false | true | true |
| set_reporting_mode | false | false | true | false |

Catalog discovery reads field definitions. Reporting records Adzviser usage;
reporting workflows can also involve upstream report jobs. Preview compatibility
paths can save preferences or retrieve reports and record usage. Workspace
resolution can clear a stale saved account preference. Reporting-mode selection
saves a presentation preference and is idempotent for the same mode. None of
these tools edits campaign bids, budgets or delivery.

The shared server retains its conservative open-world classification for
external account/service reporting. Access is limited to connected authorized
accounts. These are local source checks, not verified annotations from the
saved portal scan. Anonymous initialize and tools/list requests to the exact
endpoint returned OAuth 401 challenges as expected; authenticated descriptors
from the saved submission were not available. Notes cannot override annotations
or establish that reviewers will accept them.

## Demo and listing checks

Demo URL: https://youtu.be/QBKK6XeZPec

Anonymous YouTube metadata identified “Adzviser Amazon Ads ChatGPT Plugin Demo”
by Adzviser, with a duration of approximately 197 seconds, non-private status
and player status OK. An isolated browser played the recording without signing
in. The inspected early frame shows ChatGPT plugin setup. Later seek attempts
were buffering, so complete scenario coverage, legibility throughout and absence
of exposed secrets across the entire recording remain unverified.

The website, contact/support, privacy and terms URLs were fetched anonymously
and inspected for the correct Adzviser content. The supplied square 256-pixel
Adzviser PNG is included as both logo and composer icon. The package carries all
supported countries and website-only subscription commerce details, following
the owner's previous instructions. Release notes describe reporting benefits.

No new widget test cases were added. Existing explicit Preview UI functionality
is retained, but it was not exercised during these Data Mode checks.

## Portal handoff

Use the archive for the existing Amazon Ads entry; it preserves that entry's
package identity. Do not change the ID, create a duplicate entry or change the
registered endpoint to work around a migration warning. A valid ZIP cannot
complete OAuth, developer/domain verification, reviewer access, attestations or
tool scans. Verify imported metadata and the current scan after an accepted
upload. The direct reporting checks now pass; complete the remaining saved-plugin
conversation checks and reviewer-access verification before submitting.
