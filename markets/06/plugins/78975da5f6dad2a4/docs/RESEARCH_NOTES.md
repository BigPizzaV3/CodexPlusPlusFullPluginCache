# Research Notes — Software, Data & AI Copilot

Research date: 2026-09-23

## Recommended name
Public name: **Software, Data & AI Copilot**

The earlier name, “Software, Data & AI Coding Copilot,” is longer and more repetitive. The shorter name still describes the scope while the subtitle explains the coding function.

Package/skill name: `software-data-ai-copilot`

## Recommended architecture
Use a **skills-only plugin** for v0.1.

OpenAI's current plugin documentation supports plugins containing skills, MCP servers, or both. A skill can work without MCP when it needs only packaged instructions/resources. This copilot's current value is repository-aware reasoning, implementation discipline, testing strategy, code review, and engineering guidance, so an MCP server is not required for the first public version.

MCP would become useful later for controlled live actions such as repository reading/writing, running tests, CI status, code search, issue/PR operations, or deployment systems.

## Current packaging requirements checked
- Portable plugin uses root `plugin.json`.
- `skills` points to `./skills/`.
- Every skill is an immediate child of `skills/` and contains `SKILL.md`.
- `SKILL.md` has YAML frontmatter with `name` and `description`.
- Final directory display name: max 30 characters.
- Final subtitle: max 30 characters.
- Long description: max 4,000 characters.
- Capabilities: max 20; max 120 characters each.
- Starter prompts: max 3; max 128 characters each.
- Skill agent metadata belongs in `skills/<skill>/agents/openai.yaml`.
- Declared asset paths start with `./`, remain inside the package, and do not use `..` traversal.
- Public publication requires verified developer/business identity and required policy attestations.
- Bundled skills must pass safety/security scans.

Official OpenAI references:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Engineering-security references
- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OpenSSF developer resources: https://best.openssf.org/developers.html
- OpenSSF secure software guiding principles: https://best.openssf.org/SecureSoftwareGuidingPrinciples.html
- OpenSSF guides: https://openssf.org/resources/guides/

OpenSSF publishes guidance for secure software development and security-focused instructions for AI code assistants. These references are current security context, not a replacement for project-specific rules or official framework documentation.

## Scope decisions
The skill remains repository-first:
1. inspect relevant code and repository instructions;
2. understand requested behavior and existing contracts;
3. prefer the smallest coherent change;
4. validate with tests matched to risk;
5. distinguish observed results from recommended checks;
6. verify version-sensitive APIs/SDKs from primary documentation.

The plugin deliberately does not claim to run code, tests, migrations, or deployments without an enabled tool that actually does so.
