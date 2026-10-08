# Public Submission Checklist

## Package
- [ ] ZIP root contains `plugin.json`, `skills/`, and `assets/` directly.
- [ ] No extra outer parent directory.
- [ ] `plugin.json` parses as valid JSON.
- [ ] Package name uses only allowed characters and is <= 64 characters.
- [ ] Version uses semantic versioning.
- [ ] `skills` points to `./skills/`.

## Skill
- [ ] `skills/product-app-architect/SKILL.md` exists.
- [ ] Skill frontmatter has a non-empty name and description.
- [ ] Combined plugin/skill identity is <= 64 characters.
- [ ] Reference files are inside the skill directory.
- [ ] `agents/openai.yaml` parses as YAML.
- [ ] Skill icon path is relative to the skill root and contains no `..`.

## Listing
- [ ] Display name is <= 30 characters.
- [ ] Subtitle is <= 30 characters.
- [ ] Description is <= 4,000 characters.
- [ ] Category is supported.
- [ ] Capabilities are <= 120 characters each.
- [ ] No more than 20 capabilities.
- [ ] No more than 3 starter prompts.
- [ ] Each starter prompt is <= 128 characters.

## Branding
- [ ] Logo and composer icon exist.
- [ ] Each is square and at least 48×48.
- [ ] Each is under 5 MiB.

## Review material
- [ ] 5 positive test cases.
- [ ] 3 negative test cases.
- [ ] Release notes prepared.
- [ ] Country/region availability selected.
- [ ] Required policy attestations completed.
- [ ] Publisher identity matches a verified individual or business.

## Skills-only note
No MCP server is included in v0.1. Website/support/privacy/terms URLs are optional for a ZIP-uploaded skills-only plugin under the current submission rules.
