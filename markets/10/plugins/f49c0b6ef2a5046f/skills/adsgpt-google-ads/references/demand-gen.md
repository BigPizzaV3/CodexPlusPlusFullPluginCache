# Google Ads: Demand Gen campaign

Image and video ads in the feeds of YouTube, Discover and Gmail, on YouTube's videos and Shorts,
and on the Display Network, for people who are not searching yet: Google combines the texts,
images, videos and logo of each ad for each place. `google_ads_create_campaign` with
`campaign.type: demand_gen` creates:

- one budget, as a total for the dates or per day;
- the campaign, paused unless the user asked to start it, bidding for clicks on traffic and
  engagement and for conversions on leads and sales;
- one ad group on every channel, or only on YouTube (in-stream, in-feed and Shorts), with its
  locations and languages;
- its ads, from 1 to 3, each an image ad or a video ad with its texts and the brand's name and
  logo, leading to the destination with AdsGPT's tracking.

Write the fields of `campaign`:

- **Business name** (`businessName`): the brand's name, up to 25 characters.
- **Only YouTube** (`youtubeOnly`): true only when the user asks to show the ads on YouTube alone;
  otherwise Google chooses among all the channels, which usually reaches more people for the
  money.
- **Locations and languages** (`locations`, `languages`): their ids, from
  `google_ads_search_targeting`; never assume them. The campaign targets locations and languages
  only: tell the user when they asked for age, gender, interests or keywords.
- **Logo** (`logo`): a square image by asset id or public URL, such as the logo of the brand's
  site; left out, the logo the account already uses. Without either, the result has an issue: ask
  the user for a link to their logo.

What else it needs:

- **Conversions.** On leads and sales it bids for conversions, which the account must be
  measuring: look up its conversion actions as the `adsgpt-google-ads` skill says before proposing
  it.
- **Budget.** Google asks a total budget for at least a minimum per day of the dates: when the
  result rejects the amount, tell the user and propose a larger budget or fewer days.
- **Image ads** (`demand_gen_image`): images by asset id or public URL, 1.91:1, 1:1 or 4:5, at
  least one 1.91:1 or 1:1; more shapes reach more places. Take them, in this order, from the
  account's library (`google_ads_list_assets`), which usually has them, the image the brand's site
  shares, and URLs the user gives when neither has them. Never an image an AI model generates.
- **Video ads** (`demand_gen_video`): the user's videos on YouTube, public or unlisted, up to 5 per
  ad and each in one ad only: ask for their links when the user mentions video or YouTube.
  Horizontal (16:9), square or vertical (9:16, the one Shorts show), of at least 5 seconds; under
  10 seconds they do not show before YouTube videos. AdsGPT does not upload videos to YouTube yet:
  a user without the video on YouTube uploads it there first.
- **Ad texts.** From 1 to 5 headlines of up to 40 characters and from 1 to 5 descriptions of up to
  90 characters, without repeats, and, in a video ad, from 1 to 5 long headlines of up to 90
  characters.
