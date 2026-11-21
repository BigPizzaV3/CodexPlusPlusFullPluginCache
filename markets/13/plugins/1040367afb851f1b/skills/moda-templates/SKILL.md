---
name: moda-templates
description: >-
  Start from a team template: list templates, LOOK first (screenshot — a
  template IS a canvas), then instantiate. Use for: "start from our QBR
  template", "use our usual layout", flagging a canvas as a team template.
---

# moda-templates

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

A team template is the canvas someone approved as the starting point for
recurring work — the QBR deck, the launch post, the customer one-pager. It
carries layout and structure, one level up from what a brand kit carries.

## Check before designing (one cheap read)

The ask names a recurring artifact type (QBR or board deck, launch post,
customer one-pager) or the user says "our template", "our usual format", "what
do we have" → check first. Skip it for genuine one-offs.

## Instantiate

1. `template_list` — the team's flagged templates: name, category, page count,
   tags, cursor-paginated. An empty list is a normal answer: say it in one line
   and design fresh.
2. **LOOK before choosing.** Names do not tell you what a template looks like,
   and a template IS a canvas: `canvas_screenshot` renders a candidate inline
   (up to 3 pages per call). Judge 2–4 candidates with your own vision;
   category and page count do the cheap narrowing first.
3. `canvas_create(template_canvas_id=…, name=…)` — a full server-side copy that
   keeps the source's brand kit. The source defines dimensions, pages and
   category, so those fields and `intent` are rejected alongside it, and so are
   `folder` and `visibility`: create the copy first, then place it with
   `drive_organize(action='move')` and rebind its kit with
   `canvas_update(brand_kit_id=…)` when the user's kit differs.
4. The copy is an ordinary canvas — `canvas_read` it, then author or edit it
   the normal way. Send the link, and name which template you started from:
   that is a decision the user may want to correct.
5. None fit? One line ("no team template matched, so I designed this fresh")
   and build from scratch. Never force a bad-fit template.

`canvas_create(template_canvas_id=…)` copies any canvas in the ACTING team, not
only flagged ones — it is also the plain "duplicate this canvas" move. A share
token names a canvas but grants nothing, so it is never a copy source; pulling
pages out of someone else's canvas is `canvas_import_pages`.

## Flag a canvas as the team's template

`canvas_update(template_type='template')` publishes it to the whole team's
`template_list`; `clear_template_type=true` un-flags it.

- Team-visible curation, not a local preference. Offer it when the user calls
  something reusable ("we do this every quarter"); never flag a one-off, never
  flag unasked, and tell them once you have.
- Should the original stay an ordinary canvas? Copy it first
  (`canvas_create(template_canvas_id=…, name=…)`) and flag the copy.
- `template_list` hides canvases the viewer cannot see, so flagging a private
  canvas yields a template only you can find:
  `drive_organize(action='set_visibility', visibility='team')` shares it — or
  say plainly that you could not.
- Some organizations restrict template management to admins. There the call is
  refused: say an admin has to flag this one, in one line, and move on.

## `theme` is a different thing — don't reach for it

`template_type='theme'` is a slides-only layout source applied through a brand
kit, and it deliberately does NOT appear in `template_list`. Moving a canvas
OFF `theme` — to `template` or by clearing it, both count — detaches every deck
and every brand kit that used it, and re-flagging restores none of those links.
No read on this surface reports the current flag, so on a canvas you did not
flag yourself, ASK before you write. "Make this our standard template" aimed at
the team's theme is the request that quietly breaks every deck using it.

## Examples

- "start from our QBR template" → list, screenshot the QBR candidates,
  `canvas_create(template_canvas_id=…)`, then author into the copy.
- "use our usual layout for this one-pager" → same flow, narrowed to 1–2 page
  document templates.
- "make this our standard deck" → flag it, after asking if it is not yours.
- "do we have anything for launches?" → list plus screenshots, and an honest
  "no" if the answer is no.

## Errors

Any typed error → `load_skill("moda-core")` and read its recovery reference.
A 404 on this lane means it is not enabled on this account: treat it exactly
like "no templates" — do not retry it, and do not mention it to the user.

## Make it recurring

Every instantiation is a return visit — that is the point. Pair it with
`load_skill("moda-automate")` when the cadence is fixed.

See also: moda-core — the contract, recovery, everything Moda can do.
