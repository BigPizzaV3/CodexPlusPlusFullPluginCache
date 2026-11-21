# Google Ads 2.0.0 resubmission preparation

Prepared November 20, 2026 (America/Los_Angeles).

Package identity: `app-6aa067c6b00c819184fd02ecea043a21`, matching the
publisher's screenshot. Display name: Adzviser Google Ads. Version: 2.0.0.
The existing Codex package layout, Google Ads MCP key, registered hostname,
branding, subtitle, starter prompts, publisher and country targeting are retained.

Registered endpoint:
https://google-ads.mcp.adzviser.com/widgets/http

## What changed

The About description names concrete Google Ads tasks in plain paragraphs:
comparing performance, changing individual daily budgets, pausing or resuming
campaigns, renaming campaigns and ad groups, adding Search/negative keywords,
editing responsive Search ad text, adjusting Manual CPC bids, and changing
existing CPA/ROAS targets. It illustrates a 10% budget-reduction preview and
explains the settings/permission check, exact confirmation and result check.
There are no Markdown formatting markers or vague "supported changes" claims
in the listing text.

The package contains three skills:

- `adzviser-data-mode`: performance reporting, with an explicit handoff to
  management when the user requests an edit.
- `adzviser-preview-ui-mode`: interactive report previews, distinct from
  previews of account changes.
- `adzviser-account-management`: Google Ads capability discovery, resource and
  advertiser selection, saved previews, confirmation, execution, receipts and
  per-connection write access.

The management skill uses all six existing tools: `get_resources`,
`preview_changes`, `apply_changes`, `get_change_result`,
`get_data_source_access`, and `set_data_source_access`. Every packaged skill
uses the existing `google-ads` MCP dependency and registered endpoint.

Management instructions explicitly use `source=google_ads` for discovery.
The access tool accepts only a workspace and can return other providers;
match its results to discovered Google Ads connections before any permission
change. These are skill instructions, not a new claim that the shared backend
rejects every cross-provider management reference. No backend behavior or
annotations were changed in this package update.

## Review cases and prerequisites

The original five reporting cases remain. Four management cases were added:
capability/access discovery without mutations, a rename preview without apply,
confirmation and execution of that saved preview with receipt verification,
and a permission preview that stops before apply. All six tools occur in their
expected workflows. The obsolete negative budget-edit case is replaced by
unsupported billing; campaign deletion and public competitor searches remain
negative cases.

The existing Demo workspace and Google Ads reporting connection are used by
reporting cases. New rename cases require a dedicated test advertiser with
writing enabled and a paused campaign named `Adzviser Review Original`.
This is a proposed fixture, not a claim that it has been provisioned. If several
advertisers match, select the intended one before preparing a preview. After
an approved rename, restore the original name through a separate preview and
confirmation, keeping the campaign paused throughout.

The permission case requires a dedicated Google Ads connection currently set
to Read and write. Show all affected advertisers for grouped connections. It
prepares a switch to Read-only and does not authorize applying it. Credentials
belong only in secure portal fields, never the package.

The commerce description now acknowledges that supported budget, bidding and
enabled-status changes can affect future advertising spend. The existing
commerce declaration and website subscription arrangement are retained.

## Demo and verification

The existing Google Ads demo URL is retained:
https://youtu.be/VC3-yn69VeM

Its new account-management coverage is unverified. If updating the recording,
show capability discovery, a selected test account and paused campaign, the
exact rename preview, confirmation, apply result and receipt. Restore the
original name only after another preview and confirmation. Show the access
preview stopping before apply. A walkthrough script is not a completed demo.

| Check | Evidence and limit |
| --- | --- |
| Google Ads connector tests | Passed: 63 tests covering scoped reporting/tool catalogs and the Google Ads UI transport. External authentication/data are mocked; this is not live execution. |
| Skill structure | All three packaged skills passed frontmatter and naming validation. Tool references and dependency URLs were checked against the current schemas and package configuration. |
| Live public tool catalog | November 20: build `2da50fcc-20261120001812` lists all six management tools in both data and UI catalogs. A public status response is not an authenticated tools/list or execution test. |
| New management review cases | Not run against live accounts. Test fixtures, provider permission, owner OAuth and fresh-chat behavior remain unverified. |
| Previous reporting evidence | The 1.0.0 archive retains the October 7 direct-query results. Those historical results were not rerun and do not validate the new management workflows. |
| Listing and icon | The registered HTTPS links and original square PNG are retained. Previous preparation checked the listing pages; this update does not assert a new policy review. |
| Demo | Existing link retained; playback and coverage of the new workflows were not verified in this update. |
| Portal | No upload, authenticated scan, submission, publication or attestations performed. Earlier naming/affiliation concerns recorded in the 1.0.0 notes are not claimed resolved by this package. |

## Upload and check

Use `adzviser-google-ads-2.0.0.zip` for the existing plugin with the matching
package ID. Inspect the imported About text and all three skills, and scan the
registered Google Ads endpoint for all six management tools alongside reporting.
Run the saved version's cases with dedicated test fixtures and reviewer access.
The ZIP describes and guides the existing remote tools; it does not embed their
server implementation or make them available in an older installed catalog.
No server deployment was performed.
