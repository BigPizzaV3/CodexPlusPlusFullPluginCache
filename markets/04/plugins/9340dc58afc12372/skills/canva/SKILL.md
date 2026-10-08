---
name: canva
description: Generate artwork with ImagineArt and build it into an editable Canva design — add real text layers, a logo and a CTA, then resize for each destination and export. Use when the user wants a finished, editable design rather than a flat generated image. Requires browser access to Canva.
---

# Canva Finishing

The deliverable is an **editable Canva design**, not a picture. If the result is a flat
image with text burned in, this skill failed — that is what Social Studio already does.

Read `references/canva-ui.md` for the interface playbook and `references/models.md` before
generating anything.

## Tokens

| Token | What it does |
|---|---|
| `/canva` | Generate artwork, build a design, add editable text |
| `/resize` | Adapt an existing design to another size |
| `/headline` | Change only the text on an existing design |
| `/export-design` | Render and download the current Canva design |

## Step 0 — check what you actually have

Before promising anything, establish three things:

1. **Is the official `@Canva` connector available?** If it is, **prefer it** for anything it
   exposes — creating, editing, resizing, Brand Kit. It is faster and more reliable than
   driving the UI.
2. **Is computer use available?** It needs the ChatGPT desktop app, macOS or Windows, a
   Work or Codex plan, and granted permissions. You cannot switch it on yourself.
3. **Is the user signed in to Canva?** Never attempt to authenticate on their behalf.

If none of the above is available, say so in one line, generate the assets anyway, and hand
them off with the sizes and text spelled out. **Never imply a Canva design was created when
it wasn't.**

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

1. **Establish the brief.** What it advertises, the headline, the CTA, and the
   destinations (feed, story, both). Ask once, together.

2. **Generate the artwork — with room for text.** This is the step that decides whether
   the design works. Prompt for deliberate negative space where the headline and CTA will
   sit; do not let the model render any text. See `references/canva-ui.md`.

3. **Import.** Upload the generated asset through Canva's Uploads panel, then place it on
   the page as a **new element**. Never replace an existing frame in a Brand Kit template.

4. **Add text as real Canva text elements.** Headline, CTA, logo — each its own editable
   element. This is the entire point of the skill.

5. **Verify after every meaningful change.** Screenshot and read what is actually on the
   canvas. Do not assume a click landed.

6. **Resize per destination**, then export. Confirm the export finished before reporting.

7. **Report what you verified and what you didn't**, explicitly.

## Hard rules

- **Never use fixed screen coordinates.** Find elements by what they look like, every time.
  Canva's layout shifts by window size, account and release.
- **Never bake text into the generated image.** Diffusion models cannot render reliable
  letterforms, and baked text isn't editable — failing the whole purpose.
- **If a step fails twice, stop.** Describe what you see rather than clicking blindly.
- **Never claim an export exists without confirming it.**

## Done means reopened, not saved

"The export downloaded" is too weak. Before reporting success, confirm:

- The **saved design** contains the headline, CTA and logo as **separate selectable
  elements** — not flattened into the artwork.
- The exported file exists **and** is the size that was asked for.
- Every pre-existing element is still present.

State explicitly what you verified and what you could not.

## The follow-up edit test

"Change only the headline" is the request that proves this skill works. It must change the
headline text and **nothing else** — not the image, not the CTA, not the layout, not the
other sizes. Locate the existing text element, edit it in place, and verify by screenshot
that everything else is untouched.

If you cannot locate the element, say so. Do not rebuild the design.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
