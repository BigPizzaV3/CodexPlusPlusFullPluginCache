# OpenAI porting notes

This package converts the Claude-authored `spend-management-analysis` skill into a skills-only OpenAI plugin. The analytical scope and helper scripts are preserved; no MCP server, app connection, backend, authentication, or custom UI is added.

## Structure mapping

- `.codex-plugin/plugin.json` gives the plugin a stable identity and points to `./skills/`.
- `skills/spend-management-analysis/SKILL.md` contains the concise trigger, workflow, boundaries, and reference routing.
- `skills/spend-management-analysis/agents/openai.yaml` adds OpenAI UI metadata and keeps implicit invocation enabled.
- `scripts/` contains the deterministic LEDES converter and workbook builder.
- `references/` separates detailed analysis, LEDES, and export guidance for progressive disclosure.
- `tests/` preserves the synthetic fixtures, prior outputs, and evaluation cases as regression material; it is not part of the runtime instructions.

This mapping follows OpenAI’s [Build skills](https://learn.chatgpt.com/docs/build-skills) documentation and [Package your plugin](https://developers.openai.com/plugins/build/plugins) documentation.

## Intentional changes from the Claude package

- The long activation description was shortened and given a clear exclusion for general procurement spend and legal advice.
- Product-specific UI metadata moved to `agents/openai.yaml`.
- Detailed instructions moved into routed references so hosts load only the context needed for the task.
- The plugin manifest contains no `apps` or `mcpServers` fields because the package has neither component.
- A dependency fallback explains what to do if Python or `openpyxl` is unavailable without fabricating a completed workbook.
- Workbook and findings-CSV text is neutralized before export when it begins with a spreadsheet formula-control character.
- The LEDES parser enforces the 24-column 1998B header order, record terminators, valid line types, field counts, and finite numeric fields before accepting rows.
- Golden reports and workbooks label their fixture data as synthetic, and AI-leverage sections require task codes, activity codes, or narrative work descriptions rather than matter names alone.
- `tests/test_scripts.py` covers these safety and artifact-contract requirements.
