---
name: obi-image-generator
description: Generate or revise a private Open Bible Images candidate from an OBI composition and prompt package. Use when the user explicitly asks to create, generate, render, fix, revise, or try an actual Bible image; do not use it to publish or approve an image.
---

# OBI Image Generator

Create a private image candidate only after the user explicitly asks to generate, render, make, fix, or revise an image. A request for research, metadata, a prompt, a review, or a composition is not permission to generate. Read [references/generation-record.md](references/generation-record.md) when recording the result.

When a canonical project JSON file is supplied, preserve all other sections, append to `generations`, increment its artifact revision and the project revision, and append a history/capability-run entry. If generation follows feedback or review, preserve links to the originating finding and the exact upstream artifact revisions used. If no project file is supplied, label the generation record `unpersisted`.

## Workflow

1. Load the latest composition, character references, prompt package, exclusions, aspect ratio, style direction, and originating feedback/review finding when applicable.
2. Confirm that upstream issues identified by the current feedback loop have actually been resolved or deliberately left provisional. Do not use generation to conceal unresolved factual or composition problems.
3. Determine whether the generation is `working_private_draft` or `approved_generation`. A working or draft composition is sufficient for a one-off private candidate.
4. If no usable prompt package exists, compile a concise working prompt from the available project artifacts without silently changing project facts.
5. Generate the image with the available image-generation capability. If the request is a revision, include the target image and preserve elements the user did not ask to change.
6. Save the exact prompt, provider/model when known, settings, references and their intended controls, output identity, source artifact versions, and originating feedback/finding IDs.
7. Inspect the result briefly for the requested narrative moment and obvious failures. If a serious issue is visible, state it concisely and return disposition `needs_review`; do not automatically start repeated paid generations.

## Boundaries

- Never publish, approve, or submit an image.
- Require approved composition and explicit authorization before costly batch generation or formal OBI use.
- Do not add unsupported events, identities, symbols, fake writing, halos, fantasy conventions, or anachronisms.
- Do not imply exact character consistency when the generator cannot guarantee it.
- Ask a question only when the answer materially changes the image or generation cost.
- Do not trigger image generation merely because a complete prompt is available.
- Do not automatically repeat generation after a failed or imperfect result unless the user asked for iterative revision or explicitly authorizes another attempt.

## User-facing response

Lead with the generated image. Follow with a one- or two-sentence note containing only material assumptions or issues and the most useful next action, normally **Review image** when the user wants verification. Do not paste the prompt or generation record unless requested.
