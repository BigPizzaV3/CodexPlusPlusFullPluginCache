# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/production-rag-genai-copilot/SKILL.md` has valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and uses only in-package asset paths.
- [ ] Branding assets are square and production-ready.
- [ ] No credentials, private corpus data, user traces, prompts, or secrets are bundled.

## Listing
- [ ] Display name is 30 characters or fewer.
- [ ] Subtitle is 30 characters or fewer.
- [ ] Description is 4,000 characters or fewer.
- [ ] Capabilities are at most 20 and 120 characters or fewer each.
- [ ] Starter prompts are at most 3 and 128 characters or fewer each.
- [ ] Category is `Developer Tools`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Review
- [ ] Review five positive test cases.
- [ ] Review three negative test cases.
- [ ] Add release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It does not query a live index, run evals, modify vector stores, call production models, or change external systems by itself.
