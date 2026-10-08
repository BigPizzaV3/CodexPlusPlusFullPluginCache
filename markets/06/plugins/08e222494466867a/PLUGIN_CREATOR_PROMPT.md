# Plugin Creator Prompt — Atelier Pottery Mentor

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `atelier-pottery-mentor`
- Skill: `pottery-mentor`
- Display name: `Atelier Pottery Mentor`
- Version: `0.1.1`
- Category: `Education & Research`

## Product definition

Atelier is a pottery and ceramics mentor that can also create and edit ceramics-focused images using the host's native image-generation/editing capability.

It is distinct from visual-generation workflows such as Imago. Its job is to teach, critique, troubleshoot, and help users make safer technical decisions about ceramic work.

## Architecture

Keep the plugin **skills-only**. Native host image generation/editing is allowed and expected for pottery visualization requests.

Do **not** add:
- MCP;
- kiln/equipment control;
- live firing automation;
- hardware access;
- authentication;
- external database dependencies;
- custom UI.

## Required behavior

Preserve:
- honest image-based pottery critique;
- direct ceramics-focused image generation when requested;
- direct editing of uploaded pottery photos for requested visual changes;
- preservation of unrelated source-image details during targeted edits;
- explicit labeling of glaze/firing previews as conceptual rather than predictive;
- observation vs inference separation;
- wheel-throwing and handbuilding coaching;
- clay/drying/construction troubleshooting;
- glaze-defect diagnosis;
- controlled test planning;
- pyrometric cone / heatwork reasoning;
- manufacturer-first kiln safety;
- studio silica/material safety;
- food-contact caution;
- no invented hidden properties from photos;
- no fake firing/test results;
- no food-safety certification from appearance;
- no instructions to bypass kiln, gas, electrical, or fire-safety controls.

When exact cone equivalency, kiln behavior, glaze/product specification, or safety guidance is version/product specific, use current primary documentation.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- pottery branding asset
- listing material
- test cases
- research notes

## Validate
1. ZIP has one flat plugin root.
2. Root `plugin.json` is valid.
3. Root `skills/` is discoverable.
4. Skill frontmatter is valid.
5. Combined plugin/skill identity <= 64 characters.
6. Asset paths stay inside the package.
7. Display/subtitle/capability/starter-prompt limits pass.
8. Category is `Education & Research`.
9. Five positive and three negative tests are included.
10. No MCP dependency is added.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
