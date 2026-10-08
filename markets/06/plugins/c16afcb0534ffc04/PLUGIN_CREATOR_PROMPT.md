# Plugin Creator Prompt — Product & App Architect

Create a plugin from the attached `product-app-architect-plugin.zip`.

## Requirements

- Plugin name: `product-app-architect`
- Public display name: **Product & App Architect**
- Version: `0.1.0`
- Keep this as a **skills-only plugin**.
- Do **not** add MCP servers, external apps, authentication, hooks, custom UI, or network dependencies.
- Preserve the existing `SKILL.md`, reference files, icon, manifest metadata, starter prompts, and test cases.
- Use the existing root `plugin.json` as the portable plugin manifest.
- Confirm the skill is discovered from `./skills/`.
- Confirm `skills/product-app-architect/agents/openai.yaml` uses `./assets/icon.svg` relative to the skill root.
- Do not replace the supplied branding unless the asset is invalid.
- Validate that all declared asset paths stay inside the plugin and contain no `..` traversal.
- Do not create or infer product claims, integrations, APIs, or external capabilities that are not in the package.

## Intended behavior

The plugin should help users:
1. frame product ideas around a real user/problem;
2. distinguish evidence from assumptions;
3. define the smallest useful MVP;
4. audit existing products before proposing redesigns;
5. create feature specs, UX flows, PRDs, and acceptance criteria;
6. recommend the simplest architecture that satisfies real requirements;
7. consider security, accessibility, reliability, performance, operability, and cost when relevant;
8. create phased build plans and implementation-ready engineering handoffs.

## Important behavior rules

- Product reasoning comes before architecture.
- Do not invent users, market demand, metrics, repository capabilities, pricing, integrations, or constraints.
- Do not automatically add AI, accounts, subscriptions, notifications, microservices, queues, admin panels, social features, or real-time systems.
- Prefer a small complete vertical slice over broad incomplete scope.
- Separate observed facts from inference.
- Research current platform/API/competitor details when they materially affect the recommendation.
- Do not claim to inspect a repository, analytics system, design file, or deployed app unless that material was actually supplied or an enabled tool accessed it.

## Validation

Validate:
- root `plugin.json`;
- skill discovery;
- skill frontmatter;
- `agents/openai.yaml`;
- logo/composer icon paths;
- starter-prompt limits;
- public display-name and subtitle limits;
- five positive and three negative submission tests.

Return any validation errors clearly. Do not install, publish, or change discoverability unless I explicitly ask.
