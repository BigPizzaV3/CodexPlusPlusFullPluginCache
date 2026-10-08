---
name: interior
description: Interior redesigns and virtual staging — re-decorate a room from a photo, stage an empty space, or restyle it. Use when the subject is a room or property interior. Not for architectural exteriors and not for product placement (use Product Studio).
---

# Spaces

## Tokens

`/interior` `/redesign` `/restyle` — redesign an existing room
`/staging` `/stage` — furnish an empty space for sale or rent

## Workflow

1. `request_image_upload` for the room photo — this skill works from a real space.
2. `generate_interior_design`.

## The rule that makes results usable

**Keep the architecture.** Walls, windows, doors, ceiling height and proportions are
**fixed**. Change furniture, finishes, colour, textiles and styling.

A redesign that moves a window is not usable by an agent, a homeowner or a contractor —
it is a picture of a different house. If the user explicitly asks for a structural change,
produce it but say once that the result is illustrative rather than a buildable plan.

## For staging

Empty rooms need furniture at believable scale. A sofa that doesn't fit the wall it's
against reads as fake immediately and undermines the listing.

## Defaults

`16:9` — rooms read wide. Magazine-quality and photoreal regardless of the input photo's
quality; a phone snapshot should still produce a polished result.

## Finishing a generation

Where a widget renders, it polls itself. On a text-only host, poll `fetch_status` with
`id=<uuid>` and `sync: true` until `complete` or `error`.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
