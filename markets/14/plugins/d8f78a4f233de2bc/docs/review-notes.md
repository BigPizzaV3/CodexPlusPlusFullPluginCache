# Microsoft Ads 2.0.0 submission preparation

Updated November 20, 2026. The existing package identity
`app-6aa3b20dd9fc8191ad1ea4f46e9e2808`, display name, subtitle, starter
prompts, icon, listing links, countries and demo URL are preserved. Both the
portable and compatibility manifests now use version `2.0.0` and matching
plain-text About descriptions. The original `1.0.0` ZIP is unchanged.

The existing MCP connection remains `microsoft-ads` at
https://microsoft-ads.mcp.adzviser.com/widgets/http. Management discovery uses
`source=bing_ads`; reporting uses `assorted_requests.bing_ads_request`.
No server implementation, deployment, account permission, campaign, cloud
plugin or submission was changed while preparing this ZIP.

## Changes in this package

- Add `adzviser-account-management` with instructions for `get_resources`,
  `preview_changes`, `apply_changes`, `get_change_result`,
  `get_data_source_access` and `set_data_source_access`.
- Describe actual Microsoft Ads actions: rename or pause existing eligible
  Search campaigns and set or adjust individual daily budgets. Do not claim
  campaign resuming, keyword edits, ad copy edits, bids, creation or deletion.
- Require an exact saved preview and confirmation before applying an account
  edit or connection-permission change. Keep account identities and grouped
  connection scope clear; inspect existing receipts after uncertain outcomes.
- Explain that previews validate locally against current settings. Microsoft
  validates updates when applied; a preview is not provider acceptance.
- Update the two reporting skills to hand account-management requests to the
  new skill and distinguish report previews from account-change previews.
- Retain the five historical reporting cases and add four management cases.
  Replace the obsolete budget/pause rejection cases with unsupported campaign
  resuming and keyword creation. Retain the individual-ad-clicker identity case.
- Retain website-only subscription information and explain that confirmed
  campaign budget changes can affect advertising spend.

## Review cases

The five reporting cases use the owner's Demo workspace, which contained
Adzviser LLC - Expert when verified on October 27, 2026. The owner selected that
workspace and confirmed that the campaigns were suspended. Keep the fixed
August 1–31, 2026 period and the July 1–31 comparison period; rolling dates can
exclude the historical activity. Answers must come from live returned rows,
not the historical observations below. All five original cases and prompts
are preserved verbatim in the review metadata.

The four added management cases are:

1. Discover capabilities, account identities and write access without preparing
   or applying a change. Include a Read-only connection when available.
2. Preview renaming a dedicated paused Search test campaign from
   `Adzviser Review Original` to `Adzviser Review Renamed`, without applying it.
3. Continue the same conversation, confirm that exact preview, apply it and
   inspect its receipt. Keep the campaign paused and its budget unchanged.
4. Prepare changing a dedicated connection from Read and write to Read-only,
   showing every affected advertiser, without applying the permission change.

The management fixture has not been created or verified during this update.
Before rehearsing cases 2–4, select a dedicated test advertiser with owner OAuth
access, provider editing permission and Adzviser writing enabled. The test
campaign must be a paused Search campaign outside an experiment or experiment
base campaign. Resolve ambiguous advertisers or connections before previewing.
If the fixture is absent, report the setup gap instead of selecting a production
campaign. Restore the original name only through a separately previewed and
confirmed change. Merely preparing the permission case must leave access intact.

The three negative conversations cover resuming campaigns, creating keywords
and identifying individual ad clickers. Do not invent unsupported actions or
substitute unsolicited reporting calls. The new management and negative
conversations have not been executed in ChatGPT.

## Current verification

On November 20, 2026, the public Microsoft Ads health endpoint returned
`status=running`, build `2da50fcc-20261120001812`. Its reporting and ChatGPT UI
tool inventories both advertise all six management tools. This public response
does not prove authenticated MCP tool listing, reviewer login, write access or
successful provider execution.

The two focused Microsoft Ads connector test suites passed: 63 tests passed;
3,152 tests for other connectors or unmatched cases were skipped. These checks
exercise connector registration and UI wiring, not live Microsoft Ads writes.
Package validation checks matching manifests, skill frontmatter and MCP
dependencies, all six tool references, retained identity and assets, review
metadata and the contents of the final ZIP.

## Historical reporting verification — October 27, 2026

The prior preparation recorded successful direct Data Mode execution of all
five fixed-period cases after the owner authorized replacing the expired Demo
Microsoft Ads connection. Workspace and metric discovery succeeded. These are
historical observations, not fresh checks or hardcoded expected answers.

| Case | Recorded evidence |
| --- | --- |
| Overall performance | August: USD 481.70 Cost, 54,462 Impressions, 697 Clicks. |
| Campaign performance | Four distinct campaign IDs and names; totals matched the overview. |
| Device performance | Computer, Smartphone and Tablet; totals matched the overview. |
| Period comparison | July: USD 863.50 Cost, 103,147 Impressions, 1,604 Clicks. |
| Daily performance | 22 unique August daily rows; totals matched the overview. |

Daily rows spanned August 3–31. One returned row was explicitly zero; nine
requested dates had no row. Disclose absent dates instead of manufacturing
zeros. A recent-period probe for September 26–October 25 returned no rows.
Historical availability and authorization still depend on the source service.

## Demo and remaining portal checks

The existing demo is https://youtu.be/_lt7XO4DzAU. Prior preparation recorded an
unlisted, non-private 196-second video with a successful reporting answer using
the same underlying account in the `bing ads new` workspace. Sampled beginning,
middle and final sections were inspected; uninterrupted full playback was not
verified. The video has not been rechecked for this release, and preview,
confirmation, application and receipt coverage for account edits is unverified.

Upload the ZIP to the existing Microsoft Ads entry and inspect the imported
About text, three skills, review cases and refreshed MCP tools. Keep reviewer
credentials and exact sign-in instructions in secure dashboard fields, outside
this package. Verify a fresh reviewer login, the test fixture and the review
conversations through the saved submitted version before completing portal
attestations. This update does not verify portal import, authenticated account
changes, reviewer access or approval.
