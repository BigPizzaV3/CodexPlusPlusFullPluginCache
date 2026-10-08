---
name: google-business-profile
description: Analyze Google Business Profile (Google My Business) listing performance and manage the profile through Windsor.ai. Use when the user asks about a location's views, searches, calls, direction requests, or reviews — or wants to publish or update a local post, reply to a review, upload a photo, update business info or hours, or set the open status. Do not use for Google Ads, other review platforms (Yelp, …), or generating post creative.
---

# Google Business Profile via Windsor.ai

Windsor.ai exposes live Google Business Profile (GBP / Google My Business) data
(read) and profile management (write) through MCP tools. The connector id is
`google_my_business`. On the Business Profile app the connector is already
scoped; when a tool asks for a connector, use `google_my_business`.

Golden rules:

- **Never guess field, location, action, or option names** — get them from
  `get_fields`, `get_connectors`, `list_actions`, and `get_options`. Call those
  first.
- **Reads are safe; writes are public and change the live listing.** Only call
  `execute_action` after the user confirms the specific change.
- Report what the user asked for, concisely.

## 1. Ground yourself first

Call `get_connectors` to see connected Business Profile locations. If none is
connected, help the user connect: `get_connector_authorization_url` (or
`get_connector_connect_info`) and give them the setup link (GBP needs the
`business.manage` scope). If several locations are connected, ask which one.

## 2. Reading insights and reviews

1. `get_fields` for `google_my_business` — insight metrics (impressions on maps
   and search across desktop/mobile, `CALL_CLICKS`, `WEBSITE_CLICKS`, direction
   requests, bookings, conversations) and review / local-post / media data. Use
   the exact ids returned.
2. `get_data` with the fields, target location `account`(s), and a date range.

## 3. Managing the profile (write actions)

Call `list_actions` first for exact ids/schemas. GBP exposes:

- **`create_local_post` / `update_local_post`** — publish or edit a "What's New"
  post (text, optional public photo URL, optional call-to-action button).
- **`reply_to_review`** — publish (or replace) the owner's public reply to a
  review.
- **`upload_media`** — add a photo to the gallery (category ADDITIONAL / COVER /
  PROFILE / …).
- **`update_location`** — update the business description, website, and/or phone
  (Google may review edits before they appear).
- **`set_regular_hours` / `set_special_hours`** — replace the weekly hours or set
  exceptional (holiday) hours; both replace all existing entries, so include
  every period in one call.
- **`set_open_status`** — mark the location OPEN or CLOSED_TEMPORARILY.

Write workflow — every time: resolve the target (post/review/location) to its id
via a `get_data` read if needed, build params from the `list_actions` schema,
**show the user the exact change and confirm** (these are public and edit the
live listing), then call `execute_action` and report the result.

## 4. Reference real data, don't fabricate

On an error, call the relevant discovery tool and retry with correct ids, or
report the specific error. Never invent metrics, review text, post ids, or hours.
