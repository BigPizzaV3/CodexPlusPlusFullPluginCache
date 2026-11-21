---
name: create-invitation
description: Create or edit an Invitio V4 invitation from a catalog template or a unique prompt-built canvas, including photos and music. Use when the user wants to browse templates, design, create, or change an invitation.
---

# Create invitation

Use Invitio tools to persist the invitation. Prefer a catalog template when the user wants to pick a design; otherwise design a unique canvas from the prompt.

## Auth

1. The user must be signed in to Invitio via MCP OAuth.
2. If a tool returns Unauthorized or the client gets HTTP 401, tell them to connect Invitio MCP and sign in. Do not invent an invitation, URLs, or IDs.

## Show templates

1. When the user asks to see, browse, or choose templates, call `list_templates` (optional `type` filter, e.g. Boda).
2. ChatGPT renders a gallery. In other clients, present `name`, `type`, `thumbnail_url`, and `template_id`.
3. After they pick one, create or edit with `upsert_invitation` using that `template_id`. Do not rebuild the canvas yourself.

## Create (template)

1. `list_templates` if they have not chosen yet.
2. Call `upsert_invitation` with `name`, `date`, `type`, `template_id`, optional `time`/`locale`/`media`.
3. Attached photos fill the template's image slots in order. Do not send `canvas` when using `template_id`.
4. If they attached a song or gave a Spotify/Apple Music link, call `set_invitation_music`.
5. Return `editor_url` and `share_url`.

## Create (unique canvas)

1. Read the whole prompt: names, date, time, venue, colors, tone.
2. Map each attached photo to `media[]` with a short `id` and `data_base64` or `url`. In the canvas, set image `src` to `media:<id>`.
3. Build a unique 400px-wide canvas. Vary layout, fonts, and colors from the prompt.
4. Typical first section: names, date, hero photo, RSVP.
5. Bind countdown/calendar to the event date (`dateSource: "event"`).
6. Call `upsert_invitation` with `name`, `date`, `type`, optional `time`/`locale`, `canvas`, and `media`.
7. Music: `set_invitation_music` if they provided a song.
8. Return `editor_url` and `share_url`.

## Add to an existing event (no invitation yet)

1. `list_events` then `get_invitation` with that `evento_id`. If it is missing, the event has no invitation.
2. Call `add_invitation` with `evento_id`. Optional `template_id` or `canvas`; otherwise a blank V4 canvas is used. Name/date/type come from the event.
3. Do not use `upsert_invitation` for this — that either creates a new event or edits an existing invitation.
4. Music: `set_invitation_music` if they provided a song.

## Edit

1. `get_invitation` with `evento_id` or `invitacion_id`.
2. To switch design: `list_templates` then `upsert_invitation` with the id plus `template_id` (and `media` to replace photos).
3. To change a custom canvas: send the updated `canvas` (and media if replacing photos).

## Canvas rules

- Width is always 400. Section height 200–900 on the basic plan, up to 4000 on planner.
- One `music`, one guestbook, one `rsvp`.
- Basic plan: max 3 sections; no `video`, `photoGallery`, `youtube`, `pinterest`, or `map`.
- Sparse primitives are fine (`type`, `text`, `x`, `y`, `width`, `height`); the server fills defaults.

## Rules

- Prefer MCP tools; never claim an invitation exists without a successful tool result.
- Respect the user's prompt: names, wording, photos, and music they provided.
- Do not delete events or send WhatsApp.
