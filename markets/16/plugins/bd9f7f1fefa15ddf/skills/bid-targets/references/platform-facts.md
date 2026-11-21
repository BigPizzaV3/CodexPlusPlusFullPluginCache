# Google Ads platform facts

Checked on 2026-10-02 against official Google sources. Platform rules change: when a fact matters for a decision, tell the user to confirm it in Google's help pages. Industry sources are labelled **[industry]**. Quotes are verbatim from the page as served on the check date.

Verdicts:
- **Confirmed**: the claim matches the source.
- **Corrected**: the claim is wrong, incomplete or needs a qualifier. The current fact is stated.
- **Unverified**: no source found that supports the claim.

---

## 1. Attribution models

**Verdict: confirmed** (dates added)

Google Ads supports only data-driven and last click attribution. First click, linear, time decay and position-based stopped being selectable from mid-July 2023. Conversion actions still on them were switched to data-driven from September 2023.

> "The first click, linear, time decay, and position-based attribution models are no longer supported by Google. Conversion actions that used the deprecated attribution models have been upgraded to use data-driven attribution."

> "Starting in mid-July 2023, developers will no longer be able to choose the following attribution models [...] Starting in September 2023, we'll switch any conversion actions still using these models to data-driven attribution."

- https://support.google.com/google-ads/answer/6259715?hl=en
- https://ads-developers.googleblog.com/2023/04/first-click-linear-time-decay-and.html (published 2023-04-20, updated to say mid-July instead of June)

## 2. Smart Bidding and bid adjustments

**Verdict: corrected** (one exception missing)

Smart Bidding (Target CPA, Target ROAS, Maximize conversions, Maximize conversion value) does not use manual bid adjustments for location, ad schedule, audiences, calls or demographics. Device supports -100% to opt out.

Exception: for Target CPA, a device adjustment is applied as an adjustment to the CPA target, not ignored. Targeting and exclusions (for example the ad schedule itself) are still respected.

> "If you make a manual bid adjustment to your automated Smart Bidding strategy, it won't be supported. Device bid adjustments for Target CPA allows you to modify the value of your CPA target, rather than the bids themselves."

> "In cases where -100% adjustments aren't possible, Smart Bidding strategies will still consider targeting and exclusions for each bid adjustment type."

- https://support.google.com/google-ads/answer/2732132?hl=en

## 3. Performance Max negative keywords and lists

**Verdict: confirmed** (dates added)

PMax campaign-level negative keywords launched in January 2025 with a cap of 100. Google raised the cap to 10,000 per campaign in March 2025 and the help page says it is available in all PMax campaigns. Campaign-level negative keyword lists can be applied to PMax since mid-2025 (global rollout reported on 2025-08-07). Negatives apply to Search and Shopping inventory only.

> "In January, we announced campaign-level negative keywords with an initial limit of 100 negative keywords per Performance Max campaign. [...] a few weeks ago, we started to roll out an update where we've raised the limit to 10,000 negative keywords per campaign and this is now available in all Performance Max campaigns."

> "we're adding the ability to apply campaign-level negative keyword lists to your Performance Max campaigns."

> "Performance Max negative keywords are applicable to Search and Shopping inventory only."

- https://support.google.com/google-ads/answer/16127398?hl=en
- https://business.google.com/us/accelerate/announcements/unlock-more-visibility-and-control-in-performance-max/
- https://support.google.com/google-ads/answer/15726455?hl=en
- **[industry]** https://ppc.land/google-raises-negative-keywords-limit-to-10-000-for-performance-max-campaigns/ (announced 2025-03-10)
- **[industry]** https://ppc.land/google-wraps-up-performance-max-feature-rollouts-in-2025/ (lists rollout, 2025-08-07)

## 4. Performance Max search themes

**Verdict: confirmed**

The limit is 50 search themes per asset group, raised from 25 in 2025.

> "Add up to 50 search themes per asset group."

> "we've increased the limit of how many search themes you can add from 25 search themes to 50 per asset group."

- https://support.google.com/google-ads/answer/14767319?hl=en
- https://business.google.com/us/accelerate/announcements/unlock-more-visibility-and-control-in-performance-max/
- **[industry]** https://ppc.land/google-doubles-search-themes-limit-for-performance-max-campaigns/ (reported May 2025)

## 5. Performance Max search terms and channel reporting

**Verdict: confirmed** (dates added)

Google announced PMax search terms reporting on 2025-04-30 as "rolling out now". The channel performance report launched as a beta from late May 2025. Its data starts on 2025-06-06 in the UI. Some Google pages still label the report "beta".

> "Search terms reporting is rolling out now, on top of existing search terms insights."

> "Channel performance reporting helps you understand how your Performance Max campaign is delivering results across Google's full range of channels and inventory."

> "You can view any date range after June 6, 2025 using the date picker."

- https://blog.google/products/ads-commerce/channel-performance-reporting-coming-to-performance-max/ (2025-04-30)
- https://support.google.com/google-ads/answer/16260130?hl=en

## 6. Account-level negative keywords

**Verdict: confirmed** (campaign types added)

The limit is 1,000 per account. They apply to Search and Shopping inventory in Search, Performance Max, App, Shopping, Smart and Local campaigns.

> "A limit of 1,000 negative keywords can be excluded for each account."

> "These include all search and shopping inventory in Search, Performance Max, App, Shopping, Smart, and Local campaigns."

- https://support.google.com/google-ads/answer/11396330?hl=en

## 7. Shared negative keyword lists

**Verdict: confirmed**

Up to 5,000 negative keywords per list and 20 lists per account. A manager account can also hold 20 lists. A campaign holds up to 10,000 negative keywords.

> "Each Google Ads manager account can have a maximum of 20 lists, and each child account can have up to 20 lists of its own. 5,000 keywords per negative keyword list (Manager account or child account) 10,000 negative keywords per campaign"

- https://support.google.com/google-ads/answer/6372658?hl=en
- https://support.google.com/google-ads/answer/2453983?hl=en

## 8. Negative keywords and misspellings

**Verdict: corrected** (misspellings only, not close variants)

Since June 2024, negative keywords also block misspellings. They still do not match close variants, synonyms or singular/plural forms, which must be added separately. Google announced the change on 2024-06-26.

> "We've also applied the misspellings behavior mentioned above to negative keywords. Before, you needed to add all misspellings of each keyword if you wanted to exclude them."

> "Negative keywords won't match to close variants or other expansions."

> "you'll need to add synonyms and singular or plural versions if you want to exclude them."

- https://support.google.com/google-ads/answer/15070437?hl=en
- https://support.google.com/google-ads/answer/2453972?hl=en
- **[industry]** https://ppc.land/google-ads-updates-search-query-matching-and-brand-controls/ (2024-06-27: "Google Ads yesterday announced")

## 9. AI Max for Search campaigns

**Verdict: confirmed** (status update added)

Announced 2025-05-06, rolled out globally in beta from later in May 2025. It includes:
- Search term matching (broad match plus keywordless technology).
- Text customization.
- Final URL expansion.
- Brand controls at campaign and ad group level.
- Locations of interest at ad group level.

In April 2026 Google said AI Max is moving out of beta. Dynamic Search Ads upgrade to AI Max from September 2026, with the DSA sunset extended to February 2027.

> "expand upon your existing keywords using broad match and keywordless technology to find more relevant and high-performing search queries"

> "text customization [...] formerly known as 'automatically created assets'"

> "reach specific customers based on their geographical intent at the ad group level"

> "AI Max is moving out of beta [...] Starting in September, legacy features like Dynamic Search Ads will automatically upgrade to AI Max"

- https://blog.google/products/ads-commerce/google-ai-max-for-search-campaigns/ (2025-05-06)
- https://support.google.com/google-ads/answer/15910366?hl=en
- https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/ (2026-04-15, updated 2026-06-11)

## 10. Smart Bidding Exploration

**Verdict: confirmed**

An opt-in Smart Bidding feature, announced 2025-05-21 at Google Marketing Live. It uses a flexible ROAS target to bid on less obvious queries. It works with broad match, Dynamic Search Ads or AI Max. Google recommends running it for at least 6 weeks.

> "our biggest update to bidding in over a decade"

> "Smart Bidding Exploration is an opt-in feature that works with broad match, Dynamic Search Ads, or AI Max, and utilizes Google AI to bid on searches that were previously out of reach."

> "It's recommended that you enable exploration for at least 6 weeks to understand the impact."

- https://blog.google/products/ads-commerce/smart-bidding-exploration-ai/ (2025-05-21)
- https://support.google.com/google-ads/answer/16294223?hl=en

## 11. Seasonality adjustments

**Verdict: confirmed**

Google says they suit short events of 1 to 7 days and may not work as well beyond 14 days. They are available for Search, Shopping and Display on Target CPA and Target ROAS, and for Performance Max and App (beta) on all bid strategies.

> "Seasonality adjustments are ideal for short events of 1–7 days. They may not work as well if you use them for extended periods (more than 14 days at a time)."

- https://support.google.com/google-ads/answer/10369906?hl=en

## 12. Smart Bidding learning period

**Verdict: corrected**

Google does not state a day count such as "up to 7 days" in its current help pages. It says calibration typically takes 1 to 2 conversion cycles. It recommends evaluating over at least 2 full conversion cycles, or a month or at least 50 conversions. "3 conversion cycles" is not Google's figure.

> "It can take a few conversion cycles (1-2 typically) for the bid strategy to calibrate to the new objective, although it can be faster depending on the amount of conversion data present."

> "It can be helpful to assess over longer periods of time, like a month, or at least 50 conversions, for a clearer perspective."

- https://support.google.com/google-ads/answer/13020501?hl=en
- https://support.google.com/google-ads/answer/6268633?hl=en

## 13. Call-only ads

**Verdict: confirmed**

Creation of new call-only ads was removed in February 2026. Existing call-only ads stop receiving impressions in February 2027. Google directs advertisers to responsive search ads with call assets.

> "February 2026: All options to create a new call-only ad will be removed."

> "February 2027: All existing call-only ads will stop receiving impressions."

- https://support.google.com/google-ads/answer/16598240?hl=en

## 14. Video action campaigns to Demand Gen

**Verdict: confirmed** (dates added)

- **April 2025**: creation of new Video Action Campaigns removed.
- **July 2025**: automatic upgrades to Demand Gen started.
- **December 2025**: end dates past 2026-01-31 blocked.
- **April 2026**: final campaigns upgraded.

> "April 2025: Google removes the option to create new Video Action Campaigns from Google Ads."

> "We are automatically upgrading the final campaigns to Demand Gen by April 2026."

- https://support.google.com/google-ads/answer/15110871?hl=en

## 15. Offline conversion imports and the Data Manager API

**Verdict: confirmed** (scope narrowed)

From 2026-06-15 the Google Ads API stopped accepting new adopters of offline conversion imports, including enhanced conversions for leads. New adopters must use the Data Manager API. Existing API importers can keep using the Google Ads API while they migrate. The change applies to API uploads (`ConversionUploadService.UploadClickConversions`); the source does not cover UI or file uploads.

> "Starting on June 15, 2026, the Google Ads API will no longer accept new adopters of offline conversion imports, including enhanced conversions for leads."

> "Developers who have not adopted offline conversion imports or Enhanced conversion for leads, or have not imported offline conversions between December 2025 and May 2026, will receive an error"

> "Developers who have already adopted offline conversions or Enhanced conversions for leads can continue importing using the Google Ads API while they integrate with the Data Manager API."

- https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html (2026-05-15)

## 16. Consent Mode v2 in the EEA

**Verdict: corrected** (the requirement is the consent policy; Consent Mode v2 is how to meet it)

Since March 2024, advertisers must comply with the EU user consent policy to use ad personalization and measurement on EEA traffic.

Advertisers with their own banner must implement Consent Mode v2, which adds `ad_user_data` and `ad_personalization`. CMP users get v2 through their provider.

Without valid consent signals, audience and measurement features degrade for EEA users. Consent Mode v2 is not a legal requirement in itself.

> "Advertisers must adhere to the EU UCP to use ad personalization and for measurement when using tags/SDKs"

> "If you maintain your own banner, implement consent mode v2."

> "you will need to update to the latest APIs or SDK for Apps to prevent offline audiences (i.e. Customer Match) degrading from March 2024."

- https://support.google.com/google-ads/answer/14625550?hl=en
- https://developers.google.com/tag-platform/security/concepts/consent-mode

## 17. Responsive search ads and Ad Strength

**Verdict: confirmed**

An RSA takes up to 15 headlines of 30 characters, 4 descriptions of 90 characters and 2 paths of 15 characters. The minimum is 3 headlines and 2 descriptions. Google states that Ad Strength does not feed Ad Rank, Quality Score or auctions.

> "you can provide up to 15 headlines and 4 descriptions for a single responsive search ad"

> "Ad Strength is a feedback tool for asset diversity and combination testing. It isn't used to calculate Ad Rank, Quality Score, or auction wins."

- https://support.google.com/google-ads/answer/7684791?hl=en
- https://support.google.com/google-ads/answer/9921843?hl=en

## 18. Broad match with Smart Bidding

**Verdict: confirmed** (wording qualified)

Broad match is the default match type for new keywords. Google says broad match should always be paired with Smart Bidding. It promotes the pairing as "AI-powered Search ads". The sources do not use the phrase "recommended default". AI Max now extends this approach.

> "Broad match is the default match type for all keywords."

> "It's critical to use Smart Bidding with broad match."

> "By pairing broad match with Smart Bidding, you can use auction-time signals to set the right bid for each query."

- https://support.google.com/google-ads/answer/12159290?hl=en
- https://support.google.com/google-ads/answer/7478529?hl=en
- https://support.google.com/google-ads/answer/12158267?hl=en

## 19. Location options

**Verdict: confirmed**

**Presence or interest** reaches people who are in or regularly in the targeted locations, plus people who have shown interest in them. **Presence** reaches only people who are in or regularly in them. Presence or interest is the default and Google's recommended setting for Search and Demand Gen. Location exclusion uses Presence.

> "By default, location targeting includes both physical locations and locations of interest"

> "Reach people in, regularly in, or who've shown interest in your targeted locations (Presence or Interest) Reach people in or regularly in your targeted locations (Presence)"

> "While broad geo targeting is recommended as a best practice on Search and Demand Gen, it's important to know when targeting for "Presence" makes sense."

- https://support.google.com/google-ads/answer/1722038?hl=en

## 20. Brand exclusions in Performance Max

**Verdict: corrected** (YouTube search is included)

In PMax, brand exclusions apply to Search, Shopping and YouTube search inventory. Advertisers can choose to let Shopping ads still serve on excluded brand searches.

> "For Performance Max, brand exclusions apply to only Search, Shopping, and YouTube search inventory, but you also have the option to allow your Shopping ads to appear in searches for excluded brands."

- https://support.google.com/google-ads/answer/14505308?hl=en

## 21. Jurisdiction-specific surcharges

**Verdict: confirmed** (current rates listed)

- **Spain**: 3% Regulatory Operating Cost since 2024-07-01 (2% before).
- **UK**: 2% DST Fee since 2020-11-01.
- **Italy**: 2.5% Regulatory Operating Cost since 2024-07-01 (2% before).
- **France**: 2% Regulatory Operating Cost since 2021-05-01.
- **Austria**: 5% DST Fee since 2020-11-01.
- **Turkey**: 4.5% Regulatory Operating Cost since 2026-01-01 (7% before).
- **Canada**: 2.5% DST fee removed, effective 2025-07-01.
- **India**: 2% removed from 2024-09-01.

> "As of July 1, 2025, ads served in Canada are no longer subject to the 2.5% DST fee, following Canada's official legislative repeal of the Digital Services Tax on March 26, 2026."

> "As of January 1, 2026, the Turkey Regulatory Operating Cost has been reduced from 7% to 4.5%."

> "As of July 1, 2024, a 3% Spain Regulatory Operating Cost will be added to your next invoice or statement for ads served in Spain."

> "As of July 1, 2024, a 2.5% Italy Regulatory Operating Cost will be added"

- https://support.google.com/google-ads/answer/9750227?hl=en

---
