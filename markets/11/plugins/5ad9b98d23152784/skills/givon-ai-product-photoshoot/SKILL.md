---
name: givon-ai-product-photoshoot
description: "Create or transform product visuals through Givon AI using a product brief, live model guidance and schema-supported inputs."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Givon AI Product Photoshoot

Turn the user's product brief into one or more schema-valid image generations. The brief
describes the desired visual; the live catalog and selected model schema own executable modes,
inputs, settings and defaults.

## Workflow

1. Capture the requested deliverable, product identity, reference roles and intended use.
2. Ask only for information required to make the next action executable when it cannot be
   inferred from the brief, attached media, current context or live schema defaults. Collect all
   such missing inputs together.
3. Use `givon-ai-create` to inspect active models and the selected model's detailed schema.
4. Build a compact prompt from the user's creative facts and the relevant structure in
   [references/prompt-structures.md](references/prompt-structures.md).
5. Pass product/reference media only through schema-supported asset fields.
6. Generate the requested number of results and return labeled ready assets.

Read [references/mode-selection.md](references/mode-selection.md) when the brief is incomplete
and you need to resolve blocking creative inputs. Apply the selected model family guidance
exposed by `givon-ai-create` after model selection.

## Product brief

Use only relevant dimensions:

- product identity and details to preserve;
- source/reference role;
- intended use and output container;
- scene, composition, crop, pose or interaction;
- light, material and visual direction;
- exact visible text;
- count and aspect when explicitly chosen or required.

For a series, keep a coherent visual system while giving each image a distinct purpose. Default
delivery contains short labels and ready asset URLs or handles; include implementation detail
when the user asks for it.
