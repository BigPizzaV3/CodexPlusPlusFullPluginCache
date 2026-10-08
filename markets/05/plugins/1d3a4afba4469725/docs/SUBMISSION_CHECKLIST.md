# OpenAI submission checklist

This archive is packaged as a skills-only plugin. In the OpenAI plugin submission portal, choose **Skills only** and upload the final skill bundle from this tested file tree.

## Included in the archive

- Required plugin manifest at `.codex-plugin/plugin.json`
- Square plugin artwork at `assets/logo.png`, referenced by both `interface.composerIcon` and `interface.logo`
- Final skill at `skills/spend-management-analysis/`
- OpenAI UI metadata at `skills/spend-management-analysis/agents/openai.yaml`
- Referenced analysis, LEDES, and export guidance
- Deterministic LEDES parser and workbook exporter
- Automated regression tests for spreadsheet-injection defenses, strict LEDES validation, fixture references, synthetic labeling, and the five-tab workbook contract
- Six positive and three negative submission test cases
- Explicitly labeled synthetic fixtures and representative expected outputs, including the completed Brightflag-style run
- Quick-start and OpenAI porting notes

## Portal information already represented in the package

- Plugin name: Spend Management Analysis
- Publisher: LegalEng Consulting Group (LECG)
- Category: Productivity
- Short and long descriptions: `.codex-plugin/plugin.json`
- Starter prompts: `.codex-plugin/plugin.json`
- Test cases: `tests/submission-test-cases.json`

## Portal-only materials the publisher must supply

- A verified developer or business identity in the OpenAI Platform
- Apps Management write access for the submitter
- Country or region availability selections
- Final policy attestations

Website, support, privacy-policy, and terms-of-service URLs are optional for this skills-only submission under the current validation rules. The publisher should supply them when accurate public URLs are available; do not use placeholders. These URLs are required if the plugin later adds an MCP server.

These items are intentionally not invented or embedded as placeholders because they must be accurate public publisher information.

## Suggested initial release notes

Initial submission of Spend Management Analysis, a skills-only plugin that analyzes uploaded legal e-billing, outside-counsel spend, law-firm timekeeping, and matter-economics data. It produces an audience-tailored report, ranked action plan, Excel workbook, and findings CSV; supports CSV, Excel, and strictly validated LEDES 1998B inputs; protects workbook and CSV exports from formula injection; and identifies AI-leverage opportunities only when task-level evidence supports them, without inventing savings estimates. The package has no MCP server, authentication, live system access, or custom UI.

## Local verification

Run the commands in `tests/TEST_MATRIX.md` from the plugin root before rebuilding the submission archive. All automated tests and both package validators must pass, and the five reference workbooks must be visually inspected after regeneration.

## Final portal check

Before selecting **Submit for Review**, confirm the public listing, publisher identity, any supplied public URLs, starter prompts, test cases, availability, release notes, and attestations all match the final package. The selected verified identity must match `LegalEng Consulting Group (LECG)`; change the manifest only after the publisher supplies a different verified identity.
