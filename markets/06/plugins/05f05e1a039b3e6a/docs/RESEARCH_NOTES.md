# Research Notes — 2026-09-23

## OpenAI plugin packaging

Current OpenAI guidance supports a portable plugin with a root `plugin.json`, skills under `skills/<skill-name>/SKILL.md`, optional assets, and optional MCP only when server-backed capabilities are needed.

A skill can work without MCP when the workflow needs only packaged instructions/resources. That is the correct v0.1 architecture for this plugin.

For public submission, current documentation requires:
- a verified developer or business identity;
- Apps Management write access for the submitter;
- listing metadata and production branding;
- starter prompts;
- at least five positive and three negative test cases;
- release notes, availability, and policy attestations.

Current final-directory metadata limits include:
- display name: 30 characters maximum;
- short description: 30 characters maximum;
- long description: 4,000 characters maximum;
- up to three starter prompts, each 128 characters maximum.

This package therefore uses `Power BI Report Copilot` as the public display name even though the package/skill identity remains `power-bi-report-builder-copilot`.

## Microsoft Power BI / Fabric research

Official Microsoft documentation confirms the core architecture represented in this skill:
- Report Builder expressions use Visual Basic expression syntax.
- Paginated report parameters can drive filtering, appearance, linking, and query inputs.
- Paginated rendering/export behavior varies by renderer, so PDF/Excel/print must be validated separately.
- URL rendering uses `rdl:` controls for current rendering behavior such as format.
- Star schema remains recommended guidance for performant and usable semantic models.
- DirectQuery performance depends on source, model, and report design; source-side optimization can be important.
- Incremental refresh relies on case-sensitive `RangeStart` and `RangeEnd` Date/Time parameters.
- Microsoft Fabric supports semantic models using Direct Lake, Import, or DirectQuery depending on the scenario.
- Direct Lake models can be edited live against the Fabric workspace in current Power BI Desktop workflows.

See `skills/power-bi-report-builder-copilot/references/official_source_registry.md` for the official source map.
