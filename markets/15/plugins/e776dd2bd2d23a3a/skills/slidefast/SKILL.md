---
name: slidefast
description: Create, edit, review, export, or publish LinkedIn, Instagram, and TikTok carousels with Slidefast. Use for social slide decks and client-review workflows, not general presentation files.
---

# Slidefast

Use the bundled Slidefast MCP tools to take a carousel from brief to delivery.

## Scope and discovery

- Decks, themes, brand kits, and social accounts belong to projects. Use the user's explicit `project_id`; otherwise use the account default. When scope is unclear and multiple projects exist, show the choices before creating content.
- Reuse an existing deck when the user asks to revise one. Search by title before creating a replacement.
- Use the brand kit and an existing theme when available. Search the image library before generating or uploading another image.

## Create and edit

For a new deck, create the presentation once, then call `slidefast_chat` with the complete brief. Whole-deck generation is saved even in `default` mode and consumes one AI message.

For creative edits to an existing deck:

1. Call `slidefast_chat` with `mode="default"`.
2. Present the returned `suggestions[]` to the user.
3. Call the same edit with `mode="apply"` only after the user accepts it.

A small factual correction dictated verbatim may be applied directly. Both dry-run and apply calls consume an AI message, so never repeat a call merely to reread its output.

## Review, export, and publish

- Client review links require the Agency plan. Creating one exposes a no-login URL; rotating it invalidates the previous URL.
- Export tools return public CDN URLs. Tell the user that the link is publicly reachable.
- LinkedIn and Meta publishing goes live immediately. TikTok `DIRECT_POST` also goes live; its default media-upload mode creates a draft in the creator inbox. Obtain explicit confirmation immediately before any live publish.
- Call `slidefast_get_social_connections` before publishing so the user can verify the platform and destination. Reuse an `idempotency_key` when retrying a failed publish.
- Publishing is asynchronous. Return the post id and check it once when requested; do not poll in a loop.

## Stop conditions

- `401`: the Slidefast OAuth session is missing, expired, or revoked. Ask the user to reconnect Slidefast. Legacy `sk-sf-` API keys remain supported for manual/local configurations; never print or persist one in project files.
- `402`: report the named plan or quota limit and stop.
- `403` with a pinned key: omit a conflicting `project_id` or use the pinned project.
- `409` on publishing: return the provided `connect_url`; connecting a social account is a browser OAuth step for the user.
- `429`: report the limit and reset information; do not retry-loop.
- Never delete a deck or revoke/rotate a review link without an explicit request.
