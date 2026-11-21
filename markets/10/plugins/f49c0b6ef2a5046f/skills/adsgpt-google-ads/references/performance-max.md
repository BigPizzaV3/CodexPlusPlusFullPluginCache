# Google Ads: Performance Max campaign

One campaign across Search, YouTube, Display, Discover, Gmail and Maps: Google combines the texts,
images and logo of each asset group and chooses where to show them. `google_ads_create_campaign`
with `campaign.type: performance_max` creates:

- one budget, as a total for the dates or per day;
- the campaign, paused unless the user asked to start it, bidding for conversions, the only
  bidding Performance Max takes;
- its locations and languages;
- the brand's name and logo on the campaign;
- its asset groups, from 1 to 3, each with its texts, images, videos, search themes and audience
  signal, leading to the destination with AdsGPT's tracking.

Google's text generation and final URL expansion stay off: they would change the ads the user
approves.

Write the fields of `campaign`:

- **Business name** (`businessName`): the brand's name, up to 25 characters.
- **Locations and languages** (`locations`, `languages`): their ids, from
  `google_ads_search_targeting`; never assume them. The campaign targets locations and languages
  only: who is likely to convert goes in each asset group's audience signal, which guides Google
  without limiting who sees the ads.
- **Logo** (`logo`): a square image by asset id or public URL, such as the logo of the brand's
  site; left out, the logo the account already uses. Without either, the result has an issue: ask
  the user for a link to their logo.

What else it needs:

- **Conversions.** It bids for conversions, which the account must be measuring: look up its
  conversion actions as the `adsgpt-google-ads` skill says before proposing it.
- **Images** (each asset group's `images`): by asset id or public URL, at least one 1.91:1 and one
  1:1; 4:5 is optional. Take them, in this order, from the account's library
  (`google_ads_list_assets`), which usually has them, the image the brand's site shares, and URLs
  the user gives when neither has them. Never an image an AI model generates.
- **Ad texts.** From 3 to 15 headlines of up to 30 characters and from 2 to 5 descriptions of up to
  90 characters, without repeats, and from 1 to 5 long headlines of up to 90 characters.
