# Spotify Ads tool annotations

These are the annotations in the corrected local MCP source. Deploy and rescan
before expecting the portal to see them. This document explains the values;
it does not set annotations or replace any required portal justification fields.

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_spotify_ads | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

- **Catalog discovery:** reads the predefined Spotify Ads field catalog without
  changing user or provider state. It does not delete anything, repeat calls
  have no additional effects, and it does not access open-ended entities.
- **Reporting:** retrieves data only from accounts authorized in the selected
  workspace. It records usage, so it is not strictly read-only and repeated
  calls can produce additional usage records. It does not create, edit or
  delete Spotify ads, campaigns, bids or budgets. Its scope is a bounded
  private account even though Spotify hosts the data externally.
- **Preview reporting:** prepares the interactive report; supported compatibility
  paths can run reporting and save a presentation preference. Those potential
  effects make it non-read-only and non-idempotent. It does not perform
  destructive advertiser actions and stays within authorized account data.
- **Workspace discovery:** lists authorized workspaces and can clear stale
  account preferences, so readOnlyHint is false. Repeating the normalization
  has no additional effect. It does not delete workspaces, accounts or source
  records, and does not enumerate other users' private workspaces.
- **Reporting mode:** saves a presentation preference. It is not read-only;
  setting the same preference repeatedly is idempotent. It neither destroys
  source data nor accesses open-ended external entities. It is app-only and
  must not be invoked by the model as part of Data Mode test cases.

[OpenAI's review guidance](https://developers.openai.com/plugins/deploy/app-review#review-and-approval-faqs)
distinguishes bounded private-account tools from tools that access the public
internet or open-ended external entities. An externally hosted private account
does not alone justify openWorldHint=true. Preserve explicit boolean values for
all hints and compare them with the actual scanned definitions before review.
