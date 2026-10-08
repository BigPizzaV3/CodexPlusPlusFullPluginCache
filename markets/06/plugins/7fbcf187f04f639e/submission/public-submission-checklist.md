# Public Submission Checklist

## Package
- [x] Root `plugin.json` exists at ZIP root.
- [x] `skills/sql-copilot/SKILL.md` exists.
- [x] `skills` is declared as `./skills/`.
- [x] Declared asset paths start with `./` and contain no `..` traversal.
- [x] Plugin icon/logo are square SVG assets.
- [x] Skill icon exists at `skills/sql-copilot/assets/icon.svg`.
- [x] Skills-only architecture: no MCP server required for v0.1.

## Listing
- [x] Display name: SQL Copilot.
- [x] Short description prepared.
- [x] Long description prepared.
- [x] Category prepared.
- [x] Capabilities prepared.
- [x] Three starter prompts prepared.
- [ ] Add public website URL.
- [ ] Add support URL.
- [ ] Add privacy-policy URL.
- [ ] Add terms URL.

## Review materials
- [x] Five positive test cases.
- [x] Three negative test cases.
- [x] Initial release notes.
- [ ] Choose supported countries/regions.
- [ ] Complete required policy attestations.

## Publisher
- [ ] Verify individual or business identity in the OpenAI Platform.
- [ ] Confirm the publishing identity matches the listing/support/legal URLs.
- [ ] Confirm Apps Management write access for the submitting organization/project.

## Final manual checks
- [ ] Upload ZIP and confirm no missing asset/skill errors.
- [ ] Test starter prompts.
- [ ] Test PostgreSQL, SQL Server, Snowflake, BigQuery, and Databricks examples.
- [ ] Test a destructive-write request and confirm preview-first behavior.
- [ ] Confirm the plugin never claims it ran SQL without an execution tool.
