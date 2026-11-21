# HasData source and tool catalog

Discovered from anonymous tools/list on 2026-10-26. The configured plugin connection selects 66 tools from this snapshot, and the unfiltered server advertises 68. This is a routing snapshot, not proof that every scraper was executed. Prefer the current connected tool schema for required combinations, filters, enums and response fields. Read only the section relevant to the task. The plugin connects https://mcp.hasdata.com/mcp with an `apis` filter that selects its supported sources.

A source-specific workflow does not restrict other exposed tools. Batch submission and status tools are not in this live catalog. Do not promise them merely because another HasData integration exposes them.

## Google SEO and Maps

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| google_maps_contributor_reviews: GET / | `hasdata_google_maps_contributor_reviews_getMapReviews` | `contributorId` |
| google_maps_photos: GET / | `hasdata_google_maps_photos_getMapPhotos` | Check descriptions for required alternatives |
| google_maps_place: GET / | `hasdata_google_maps_place_getPlaceDetails` | `placeId` |
| google_maps_posts: GET / | `hasdata_google_maps_posts_getMapPosts` | Check descriptions for required alternatives |
| google_maps_reviews: GET / | `hasdata_google_maps_reviews_getMapReviews` | Check descriptions for required alternatives |
| google_maps_search: GET / | `hasdata_google_maps_search_performMapSearch` | `q` |
| google_serp_serp: GET / | `hasdata_google_serp_serp_getSearchResults` | `q` |
| google_serp_serp_light: GET / | `hasdata_google_serp_serp_light_getSearchResults` | `q` |

## Google AI answers

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| google_serp_ai_mode: GET / | `hasdata_google_serp_ai_mode_getAiModeResponse` | `q` |
| google_serp_ai_overview: GET / | `hasdata_google_serp_ai_overview_getAiOverviewResponse` | `pageToken` |

## Ecommerce

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| amazon_product: GET / | `hasdata_amazon_product_getProductDetails` | `asin` |
| amazon_reviews: GET / | `hasdata_amazon_reviews_getProductReviews` | `asin` |
| amazon_search: GET / | `hasdata_amazon_search_getSearchResults` | `q` |
| amazon_seller: GET / | `hasdata_amazon_seller_getSellerDetails` | `sellerId` |
| amazon_seller_products: GET / | `hasdata_amazon_seller_products_getSellerProducts` | `sellerId` |
| google_serp_immersive_product: GET / | `hasdata_google_serp_immersive_product_getImmersive_e29f691177` | `pageToken` |
| google_serp_product: GET / | `hasdata_google_serp_product_getProductInformation` | `productId` |
| google_serp_shopping: GET / | `hasdata_google_serp_shopping_getSearchResults` | `q` |
| shopify_collections: GET / | `hasdata_shopify_collections_getCollections` | `url` |
| shopify_products: GET / | `hasdata_shopify_products_getProducts` | `url` |
| walmart_product: GET / | `hasdata_walmart_product_getWalmartProduct` | Check descriptions for required alternatives |
| walmart_reviews: GET / | `hasdata_walmart_reviews_getWalmartReviews` | Check descriptions for required alternatives |
| walmart_search: GET / | `hasdata_walmart_search_getSearchResults` | Check descriptions for required alternatives |

## Social and video

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| facebook_profile: GET / | `hasdata_facebook_profile_getFacebookProfile` | `handle` |
| instagram_comments: GET / | `hasdata_instagram_comments_getInstagramComments` | `url` |
| instagram_posts: GET / | `hasdata_instagram_posts_getInstagramPosts` | `handle` |
| instagram_profile: GET / | `hasdata_instagram_profile_getInstagramProfile` | `handle` |
| tiktok_comments: GET / | `hasdata_tiktok_comments_getTikTokComments` | `videoId` |
| tiktok_posts: GET / | `hasdata_tiktok_posts_getTikTokPosts` | `handle` |
| tiktok_profile: GET / | `hasdata_tiktok_profile_getTikTokProfile` | `handle` |
| tiktok_search: GET / | `hasdata_tiktok_search_getTikTokSearch` | `keyword` |
| youtube_channel: GET / | `hasdata_youtube_channel_getYoutubeChannel` | `channelId` |
| youtube_search: GET / | `hasdata_youtube_search_getYoutubeSearchResults` | `q` |
| youtube_transcript: GET / | `hasdata_youtube_transcript_getYoutubeTranscript` | `v` |
| youtube_video: GET / | `hasdata_youtube_video_getYoutubeVideo` | `v` |

## Property

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| redfin_listing: GET / | `hasdata_redfin_listing_getRealEstateListings` | `keyword`, `type` |
| redfin_property: GET / | `hasdata_redfin_property_getPropertyDetails` | `url` |
| zillow_listing: GET / | `hasdata_zillow_listing_getRealEstateListings` | `keyword`, `type` |
| zillow_property: GET / | `hasdata_zillow_property_getPropertyDetails` | `url` |

## Jobs

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| glassdoor_job: GET / | `hasdata_glassdoor_job_getJobDetails` | `url` |
| glassdoor_listing: GET / | `hasdata_glassdoor_listing_getJobListings` | `keyword`, `location` |
| indeed_job: GET / | `hasdata_indeed_job_getJobDetails` | `url` |
| indeed_listing: GET / | `hasdata_indeed_listing_getJobListings` | `keyword`, `location` |

## Travel

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| airbnb_listing: GET / | `hasdata_airbnb_listing_getAirbnbListings` | `checkIn` |
| airbnb_property: GET / | `hasdata_airbnb_property_getAirbnbPropertyDetails` | `url` |
| booking_place: GET / | `hasdata_booking_place_getBookingPlaceDetails` | `url`, `checkInDate`, `checkOutDate`, `rooms`, `adults`, `children` |
| booking_search: GET / | `hasdata_booking_search_getBookingSearchResults` | `keyword`, `checkInDate`, `checkOutDate`, `rooms`, `adults`, `children` |
| google_travel_flights: GET / | `hasdata_google_travel_flights_getGoogleFlights` | `departureId`, `arrivalId`, `outboundDate` |
| google_travel_flights_deals: GET / | `hasdata_google_travel_flights_deals_getGoogleFlightsDeals` | `q`, `departureId` |
| google_travel_hotels: GET / | `hasdata_google_travel_hotels_getGoogleHotels` | `q`, `checkInDate`, `checkOutDate` |

Traveler-count encoding differs by source. For Google Flights/deals omit optional zero children/infant counts; Google Hotels omits children and childrenAges for no children and has no rooms input. Airbnb omits optional zero children/infants/pets. Explicit zero for these optional counts is rejected upstream; preserve positive supplied counts. Booking instead requires children:0 for a supplied child-free party, together with rooms and adults. Read the source-specific skill before calling.

## Search sources

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| bing_serp: GET / | `hasdata_bing_serp_getSearchResults` | `q` |
| duckduckgo_serp: GET / | `hasdata_duckduckgo_serp_getSearchResults` | Check descriptions for required alternatives |
| google_images_images: GET / | `hasdata_google_images_images_getImageSearchResults` | `q` |
| google_scholar_case_law: GET / | `hasdata_google_scholar_case_law_getScholarCaseLawOpinion` | `caseId` |
| google_scholar_cite: GET / | `hasdata_google_scholar_cite_getScholarCitationFormats` | `q` |
| google_scholar_scholar: GET / | `hasdata_google_scholar_scholar_getScholarSearchResults` | `q` |
| google_serp_events: GET / | `hasdata_google_serp_events_getEventInformation` | `pageToken` |
| google_serp_news: GET / | `hasdata_google_serp_news_getGoogleNews` | Check descriptions for required alternatives |
| google_serp_short_videos: GET / | `hasdata_google_serp_short_videos_getShortVideosSearchResults` | `q` |
| google_trends_search: GET / | `hasdata_google_trends_search_getTrendsData` | `q` |

## Business directories

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| yellowpages_place: GET / | `hasdata_yellowpages_place_getPlaceDetails` | `url` |
| yellowpages_search: GET / | `hasdata_yellowpages_search_getSearchResults` | `keyword`, `location` |
| yelp_place: GET / | `hasdata_yelp_place_getPlaceDetails` | `placeId` |
| yelp_reviews: GET / | `hasdata_yelp_reviews_getPlaceReviews` | `placeId` |
| yelp_search: GET / | `hasdata_yelp_search_getSearchResults` | `keyword`, `location` |

## Public web

| Operation | Actual tool name | Schema-required inputs |
| --- | --- | --- |
| web_scraping_web_scraping: POST / | `hasdata_web_scraping_web_scraping_scrapeWebPage` | `url` |

## Not on this connection

`hasdata_chatgpt_chat_getChatgptAnswer` and `hasdata_perplexity_chat_getPerplexityAnswer` exist on the shared server and are excluded by the connection's `apis` filter. They are not plugin capabilities. Do not invoke them from a plugin workflow even if another connection in the host exposes them.

## Non-obvious input boundaries

Maps search takes q, not a city-valued location parameter. Maps reviews, photos and posts need a real returned placeId or dataId even where the schema-required array is empty. Walmart details and reviews accept an actual itemId or product URL. Scholar Cite takes q equal to the selected Scholar resultId, not its title, search query, DOI or URL. SERP continuation IDs must come from corresponding results. AI Overview expansion takes the fresh aiOverview.pageToken from full SERP; lookup plus expansion may require two requests, and the token expires in about one minute. YouTube transcript and video tools use v, not a full URL. Instagram and TikTok handles omit @.

Flight and lodging dates, passenger counts and currencies must follow the chosen source. Booking search and place details require rooms, adults and children. When children > 0, childrenAges is required as a comma-separated list with exactly one age per child, each from 0 to 17; ask for missing ages before calling. Zillow and Redfin type values and filters differ. Inspect the live schema before translating user requirements.

Web Scraping is annotated readOnlyHint=false and destructiveHint=true because its full API permits interactions. These research workflows use public-page reads only, without jsScenario, cookies, authorization headers or form submission. Skill restrictions do not replace server-side security enforcement.
