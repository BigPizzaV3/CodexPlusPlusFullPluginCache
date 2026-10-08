# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/research-writing/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and references only in-package assets.
- [ ] Branding assets are valid, square, and text-free.
- [ ] No private drafts, unpublished research, credentials, or proprietary source material are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] At most 20 capabilities, each at most 120 characters.
- [ ] At most 3 starter prompts, each at most 128 characters.
- [ ] Category is `Productivity`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Behavior
- [ ] Test current technical research.
- [ ] Test fact-check/refresh workflow.
- [ ] Test comparison report.
- [ ] Test documentation/how-to conversion.
- [ ] Test Medium + LinkedIn adaptation.
- [ ] Verify no invented sources, citations, quotations, results, or personal experience.
- [ ] Verify current claims use appropriately current evidence.

## Review
- [ ] Review five positive and three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete region availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It can use the host's research, web, file, and writing capabilities when available, but it does not need its own MCP server or publishing integration.
