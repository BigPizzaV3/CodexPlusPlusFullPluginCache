---
name: local-business-research
description: Find public Google Maps business information or a local-business shortlist with HasData, including requested place details, photos or posts. Use Maps when no directory was specified; Yelp and YellowPages have a dedicated skill.
---

# Build a useful business shortlist

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md` before tool calls. Their scope, security and credit limits apply.

For explicitly requested Yelp or YellowPages data, use `../business-directory-research/SKILL.md` rather than a Maps lookup. Review-theme analysis uses `../review-insights/SKILL.md`. A selected Maps place's photos use `hasdata_google_maps_photos_getMapPhotos`, and business posts use `hasdata_google_maps_posts_getMapPosts`, with its actual returned placeId/dataId. Photo category IDs must be supplied or returned, not guessed. Do not call `hasdata_google_maps_contributor_reviews_getMapReviews` to investigate an individual reviewer or trace visited places. Do not call extra operations as incidental enrichment.

Honor the requested directory; use Google Maps when none was specified. For Google Maps, search for the business type or name and geography together in q. A city name is not a Maps location parameter. Yelp and Yellowpages instead use keyword and location. Read the Business directories section of `../hasdata-research/references/tool-catalog.md` for those tools and inspect their actual schema. Do not substitute Maps for a requested directory. Start with one search page. A request for one business or one contact detail calls for one matching result, not a five-row shortlist. For a requested list, use the supplied count or five candidates by default. Do not silently broaden geography when the list is short.

For Maps, use returned localResults and deduplicate by returned placeId or dataId. For other directories, use their actual returned result collection and stable directory IDs or URLs. Never use a Maps placeId in a Yelp tool. Keep branches separate unless a company-level summary was requested. Retain exact IDs or URLs for details. Never manufacture an identifier from a business name.

Maps pagination requires ll with start. Prefer a supplied ll or the actual viewport returned in source context. If absent, a genuine latitude/longitude pair from the same page can supply a derived center; use a supplied/returned zoom or the documented 14z example as an explicit viewport assumption. Format @latitude,longitude,zoomz, keep q and localization unchanged, and never invent coordinates. A derived viewport can change coverage; do not represent it as the exact original search center. Continue only when needed for the requested count within budget and stop if no usable coordinates were returned.

Compare only requested public fields, usually name, address, website, rating and review count. Include a phone only when relevant. Prefer the returned directory listing link, otherwise cite the returned search snapshot or the company's website with clear source labeling. A website link does not independently verify every directory field. Missing values stay visibly unavailable. Do not assume Yellowpages place details include a street address or hours if they are not present.

Use one place-details request only when it answers a specific remaining question about a selected candidate. If reading a company's public site would establish a requested service or product, do that within the remaining request budget. Do not scrape every candidate by default or guess contact emails.

When comparing business websites, distinguish the website links returned by the directory from information read on those websites. Comparing links, ratings and review counts does not require visiting every site. Only fetch site content when the user asks for facts that the directory does not provide.

Explain why candidates fit the user's supplied criteria. Ratings and review counts are observations, not proof of service quality, licensing, current availability or willingness to buy. Avoid presenting a bounded Maps page as the complete local market. Offer a concrete next step, such as reviewing the top two candidates' websites, without performing it automatically.

This workflow produces a shortlist, not unsolicited outreach. It does not create CRM records or send messages unless separately authorized through a suitable connected tool.
