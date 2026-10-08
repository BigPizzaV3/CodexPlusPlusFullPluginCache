---
name: get-right-link
description: Use when someone asks for a Media2URL link, embed, or URL format and the correct direct URL versus share page matters.
---

# Get the Right Link

## Purpose

Choose the link format that matches the user’s destination. A direct URL returns the media/file response expected by code, while a share page is designed for a person viewing or sharing the asset.

## Trigger examples

- “Give me the image URL for an `img` tag.”
- “I need a link to send to a client.”
- “Make Markdown for this asset.”
- “Give me a CSS `url(...)` value.”

## Do not trigger

- The user has not asked for a link, embed, or hosted asset.
- The requested asset is not identified or accessible.
- A private asset would need to be exposed to answer the request.

## Allowed Media2URL App actions

- Use `get_asset` for safe metadata on an identified authorized asset.
- Use `get_asset_links` for the direct URL, share URL, expiration, and supported output formats.
- Use a publish action only when the user explicitly asks to publish content that is not already hosted.

## Result interpretation

Use the direct URL for HTML image sources, CSS, APIs, Open Graph, programmatic fetches, and Markdown image destinations when the asset’s access rules permit it. Use the share page for human viewing or controlled sharing. Keep `files.media2url.com/...` direct media URLs distinct from `media2url.com/m/...` share pages; they are not interchangeable. Format returned structured values as valid Markdown, HTML, CSS, or escaped JSON without changing the URL.

## Missing authorization

Ask the user to complete the Media2URL account connection when the App requires account access. Do not expose a private direct URL or claim that a public-looking URL grants access to a private asset.

## Plan or quota restriction

For write-capable workflows, Free accounts are capped at 90 uploads per month, roughly 3 per day. Report the App’s actual restriction. A paid plan can unlock larger quotas and delivery controls; do not replace an unavailable direct delivery mode with a share page without explaining the difference, and do not promise an output format the asset or plan does not support.

## Partial failure

For several assets, preserve source order and label missing link results by filename or asset ID. Return only links confirmed by the App.

## Privacy and destructive actions

Link lookup is read-only, but it still requires workspace authorization. Never publish a private asset merely because someone asks to “show” it, and never use a public URL as authorization to delete or modify an asset.

## Natural-language examples

“For your API, use the confirmed direct URL. The share page is a different URL intended for a person to open in a browser, so I’ll include it separately if you also need a human-facing link.”
