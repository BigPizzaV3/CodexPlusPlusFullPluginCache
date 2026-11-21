# Google Ads: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `account_snapshot` | own tool | Wants one overview of a single ad account on Google Ads, Meta Ads, TikTok Ads, LinkedIn Ads, Microsoft Advertising or ChatGPT Ads: every campaign with its dates, lifetime and recent performance, and account totals. |
| `ad_library_competitor_ads` | google_ads_read | Wants to see the live ads a competitor brand or domain runs, from the public Google, Meta or LinkedIn ad library. |
| `get_report` | own tool | Wants performance metrics (spend, clicks, impressions, conversions and more) from a connected platform: Google Ads, Meta Ads, TikTok Ads, LinkedIn Ads, Microsoft Advertising, ChatGPT Ads, Google Analytics 4, Search Console, YouTube or Business Profile, optionally split by level or dimension. |
| `google_ads_account_audit` | google_ads_read | Wants a quick Google Ads hygiene check that finds wasteful keywords and keywords with a low Quality Score. |
| `google_ads_budget_pacing_alerts` | google_ads_read | Asks whether Google Ads campaigns will overspend or underspend their budget this month. |
| `google_ads_conversion_tracking_health` | google_ads_read | Asks whether Google Ads conversion tracking works: paused, removed or silent conversion actions. |
| `google_ads_extension_asset_performance` | google_ads_read | Asks how Google Ads sitelinks, callouts, call assets, images and other extensions perform. |
| `google_ads_geo_target_search` | google_ads_read | Needs Google Ads location IDs for a city, region, district or country before targeting it. |
| `google_ads_get_ad_details` | google_ads_read | Wants the full copy, URLs, status and ad strength of Google Ads ads. |
| `google_ads_get_ad_schedule` | google_ads_read | Asks on which days and hours a Google Ads campaign is allowed to serve. |
| `google_ads_get_campaign_targeting` | google_ads_read | Asks which locations, radius, languages, devices and audiences a Google Ads campaign targets or excludes. |
| `google_ads_get_change_history` | google_ads_read | Asks who changed what in a Google Ads account in the last 30 days. |
| `google_ads_get_conversion_settings` | google_ads_read | Asks how Google Ads conversion actions count and value conversions: counting type, lookback windows, attribution model and default value. |
| `google_ads_get_conversion_tags` | google_ads_read | Needs the Google Ads conversion ID and label (send_to value) to install a conversion tag or set it up in Tag Manager. |
| `google_ads_get_pmax_assets` | google_ads_read | Wants to see a Google Ads Performance Max asset group's headlines, images, videos, audience signal and search themes. |
| `google_ads_get_shared_negative_list` | google_ads_read | Wants the keywords inside one Google Ads shared negative keyword list. |
| `google_ads_impression_share_analysis` | google_ads_read | Asks how much impression share Google Ads Search campaigns or ad groups get and how much is lost to budget or rank. |
| `google_ads_keyword_historical_metrics` | google_ads_read | Wants month-by-month Google search volume and competition for keywords they already have. |
| `google_ads_keyword_opportunities` | google_ads_read | Wants keyword opportunities from their own Google Ads data: converting search terms to add as keywords and keywords that spend without converting. |
| `google_ads_keyword_planner` | google_ads_read | Wants new keyword ideas with average monthly searches and competition from Google Keyword Planner. |
| `google_ads_keyword_quality_report` | google_ads_read | Asks when and why a Google Ads keyword's Quality Score changed over time. |
| `google_ads_keyword_report` | google_ads_read | Wants Google Ads keyword performance with Quality Score and its three components. |
| `google_ads_list_ad_extensions` | google_ads_read | Wants the sitelinks, callouts, structured snippets, call, promotion and price extensions attached to Google Ads campaigns. |
| `google_ads_list_ad_policy_issues` | google_ads_read | Asks which Google Ads ads are disapproved or limited, and why. |
| `google_ads_list_assets` | google_ads_read | Wants the whole Google Ads asset library: sitelinks, callouts, images, lead forms, text assets and more across the account. |
| `google_ads_list_audiences` | google_ads_read | Wants the Google Ads audience lists (remarketing, customer match, lookalike) with their sizes. |
| `google_ads_list_conversion_actions` | google_ads_read | Wants the Google Ads conversion actions with their category, status and whether each counts in the Conversions column. |
| `google_ads_list_conversion_goals` | google_ads_read | Asks which Google Ads conversion goal categories are primary and drive Smart Bidding. |
| `google_ads_list_custom_conversion_goals` | google_ads_read | Wants the Google Ads custom conversion goals, the actions inside each and the campaigns that use them. |
| `google_ads_list_extension_assets` | google_ads_read | Wants the extension assets currently linked to one Google Ads campaign, with their IDs. |
| `google_ads_list_ip_exclusions` | google_ads_read | Wants the IP addresses excluded on Google Ads campaigns. |
| `google_ads_list_lead_form_submissions` | google_ads_read | Wants the leads submitted through Google Ads lead forms. |
| `google_ads_list_negative_keywords` | google_ads_read | Wants the negative keywords that apply to a Google Ads account at campaign, ad group and shared-list level. |
| `google_ads_list_recommendations` | google_ads_read | Wants Google's recommendations and optimization score for a Google Ads account, with their projected impact. |
| `google_ads_list_shared_negative_lists` | google_ads_read | Wants the shared negative keyword lists of a Google Ads account. |
| `google_ads_negative_keyword_suggestions` | google_ads_read | Wants ranked suggestions of Google Ads search terms that spend money without converting, as negative keyword candidates. |
| `google_ads_performance_report` | google_ads_read | Wants Google Ads cost, clicks, impressions and conversions at campaign, ad group, ad or keyword level. |
| `google_ads_query` | google_ads_read | Needs Google Ads data that no dedicated report returns, through a read-only GAQL SELECT query. |
| `google_ads_rsa_asset_performance` | google_ads_read | Asks which Google Ads responsive search ad headlines and descriptions perform best. |
| `google_ads_search_terms_report` | google_ads_read | Wants the actual searches that triggered their Google Ads ads, with cost and conversions, for example to find wasted spend. |
| `list_entities` | own tool | Wants the campaigns, ad groups or ad sets, ads or keywords of one connected ad platform with their IDs, status and dates. |
| `list_google_ads_experiments` | google_ads_read | Wants to see Google Ads campaign experiments and their status. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `click_fraud_setup` | google_ads_create | Wants to start click-fraud tracking on their website and needs the tracking tag. |
| `connect_google_ads` | google_ads_create | Wants to connect a Google Ads account to Opus Growth. |
| `create_public_image_url` | google_ads_create | Another tool needs a public image URL and the image is on the web, can be dropped through an upload link, or is a small image already in the conversation. |
| `google_ads_add_keywords` | google_ads_create | Wants to add positive keywords to a Google Ads search ad group. |
| `google_ads_add_negative_keywords` | google_ads_create | Wants to block searches by adding negative keywords to a Google Ads campaign or ad group, one or many at once. |
| `google_ads_add_pmax_images` | google_ads_create | Wants to attach uploaded images or logos to a Google Ads Performance Max asset group. |
| `google_ads_copy_ad_group` | google_ads_create | Wants to duplicate Google Ads ad groups, with their keywords and ads, into the same or another campaign. |
| `google_ads_create_ad_group` | google_ads_create | Wants to add a new ad group to an existing Google Ads campaign. |
| `google_ads_create_app_campaign` | google_ads_create | Wants a Google Ads App campaign that promotes a mobile app; it is created paused. |
| `google_ads_create_customer_match_audience` | google_ads_create | Wants an empty Google Ads Customer Match list to fill later with customer emails or phone numbers. |
| `google_ads_create_demand_gen_ad` | google_ads_create | Wants to add a video or image ad to a Google Ads Demand Gen ad group. |
| `google_ads_create_demand_gen_campaign` | google_ads_create | Wants a new Google Ads Demand Gen campaign with its daily budget; it is created paused. |
| `google_ads_create_display_campaign` | google_ads_create | Wants a new Google Display Network campaign, for example remarketing to site visitors; it is created paused. |
| `google_ads_create_lead_form` | google_ads_create | Wants a Google Ads lead form that collects contact details inside the ad, optionally attached to a campaign or ad group and optionally sending each lead to the user's own webhook. |
| `google_ads_create_lookalike_audience` | google_ads_create | Wants a Google Ads lookalike audience built from existing seed lists. |
| `google_ads_create_pmax_campaign` | google_ads_create | Wants a new Google Ads Performance Max campaign with its budget, asset group and assets; it is created paused. |
| `google_ads_create_responsive_display_ad` | google_ads_create | Wants a responsive display ad in a Google Ads display ad group. |
| `google_ads_create_responsive_search_ad` | google_ads_create | Wants a new responsive search ad (headlines and descriptions) in a Google Ads ad group. |
| `google_ads_create_search_campaign` | google_ads_create | Wants a new Google Ads Search campaign with its daily budget; it is created paused. |
| `google_ads_create_website_audience` | google_ads_create | Wants a Google Ads remarketing audience of people who visited specific website pages. |
| `google_ads_upload_image_asset` | google_ads_create | Wants to upload an image to the Google Ads asset library for Performance Max, display ads or image extensions. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `click_fraud_scan` | google_ads_edit | Asks whether their Google Ads clicks include click fraud, or wants to look up a suspicious click by GCLID, IP or time; it needs the tracking tag from click_fraud_setup. It does not block anything, and as part of data retention it deletes captured clicks older than 90 days. |
| `create_google_ads_account` | google_ads_edit | An agency user wants to open a new Google Ads client account under their manager (MCC) account. |
| `google_ads_add_extension_assets` | google_ads_edit | Wants to add sitelinks, callouts, structured snippets, call, promotion, price or similar extensions to a Google Ads campaign or ad group. |
| `google_ads_apply_recommendation` | google_ads_edit | Wants to apply or dismiss specific Google Ads recommendations listed by google_ads_list_recommendations. |
| `google_ads_block_ip_addresses` | google_ads_edit | Wants to exclude specific IP addresses from a Google Ads campaign, for example suspicious clicks found by click_fraud_scan. |
| `google_ads_create_conversion_action` | google_ads_edit | Wants to create a new Google Ads conversion action, such as a website, call or import conversion. |
| `google_ads_dismiss_recommendations` | google_ads_edit | Wants to dismiss Google Ads recommendations without applying them. |
| `google_ads_manage_audience_targeting` | google_ads_edit | Wants to attach, exclude or remove an audience list on a Google Ads campaign or ad group. |
| `google_ads_manage_campaign_settings` | google_ads_edit | Wants to change Google Ads campaign settings such as networks, location targeting type, tracking template, the EU political ads declaration or AI Max for Search. |
| `google_ads_manage_device_targeting` | google_ads_edit | Wants to raise, lower or exclude mobile, desktop or tablet bids on a Google Ads campaign. |
| `google_ads_manage_experiment` | google_ads_edit | Wants to create a Google Ads campaign experiment, change its treatment's landing page or ad text, schedule it, or read its status and results. |
| `google_ads_manage_keywords` | google_ads_edit | Wants to pause, enable, remove or re-bid existing Google Ads keywords, or give a keyword its own landing page; removing an ad group's negative keyword also works here (action=remove). |
| `google_ads_manage_portfolio_bid_strategy` | google_ads_edit | Wants to create, update, list or assign shared portfolio bid strategies in Google Ads. |
| `google_ads_manage_radius_targeting` | google_ads_edit | Wants to add or remove radius targeting around an address or coordinates on a Google Ads campaign. |
| `google_ads_manage_recommendation_auto_apply` | google_ads_edit | Wants to see or turn off the recommendation types Google Ads applies automatically. |
| `google_ads_manage_shared_negative_list` | google_ads_edit | Wants to create or rename a Google Ads shared negative keyword list, add or remove its keywords, or attach it to or detach it from a campaign. |
| `google_ads_pause_campaign` | google_ads_edit | Wants to pause one Google Ads campaign. |
| `google_ads_remove_extension_assets` | google_ads_edit | Wants to unlink sitelinks, callouts or other extensions from a Google Ads campaign or ad group. |
| `google_ads_remove_negative_keywords` | google_ads_edit | Wants to remove campaign-level negative keywords from a Google Ads campaign. |
| `google_ads_set_ad_group_targeting` | google_ads_edit | Wants to set locations and languages on a Google Ads Demand Gen ad group. |
| `google_ads_set_ad_schedule` | google_ads_edit | Wants to set the days and hours a Google Ads campaign serves, with optional hourly bid adjustments. |
| `google_ads_set_bid_strategy` | google_ads_edit | Wants to change a Google Ads campaign's bid strategy or its target CPA or ROAS. |
| `google_ads_set_business_logo` | google_ads_edit | Wants to replace the business logo shown in a Google Ads campaign's ads. |
| `google_ads_set_business_name` | google_ads_edit | Wants to correct the business name shown in a Google Ads campaign's ads. |
| `google_ads_set_call_reporting` | google_ads_edit | Wants to turn Google Ads account-level call reporting on or off so that calls from ads can be tracked. |
| `google_ads_set_campaign_budget` | google_ads_edit | Wants to change a Google Ads campaign's daily budget. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `google_ads_set_campaign_targeting` | google_ads_edit | Wants to set the locations and languages a Google Ads campaign targets. |
| `google_ads_set_conversion_settings` | google_ads_edit | Wants to change a Google Ads conversion action's value, counting or lookback window. |
| `google_ads_unblock_ip_addresses` | google_ads_edit | Wants to remove IP exclusions from a Google Ads campaign. |
| `google_ads_update_ad_group` | google_ads_edit | Wants to rename a Google Ads ad group or change its default max CPC bid. |
| `google_ads_update_ad_group_status` | google_ads_edit | Wants to enable, pause or remove a Google Ads ad group. |
| `google_ads_update_ad_status` | google_ads_edit | Wants to enable, pause or remove a single Google Ads ad. |
| `google_ads_update_campaign` | google_ads_edit | Wants to rename a Google Ads campaign, change its status, or remove (delete) it. |
| `google_ads_update_campaign_status` | google_ads_edit | Wants to enable (resume) or pause a Google Ads campaign. |
| `google_ads_update_conversion_action` | google_ads_edit | Wants to make a Google Ads conversion action primary or secondary. |
| `google_ads_update_conversion_goal` | google_ads_edit | Wants to make a Google Ads conversion category primary or secondary for bidding in a goal-based account. |
| `google_ads_update_custom_conversion_goal` | google_ads_edit | Wants to edit, rename or delete a Google Ads custom conversion goal. |
| `google_ads_update_pmax_asset_group` | google_ads_edit | Wants to change or remove a Google Ads Performance Max asset group itself: landing page, name, status or display paths. |
| `google_ads_update_pmax_assets` | google_ads_edit | Wants to add or remove text assets in an existing Google Ads Performance Max asset group. |
| `google_ads_update_responsive_search_ad` | google_ads_edit | Wants to edit the headlines or descriptions of an existing Google Ads responsive search ad. |
| `google_ads_update_sitelink` | google_ads_edit | Wants to edit an existing Google Ads sitelink's text, descriptions or URL. |
| `google_ads_upload_conversion_adjustments` | google_ads_edit | Wants to retract or restate Google Ads conversions already reported, for example after a refund. |
| `google_ads_upload_offline_conversions` | google_ads_edit | Wants to send sales or qualified leads from their CRM to Google Ads as offline conversions. |
| `select_ad_account` | google_ads_edit | Asks to authorize another ad account of an already connected Google Ads, Meta, LinkedIn, TikTok or Microsoft login, typically after a tool returned account_not_authorized. |
