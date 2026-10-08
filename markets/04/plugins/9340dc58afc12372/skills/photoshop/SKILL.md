---
name: photoshop
description: Generate or retouch assets with ImagineArt and build them into a layered Photoshop document — separate layers, masks, and editable type. Use when the user wants a working PSD rather than a flat image. Requires desktop access to Photoshop.
---

# Photoshop Finishing

The deliverable is a **layered, reopenable PSD**. A flattened JPEG is a failure — Social
Studio and Product Studio already make flat images.

Read `references/photoshop-ui.md` before touching the app and `references/models.md` before
generating.

## Tokens

`/photoshop` `/psd` `/layers` `/composite` `/mask` `/retype`

## Step 0 — check what you have

1. **Is the official `@Adobe` connector available?** If it covers the task, **prefer it** —
   it runs server-side with no desktop dependency. Driving the UI is the fallback.
2. **Is computer use available**, with Photoshop actually open or installed? You cannot
   switch computer use on yourself.
3. **Is there an open document**, and does the user want to work in it or start fresh?

If none of this is available, generate the assets, state the layer structure you'd have
built, and hand off. **Never imply a PSD was created when it wasn't.**

## Before anything else — is this an edit or a build?

**Inspect first. Generate only what the requested change actually needs.**

"Change the headline", "trim this clip", "export this", "move that" are **edits**. They must
not generate new artwork, footage or music. Open what exists, find the specific element, and
change it.

Only generate when something genuinely required is missing. A six-second clip asked to be
five seconds gets **trimmed**, not regenerated.

## The preservation rule

One rule, applied consistently:

> **Preserve unrelated work. Modify exactly the element the user asked about. Verify the
> change landed and that nothing else moved.**

This is not "never replace anything" — the user may well want an element replaced. It means
never touch what they didn't ask about. And note that *adding* is not automatically safe:
a layer placed on top can hide what's beneath it, and a clip on a new track can duplicate
audio. Check what your addition covers.

## The workflow

1. **Establish the composition.** What is the background, what is the subject, what type
   goes on it, and what is the final output size.
2. **Generate only what's missing** with ImagineArt. Use `remove_background` for a subject
   that needs to sit on its own layer.
3. **Place each asset on its own named layer** — File > Place Embedded, never Place Linked,
   so the document travels.
4. **Mask rather than erase.** A layer mask is reversible; erased pixels are not.
5. **Add type as real editable type layers.** Never rasterize, never use generated text.
6. **Verify by screenshot after each meaningful change** — read the Layers panel, don't
   assume the click landed.
7. **Save the PSD, then export** the flat file separately.
8. **Report what you verified** and what you couldn't.

## Hard rules

- **Never flatten**, and never Save over the user's original — Save As a new file.
- **Never use fixed screen coordinates.** Find panels and controls by what they look like.
- **Never bake text into a generated image.** Diffusion can't render reliable letterforms,
  and baked text isn't editable.
- **Name every layer.** An unnamed stack of "Layer 1, Layer 2" is not a deliverable.
- **If a step fails twice, stop** and describe what you see.

## Done means reopened, not saved

"The file exists" is too weak. Before reporting success, confirm:

- The **PSD reopens**.
- **Type layers are still editable type**, not rasterized.
- **Masks are intact** and nothing was erased destructively.
- Placed assets are still Smart Objects.
- The user's original file is untouched.

State explicitly what you verified and what you could not.

## The follow-up edit test

"Change only the headline" must edit the type layer and leave the image, the masks and
every other layer untouched. Find the existing type layer; don't rebuild the document.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
