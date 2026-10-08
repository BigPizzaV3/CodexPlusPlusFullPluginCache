# Power BI Report Builder Copilot Plugin

Version: 0.1.0

This is a **skills-only portable Agent Plugins package** for Power BI report development and troubleshooting. It intentionally does not include MCP, authentication, external services, or actions in v0.1.

## Why skills-only first

The core value is a reusable expert workflow around user-supplied Power BI artifacts:
- RDL / paginated reports;
- Report Builder datasets, parameters, tablix, expressions, and layout;
- PDF / Excel / print / delivery issues;
- semantic models, DAX, Power Query, and relationships;
- Fabric storage-mode and architecture choices;
- performance and security review.

An MCP server becomes useful later only if the plugin should inspect live Fabric/Power BI workspaces, execute queries, read refresh history, publish reports, manage subscriptions, or take other authenticated actions.

## Package layout

```text
power-bi-report-builder-copilot-plugin/
├── plugin.json
├── README.md
├── PLUGIN_CREATOR_PROMPT.md
├── assets/
│   ├── icon.svg
│   └── logo.svg
├── docs/
│   └── RESEARCH_NOTES.md
├── skills/
│   └── power-bi-report-builder-copilot/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       ├── assets/
│       │   └── icon.svg
│       └── references/
│           ├── paginated_report_patterns.md
│           ├── paginated_export_delivery_reference.md
│           ├── semantic_model_dax_patterns.md
│           ├── power_bi_architecture_patterns.md
│           ├── power_bi_performance_security_playbook.md
│           └── official_source_registry.md
└── submission/
    ├── listing-and-prompts.md
    ├── test-cases.md
    ├── public-submission-checklist.md
    └── release-notes.md
```

## Local testing

Use the attached `PLUGIN_CREATOR_PROMPT.md` with `@plugin-creator` when you are ready to create a personal/local test plugin. Do not add MCP for v0.1.

Test with real examples across these modes:
1. paginated report / RDL debugging;
2. parameters and tablix;
3. PDF/Excel export;
4. DAX/model debugging;
5. Fabric architecture;
6. performance/security.

## Public submission later

The `submission/` directory contains starter prompts, five positive tests, three negative tests, listing copy, and a checklist aligned to current OpenAI public-plugin submission requirements.

Before public submission, confirm the publisher identity, production logo, public website/support/privacy/terms requirements applicable to the final submission, and current category/metadata rules.
