# Account, connections and support: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `describe` | google_ads_read | You need the report levels, breakdowns and entity types that get_report and list_entities accept for one platform. |
| `fetch` | own tool | You need the details (name, id, currency, status) of an account returned by search. |
| `get_connection_status` | own tool | You need to know which advertising, analytics and website services the user has connected, for example before choosing a platform. |
| `google_ads_instant_audit` | opus_growth_read | Wants a fast first audit of a Google Ads account: wasted spend on search terms without conversions, impression share lost to rank and conversion tracking problems. |
| `list_google_ads_accounts` | opus_growth_read | Wants their connected Google Ads accounts. |
| `opus_growth_issue_status` | google_ads_read | Asks whether a problem they reported to Opus Growth support has been resolved. |
| `opus_growth_plan_status` | opus_growth_read | Asks about their Opus Growth plan, remaining monthly quota or trial dates. |
| `search` | own tool | Wants to find one of their connected ad accounts by name or id. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `opus_growth_report_issue` | own tool | A tool failed unexpectedly or behaved wrongly and the user wants Opus Growth support to fix it. |
