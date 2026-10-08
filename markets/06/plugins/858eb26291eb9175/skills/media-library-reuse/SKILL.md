---
name: media-library-reuse
description: Use when someone asks to find, reuse, or retrieve a file already stored in their Media2URL library.
---

# Media Library Reuse

## Purpose

Find a small, relevant set of authorized Media2URL assets so the user can reuse an existing file instead of publishing another copy.

## Trigger examples

- “Use my company logo.”
- “Find the screenshot I uploaded yesterday.”
- “Give me the URL for product-demo.mp4.”
- “Use my latest hero image.”

## Do not trigger

- The user has not referred to an existing Media2URL asset or library.
- The request is to publish newly generated content.
- The result would require exposing another account’s or workspace’s private asset.

## Allowed Media2URL App actions

- Use narrow `search_assets` calls with the user’s query, media type, date, workspace, and small limit.
- Use `list_recent_assets` for “latest” or “uploaded yesterday” requests.
- Use `get_asset` and `get_asset_links` after the user selects or clearly identifies one result.

## Result interpretation

Return a small ranked set with filenames, media type, and safe identifiers or links as permitted. Ask the user to choose when several assets are plausible. Prefer the direct URL for code and the share page for people, according to the user’s destination.

## Missing authorization

Require a Media2URL account connection for library access. Resolve the active authorized workspace through the App; do not accept a user-supplied workspace ID or public URL as sufficient authorization.

## Plan or quota restriction

Free accounts are capped at 90 uploads per month, roughly 3 per day. Explain when only recent/basic search is available or when full library search requires a paid plan. Do not dump the entire library or silently search outside the available scope.

## Partial failure

If a search or link lookup returns incomplete results, say which result was confirmed and which could not be retrieved. Preserve filenames and identifiers so one asset’s URL cannot be assigned to another.

## Privacy and destructive actions

Searching is read-only but still private. Never publish an asset merely because the user asks ChatGPT to show or use it, and never delete, replace, or change access without separate explicit intent and App authorization.

## Natural-language examples

“I found two recent logo files in your authorized library. Tell me which one you mean, and I’ll return the direct URL separately from the human-facing share page.”
