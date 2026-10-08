---
name: premiere
description: Generate clips and music with ImagineArt and assemble them into a Premiere Pro sequence — import, lay out the timeline, trim, title, mix audio and export. Use when the user wants a cut sequence and a saved project rather than isolated clips. Requires desktop access to Premiere Pro.
---

# Premiere Finishing

Requires access to Premiere Pro through an available integration or desktop controls.
Check those capabilities before promising a project; verify save, reopen and export before
reporting completion.

The deliverable is a **saved project plus a verified export**. Loose clips in a folder are
what Motion already produces.

Read `references/premiere-ui.md` before touching the app and `references/models.md` before
generating — durations and resolutions are per-model and matter more here than anywhere
else, because mismatched footage breaks a sequence.

## Tokens

`/premiere` `/assemble` `/timeline` `/cut` `/titles` `/mix` `/export`

## Step 0 — check what you have

1. **Is an integration available that explicitly supports Premiere Pro?** Inspect its
   exposed tools before using it; an Adobe integration may cover a different application.
2. **Is computer use available**, with Premiere open or installed?
3. **Is there an open project and sequence**, or does one need creating?

If app access is unavailable, state that limitation. Offer a clip-and-edit-plan handoff;
generate assets only if the user wants that fallback. **Never imply a project was created
when it wasn't.**

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

## Plan the cut before generating anything

This is where this skill is won or lost. Decide first:

- **Total duration** and how it divides across shots
- **Aspect ratio and resolution** — every clip must match, or the sequence letterboxes
- **Shot list** — what each clip shows and how long it holds

Then generate to that plan. Generating first and cutting later wastes credits on clips
that don't fit.

Choose source aspect ratios and resolutions for the target sequence. Generate a supported
duration long enough for each shot, then trim locally. For example, a six-second source
can supply a five-second shot without regeneration. See `references/models.md`.

## The workflow

1. **Plan** the cut as above.
2. **Generate only missing assets** with `generate_video` or `generate_music`, to plan.
3. **Import** into the Project panel, then drag to the timeline.
4. **Place clips at the planned times and tracks.** For an existing edit, change only the
   requested clips and check overlays and linked audio; a higher track can hide prior work.
5. **Trim** to the planned durations.
6. **Titles** — text layers in **Properties** (Premiere 25.0+) or **Essential Graphics**
   (earlier). **Captions** are a choice: editable Premiere captions, or burned-in via
   `generate_video_captions`. Say which one you're delivering.
7. **Mix** — duck the music under any voice; don't leave it at full level.
8. **Save the project, then export**, and confirm the file exists.
9. **Report** what you verified and what you couldn't.

## Hard rules

- **Never use fixed screen coordinates.**
- **Never report an export you didn't confirm.** Exports queue and fail silently.
- **Sequence settings must match the footage** — check before laying anything down.
- **If a step fails twice, stop** and describe what you see.

## Done means reopened, not queued

"The export started" is the most common false success in this skill. Before reporting:

- The **project reopens with media online** — no red offline clips.
- The export file exists **and** its dimensions and duration match the sequence.
- The exported video actually **has picture and audio**, not black or silence.
- No pre-existing clip was hidden, replaced, or duplicated in audio.

State explicitly what you verified and what you could not.

## The follow-up edit test

"Change only the second clip" must replace that one clip and leave the rest of the
timeline, the titles and the audio mix untouched.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.
