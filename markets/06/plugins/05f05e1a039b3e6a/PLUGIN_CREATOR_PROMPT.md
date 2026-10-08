# Prompt for @plugin-creator

Create a **private personal/local plugin for testing** from the attached `power-bi-report-builder-copilot-plugin.zip` package.

## Identity

- Package name: `power-bi-report-builder-copilot`
- Version: `0.1.0`
- Customer-facing display name: `Power BI Report Copilot`
- Architecture: **skills-only**

## Important constraints

1. Preserve the portable root `plugin.json` as the canonical package manifest.
2. Preserve the existing skill at `skills/power-bi-report-builder-copilot/`.
3. Preserve all reference files and branding assets.
4. Do **not** add MCP servers, apps, authentication, hooks, network dependencies, or custom UI.
5. If a `.codex-plugin/plugin.json` compatibility manifest or personal marketplace entry is needed for local testing, scaffold it without changing the core behavior.
6. Do not replace the supplied logo/icon with a generated asset.
7. Validate skill discovery, paths, frontmatter, OpenAI skill metadata, interface metadata, and starter prompts.
8. Create a **personal/local marketplace entry only** so I can install and test it. Do not submit or publish it publicly.

## Required behavior

The plugin should automatically route Power BI questions into the appropriate workflow:

### Report Builder / paginated mode — default for RDL
Use for datasets, report/query parameters, tablix, grouping, filters, Visual Basic expressions, headers/footers, page breaks, PDF/Excel/print, subscriptions, URL rendering, and export behavior.

### Semantic model / DAX / Power Query mode
Use for measures, calculated columns, relationships, star schemas, wrong totals, filter context, Power Query, date tables, and model correctness.

### Fabric / architecture mode
Use for Import, DirectQuery, Direct Lake, composite models, incremental refresh, OneLake/Fabric architecture, capacity, governance, performance, and cost.

## Critical quality rules

The plugin must:
- use user-supplied files, screenshots, SQL/DAX/M, model details, and errors as evidence;
- provide exact Report Builder steps when appropriate;
- provide copy-pasteable SQL, DAX, Power Query M, or VB expressions when useful;
- identify dataset/model grain and expression/filter context before guessing;
- distinguish query filtering from report/dataset/group filtering;
- treat HTML preview, PDF, Excel, CSV, Word, and print as different rendering targets;
- never claim that a page break alone creates separate output files;
- never claim to execute, refresh, export, publish, subscribe, or deploy unless a connected tool actually did it;
- protect credentials and regulated data;
- verify current Microsoft product behavior from official documentation when current capabilities, licensing, limits, or storage-mode behavior matter.

## Validation tests

After wiring the local plugin, verify that it handles all test cases in `submission/test-cases.md` and that an unrelated request does not force a Power BI workflow.

Return:
1. what compatibility/local marketplace files were added;
2. whether manifest and skill validation passed;
3. any warnings that could affect public submission;
4. the local/private plugin or marketplace reference needed for me to test it.
