# Product & App Architect Plugin

A skills-only plugin for turning ideas, existing products, feature requests, screenshots, repositories, and constraints into focused product plans, UX flows, PRDs, architecture decisions, and engineering handoffs.

## Recommended public name

**Product & App Architect**

The original working name, **Product Builder & App Architect**, is over the current 30-character public display-name limit.

## Package structure

```text
plugin.json
assets/
skills/product-app-architect/
  SKILL.md
  agents/openai.yaml
  assets/icon.svg
  references/
submission/
docs/
```

## Architecture

Version 0.1 is skills-only. No MCP server is required.

## Primary workflows

- Product discovery and MVP definition
- Existing-product audits
- Feature design and delta specs
- UX flows and state design
- PRDs and acceptance criteria
- Application architecture
- Security, accessibility, reliability, and cost considerations
- Phased build plans and engineering handoffs
- Launch-readiness review

## Upload

Upload the ZIP with `plugin.json`, `skills/`, and `assets/` directly at the ZIP root. Do not wrap the entire package in an extra parent folder.

## Testing

Use the cases in `submission/test-cases.md` before public submission. Confirm both activation and output quality.

## Publishing

The package includes listing copy, starter prompts, test cases, release notes, and a submission checklist. Do not add MCP unless a future version genuinely needs live authenticated data or actions.
