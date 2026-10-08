# Better Plans 0.1.4 — release notes and checks

Publisher: Better Plans, Better Life

Date: 2026-09-24

## Scope

This is a packaging, discovery, and activation-metadata update. The Better Plans framework itself is intentionally unchanged.

### Changed

- Added a portable root `plugin.json` using the Agent Plugins 1.0.0 schema.
- Kept `.codex-plugin/plugin.json` as a compatibility fallback and updated its version to 0.1.4.
- Changed the user-facing display name from “Better Plans, Better Life” to “Better Plans”; publisher/developer identity remains “Better Plans, Better Life.”
- Preserved the directory subtitle “Clear plans for big decisions.”
- Reworked the long description to lead with user outcomes and concrete examples drawn from Better Plans positioning: weddings/trips, renovations, major purchases, career moves, and other complicated projects.
- Added dark-mode presentation fields to the portable root manifest so normalization carries `#F4F1EC` text/brand treatment and `assets/logo-dark.png` instead of requiring manual portal fixes.
- Replaced generic capabilities (`Interactive`, `Write`) with planning-specific capabilities.
- Tightened discovery keywords around planning, decision support, tradeoffs, prioritization, risk analysis, and execution planning.
- Added three starter prompts to the portable manifest. The compatibility manifest and skill UI retain the first prompt as a single default for backward compatibility.
- Refined `SKILL.md` activation metadata to remove the unnecessary “personal” limitation and explicitly cover comparing meaningful options and stress-testing an existing plan.
- Aligned `agents/openai.yaml` display name, short description, and default prompt with the plugin listing.
- Added `tests/activation-regression-0.1.4.md` with positive, negative, and boundary prompts.

### Intentionally unchanged

- The five-category primary sequence and cross-cutting Review With Others category.
- The 17-tool library and tool definitions.
- The operating reference and engineering-depth reference.
- Cumulative planning-record behavior, iteration logic, tracker, data boundaries, and external-action boundaries.
- Skills-only architecture; no MCP server, backend, custom UI, or external API dependency was added.
- Existing logo and icon asset files (the portable manifest now references the existing dark-mode logo explicitly).

## Pre-submission checks

- [ ] Upload/import the ZIP and confirm the portal recognizes `plugin.json` as the portable manifest.
- [ ] Confirm the normalized compatibility manifest preserves the intended listing metadata.
- [ ] Confirm all three starter prompts appear on the public listing/submission form.
- [ ] Run at least five positive and three negative activation cases from `activation-regression-0.1.4.md`.
- [ ] Verify a routine factual request does not trigger the full Better Plans workflow.
- [ ] Verify an existing-plan stress-test request does activate without restarting intake unnecessarily.
- [ ] Confirm light/dark branding looks correct on supported surfaces.
- [ ] Complete OpenAI's submission scans and review any normalization warnings before publishing.

## Rollback

If 0.1.4 introduces undesirable activation or listing behavior, use the unchanged 0.1.3 package as the baseline and reapply only the portable-manifest change.
