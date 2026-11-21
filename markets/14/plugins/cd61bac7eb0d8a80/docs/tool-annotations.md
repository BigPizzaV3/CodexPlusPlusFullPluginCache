# Zoho CRM tool annotations

These values describe the corrected local MCP source. Deploy and rescan before
expecting the portal to see them. This document explains the flags; it does not
set them or replace any required portal justification fields.

| Tool | readOnlyHint | destructiveHint | idempotentHint | openWorldHint |
| --- | --- | --- | --- | --- |
| list_metrics_and_breakdowns_zoho | true | false | true | false |
| retrieve_reporting_data | false | false | false | false |
| preview_and_retrieve_reporting_data | false | false | false | false |
| list_workspace | false | false | true | false |
| set_reporting_mode | false | false | true | false |

- **Catalog discovery:** reads predefined Zoho CRM field definitions without
  changing user or provider state. It deletes nothing, repeating it has no
  additional effect, and it does not access open-ended entities.
- **Reporting:** retrieves data only from authorized CRM accounts in the selected
  workspace. It records usage, so it is not strictly read-only and repeated calls
  can add usage records. It does not create, edit or delete CRM records. Scope is
  a bounded private account even though Zoho hosts the data externally.
- **Preview reporting:** prepares an interactive report; supported compatibility
  paths can run reporting and save a presentation preference. These potential
  effects make it non-read-only and non-idempotent. It does not destructively
  change CRM data and stays within authorized account data.
- **Workspace discovery:** lists authorized workspaces and can clear stale
  account preferences, so readOnlyHint is false. Repeating this normalization
  has no additional effect. It does not delete workspaces, connected accounts
  or CRM records, or enumerate other users' private workspaces.
- **Reporting mode:** saves a presentation preference. It is not read-only;
  setting the same preference repeatedly is idempotent. It neither destroys
  source data nor accesses open-ended entities. It is app-only and must not be
  invoked by the model in Data Mode cases.

[OpenAI's review guidance](https://developers.openai.com/plugins/deploy/app-review#review-and-approval-faqs)
distinguishes bounded private-account tools from public-internet or open-ended
tools. External hosting alone does not justify openWorldHint=true. Keep all
hints explicitly boolean and compare them with the actual scanned definition.
