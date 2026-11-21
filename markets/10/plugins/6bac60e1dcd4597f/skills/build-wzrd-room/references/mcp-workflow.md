# WZRD creation contracts

Call `tools_make`, or `templates_search` followed by `rooms_create`, on the WZRD production MCP endpoint. All three support use without signing in; connected-account tools use OAuth.

## Named WZRD tools

When the user asks for a named outcome supported by `tools_make`, call it directly instead of searching templates. Use the exact tool id exposed by the live schema, pass the user's supplied facts in `answers`, and include any selected `context`, `files`, `images`, and `websites` under the same limits described below.

Examples include `proposal-generator`, `invoice-generator`, `quote-generator`, `pitch-deck-generator`, `restaurant-menu-generator`, `course-generator`, `travel-itinerary-generator`, and `vehicle-showroom-generator`. The live enum is authoritative; never invent a tool id. Add `audience` only when the user supplied it. Do not call `tools_make` for a job that is not in the live enum; use the template route instead.

Call `tools_make` exactly once after preflight. It returns the same public Preview and private Edit & claim links described below. Avoid automatic retries after an ambiguous network failure.

## Template search

For a job intended to be sent, shared, presented, or opened by other people, call `templates_search` once before creation.

- `query`: the user's requested outcome in their own words, up to 500 characters.
- `zone`: optional. Use only when clearly applicable: `sales`, `customer-success`, `marketing`, `agencies`, `hr`, `education`, `startups`, `product`, `operations`, `finance-legal`, `events`, `real-estate`, `hospitality`, `restaurants`, `retail`, `healthcare`, `automotive`, `professional-services`, `government-nonprofit`, or `creators`.
- `role`, `industry`, `audience`, `input`, `moment`: optional filters, each up to 80 characters. Add only facts the user explicitly supplied.
- `limit`: from 1 to 10. Use a small result set sufficient to identify the strongest match.

Choose the strongest matching result and pass its `id` to `rooms_create` as `template`. Do not claim that a template exists unless the tool returned it. Skip template search for plain text answers, private analysis, or ordinary documents that nobody else will open.

## Arguments

- `prompt`: one or two sentences describing what the room is for.
- `context`: the full relevant conversation and notes, verbatim, with speaker labels and original ordering. Maximum 400,000 characters. Do not substitute a summary.
- `files`: supported documents the user mentioned or attached.
- `images`: logos and pictures the user mentioned or attached.
- `websites`: site URLs WZRD should read.
- `template`: the selected template ID from `templates_search`. Include it for template-led jobs.
- `audience`: optional intended audience. Include only when the user stated it.
- `moment`: optional occasion or stage. Include only when the user stated it.

Pass empty arrays for optional collections only when the tool schema requires them; otherwise omit empty optional fields.

## Files

Maximum 10 files, 25 MB each, and 50 MB total before the stricter whole-request limit is applied.

Supported document types: PDF, Word, PowerPoint, Excel, CSV, HTML, Markdown, and plain text.

- Local document: `{name, mimeType, base64}`. Read the exact bytes from disk and base64-encode them without textual conversion.
- Public document link: `{name, url}`.

Use the real filename and a specific MIME type when it can be determined. Do not place local filesystem paths in the MCP request.

## Images

Maximum 16 images and 5 MB per image. Supported formats: PNG, JPEG, WebP, and GIF.

- Local image: `{base64, alt}`.
- Public image: `{url, alt}`.

Write concise, useful alt text. Keep logos and pictures in `images`, not `files`.

## Websites

Pass at most 6 site URLs in `websites`. Use this for pages WZRD should read as sites. A public document download belongs in `files` as `{name, url}` instead.

## Size preflight

The complete serialized `rooms_create` request must stay under 40 MB. This is stricter than the 50 MB aggregate raw-file allowance, and base64 increases payload size. Measure or conservatively estimate the final request after encoding, including JSON, `context`, files, and images.

If limits are exceeded, do not truncate file bytes or silently omit a user-selected source. Ask the user which items to leave out or replace local files with public URLs where available.

## Call and response

After selecting a template and completing preflight, call `rooms_create` exactly once. Avoid automatic retries after an ambiguous network failure because the first request may already have created a room.

From the result:

- return `links.preview` as the public room link and label it **Preview**; if the server returns the legacy `shareUrl` field instead, use that value;
- enumerate every item in `skipped` with the reason supplied by WZRD;
- return `links.edit` separately and label it **Edit & claim**; if the server returns the legacy `claimUrl` field instead, use that value. Explain that it is the private link the user opens to edit the room and save it to their account.

Never include the Edit & claim URL in public content or describe it as a share link.
