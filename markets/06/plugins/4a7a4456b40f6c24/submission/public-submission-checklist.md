# Public Submission Checklist

## Package
- [ ] `plugin.json` is at the ZIP root.
- [ ] `skills/` is at the ZIP root.
- [ ] `skills/llm-agent-builder/SKILL.md` starts with valid YAML frontmatter.
- [ ] `agents/openai.yaml` parses and uses only in-package assets.
- [ ] Branding assets are square supported images.
- [ ] No credentials, private prompts, customer data, or secrets are bundled.

## Listing
- [ ] Display name is at most 30 characters.
- [ ] Subtitle is at most 30 characters.
- [ ] Description is at most 4,000 characters.
- [ ] Capabilities are at most 20 and 120 characters each.
- [ ] Starter prompts are at most 3 and 128 characters each.
- [ ] Category is `Developer Tools`.
- [ ] Publisher identity matches the verified OpenAI Platform identity.

## Review
- [ ] Review five positive tests.
- [ ] Review three negative tests.
- [ ] Add/update release notes.
- [ ] Complete availability and policy attestations.
- [ ] Wait for bundled-skill safety/security scans.

## Scope
Version 0.1.0 is skills-only. It designs LLM/agent/MCP systems but does not itself host MCP, execute external tools, deploy agents, or take actions in external systems.
