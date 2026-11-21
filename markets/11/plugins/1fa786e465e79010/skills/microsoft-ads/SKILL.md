---
name: microsoft-ads
description: Microsoft Advertising (Bing) with Opus Growth - campaigns, ad groups, keywords, negatives, responsive search ads, extensions, location, device, demographic and schedule targeting, bid strategies, UET tags, conversion goals, offline conversions, remarketing and reports. Use for any Microsoft Advertising or Bing Ads question or change. Covers bid strategies that need a conversion goal first and what the API cannot show.
---

# Microsoft Advertising

Follow the `opus-growth` skill for preview, confirm, dates and budgets. Structure mirrors Google
Search: campaign → ad group → keywords and responsive search ads. Budgets are daily, in the
account currency.

## Which tool

| Need | Tool |
|---|---|
| One-call picture | `account_snapshot` (platform microsoft) |
| Performance | `microsoft_performance_report`, `microsoft_entity_performance_report`, `get_report` |
| Custom report columns | `microsoft_report_query` |
| What people searched | `microsoft_search_terms_report` |
| Accounts | `list_microsoft_accounts` |

## Building a Search campaign

1. `create_microsoft_campaign` (Search, Audience, Shopping or DynamicSearchAds); created paused.
2. Targeting: resolve places with `microsoft_location_search`, then
   `add_microsoft_location_target`; devices, age and gender, schedule with
   `add_microsoft_device_target`, `add_microsoft_demographic_target`, `add_microsoft_ad_schedule`.
   Add the location target before enabling; check it with the campaign read-back.
3. `create_microsoft_ad_group`, `add_microsoft_keywords`, `create_microsoft_responsive_search_ad`
   (as on Google: many distinct headlines, 3-4 descriptions).
4. Extensions: `add_microsoft_ad_extensions` (sitelinks, callouts and others), edit sitelinks with
   `update_microsoft_sitelink`.
5. Read back with `list_microsoft_campaigns` / `list_microsoft_ads`, enable on request with
   `update_microsoft_campaign_status`.

## Bidding

- MaxConversions, TargetCpa, TargetRoas and MaxConversionValue need a conversion goal in the
  account first: `list_microsoft_uet_tags` → install the tag on the site → 
  `create_microsoft_conversion_goal`. Without a goal Microsoft rejects them.
- Target ROAS is a percentage (350 = 350%).
- After setting ManualCpc, Microsoft may show the campaign as EnhancedCpc when read back; that is
  Microsoft's own behavior, not a failed change.
- As on Google, a strategy change restarts learning; avoid stacking changes.

## Conversions and audiences

- UET tag (`create_microsoft_uet_tag`) must be installed on every page before goals or
  remarketing lists (`create_microsoft_remarketing_list`) work.
- URL goals match a thank-you page path (`Contains`, `BeginsWith`, `Equals`, regex).
- Offline conversions (`upload_microsoft_offline_conversions`) need the click id (MSCLKID)
  captured on the site at the time of the click; auto-tagging must be on.

## Keywords and negatives

Use the `keywords` skill for the method. Microsoft tools: `microsoft_search_terms_report`,
`add_microsoft_negative_keywords`, `remove_microsoft_negative_keywords`,
`update_microsoft_keyword` (bid, status, match type). Microsoft search volume is smaller than
Google's, so wait for more data before calling a term a waste.

## Limits worth knowing

- The Microsoft Advertising API exposes no creation date on campaign objects (only ad group
  start and end dates). `microsoft_change_history` is the change report (who, old value, new
  value). A change can take about an hour to appear there.
- Many advertisers import Google Ads campaigns into Microsoft. Imported campaigns keep Google's
  structure, but budgets, bids and negatives drift unless the import is scheduled; compare
  before assuming they match.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
