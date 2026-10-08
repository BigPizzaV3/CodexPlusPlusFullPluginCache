# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/software-data-ai-copilot/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and all declared asset paths remain inside the skill.
- [ ] Logo and composer icon are square supported image files.
- [ ] No secret, credential, private repository content, or user-specific data is bundled.

## Listing
- [ ] Display name is 30 characters or fewer.
- [ ] Subtitle is 30 characters or fewer.
- [ ] Long description is 4,000 characters or fewer.
- [ ] Capabilities are one line and 120 characters or fewer each.
- [ ] There are at most 3 starter prompts and each is 128 characters or fewer.
- [ ] Category is `Developer Tools`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Review material
- [ ] Review the five positive test cases.
- [ ] Review the three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete country/region availability.
- [ ] Complete policy attestations.
- [ ] Wait for bundled skill safety/security scans to complete.

## Scope
Version 0.1.0 is skills-only. It does not connect to repositories, run code, execute tests, deploy software, or modify external systems unless a future tool integration is explicitly added.
