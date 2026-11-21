---
name: business-profile
description: Google Business Profile (Google Maps listing) with Opus Growth - locations, details, hours, categories, services, photos and videos, posts, reviews and replies, verification, performance insights and the searches people use to find the business. Use for local visibility, Maps listings, reviews or Business Profile questions and changes.
---

# Google Business Profile

Follow the `opus-growth` skill. Every listing change is public on Google Search and Maps as soon as
Google accepts it, and Google may review edits before they show.

## Reading

- Locations: `gbp_list_locations`, details `gbp_location_details`.
- Performance: `gbp_insights` (search and Maps impressions, calls, direction requests, website
  clicks, bookings; `by_day` for trends). Messages are always 0: Google shut Business Profile
  messaging down in July 2024.
- Searches used to find the business: `gbp_search_keywords`. Google reports exact counts only for
  high-volume terms; the rest arrive as "fewer than N". Data lags about two months.
- Reviews: `gbp_reviews`. Photos: `list_business_profile_photos`. Posts: `gbp_list_posts`.

## Improving local visibility

1. **Categories**: the primary category matters most for ranking; find exact names with
   `gbp_search_categories` and set them with `gbp_update_location`.
2. **Services**: `gbp_manage_services` with short descriptions. Google's AI answers on Maps read
   this list. `replace` deletes everything not passed; use `add` to extend.
3. **Details**: hours (including special hours), phone, website, description. Service areas
   cannot be edited through the API right now; the user edits them in the Business Profile
   manager.
4. **Photos and videos**: `gbp_upload_photo`, `gbp_upload_video`, recategorize with
   `gbp_update_photo_category`. Images need a public direct link; `create_public_image_url`
   provides one.
5. **Posts**: `gbp_create_post` (text, optional image, button). CALL buttons take no URL.
6. **Reviews**: answer every review, negative ones first, briefly and without personal data
   (`gbp_reply_review`). Never write or solicit fake reviews and never offer incentives for
   reviews; that violates Google's policy.

## Verification

`gbp_verification_options` shows the methods Google offers for that listing,
`gbp_start_verification` starts one, `gbp_complete_verification` enters the code. A listing that
is not verified cannot be fully edited and does not show its edits publicly.

## Ads connection

Location assets in Google Ads (address, map pin, directions) come from this profile:
`google_ads_add_location_assets`. The Business Profile and the Google Ads account must be linked.

## Every operation

The complete list of this area's operations, what each is for and the tool that runs it: `references/operations.md`.
