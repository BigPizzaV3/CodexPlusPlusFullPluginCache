---
name: business-directory-research
description: Find business listings, public company details or Yelp review samples from Yelp and YellowPages with HasData. Use when those directories are requested, not Google Maps data or unsolicited outreach.
---

# Research Yelp and YellowPages businesses

Read `../hasdata-research/SKILL.md` and the Business directories section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_yelp_search_getSearchResults` or `hasdata_yellowpages_search_getSearchResults` with keyword and location. Start with one page; a named business calls for one matching location, not an arbitrary five-item lead list. Keep branches distinct and clarify a genuine location ambiguity.

Yelp details use `hasdata_yelp_place_getPlaceDetails`; its placeId accepts a genuine Yelp ID or a supported Yelp alias. Reviews use `hasdata_yelp_reviews_getPlaceReviews` and require the exact Yelp ID, not an alias or the /biz/ URL slug. Reuse a returned ID or resolve it through Yelp search within budget; if only an alias is available and the needed lookup is disallowed, ask for the ID or explain the missing prerequisite. Do not copy a details alias into a reviews call. Yelp IDs are not Google place IDs. YellowPages details use `hasdata_yellowpages_place_getPlaceDetails` with the actual listing url.

Return only requested observed public fields and original listing links. Phone/website values can be missing; a directory link is not independent verification of company contact ownership. Do not scrape every business website by default.

For Yelp review themes, use `../review-insights/SKILL.md`. Query-based review searches can ignore the rating filter; inspect actual ratings instead of claiming an enforced cutoff. Use either a returned nextPageToken or supported offset, not both. No automatic pagination, contact harvesting or delivery. For an unspecified local-business source, `../local-business-research/SKILL.md` provides the Maps default.
