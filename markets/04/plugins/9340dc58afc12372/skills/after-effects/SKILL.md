---
name: after-effects
description: Generate assets with ImagineArt and build them into an editable After Effects composition — layers, keyframes, animated text and precomps, then render. Use for motion graphics, logo reveals, animated titles and layered comps. Requires desktop access to After Effects.
---

# After Effects Finishing

Requires access to After Effects through an available integration or desktop controls.
Check those capabilities before promising a project; verify save, reopen and render before
reporting completion.

The deliverable is an **editable composition** — layers, keyframes and live text a
motion designer can keep working in. A rendered MP4 alone is what Motion already gives you.

Read `references/after-effects-ui.md` before touching the app and `references/models.md`
before generating.

## Tokens

`/after-effects` `/ae` `/comp` `/animate-text` `/animate-logo` `/lower-third` `/render`

`/logo-reveal` belongs to **Brand Studio**, which generates the reveal. Use `/animate-logo`
here when the logo must be animated *inside an existing composition* instead.

## Step 0 — check what you have

1. **Is an integration available that explicitly supports After Effects?** Inspect its
   exposed tools before using it; an Adobe integration may cover a different application.
2. **Is computer use available**, with After Effects open or installed?
3. **Is there an open project and composition**, and what are its frame rate, duration and
   frame size? Everything downstream depends on these three numbers.

If app access is unavailable, state that limitation. Offer an asset-and-timing handoff;
generate assets only if the user wants that fallback. **Never imply a comp was created
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

## Why this skill exists

Diffusion models cannot render legible text or precise vector motion. After Effects can.
So the division of labour is fixed:

| ImagineArt generates | After Effects does |
|---|---|
| Backgrounds, footage, textures, 3D logo reveals | Text, titles, lower thirds, shape animation, precise timing |

**Never ask a generation model for animated text.** Generate the plate; animate the type
in AE.

## The workflow

1. **Read the comp's frame rate, duration and frame size.** Match everything to them.
2. **Generate a missing plate only if needed** with ImagineArt — background, footage, or a 3D logo reveal via
   `generate_3d_logo_animation` (which blocks up to a minute; say so before calling it).
3. **Import** File > Import > File, then drag into the open comp.
4. **Place assets at the intended layer position.** Keep backgrounds below titles; replace
   an existing layer only when the requested edit calls for it.
5. **Add text as live text layers**, then keyframe them.
6. **Precomp groups** that belong together, so the timeline stays readable.
7. **Verify by screenshot after each meaningful change** — read the timeline.
8. **Save the project, then render**, and confirm the output exists.
9. **Report** what you verified and what you couldn't.

## Hard rules

- **Check footage timing against the comp's frame rate.** Preview mixed-rate footage;
  conform or retime only when needed and disclose timing changes.
- **Never use fixed screen coordinates.**
- **Text stays live.** Never a generated image of text, never converted to shapes unless
  asked — the point is that it stays editable.
- **Never report a render you didn't confirm.** Renders queue and fail silently.
- **If a step fails twice, stop** and describe what you see.

## Done means reopened, not queued

"The render started" is not done. Before reporting:

- The **project reopens with footage online**.
- **Text layers are still live text**, keyframes intact.
- The render output exists **and** its dimensions, frame rate and duration match the comp.
- No pre-existing layer was hidden behind what you added.

State explicitly what you verified and what you could not.

## The follow-up edit test

"Change only the headline" must edit the text layer's source text and leave every keyframe,
every other layer and the render settings untouched.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.
