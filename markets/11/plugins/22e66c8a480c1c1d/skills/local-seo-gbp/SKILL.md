---
name: local-seo-gbp
description: Manages a client's Google Business Profile through the Agency Autopilot connector — locations, reviews and owner replies, posts, performance (calls, direction requests, website clicks, impressions), and editing the listing itself (categories, description, service areas, services, website, phone). Use for "reply to that review", "any new reviews", "how many people found us on Maps", "post an update to our profile", "fix our categories", "add a service area", "update the description". Business Profile is a separate, optional sign-in on the Agency Autopilot dashboard ("Connect Business Profile"); if the tools report it is not connected, send the person there.
---

# Local SEO — Google Business Profile

## Availability
Business Profile uses its own sign-in, separate from the main Google connection. On the Agency Autopilot dashboard the person opens the **Business Profile** tab and clicks **Connect Business Profile**, signing in with the Google account that manages their clients' profiles (the one they use at business.google.com), keeping the Business Profile box ticked. If a `gbp_*` tool answers that Business Profile is not connected, say exactly that and point them to the tab; if the tools are absent from the list altogether, offer the Search Console and Analytics parts of local SEO instead (`seo-audit`).

Then link each location to its client: `gbp_list_locations` gives the `gbp_location_id`, which goes in the client's **Business Profile location** field under **Clients** so reviews and posts resolve by client name.

## Reads
- `gbp_list_locations` first; use its `gbp_location_id`.
- Reviews: `gbp_reviews` — rating, text, whether replied. Lead with unanswered reviews.
- Performance: `gbp_performance` for a date range — impressions on Maps and Search, calls, website clicks, direction requests, with daily values.
- Posts: `gbp_posts`.
- How the profile stands against the competition: `site_health` for the client carries `business_profile` (reply rate and time, how recently it posted, new reviews in 90 days, reviews against the top 3 map competitors, its map position for its main category, missing description, hours, categories, website or phone) and `competitor_news` (a new business in the top 3, a competitor gaining reviews, the client's own moves). Start a "how is our Business Profile doing" answer there, then fix with replies and posts.

## Writes — preview, confirm, apply
- `gbp_reply_review`: draft the reply, show it, apply only on `confirm: true`. Thank by name, address the specific point, never argue, invite the conversation offline for complaints.
- `gbp_create_post`: 80–150 words, one clear call to action, optional photo URL; preview, then confirm.

## Editing the listing
- Read it first: `gbp_profile` gives the main and additional categories, description, service areas, services, website and phone, plus any edit Google is still reviewing (`pending_review`).
- Ids only: `gbp_find_options` with kind `category` (e.g. "fence") or `service_area` (a city, ZIP or county) returns Google's own ids; `gbp_update_profile` takes only those.
- `gbp_update_profile` previews first (Google checks the change, nothing saved). Show every before and after, and confirm only on the person's yes. Changing the **main** category also needs `confirm_primary_category`, because it moves where the business shows in Maps; say that plainly.
- Google reviews each edit before publishing it (usually minutes, sometimes longer) and can reject it. Say which fields are pending, and check later with `gbp_profile` rather than assuming it is live.
- Usual wins: a main category that matches the main service, additional categories for the others, every town actually served as a service area, a description that names the services and the area in the first sentence.

## Rules
- Replies, posts and listing edits are public under the business name; never apply one the person has not read.
- Report performance with the period and compare to the previous period.
