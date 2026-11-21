# Google Ads: Display campaign

Responsive image ads on the sites and apps of the Google Display Network: Google combines the
texts, images and logo of each ad for each placement, and finds the people with optimized
targeting. `google_ads_create_campaign` with `campaign.type: display` creates:

- one budget, as a total for the dates or per day;
- the campaign, paused unless the user asked to start it, with its locations and languages,
  bidding per thousand viewable impressions on awareness, for clicks on traffic and for
  conversions on leads and sales;
- one ad group and its responsive display ads, from 1 to 3, each with its texts, its images, the
  brand's name and logo, leading to the destination with AdsGPT's tracking.

Write the fields of `campaign`:

- **Business name** (`businessName`): the brand's name, up to 25 characters.
- **Locations and languages** (`locations`, `languages`): their ids, from
  `google_ads_search_targeting`; never assume them. The campaign is created with locations and
  languages only: tell the user when they asked for age, gender, interests or keywords. Other
  targeting is a change to the created campaign: some apps, as **Placements in apps** says below;
  anything else, as the skill's changes say.
- **CPM bid** (`cpmBid`), only for awareness: the most the campaign pays per thousand viewable
  impressions, in units of the account's currency. Ask the user how much they want to pay. When
  they have no figure in mind, propose one from the account's history, and say where it comes
  from: the viewable CPM (`activeViewCpm`, in the account's currency) of its Display campaigns
  with viewable impressions in the last 30 days, in the `campaigns` report. Without history, say there is none and ask for a figure:
  never invent a market price. A low bid shows few ads. Tell the user the bid with the campaign.

What else it needs:

- **Conversions.** On leads and sales it bids for conversions, which the account must be
  measuring: look up its conversion actions as the `adsgpt-google-ads` skill says before proposing
  it.
- **Logo** (`logo`): a square image by asset id or public URL, such as the logo of the brand's
  site; left out, the logo the account already uses, or none: the ads then show no logo.
- **Images** (each ad's `images`): by asset id or public URL, at least one 1.91:1 and one 1:1.
  Take them, in this order, from the account's library (`google_ads_list_assets`), which usually
  has them, the image the brand's site shares, and URLs the user gives when neither has them.
  Never an image an AI model generates.
- **Ad texts.** From 1 to 5 headlines of up to 30 characters and from 1 to 5 descriptions of up to
  90 characters, without repeats, and one long headline of up to 90 characters.
- **Audiences.** Remarketing and custom audiences are not supported yet: Google finds the people.

## Placements in apps

To show the ads only in some apps, create the campaign and then add the apps to its ad group with
`google_ads_add_targeting`:

- **The apps.** Ask the user for each app's package name or store link; never guess them. The id of
  an Android app is `2-` and its package name (`2-com.kiloo.subwaysurf`); of an iOS app, `1-` and
  the digits after `id` in its App Store link (`1-476943146`).
- **The ad group, not the campaign.** A campaign only excludes apps: read the ad group's id with
  `google_ads_get_campaign` (`structure`) and add the apps to it as placements.
- **Optimized targeting.** Turn it off with `google_ads_update_ad_group`
  (`optimizedTargeting: false`): with it on, Google also shows the ads beyond the apps.
- **Reach.** Say that a short list of apps reaches few people and may spend little of the budget.
