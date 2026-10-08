# Plugin Creator Prompt — Research & Writing Copilot

Create/validate a **skills-only plugin** from the attached archive.

## Identity
- Package: `research-technical-writing-copilot`
- Skill: `research-writing`
- Display name: `Research & Writing Copilot`
- Version: `0.1.0`
- Category: `Productivity`

## Product definition

This plugin turns research into trustworthy publishable technical content.

It covers:
- deep research;
- source verification;
- fact-checking;
- technical articles/blogs;
- documentation;
- explainers/tutorials;
- comparison reports;
- research briefs;
- Medium;
- LinkedIn;
- publication-ready editing.

Do not split Medium, LinkedIn, documentation, blogs, and comparison reports into separate skills. They should share one research/verification core and use publication adapters.

## Architecture

Keep v0.1 **skills-only**.

Do **not** add:
- MCP;
- CMS authentication;
- social publishing actions;
- external databases;
- custom UI.

The skill may use host-provided web, research, file, and writing capabilities when available.

## Required behavior

Preserve:
- research-question definition;
- current source verification;
- primary-source preference where appropriate;
- claim-to-source tracking;
- date/version/scope checking;
- fact vs inference vs opinion separation;
- source-reported vs independently reproduced distinction;
- conflict handling;
- explicit unknown/unverified states;
- audience-aware technical writing;
- concise/scannable structure;
- documentation/how-to patterns;
- comparison normalization and trade-offs;
- fact-check/refresh behavior that preserves supported content;
- Medium and LinkedIn as publication adapters;
- publication-specific guideline research when a publication is named;
- no invented personal experience;
- no invented citations, quotes, benchmarks, prices, dates, or URLs.

## Preserve
- `SKILL.md`
- all reference files
- `agents/openai.yaml`
- branding
- listing material
- research notes
- five positive and three negative tests

## Validate
1. ZIP root and `plugin.json`.
2. `skills: "./skills/"`.
3. Skill frontmatter.
4. Combined plugin/skill identity <= 64 characters.
5. `agents/openai.yaml`.
6. Asset paths remain inside the package.
7. Public listing limits.
8. Three starter prompts.
9. Five positive and three negative test cases.
10. No MCP/publishing dependency is added.

Do not create, install, or submit the plugin unless the user explicitly asks for that action.
