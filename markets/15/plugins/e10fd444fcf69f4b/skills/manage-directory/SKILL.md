---
name: manage-directory
description: How to add, edit, organise, publish and restyle content in a Directify directory safely and in the right order. Use for any request that changes a directory.
---

Working rules for Directify directories. Every tool takes a `directory_id`; get it from `list_directories` or from the user.

## Before writing
- Read first: `list_categories`, `list_tags`, `list_custom_fields` (and `list_languages` for multilingual directories). Categories and tags are matched by title, custom fields by their `name`.
- A listing's `url` is the unique key inside a directory. Call `check_listing_exists` before creating a listing from a website, and use `update_listing` rather than creating a duplicate.
- Create missing categories, tags or custom fields first, then the listings that use them.

## Listings
- One or a few listings: `create_listing`. More than five: `bulk_create_listings`, at most 100 per call, in several calls for longer lists.
- Fill what the source gives you (name, description, website, address, phone, image URL, categories, tags, custom field values). Do not invent facts about a business; leave unknown fields empty.
- Only pass the fields that change to `update_listing`.

## Content
- Articles and pages take Markdown. Create articles unpublished when the user wants to review them, then `toggle_article` to publish. Pages have a placement (navbar, footer, sidebar or unlisted).
- When an article should link to listings, read the listings first and use their real URLs on the directory.

## Theme
- Call `get_theme` before `update_theme`: the response lists the valid templates, fonts, palettes and template settings. Send only the keys that change.
- After a theme change, call `preview_theme` and describe what the screenshot shows.

## Deleting
- `delete_listing`, `delete_category`, `delete_tag`, `delete_custom_field`, `delete_article`, `delete_page`, `delete_organizer` and `delete_redirect` are permanent. Name exactly what will be deleted and get the user's confirmation in the conversation before calling them. Never delete in bulk from a vague request such as "clean up my directory"; list the candidates and ask.
- Deleting a custom field also removes its values from every listing. Say so.

## Scope
- Only act on directories returned by `list_directories`. If a tool returns a permission or not-found error, the directory is not in this account; say so instead of retrying.
- Directify tools manage the directory website only. Requests about other platforms (social media, Google Business Profile, email campaigns) are outside this plugin.
