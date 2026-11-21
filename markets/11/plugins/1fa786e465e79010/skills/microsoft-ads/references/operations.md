# Microsoft Advertising: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `list_microsoft_accounts` | microsoft_ads_read | Wants their connected Microsoft Advertising accounts. |
| `list_microsoft_ad_extensions` | microsoft_ads_read | Wants the sitelink, callout and structured snippet extensions of Microsoft Advertising campaigns. |
| `list_microsoft_ad_groups` | microsoft_ads_read | Wants the ad groups of a Microsoft Advertising campaign. |
| `list_microsoft_ads` | microsoft_ads_read | Wants the ads of a Microsoft Advertising ad group with their full copy. |
| `list_microsoft_audiences` | microsoft_ads_read | Wants the Microsoft Advertising audiences. |
| `list_microsoft_campaigns` | microsoft_ads_read | Wants the campaigns of a Microsoft Advertising account. |
| `list_microsoft_conversion_goals` | microsoft_ads_read | Wants the Microsoft Advertising conversion goals, for example to check Microsoft conversion tracking. |
| `list_microsoft_keywords` | microsoft_ads_read | Wants the keywords of a Microsoft Advertising ad group. |
| `list_microsoft_negative_keywords` | microsoft_ads_read | Wants the negative keywords on a Microsoft Advertising campaign or ad group. |
| `list_microsoft_uet_tags` | microsoft_ads_read | Wants the Microsoft UET tags and their status, for example to check Microsoft conversion tracking. |
| `microsoft_change_history` | microsoft_ads_read | Wants who changed a Microsoft Advertising account and the old and new values. A change can take about an hour to appear. |
| `microsoft_entity_performance_report` | microsoft_ads_read | Wants Microsoft Advertising performance below campaign level: ad groups, ads or keywords. |
| `microsoft_location_search` | microsoft_ads_read | Needs Microsoft Advertising location IDs by name. |
| `microsoft_performance_report` | microsoft_ads_read | Wants Microsoft Advertising campaign performance. |
| `microsoft_report_query` | microsoft_ads_read | Needs a Microsoft Advertising report type or columns the standard reports do not cover. |
| `microsoft_search_terms_report` | microsoft_ads_read | Wants the searches that triggered Microsoft Advertising ads, for example to find negatives. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `add_microsoft_ad_extensions` | microsoft_ads_create | Wants to add sitelink, callout or structured snippet extensions to a Microsoft Advertising campaign. |
| `add_microsoft_ad_schedule` | microsoft_ads_create | Wants to set the days and hours a Microsoft Advertising campaign serves. |
| `add_microsoft_demographic_target` | microsoft_ads_create | Wants an age or gender bid adjustment in Microsoft Advertising. |
| `add_microsoft_device_target` | microsoft_ads_create | Wants device bid adjustments on a Microsoft Advertising campaign. |
| `add_microsoft_keywords` | microsoft_ads_create | Wants to add keywords to a Microsoft Advertising ad group. |
| `add_microsoft_location_target` | microsoft_ads_create | Wants to add a location target to a Microsoft Advertising campaign. |
| `add_microsoft_negative_keywords` | microsoft_ads_create | Wants to add negative keywords to a Microsoft Advertising campaign or ad group. |
| `connect_microsoft_ads` | microsoft_ads_create | Wants to connect a Microsoft Advertising (Bing Ads) account. |
| `create_microsoft_ad_group` | microsoft_ads_create | Wants a new ad group in a Microsoft Advertising campaign; it is created paused. |
| `create_microsoft_campaign` | microsoft_ads_create | Wants a new Microsoft Advertising campaign; it is created paused. |
| `create_microsoft_conversion_goal` | microsoft_ads_create | Wants a URL-based Microsoft Advertising conversion goal on a UET tag. |
| `create_microsoft_remarketing_list` | microsoft_ads_create | Wants a Microsoft Advertising remarketing audience of visitors of a page. |
| `create_microsoft_responsive_search_ad` | microsoft_ads_create | Wants a new responsive search ad in a Microsoft Advertising ad group. |
| `create_microsoft_uet_tag` | microsoft_ads_create | Wants a new Microsoft UET tag for conversion tracking. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `delete_microsoft_audience` | microsoft_ads_edit | Wants to delete a Microsoft Advertising audience. |
| `delete_microsoft_campaign` | microsoft_ads_edit | Wants to permanently delete a Microsoft Advertising campaign. |
| `remove_microsoft_ad_extensions` | microsoft_ads_edit | Wants to remove or unlink Microsoft Advertising extensions. |
| `remove_microsoft_negative_keywords` | microsoft_ads_edit | Wants to remove negative keywords from a Microsoft Advertising campaign or ad group. |
| `set_microsoft_bid_strategy` | microsoft_ads_edit | Wants to change a Microsoft Advertising campaign's bid strategy. |
| `update_microsoft_ad_group` | microsoft_ads_edit | Wants to change a Microsoft Advertising ad group's settings, such as its bid, dates or network. |
| `update_microsoft_ad_group_status` | microsoft_ads_edit | Wants to activate or pause a Microsoft Advertising ad group. |
| `update_microsoft_ad_status` | microsoft_ads_edit | Wants to activate or pause a Microsoft Advertising ad. |
| `update_microsoft_campaign_budget` | microsoft_ads_edit | Wants to change a Microsoft Advertising campaign's daily budget. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_microsoft_campaign_status` | microsoft_ads_edit | Wants to activate or pause a Microsoft Advertising campaign. |
| `update_microsoft_keyword` | microsoft_ads_edit | Wants to change a Microsoft Advertising keyword's bid or status. |
| `update_microsoft_responsive_search_ad` | microsoft_ads_edit | Wants to edit the headlines or descriptions of a Microsoft Advertising responsive search ad. |
| `update_microsoft_sitelink` | microsoft_ads_edit | Wants to edit an existing Microsoft Advertising sitelink. |
| `upload_microsoft_offline_conversions` | microsoft_ads_edit | Wants to send offline sales or leads to Microsoft Advertising as conversions. |
