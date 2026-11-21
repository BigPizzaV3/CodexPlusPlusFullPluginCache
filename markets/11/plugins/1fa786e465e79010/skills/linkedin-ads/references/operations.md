# LinkedIn Ads: every operation

Generated from the tools' own descriptions. "Tool" is the platform tool that runs the operation on grouped connections (operation=<name>, params=<arguments>); on connections that list every operation as its own tool, call the operation name directly.

## Read (changes nothing)

| Operation | Tool | Use it when |
|---|---|---|
| `download_linkedin_leads` | linkedin_ads_read | Wants the leads from LinkedIn Lead Gen Forms. |
| `linkedin_ad_copy` | linkedin_ads_read | Wants the actual text of specific LinkedIn ads, for example to compare messaging. |
| `linkedin_audience_forecast` | linkedin_ads_read | Wants to know how many LinkedIn members a targeting setup reaches before creating a campaign. |
| `linkedin_bid_recommendations` | linkedin_ads_read | Wants LinkedIn's suggested bid and cost range for an audience. |
| `linkedin_campaign_analytics` | linkedin_ads_read | Wants LinkedIn Ads performance by campaign, creative, campaign group, account or member demographics. |
| `linkedin_targeting_search` | linkedin_ads_read | Needs LinkedIn targeting values (job titles, functions, industries, skills, companies, locations) by name. |
| `list_linkedin_ad_accounts` | linkedin_ads_read | Wants their connected LinkedIn ad accounts. |
| `list_linkedin_audiences` | linkedin_ads_read | Wants the matched audiences of a LinkedIn ad account. |
| `list_linkedin_campaign_groups` | linkedin_ads_read | Wants the LinkedIn campaign groups (called Campaigns in Campaign Manager). |
| `list_linkedin_campaigns` | linkedin_ads_read | Wants the LinkedIn API-level campaigns (called ad sets in Campaign Manager). |
| `list_linkedin_conversions` | linkedin_ads_read | Wants the conversion tracking rules of a LinkedIn ad account, for example to check LinkedIn conversion tracking. |
| `list_linkedin_creatives` | linkedin_ads_read | Wants the LinkedIn creatives (ads) of an account or campaign. |
| `list_linkedin_lead_forms` | linkedin_ads_read | Wants the LinkedIn Lead Gen Forms of an ad account. |

## Add (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `connect_linkedin_ads` | linkedin_ads_create | Wants to connect a LinkedIn ad account. |
| `create_linkedin_campaign` | linkedin_ads_create | Wants a new LinkedIn campaign (an ad set in Campaign Manager) with targeting and budget; it is created as a draft unless the user asks to launch it. |
| `create_linkedin_campaign_group` | linkedin_ads_create | Wants a new LinkedIn campaign group (called Campaign in Campaign Manager); it is created as a draft unless the user asks to launch it. |
| `create_linkedin_conversion` | linkedin_ads_create | Wants a new LinkedIn website conversion rule, based on a page URL or an Insight Tag event. |
| `create_linkedin_insight_tag` | linkedin_ads_create | Wants the LinkedIn Insight Tag for an ad account to track website conversions; if the account already has one, the existing tag and its code are returned. |
| `create_linkedin_post_ad` | linkedin_ads_create | Wants to sponsor an existing LinkedIn Company Page post. |
| `create_linkedin_text_ad` | linkedin_ads_create | Wants a LinkedIn text ad for a text ad campaign. |

## Change, pause or delete (preview, then confirm)

| Operation | Tool | Use it when |
|---|---|---|
| `attach_linkedin_conversion` | linkedin_ads_edit | Wants a LinkedIn campaign to report or optimize for an existing conversion rule. |
| `delete_linkedin_campaign` | linkedin_ads_edit | Wants to delete a LinkedIn campaign; a draft is deleted permanently, others are marked for deletion. |
| `delete_linkedin_campaign_group` | linkedin_ads_edit | Wants to delete a LinkedIn campaign group; a draft is deleted permanently, others are marked for deletion. |
| `delete_linkedin_creative` | linkedin_ads_edit | Wants to delete a LinkedIn creative (ad); a draft is deleted permanently, others are marked for deletion. |
| `detach_linkedin_conversion` | linkedin_ads_edit | Wants to remove a conversion rule from a LinkedIn campaign. |
| `update_linkedin_campaign` | linkedin_ads_edit | Wants to change a LinkedIn campaign's status, budget, schedule, bidding or ad format. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_linkedin_campaign_group` | linkedin_ads_edit | Wants to change a LinkedIn campaign group's status, budget, schedule or objective. Budget increases are capped at +50% per change and +100% within 24 hours. |
| `update_linkedin_campaign_targeting` | linkedin_ads_edit | Wants to change who a LinkedIn campaign targets. |
| `update_linkedin_creative_status` | linkedin_ads_edit | Wants to activate, pause, archive or return a LinkedIn creative to draft. |
