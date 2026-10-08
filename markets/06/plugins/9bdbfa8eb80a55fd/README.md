# VeTayStudio Support Plugin

This package contains one customer-support skill and audited knowledge references. It is a skills-only package: it has no MCP server, remote action, authentication flow, payment action, diagnostic API, or access to a customer's computer.

## Package layout

- `plugin.json`: canonical portable Agent Plugins manifest.
- `.codex-plugin/plugin.json`: supported Codex compatibility manifest for local validation.
- `skills/vetaystudio-support/SKILL.md`: support workflow.
- `skills/vetaystudio-support/references/`: source-audited product knowledge.
- `evaluations/support_skill_cases.json`: direct, indirect, follow-up, negative, and boundary evaluation inventory.
- `PUBLICATION_CHECKLIST.md`: pre-submission metadata and unresolved public requirements.

Desktop baseline: VeTayStudio `1.0.6` on September 23, 2026. The plugin has its own package version `0.1.0`.
