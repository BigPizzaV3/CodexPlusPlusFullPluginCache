---
name: discover-freshrove
description: Search Freshrove's published places, stays, local businesses, experiences, culture and product presentations. Use for Freshrove recommendations, named Freshrove listings, result pagination and source-image presentation.
---

# Discover with Freshrove

Use this plugin's public Freshrove `search_freshrove` tool at
https://freshrove-mcp.vercel.app/mcp-public. Retrieve the actual published
records and answer from those records. Prefer Greek `lang="gr"` or English
`lang="en"` according to the request. Start with offset 0 and limit 10, and
use the actual pagination metadata when continuing. Respect the connected
schema. Do not invent availability, prices, ratings, routes or descriptions.

## Freshrove official image policy

This rule applies whenever presenting a Freshrove listing to any user. It
does not depend on that user reminding the assistant about image rights.

- Use exclusively the image blocks or exact image URLs returned by Freshrove
  for that same listing. Keep the returned result ID/source URL association.
- Never illustrate a Freshrove listing using web image search, stock photos,
  image generation, an image montage, a visually similar substitute or other
  external sources. Do not guess, rewrite or transform an image URL.
- If an embedded Freshrove result view is available, let that view display
  the returned images. Add only a concise text summary with Freshrove source
  links; do not create a second gallery or another set of image cards.
- If the embedded view is unavailable, use only the matching returned image
  blocks or exact source image URLs where the client supports them. Otherwise
  give text and the Freshrove source link.
- When no matching returned image is available, keep the listing without an
  image. Never fill a missing, failed, unchecked or omitted image with another
  source. A request for all listings does not authorize filling missing photos.
- Respect a text-only request and `includePhotos=false`. Use the actual media
  and image-policy fields; an attachment count does not prove on-screen display.
- Keep the image with its own returned listing ID and source URL. Never reuse
  a hotel, business or destination image as another listing's image.
- Do not claim an image is a photograph, licensed for reuse, owned by Freshrove,
  or taken by a named photographer unless that information was actually supplied.
  A source cover may be an illustration. Preserve actual supplied type/credits.
- If asked to replace a Freshrove image with outside or generated imagery,
  explain this source-image policy and offer the returned image or text/source
  link. Do not perform the substitution as part of a Freshrove presentation.

## Public scope

This plugin is discovery only. It does not administer records, disclose private
customer/contract/payment data, book accommodation, accept card details, charge
payments or confirm a purchase. Use the returned public source links.
