# Meta Ads 2.0.0 submission preparation

Updated November 20, 2026. The existing package identity
`app-6aa067ab20f0819198ab28be70e46556`, display name, subtitle, starter
prompts, icon, listing URLs, countries and demo URL are preserved. Version
`2.0.0` adds account-management instructions and a plain-text About description.
The original `1.0.0` ZIP remains unchanged.

The existing MCP connection remains `meta-ads` at
https://meta-ads.mcp.adzviser.com/widgets/http. Management discovery uses
`source=fb_ads`; reporting uses `assorted_requests.fb_ads_request`.
No server implementation, deployment, account permission, advertising resource,
cloud plugin or submission was changed while preparing this ZIP.

## Changes in this package

- Add `adzviser-account-management` with instructions for `get_resources`,
  `preview_changes`, `apply_changes`, `get_change_result`,
  `get_data_source_access` and `set_data_source_access`.
- Describe actual Meta actions: rename or pause existing eligible campaigns and
  ad sets. Pausing a campaign also stops delivery for its ad sets and ads;
  pausing an ad set stops delivery for its ads. Budget and bid changes,
  resuming, targeting and ad copy edits, creation and deletion are unavailable.
- Require an exact saved preview and confirmation before applying an account
  edit or connection-permission change. Preserve advertiser and parent campaign
  identity, display grouped permission scope, and inspect existing receipts
  after uncertain outcomes instead of creating duplicate mutations.
- Explain Meta's separate `ads_management` grant and the reconnection workflow
  when that grant is missing. A capabilities overview or Adzviser write-access
  setting does not prove current Meta permission. Previews validate the requested
  edit with Meta without applying it.
- Update the reporting skills to route account-management requests to the new
  skill and distinguish report previews from account-change previews.
- Preserve the five reporting cases and add four management cases. Retain
  negative cases for budget changes, public competitor Ad Library searches,
  and individual audience identities; revise the budget explanation to reflect
  the newly available rename and pause actions.

## Review cases

The five original Data Mode cases and their expected behavior are preserved:
monthly spend, campaign spend and website purchases, publisher platform
performance, month comparison and daily trends. They use Demo and resolve
relative dates at review time in the advertising account's reporting timezone.
Keep Account Currency and exact conversion-event definitions; missing rows do
not prove zero activity. Historical observations below are not expected answers.

The four added management cases are:

1. Discover capabilities, advertiser identities and connection write access
   without preparing or applying anything. Include a Read-only connection when
   available and distinguish its access state from Meta's provider grant.
2. Preview renaming a dedicated paused campaign from `Adzviser Review Original`
   to `Adzviser Review Renamed`, without applying it.
3. Continue the same conversation, confirm that exact preview, apply it and
   inspect its receipt. Keep the campaign paused and unrelated settings intact.
4. Prepare changing a dedicated connection from Read and write to Read-only,
   showing every affected advertiser, without applying the permission change.

The management fixture has not been created or verified during this update.
Before rehearsing cases 2–4, select a dedicated test advertiser with owner OAuth
access, Meta editing permission, `ads_management` granted and Adzviser writing
enabled. Resolve ambiguous advertisers or connections before previewing. If the
fixture is absent, report the setup gap instead of selecting a production
campaign. Restore the original name only through a separately previewed and
confirmed change. Merely preparing the permission case must leave access intact.

For an ad set edit outside these example cases, inspect its parent campaign:
both must have an eligible active or paused status. Do not substitute an
individual ad for an ad set. A missing `ads_management` grant requires Facebook
Ads reconnection with Read and write and account selection; do not repeat failed
requests to bypass it or treat reconnection as approval of an advertising edit.

The new management and negative conversations have not been executed in ChatGPT.
The exact prompts, tools and expected behavior are in the manifest review fields.

## Current verification

On November 20, 2026, the public Meta Ads health endpoint returned
`status=running`, build `2da50fcc-20261120001812`. Its reporting and ChatGPT UI
tool inventories both advertise all six management tools. This public response
does not prove authenticated MCP tool listing, reviewer login, write access or
successful provider execution.

The two focused Meta Ads connector test suites passed: 63 tests passed;
3,152 tests for other connectors or unmatched cases were skipped. These checks
exercise connector registration and UI wiring, not live Meta Ads writes.
Package validation checks the manifest, skill frontmatter and MCP dependencies,
all six tool references, retained identity and assets, review metadata and the
contents of the final ZIP.

## Historical reporting verification — October 7, 2026

Prior preparation recorded five successful direct Data Mode queries through the
authenticated Meta Ads development connection using Demo. All returned
`isError=false`, `reportingMode=data` and `directData=true`. No reporting widget
was used. These observations are historical evidence, not fresh checks or
hardcoded expected answers.

| Case | Recorded evidence |
| --- | --- |
| Monthly spend | September 1–30: GBP 130,100.21. |
| Campaign spend and website purchases | Seven campaigns; GBP 130,100.21 and 5,364 attributed website purchases. Spend reconciled to the monthly total. |
| Publisher platform performance | Audience Network, Facebook, Instagram and Threads with spend, impressions and link clicks. Spend reconciled before display rounding. |
| Month comparison | September GBP 130,100.21 versus August GBP 114,033.71; increase GBP 16,066.50, approximately 14.09%. |
| Daily trends | September 28–October 4: all seven days returned; GBP 24,849.22 and 22,850 link clicks. |

Discovery used Demo and returned the requested labels. Reporting used
`FacebookAds.data` tables; an empty-string table key was valid, and the platform
report used `PublisherPlatform`. Currency was returned as GBP, not assumed USD.
Fresh conversations through the saved submission and reviewer login were not
verified in that preparation and have not been verified during this update.

## Demo and remaining portal checks

The existing demo is https://youtu.be/uV_317ApGyQ. Prior preparation recorded
anonymous YouTube metadata for “Adzviser Meta Ads ChatGPT Plugin Demo” by
Adzviser, 186 seconds long, non-private, with player status OK. Actual playback,
legibility, full coverage and absence of secrets were not independently inspected.
The video has not been rechecked for this release; coverage of account-change
preview, confirmation, application and receipts is unverified.

Upload the ZIP to the existing Meta Ads entry and inspect the imported About
text, three skills, nine positive and three negative cases, and refreshed MCP
tools. Keep reviewer credentials and exact sign-in instructions in secure
dashboard fields, outside this package. Verify a fresh reviewer login, the test
fixture and the review conversations through the saved submitted version before
completing portal attestations.

Prior preparation recorded an existing-entry upload restriction on a separate
Google Ads entry: “Keep the existing MCP connection” and “Publish the existing
MCP app before updating its plugin ZIP.” Whether that restriction applies to
this Meta Ads entry remains unverified. Preserve this entry's identity and
endpoint; inspect any actual upload error before changing them. No particular
Meta Ads rejection finding was supplied or claimed to be resolved. A valid ZIP
does not establish portal acceptance, reviewer access or approval.
