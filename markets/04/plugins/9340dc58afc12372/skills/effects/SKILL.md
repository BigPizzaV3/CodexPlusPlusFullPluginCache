---
name: effects
description: Turn a single uploaded photo into a short viral video using a named preset look — /effects to browse, or a named token like /zoom-punch or /main-character. Use when someone uploads an image and wants motion, a trending effect, or "make this go viral". Not for text-to-video with no source image (use Studio), and not for fashion looks (use Runway Motion).
---

# Effects

One photo in, one short video out. The user should never have to write a prompt.

## When this fires

- An image is attached and the user asks for motion, an effect, or a trending look
- The user types `/effects` or any named preset token
- "make this move", "make this go viral", "add an effect to this"

**Not this skill:** text-to-video with no source image (Studio), animating a fashion
shot from a shoot (Runway Motion), colour grading a still without motion (Retoucher).

## Workflow

1. **Establish the organization.** Every call needs one. It usually resolves silently —
   pass `org_id` when you have it, and when you don't, call the tool anyway and retry with
   the id it returns. If the tool responds that no organization could be resolved (a
   first-time user with more than one), call `select_organization`, then continue. That is
   a normal step, not an error.

2. **Get the source image.** Call `request_image_upload` — this renders the upload widget
   and places the resulting URLs into your context automatically. **Attached files are not
   handed to this server**, so there is no way to read an attachment directly, and
   `user_upload` is internal to that widget. If the user pasted an ImagineArt URL, use it
   as-is. No image means no video; ask for one.

3. **Resolve the preset.**
   - `/effects` with no name: show a short list of looks from `references/effects.md`,
     grouped by feel, and let them pick.
   - A named token (`/zoom-punch`): look it up in `references/effects.md`.
   - **Unknown token:** do not stop and ask what they meant. Infer the intent from the
     token and the conversation, pick sensible defaults, and generate. Never claim a
     preset exists that doesn't, and never pass an unknown name as a model id.

4. **Generate.** Call `generate_video` with:
   - `prompt` — the preset's prompt, with the user's subject woven in
   - `image_url` — an array containing **exactly one** URL (this is what makes it
     image-to-video rather than text-to-video)
   - `model`, `duration` and `resolution` — from the preset. Use its values unless a
     refusal sends you to the preset's `fallback` (see below); that is the one case where
     you change them, and you change all three together.
   - **Never omit `resolution`.** An omitted resolution renders at the model's *lowest*
     tier (`seedance-2.5` defaults to 480p), and low-resolution output is the fastest way
     to make this skill look broken. Durations behave the same way: a value outside the
     model's list silently falls back.

5. **Finish.** Where a widget renders, it polls on its own — don't call `fetch_status`.
   On a text-only host with no widget, poll `fetch_status` with `id=<uuid>` and
   `sync: true` until status is `complete` or `error`, then use the returned URL.

6. **Offer one more.** Suggest a second look from the same family. Repeat generation is
   the whole point of this skill.

## Model refusals

**Confirmed in testing:** `seedance-2.5` declines sources it reads as containing a real
person — including illustrated and cartoon characters. This is a **model restriction**, not
a safety judgement about the content: other models accept the same image.

So:

1. **If the source shows a person, don't open on `seedance-2.5` at all.** Use the preset's
   `fallback` from the start. Person-centric presets already default to `seedance-2.0`.
2. **If a restriction refusal happens anyway**, switch to the preset's `fallback` with that
   fallback's stated duration and resolution — and **tell the user which model you used
   instead**, in one short line. A different model is a different look; silent substitution
   leaves them confused about why two runs differ.
3. **If the refusal is a safety refusal** — the content itself was declined, not the input
   class — **do not try other models.** Say what was declined and offer a different subject.
   When you can't tell the two apart, treat it as a safety refusal.
4. **Two attempts maximum**, then stop and report.

See `references/errors.md` for the full taxonomy.


## Framing

Ask for `9:16` where the preset specifies it, but know that **`seedance-2.5` image-to-video
adopts the source image's ratio and ignores `aspect_ratio` entirely**. Don't promise
vertical output on that path. If the user needs true vertical, tell them the clip follows
their photo's shape.

## Other defaults

- **Short.** Use the preset's duration; don't lengthen it unprompted.
- **One generation per request.** Never fan out across presets unless asked.
- Video generation requires a paid organization. Relay subscription refusals verbatim —
  they carry the upgrade link.

## Conventions

- Never print `org_id`, `folder_id`, or raw asset uuids.

## Where the presets should live

`references/effects.md` is the starter library. The target architecture moves it
server-side behind `get_token_instructions(token)` so new looks ship without a plugin
resubmission. When that endpoint exists, this skill resolves tokens through it and the
reference file is deleted.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
