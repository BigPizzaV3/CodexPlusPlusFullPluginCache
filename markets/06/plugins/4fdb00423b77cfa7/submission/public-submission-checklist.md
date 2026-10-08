# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/imago/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and references only in-package assets.
- [ ] No secrets, private files, or user-specific source data are bundled.
- [ ] Replace the temporary neutral icon with the canonical Imago production logo before public submission if one exists.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] At most 20 capabilities, each at most 120 characters.
- [ ] At most 3 starter prompts, each at most 128 characters.
- [ ] Category is `Creativity`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Product behavior
- [ ] Test direct image creation.
- [ ] Test focused edits with preservation constraints.
- [ ] Test document/data-to-visual workflow.
- [ ] Test screenshot redesign.
- [ ] Test current-fact research before image generation.
- [ ] Verify the skill does not return fake file paths or prompts instead of images.

## Review
- [ ] Review five positive tests and three negative tests.
- [ ] Add/update release notes.
- [ ] Complete region availability and policy attestations.
- [ ] Wait for skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It uses image-generation/editing capabilities already available in the host product when present. It does not need its own MCP server.
