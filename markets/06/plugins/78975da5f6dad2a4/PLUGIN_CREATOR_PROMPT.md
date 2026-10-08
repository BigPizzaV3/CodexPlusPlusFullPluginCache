# Plugin Creator Prompt — Software, Data & AI Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package name: `software-data-ai-copilot`
- Public display name: `Software, Data & AI Copilot`
- Version: `0.1.0`
- Category: `Developer Tools`

## Architecture
Keep this plugin skills-only for v0.1.

Do **not** add:
- an MCP server;
- external apps/connectors;
- authentication;
- network dependencies;
- custom UI;
- hooks that execute external actions.

Preserve the root `plugin.json` and the existing skill under `skills/software-data-ai-copilot/`.

## Required behavior
The skill should remain repository-first and should:
- inspect supplied repository/files before proposing material changes;
- respect repository-specific instructions and existing patterns;
- help explain, debug, implement, review, refactor, test, migrate, and harden code;
- support software, data-engineering, ML, and LLM code;
- preserve APIs, schemas, contracts, and behavior unless change is intentional;
- prefer the smallest coherent change;
- match tests to the risk/boundary of the change;
- separate observed test/runtime results from suggested validation;
- never invent files, APIs, dependencies, environment variables, schemas, test results, or repository capabilities;
- use current primary documentation when APIs, SDKs, frameworks, runtimes, packages, or security behavior are version-sensitive.

## Files to preserve
Preserve `SKILL.md`, all reference files, `agents/openai.yaml`, branding assets, submission test cases, and listing material.

## Validate
Check ZIP/plugin root discovery, manifest schema, `skills: "./skills/"`, skill frontmatter, combined identity length, `agents/openai.yaml`, asset paths, branding dimensions, listing limits, starter prompts, and positive/negative test cases.

Do not create an MCP dependency merely because future repository actions could benefit from one. This version is intentionally instruction/resource based.
