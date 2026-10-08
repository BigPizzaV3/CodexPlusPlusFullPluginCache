---
name: try-on
description: Put a real garment from the user's own photo onto a model or person — virtual try-on, outfit swap, UGC try-on video. Use when the user supplies a photo of an actual garment or product they own. Not for generated wardrobe inside a styled shoot (use Fashion Shoot).
---

# Try-On

Read `references/models.md` before any video call.

## Tokens

`/try-on` `/outfit-swap` `/garment` `/wear-this`

The distinguishing signal: **the user has a photo of a real garment.** If the garment is
being invented rather than supplied, this is Fashion Shoot instead.

## When this fires

- "put this jacket on her", "how would this look on a model"
- "try-on video", "outfit swap"
- A garment photo is attached and a person is mentioned

## Truth and safety gate — clear this before generating

If any item fails, do not generate and do not route around it.

- **Subject authorization.** Use a generated adult, or a real person the user is authorized
  to depict. A supplied photo is not permission to impersonate its subject. Decline public
  figures, minors, and deceptive identity use. If third-party consent is unclear, ask once.
- **No synthetic testimonials.** A generated person is a model or demonstrator, never a real
  customer. Do not invent ownership, results, or lived experience.
- **Transparent framing.** Output is a brand concept or demo, not organic customer content.

## Workflow

1. **Upload the garment.** `request_image_upload` to render the upload widget. If the garment is shot on a
   hanger, flat, or worn by someone else, call `extract_garment` first to isolate it.

2. **Establish the person.** Either a model the user picks, or a photo of a person they
   supply (collected the same way).

3. **Compose.** `composite_shoot` with `image_urls` = **[garment, person]**. It requires
   **two or more** images and runs a reference-aware reconciler so the person, the garment
   and the setting stay consistent. Optional `camera_angle_id` from `list_camera_angles`
   frames the shot; optional `background_select_id` from `select_fashion_background` sets
   the scene.

   For motion, generate the still first, then animate it with `generate_video`
   (`image_url` = that one asset).

4. Let the widget poll.

## Get this right

- **Never invent the garment.** The whole value is that it's *their* product. If the
  uploaded photo is unusable, say so and ask for a cleaner one rather than generating an
  approximation.
- **Preserve garment detail** — print, logo, texture, colour. If the result drifts from the
  source garment, regenerate rather than presenting it.
- Default to `9:16` for try-on video; it is going to a social feed.
- **Try-on is people.** Never open on `seedance-2.5` — it refuses human subjects, including
  illustrated ones. Use `seedance-2.0` at 1080p, falling back to `ltx-2.3` at 6s/1080p.
- **Never omit `resolution`** — it defaults to the model's lowest tier.

## Conventions

- `org_id` resolves itself; call the tool and retry with the id it returns if you don't
  have one. Only call `select_organization` if resolution fails.
- Never print ids.

## Model refusals

On a safety or content refusal, stop and offer an alternative subject. Do not retry on
another model to bypass it. If the refusal reason is unclear, stop and clarify it.
Only switch models for a clearly established unsupported input capability, and tell the
user which model changed and why, including any duration or resolution change.
Summarize the issue plainly instead of exposing the raw upstream error.

## Tool availability

`composite_shoot` requires **two or more** `image_urls` and a **paid organization**. There
is no single-image try-on path — if you only have the garment, you must also establish the
person before compositing.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
