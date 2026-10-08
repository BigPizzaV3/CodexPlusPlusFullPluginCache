---
name: fashion
description: Fashion photoshoots and fashion motion — lookbooks, editorials, catalogue shoots, runway clips, and animating a look. Use for any request about clothing on models, collections, or campaign imagery. Not for putting a customer's own garment photo onto a person (use Try-On) and not for generic photo effects (use Effects).
---

# Fashion

Stills and motion, one pipeline. Read `references/flow.md` for the picker sequence and
`references/models.md` before any video call.

## Tokens

| Token | What it does |
|---|---|
| `/lookbook`, `/editorial` | Styled, atmospheric campaign stills — `shoot_type: editorial` |
| `/catalogue` | Clean, consistent e-commerce stills — `shoot_type: catalogue` |
| `/runway`, `/animate` | Motion from an existing shoot |
| `/model`, `/wardrobe`, `/pose` | Jump to one picker on an existing project |

## The one rule that breaks this skill

**Advance exactly one `select_*` call per turn and wait for the answer.** Each picker
renders UI and the user's choice comes back as the next message. Chaining two pickers in a
turn is the most common failure here — it produces a dead widget and a stalled flow.

## Truth and safety gate — clear this before generating

If any item fails, do not generate and do not route around it.

- **Subject authorization.** Use a generated adult, or a real person the user is authorized
  to depict. A supplied photo is not permission to impersonate its subject. Decline public
  figures, minors, and deceptive identity use. If third-party consent is unclear, ask once.
- **No synthetic testimonials.** A generated person is a model or demonstrator, never a real
  customer. Do not invent ownership, results, or lived experience.
- **Transparent framing.** Output is a brand concept or demo, not organic customer content.

## Decide the shoot type first, without asking

`shoot_type` is `catalogue` or `editorial` and carries through every later step.

- "lookbook", "campaign", "editorial", "moody" → **editorial**
- "catalogue", "product pages", "e-commerce", "consistent" → **catalogue**

Infer it, state which you picked in one short line, and move on. Don't open with a
question — the pickers already ask plenty.

## Stills

Follow the sequence in `references/flow.md`. The pickers collect their own photos, URLs and
descriptions and call the underlying upload and create tools themselves — never call
`request_image_upload` or `create_fashion_model` to feed a picker.

## Motion

Three paths, cheapest first:

| Request | Tool |
|---|---|
| One still, simple movement | `animate_fashion_image` |
| A named template or a specific runway style | `list_fashion_video_templates`, then generate |
| A whole look or collection in motion | `fashion_video_shoot` |

Take the cheapest path that answers the request, then offer the richer one.

**Fashion motion is people.** Never open on `seedance-2.5` — it refuses human subjects,
including illustrated ones. Default to `seedance-2.0` at 1080p; fall back to `ltx-2.3`
at 6s/1080p. See `references/models.md`.

## Second shoots

Once a project exists, do not rewalk the flow. Ask which single thing changes — pose,
background, wardrobe — re-run that one picker, and generate. This is the most common real
request and it should feel short.

## Conventions

Ids returned by pickers are internal. Never print `org_id`, `folder_id`,
`fashion_project_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
