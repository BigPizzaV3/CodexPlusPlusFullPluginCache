# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/pottery-mentor/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and uses only in-package assets.
- [ ] Pottery icon/logo is square, text-free, and production-ready.
- [ ] No private user photos, glaze recipes, credentials, or studio records are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] At most 20 capabilities, each at most 120 characters.
- [ ] At most 3 starter prompts, each at most 128 characters.
- [ ] Category is `Education & Research`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Behavior
- [ ] Test photo critique.
- [ ] Test pottery concept image generation and source-image editing.
- [ ] Test glaze/firing troubleshooting.
- [ ] Test cone/heatwork guidance.
- [ ] Test controlled glaze testing.
- [ ] Test silica/studio-safety guidance.
- [ ] Verify it never certifies food safety from a photo.
- [ ] Verify it never recommends bypassing kiln/electrical safety controls.

## Review
- [ ] Review five positive and three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.1 is skills-only. It may use native host image-generation/editing capabilities for ceramics visualizations, but it does not control kilns, inspect live studio equipment, execute firing programs, or certify material/food safety.
