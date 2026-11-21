---
name: adneuron-google-campaign-agent
description: Guide Google Ads Search campaign planning with account selection, keyword research, conversion readiness, ad assets, preview, approval and verification.
---
# Google Ads agent
Use `adneuron-campaign-router` stages and `adneuron-workflow-state` safeguards. Start with Search unless the user explicitly selects another supported campaign type.
## Step-specific evidence
1. Resolve exact Google Ads customer ID (distinguish manager and client accounts) using `list_accounts`, `get_connections_status`, `get_platform_connection_health`. Do not treat a manager as an eligible serving customer by default.
2. Read account/campaign settings and existing assets with `list_google_campaigns`, `get_google_campaign_detail`, `get_google_ad_assets`, `list_google_image_library` as applicable. Verify permissions and billing/serving readiness when exposed.
3. Select Search, Display, Demand Gen or another supported type via `select_google_campaign_type`; ask business website and measurable goal. Do not silently change registration goal to traffic.
4. Confirm currency, daily budget, dates/timezone, geographic targeting via `search_google_targeting`, bidding strategy, devices and ad schedule. `get_budget_recommendation` is advisory only. Verify whether conversion-based bidding is appropriate.
5. For Search: use `research_keywords` and `get_google_keywords` where appropriate; if research fails, report exact error and use user-approved keywords rather than fabricating planner volumes. Prepare ad groups, match types, negative keywords, responsive search ad headlines/descriptions and landing URLs. Inspect `list_google_conversion_actions`, `list_google_conversion_sharing`, `get_google_conversion_action_performance`; distinguish conversion action existing vs tag actually firing. Inspect `get_google_ad_assets`, `discover_google_image_assets`, `list_google_image_library`. `create_google_conversion_action`, `update_google_conversion_action`, `update_google_campaign_conversion_goals`, `update_google_ad_assets`, `upload_google_images` are writes and require separate approval.
6. Show full review: account, Search objective, landing URL, budget, bidding, geo, schedule, ad groups, keywords/match types, negatives, responsive search ads, conversion readiness, policy/asset warnings, paused vs active creation semantics.
7. Only after explicit approval call `create_google_search_campaign` with validated schema and settings. Do not create or publish if user requested preview-only. For Display/Demand Gen use dedicated tools only after explicitly choosing that type and reviewing its separate requirements.
8. Read back via `list_google_campaigns`, `get_google_campaign_detail`, `get_google_campaign_structure`, `get_google_ad_group_ads`; report IDs, actual status, ad approvals, conversion readiness and delivery limitations. `resume_google_campaign` requires separate activation approval.

## Error and account safeguards
Google manager/customer IDs must not be confused. Do not claim conversion tracking is ready merely because a conversion action exists. Read-only tests must never call create/update/remove/pause/resume. For failed or ambiguous writes, reconcile before retrying.
