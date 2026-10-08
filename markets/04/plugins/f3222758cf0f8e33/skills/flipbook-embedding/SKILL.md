---
name: flipbook-embedding
description: Embed Heyzine flipbooks and manage social sharing metadata. Use when users ask for embed HTML, website or CMS placement, or link preview titles, descriptions, and thumbnails.
---

# Embedding and sharing flipbooks

Keep embedding and social previews as separate workflows. Do not change
publication design or access settings unless the user asks.

## Resolve the target

- Accept a public flipbook URL directly.
- If the user gives an id, short id, or title, use
  `heyzine_flipbook_details` and `heyzine_list_flipbooks` as needed to get the
  canonical URL.
- If a title is ambiguous, list the candidates and ask which one. Never
  assemble or guess a publication URL.

## Return embed HTML

1. Call `heyzine_oembed` with the canonical public URL. Pass `maxwidth` or
   `maxheight` only when the user supplied a size constraint.
2. Return the `html` field in a code block without changing its iframe
   attributes.
3. If oEmbed returns an error, report it and stop. Do not fabricate embed HTML.

Access protection remains active inside an embed. Do not disable protection to
make an embed unless the user explicitly requests that separate change.

For WordPress, first suggest pasting the canonical URL into an embed block; use
the returned HTML in a Custom HTML block if auto-embedding is unavailable. For
a CMS that strips iframes, return the public link instead. Ask which platform
only when its placement requirements affect the answer.

If the user asks for responsive behavior, wrap the unmodified iframe rather
than rewriting its attributes.

## Update a social preview

Choose the tool by publication type:

- `heyzine_set_flipbook_social` for a flipbook.
- `heyzine_set_bookshelf_social` for a bookshelf.

Resolve an ambiguous title with the matching list tool. Pass the publication
`id` and only the fields the user wants to change:

| Field | Requirement |
| --- | --- |
| `title` | Social card headline |
| `description` | Social card description |
| `thumbnail` | Publicly reachable image URL |

Do not invent missing copy or a thumbnail URL. If the user asks to repair a
complete card but provides only some fields, ask for the missing content. A
landscape image near 1200 by 630 pixels is a useful recommendation, not a
requirement.

Social networks cache previews. After a successful update, explain that an
already-shared URL may keep the old card until that network refreshes it.

## Report the result

For embedding, lead with the exact HTML and the canonical URL. For social
metadata, state which fields changed and return the publication URL when it is
available.
