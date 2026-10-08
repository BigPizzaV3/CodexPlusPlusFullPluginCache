# Research Notes — Product & App Architect v0.1

Research date: 2026-09-23

## Recommended name

**Public display name:** Product & App Architect

Why: the original “Product Builder & App Architect” is descriptive but exceeds OpenAI’s 30-character public display-name limit. “Product & App Architect” keeps the two core jobs — product decisions and application architecture — while remaining concise.

**Package / skill name:** `product-app-architect`

## Plugin architecture

Use a **skills-only plugin** for v0.1. The workflow depends on instructions, templates, reference material, files, screenshots, repositories, and web research rather than a proprietary live service. OpenAI’s current plugin docs explicitly allow a skill to work without an MCP server when only packaged instructions and resources are required.

Add MCP later only if the plugin needs authenticated live actions such as reading a product analytics account, managing a backlog, inspecting a hosted repository through a custom service, or creating/updating external artifacts.

## Current OpenAI packaging rules used

- Root `plugin.json` with `skills: "./skills/"`.
- Skill at `skills/product-app-architect/SKILL.md`.
- Optional `references/`, `assets/`, and `agents/openai.yaml` kept inside the skill.
- Asset paths stay inside the bundle and use relative paths without `..`.
- Root plugin branding includes a square logo and composer icon.
- Public display name and subtitle are each <= 30 characters.
- Starter prompts are <= 128 characters and limited to three.
- Capabilities are one-line strings and <= 120 characters each.

## Product-design guidance incorporated

The skill keeps product discovery before architecture: problem, user, evidence, core value, validation risk, smallest useful product, UX, then system design. It deliberately avoids automatic feature expansion or architecture-by-trend.

## Security guidance

OWASP ASVS 5.0.0 is the current stable ASVS version referenced by OWASP. Use it for detailed application-security verification when security requirements need implementation-level rigor.

## Accessibility guidance

WCAG 2.2 is the current W3C Recommendation. W3C advises using WCAG 2.2 to maximize future applicability. The WAI-ARIA APG is included for accessible widget and keyboard-interaction patterns.

## Native app guidance

Apple’s current Human Interface Guidelines emphasize purpose, agency, flexibility, simplicity, craft, and delight, and contain platform-specific guidance for iOS, macOS, and other Apple platforms. App Store rules should be checked when distribution requirements can materially affect product scope.
