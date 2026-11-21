# Google Ads: app campaign

An app install campaign: Google shows the app's ads on Search, Google Play, YouTube, Discover and
the Display Network, and optimizes for installs. `google_ads_create_campaign` with
`campaign.type: app` creates it: a daily budget (a total is divided by the days of the dates,
since the API takes no total), the campaign with the destination's app, bidding for installs
without a target cost, its locations and languages, and one ad group with the app ad.

- **App.** `destination.app`: its id in its store (the package name on Google Play, the numeric id
  on the App Store) and the store, from the store link the user gives; the link is the
  destination's `url`. Neither changes once the campaign exists.
- **Locations and languages** (`locations`, `languages`): their ids, from
  `google_ads_search_targeting`; never assume them. The campaign targets locations and languages
  only: tell the user when they asked for age, gender or interests.
- **Measurement.** Google Play installs are measured without setup. For an App Store app, tell the
  user that measuring installs needs Firebase or a third-party app analytics tool.
- **Ad texts** (`ad`). From 2 to 5 headlines of up to 30 characters and from 1 to 5 descriptions of
  up to 90 characters, without repeats.
- **Images** (`ad.images`). Optional, by asset id or public URL. Google also takes images and
  videos from the store listing.
