# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/unix-copilot/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and references only in-package assets.
- [ ] Branding assets are valid and square.
- [ ] No credentials, personal shell history, private paths, production secrets, or user-specific data are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Long description is at most 4,000 characters.
- [ ] Capabilities are at most 20 and each is at most 120 characters.
- [ ] Starter prompts are at most 3 and each is at most 128 characters.
- [ ] Category is `Developer Tools`.
- [ ] Developer identity matches the verified OpenAI Platform identity.

## Review
- [ ] Review five positive test cases.
- [ ] Review three negative test cases.
- [ ] Add/update release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It generates and reviews commands and scripts but does not execute commands, inspect the user's machine, install packages, change files, or modify system state by itself.
