---
name: ugc
description: Creator-style product video ads — unboxing, review, tutorial, testimonial, demo and hyper-motion — plus reusable on-camera presenters and ad variations for split testing. Use when the user wants an ad with a person presenting their product. Not for garment try-on (use Try-On) and not for product stills with no presenter (use Product Studio).
---

# UGC Ads

Produce one finished creator-style ad: a presenter, a product, a hook, a setting, and a
format — assembled through the server's guided picker flow.

Read `references/flow.md` for the exact call sequence, `references/hooks.md` for hook and
setting selection, `references/creator.md` for presenter consistency, `references/script.md`
for the spoken beats, `references/qa.md` before you deliver, `references/models.md` for
model limits, and `references/errors.md` when something fails.

## Runtime contract

- **One `select_*` call per turn.** Each picker renders UI and the user's choice returns as
  the next message. Two pickers in one turn produces a dead widget and a stalled flow.
- **The pickers do their own intake.** They collect photos, URLs and descriptions and call
  the underlying upload and create tools themselves. Never call `request_image_upload`,
  `create_product` or `create_avatar` to feed a picker.
- **`duration` and `resolution` are required on `generate_ad`**, not optional. Resolve them
  with `list_durations` and `list_resolutions` — those two tools describe **ad generation
  specifically** and are the correct source here.
- **Ids are internal.** Never print `org_id`, `folder_id`, `format_id`, `product_id`,
  `avatar_id`, job ids, or phase names.
- **Never resubmit a pending job.** A queued generation is billed once; resubmitting bills
  twice for one result.

## Hard rules

- **One presenter per ad.** Never regenerate or swap the avatar mid-run.
- **Never alter the product.** Colour, shape, finish and included accessories must match
  what actually ships.
- **Never bake text into generation.** Image and video models render letterforms
  unreliably. Captions come from `generate_video_captions`; overlay copy is added after.
- **Say what you changed.** A substituted model, duration or resolution is a material
  change — one short line, every time.
- **Two attempts per stage, maximum.** Then stop and report what you observed.

## Truth and safety gate — clear this before generating

If any item fails, do not generate and do not route around it.

- **Presenter authorization.** Use a generated adult presenter, or a real person the user
  is authorized to depict. A supplied photo is not permission to impersonate its subject.
  Decline public figures, minors, and deceptive identity use. If third-party consent is
  unclear, ask once.
- **Allowed promotion.** Decline political persuasion and promotion of age-restricted or
  prohibited goods: adult content, gambling, illegal or prescription drugs, tobacco and
  nicotine, weapons, counterfeits, deceptive financial services, malware, and covert
  surveillance.
- **Truthful claims.** Treat the claims the user supplies as the complete allowlist.
  Preserve each one as written. Never strengthen, combine, or infer a new claim from them.
  With no claims supplied, write claim-free copy about what is directly observable —
  materials, controls, how it is used, what is in the box.
- **No synthetic testimonials.** A generated presenter is a host or demonstrator, never a
  real customer. Do not invent purchase, ownership, results, before/after outcomes,
  ratings, or lived experience. First-person experience is allowed only when the user
  supplies the exact script and confirms it is their own.
- **Transparent framing.** Describe the output as a brand demo or creator concept, not an
  organic customer review. If the user asks for a caption or post package, include an
  ad/sponsorship disclosure.

## Phase 0 — Intake

Establish four things in **one** question, not four:

1. **The product** — what it is and what it visibly does
2. **The ad style** — unboxing, review, tutorial, testimonial, demo, hyper-motion
3. **The claims** they are allowed to make, if any
4. **Where it runs** — feed, story, paid placement

Do not ask about models, resolutions or hooks. Those are yours to choose and state.

## Phase 1 — Product

`select_product`. If the product does not exist yet, the picker creates it — let it. Note
what the product photo actually shows; the script cannot describe features that aren't
visible.

## Phase 2 — Presenter

`select_avatar`. **This is the identity lock.** The same presenter carries the whole ad and
every later variation. See `references/creator.md` before choosing — a presenter mismatched
to the product category is the most common reason an ad reads as fake.

## Phase 3 — Format

If the user named a format, `list_formats` resolves it to a numeric `format_id`. If they
named none, `select_format` renders the picker.

## Phase 4 — Hook

`select_hook`. The ad style from Phase 0 is **not a separate step** — it shapes this pick
and the next one. Carry their words forward rather than asking them to restate the style.
`references/hooks.md` maps style to hook.

The hook is the whole ad. Most viewers decide in the first 1.5 seconds.

## Phase 5 — Setting

`select_setting`. Match the setting to where the product is actually used, not to what
looks most expensive. An unboxing in a showroom reads as an ad; an unboxing at a desk
reads as a person.

## Phase 6 — Destination

`select_folder`, then `select_market_project` (which takes that folder).

## Phase 7 — Generate

`generate_ad` with the resolved `product`, `avatar`, `format_id`, hook, setting, project,
plus `duration` and `resolution`. Then let the widget poll — don't call `fetch_status`. On a
text-only host, poll `fetch_status` with `id=<uuid>` and `sync: true` until `complete` or
`error`.

## Phase 8 — QA before delivery

Run the checklist in `references/qa.md`. Do not claim the ad is good without checking the
actual output. If you could not inspect it, say so.

## Variations — `/variants`

Only when an ad already exists. Multiplying is not regenerating.

1. **Hold the product and presenter constant.** They are the control.
2. **Vary one axis** — hooks, or formats, or settings. A test where three things changed
   teaches nothing.
3. **3–5 by default.** Quote the credit cost before a larger batch.
4. **Label what differs** in each. "Five hooks, same product and setting" is a test.

## Presenters — `/presenter`

A presenter is a reusable asset; the same face across every video is the point.

| Request | Tool |
|---|---|
| Create | `create_avatar` |
| Render an image | `generate_avatar` |
| Choose an existing one | `select_avatar` |
| Edit | `update_avatar` |
| Remove | `delete_avatar` — destructive, confirm first |

Ask three things only: who they are, what they present, the usual setting.
`references/creator.md` has the archetypes that work per category.
