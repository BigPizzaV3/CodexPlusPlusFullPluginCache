---
name: givon-ai-marketplace-cards
description: "Create the requested marketplace listing visuals through Givon AI with clear asset roles, product references and schema-supported generation inputs."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Givon AI Marketplace Cards

Build the set the user actually requested. Asset labels organize the result; the live model
catalog and schema own generation modes, inputs and settings.

## Workflow

1. Identify the requested listing assets and the purpose of each image.
2. Use product/reference media when available and assign each reference a clear role.
3. Ask only for information required to make the requested set executable when it cannot be
   inferred from the brief, attached media, current context or live schema defaults. Collect all
   such missing inputs together.
4. Use `givon-ai-create` to select an active image model and inspect its detailed schema.
5. Build each prompt from [references/prompt-structures.md](references/prompt-structures.md),
   then apply the selected model family's guidance.
6. Run separate generations or a schema-supported batch and return labeled ready assets.

Read [references/scope-selection.md](references/scope-selection.md) for useful marketplace asset
roles and set planning; derive the final set directly from the user's request.

## Set coherence

- Give each image one clear purpose and enough product context to remain recognizable.
- For a multi-image set, assign each asset a distinct buyer question and primary message.
  Replace or merge an asset that repeats another asset's main job; a fact may recur only as
  supporting context.
- Keep a shared visual system across a requested set while varying composition and message.
- Preserve exact product facts and visible identity when they are supplied as real listing data.
- Follow a creative or hypothetical brief when the user explicitly asks for one.

Default delivery contains short asset labels and ready URLs or handles. Return a prepared prompt
instead when that is the requested artifact.
