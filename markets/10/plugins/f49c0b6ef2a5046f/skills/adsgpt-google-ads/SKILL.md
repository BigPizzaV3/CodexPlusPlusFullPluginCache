---
name: adsgpt-google-ads
description: Read and change the Google Ads accounts connected to AdsGPT with its google_ads_* tools (performance reports, comparing periods, Google's recommendations, the changes made, a campaign and its ads at a glance, keyword research and forecasts, keywords, negative keywords and shared lists, extensions, targeting and audiences, campaign settings, ad groups, ads, Performance Max asset groups, conversion actions and goals, labels, bid strategies, budgets, status and deletions, the account's images and videos, image uploads), and the objectives, campaign types and rules for creating Google Ads campaigns. Use it before reading or changing anything on Google Ads, and when a new campaign includes Google Ads.
---

# Google Ads

Google's advertising platform. The tools report performance (`google_ads_report`), compare a
period with the one before (`google_ads_compare_periods`), read a campaign
at a glance (`google_ads_get_campaign`) and its ads (`google_ads_get_ads`), research and forecast
keywords (`google_ads_research_keywords`, `google_ads_forecast_keywords`), create a campaign
(`google_ads_create_campaign`, see «New campaigns»), make the frequent changes with a tool each
(see «Changes»), list the images and videos of the account's library (`google_ads_list_assets`) and upload images to it
(`google_ads_upload_images`). Each tool takes an account by its `account` id.

## Reports

- For performance, use `google_ads_report`: the account, its campaigns (with the Search impression
  share and what they lost to budget and to rank), ad groups, ads, keywords (with the quality score
  and its components, and the bids Google estimates for the first page) or search terms, the search
  terms that cost without converting (`wasted_spend`, the source of negative keywords), the
  conversion actions, each campaign's conversions by action (`conversions`), and by device, hour,
  location, demographic, audience, landing page, placement or asset, with their money in the
  account's currency. It also lists the budgets with Google's recommended one, the portfolio bid strategies (`bidding_strategies`), the reach, the ads
  Google did not approve, Google's recommendations and the changes made, and the search
  categories of a Performance Max (`pmax_search_categories`, one campaign at a time). When no
  report or tool has what the user asks, say so and where to see it in Google Ads.
- When the user asks why something changed, or how a period went against the one before, use
  `google_ads_compare_periods`: it brings both periods, what moved the most and the changes made
  meanwhile, in one call. Explain the change with those facts; do not read each report apart.
- Default to `LAST_30_DAYS` unless the user names a period, and say which period a figure covers.
  Ask for one row per day only to show a trend.
- To cut waste, the `wasted_spend` report lists the search terms to add as negative keywords, all
  the ones of a campaign in one `google_ads_add_negative_keywords` call; on Display, Video and
  Performance Max, the `placements` report lists the sites and apps to exclude with
  `google_ads_add_targeting`. Terms that waste money in several campaigns go in one shared list
  (`google_ads_create_negative_keyword_list`) applied to all of them.
- Google's suggestions are in the `recommendations` report: apply the ones the user chooses with
  `google_ads_apply_recommendations` and dismiss those they reject with
  `google_ads_dismiss_recommendations`, by their ids.
- Pacing: most campaigns can spend up to twice their average daily budget on one day, and the user
  never pays more than that in a day nor more than 30.4 times it in a month.

## Ids

- Never assume the id of a catalog item, such as an interest, a remarketing list, a custom
  audience or, for a new campaign, a location or a language: find it with `google_ads_search_targeting`,
  by a name in any language, and, if nothing matches, say so and ask. `google_ads_add_targeting`
  takes locations by their name: pass the user's, without searching it first. Its interests are the in-market and affinity ones, the
  only ones the campaigns take; creating a campaign returns, among its issues, an interest the
  campaign type does not take: then choose another. A portfolio bid strategy, with its id, is in the `bidding_strategies` report.
- When a tool fails, tell the user what you tried and what you are correcting; never go on as if
  it had worked.

## Changes

- Before editing a campaign, read it with `google_ads_get_campaign`, by its id or its name, with
  the sections the change needs: `structure` for its ad groups, `keywords` for keyword ids,
  `negative_keywords` for those of the campaign and its shared lists, `ads` for the ads' texts,
  `bidding` for its strategy, `extensions` for its sitelinks, callouts, snippets, phone, name and
  logo, `targeting` for its locations, schedule, devices, audiences, demographics, placements and
  topics, `asset_groups` for a Performance Max's asset groups with their assets and signals, and
  none (`[]`) to only find its id. The tools that add something skip what already
  exists: to add, read only the ids the tool takes. The account's shared negative keyword lists are in
  `google_ads_list_negative_keyword_lists`. For an ad's images, policy topics or pinning, read
  `google_ads_get_ads`. Their ids are the ones the tools below take.
  Each section is a query to Google Ads: ask only for those the change needs, and read a campaign
  once in a conversation. After the user confirms a change, use the ids you already read instead
  of reading the campaign again.
- Each frequent change has its tool, which checks it before calling Google and says what changed,
  what it skipped and why. For a change in this table, call its tool with the ids you read.

  | Change                                                | Tool                                        |
  | ----------------------------------------------------- | ------------------------------------------- |
  | Add keywords to a search ad group                     | `google_ads_add_keywords`                   |
  | A keyword's max CPC or final URL                      | `google_ads_update_keywords`                |
  | Delete keywords                                       | `google_ads_remove_keywords`                |
  | Add negative keywords, to a campaign or a list        | `google_ads_add_negative_keywords`          |
  | Remove negative keywords, of a campaign or a list     | `google_ads_remove_negative_keywords`       |
  | A new shared negative keyword list                    | `google_ads_create_negative_keyword_list`   |
  | Apply a shared list to campaigns                      | `google_ads_attach_negative_keyword_list`   |
  | Sitelinks, callouts, snippets, phone, name or logo    | `google_ads_add_extensions`                 |
  | Remove extensions (pausing keeps them)                | `google_ads_remove_extensions`              |
  | Add locations, radius, languages, audiences, topics   | `google_ads_add_targeting`                  |
  | Ad schedule, device adjustments or demographics       | `google_ads_set_targeting`                  |
  | Remove targeting                                      | `google_ads_remove_targeting`               |
  | Name, dates, networks, tracking, AI Max, frequency    | `google_ads_update_campaign_settings`       |
  | What conversions a campaign bids for                  | `google_ads_update_campaign_settings`       |
  | A new website conversion action, with its tag         | `google_ads_create_conversion_action`       |
  | A conversion action's value, counting or primary      | `google_ads_update_conversion_action`       |
  | Show on or exclude sites, apps and YouTube            | `google_ads_add_targeting`                  |
  | Apply Google's recommendations                        | `google_ads_apply_recommendations`          |
  | Dismiss Google's recommendations                      | `google_ads_dismiss_recommendations`        |
  | A new ad group with its ad (and keywords)             | `google_ads_create_ad_group`                |
  | An ad group's settings, Demand Gen channels, audience | `google_ads_update_ad_group`                |
  | A new search, Display or Demand Gen ad                | `google_ads_create_ad`                      |
  | A new Performance Max asset group                     | `google_ads_create_asset_group`             |
  | An asset group's assets, themes, signal or URL        | `google_ads_update_asset_group`             |
  | Edit a responsive search ad's texts, paths or URL     | `google_ads_update_ad`                      |
  | Bid strategy or its target (CPA, ROAS, CPC ceiling)   | `google_ads_update_bid_strategy`            |
  | A campaign's budget                                   | `google_ads_update_budget`                  |
  | Pause or enable anything, extensions too              | `google_ads_update_status`                  |
  | Delete campaigns, ad groups, asset groups or ads      | `google_ads_remove_campaigns_groups_or_ads` |
  | Add a label to campaigns, ad groups or ads            | `google_ads_add_labels`                     |
  | Take a label off campaigns, ad groups or ads          | `google_ads_remove_labels`                  |

- Keywords go in the match type the user asks for, or PHRASE; a campaign with campaign-level broad
  match takes BROAD only. A max CPC only applies with manual CPC bidding: under another strategy,
  say so and offer a CPC ceiling on the strategy instead.
- Prefer pausing to deleting, which cannot be undone: delete only when the user asks to delete,
  and then delete directly, without pausing first. When the user only wants something to stop
  for now, pause it. Before deleting, say what goes with it: a campaign takes its groups, ads and
  keywords. To replace a keyword or an ad, add the new one
  before pausing the old, so the ad group never stays empty.
- Negative keywords go in broad match unless the user asks for another. Removing one lets those
  searches show ads, and spend, again: say which searches before removing it. When the same
  exclusions serve several campaigns, such as job or free searches, offer a shared list: one
  change then covers them all. A list the account already has takes new keywords with
  `google_ads_add_negative_keywords`.
- Extensions go on the campaign unless the user asks for the ad group or the account. To add
  them, read the campaign with `include: []`: the tool skips the ones it already has. Sitelinks
  lead to pages of the ads' domain; write their texts and callouts with the `adsgpt-write-ads`
  rules. A structured snippet's header is one of Google's, in the language of the ads. The
  business name and logo show only for verified advertisers: pass on the tool's note when Google
  refuses them, and upload a logo first with `google_ads_upload_images`, kind logo.
- Targeting: locations, radius and languages go on the campaign, except in Demand Gen, which takes
  them on each ad group; audiences on the campaign or an ad group, demographics on an ad group,
  topics and placements to show on, on a Display or Demand Gen ad group (a campaign only excludes
  them). Search campaigns no longer take languages: Google matches
  their ads by the language of the texts. Name a location as the user does; the tool finds it.
  Audiences in observation only adjust bids; in targeting only they see the ads, which shrinks
  the reach: offer observation unless the user wants to narrow it.
  A Demand Gen ad group takes its interests, lists, ages and genders as one audience, set whole
  with the `audience` of `google_ads_update_ad_group`.
- A schedule, the device adjustments and the demographics are set whole: pass the full schedule or
  segments the user wants, not only the change. The schedule runs in the account's time zone: say
  it. To replace a location, add the new one before removing the old, so the campaign never shows
  worldwide.
- Ads: write the texts with the `adsgpt-write-ads` rules, 8 to 15 different headlines of up to 30
  characters and 2 to 4 descriptions of up to 90, on the domain of the group's other ads. Display
  and Demand Gen ads take images of the library by their id, and the tool places each one by its
  shape; their texts follow the type's rules (`references/display.md`, `references/demand-gen.md`).
- Performance Max: an asset group needs at least 3 headlines, a long headline, 2 descriptions, a
  landscape and a square image, a logo and the business name (on the campaign, when it has brand
  guidelines). To replace an asset, add the new one and remove the old in the same call to
  `google_ads_update_asset_group`, so the group never goes under those minimums; refuse removing
  the last of a kind and say what to add first. Search themes and the audience signal guide
  Google; they do not limit who sees the ads: say it. A signal is set whole. Editing
  an ad keeps its statistics, and Google reviews it again; a landing page on another domain is a
  new ad.
- Conversions: the conversion actions and their ids are in the `conversion_actions` report, and a
  campaign's goals in its `bidding` section. A primary action changes what every campaign on the
  account's goals bids for: create one as primary only when the user wants the campaigns to
  optimize for it, and ask when unsure. Pass on the tag the tool returns, and say the action
  measures nothing until it is installed on the page of the conversion. A Performance Max bids for
  every primary conversion of the account: when it must not bid for some, such as another
  campaign's app installs, set its goals, by category or by actions. Pass on what the tool skips
  with where to change it.
- Bid strategies: maximize clicks is Google's `TARGET_SPEND`. Say that an automated strategy needs
  one to two weeks to learn, and pass on the tool's warning when a target has few conversions. A
  campaign with a portfolio strategy is changed in Google Ads.
- A budget change keeps the budget daily or total and refuses one other campaigns share. Pause the
  narrowest thing that solves a problem.
- A change without a tool of its own, such as a carousel ad, is made in Google Ads: say so
  plainly, without trying another tool.

## Images and logo

The ads show images and a logo the account's library has: the tools that create a campaign, an ad
or an asset group take an image by its asset id or by a public URL, and add a URL the library lacks
first, without anything else to do.

- Only images and a logo of the brand the campaign advertises. A library can hold images of other
  brands, such as another client's ads or the logo of a tool the advertiser uses: tell them apart
  by each image's name and by the logos the account already uses (`logos`), and when you cannot
  tell whether an image is the brand's, leave it out or ask.
- List the library with `google_ads_list_assets` before asking the user for images: the account
  usually has images and a logo it already uses. An image with an `aspectRatio` fits the ads; one
  without it has another shape or is too small for the ads, and can still be a logo. `logos` has the logos the
  account already uses. It lists the newest first: when `truncated`, call it again with the smallest
  id as `before`.
- To use a new image in a campaign that already runs, give its public URL to the tool that adds
  the ad or the asset group, or changes the asset group: it adds the image to the library first. An
  extension takes asset ids: upload its image with `google_ads_upload_images` first.
- Never an image an AI model generates.

## New campaigns

Google Ads supports these objectives, each with the campaign types that fit it. Propose the type
that fits what the user wants and confirm it with the objective.

| Objective     | Campaign types                               |
| ------------- | -------------------------------------------- |
| awareness     | display                                      |
| traffic       | search, demand-gen, display                  |
| engagement    | demand-gen                                   |
| leads         | search, performance-max, demand-gen, display |
| sales         | search, performance-max, demand-gen, display |
| app-promotion | app                                          |

- **search:** text ads on Google Search for the people who search what the user offers; needs
  keywords. Its rules: `references/search.md`.
- **Keywords with data:** for a search campaign or a new ad group, find keywords with
  `google_ads_research_keywords`, seeded with the business's own words or its page, in the
  locations and language of the campaign; prefer the ones with volume and a CPC the budget can
  pay. To estimate clicks and cost, forecast them with `google_ads_forecast_keywords`: it needs
  only the keywords and a max CPC, and takes a daily budget when the user gives one. Say it is
  Google's estimate, not a result. Call them one at a time: Keyword Planner takes one request per
  second per account.
- **app:** ads that get installs of the app across Search, Google Play, YouTube, Discover and the
  Display Network; needs the app in its store. Its rules: `references/app.md`.
- **performance-max:** one campaign across Search, YouTube, Display, Discover, Gmail and Maps,
  where Google combines the texts, images and logo of each asset group and chooses where to show
  them. It bids for conversions, so it needs an account that measures them; propose it for leads or
  sales when the user wants reach beyond search, and search when they want to control which
  searches show the ads. Its rules: `references/performance-max.md`.
- **demand-gen:** image and video ads in the feeds of YouTube, Discover and Gmail, on YouTube and
  on the Display Network, for people who are not searching yet but would want what the user
  offers; or only on YouTube when the user asks for it. Propose it for engagement, for traffic or
  conversions beyond search, for a visual product, and when the user has videos on YouTube. Its
  rules: `references/demand-gen.md`.
- **display:** image ads on the sites and apps of the Display Network, where Google finds the
  people with optimized targeting. The only one for awareness, which pays per thousand viewable
  impressions; for traffic or conversions it reaches people across those sites and apps, beyond
  search. Its rules: `references/display.md`.
- **Leads and sales** bid for conversions, which the account must be measuring. Before proposing
  them, look up the conversion actions that bidding uses in the `conversion_actions` report: the
  enabled ones with `primaryForGoal`. Without any, the account does not measure conversions: say so and propose the traffic objective
  instead.

Once the user confirmed the campaign type, read its rules: they say how to fill the fields of
`google_ads_create_campaign` for it. It creates the whole campaign in one call, all or none, paused
unless the user asked to start it; the issues it returns are what to fix, with nothing created.
