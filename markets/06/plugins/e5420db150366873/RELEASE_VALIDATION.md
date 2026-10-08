# Release Validation

Validation date: 2026-09-21

## Results

- Original V1 deterministic finance tests: 4 passed.
- V2 unit and contract tests: 42 test methods passed, including 120 parameterized deterministic calculation cases.
- Behavioral regression inventory: 130 cases with unique IDs and explicit must and must-not assertions.
- Skill validation: all 28 Skill packages passed the official Skill validator.
- Plugin validation: passed the official plugin validator.
- Package audit: 92 JSON files parsed, 503 Markdown files inspected, and 50 Python files compiled without errors.
- Integrity check: passed with 106 modules, 13 appendices, 14 master labs, 28 skills, 36 sector model templates, and the expected canonical DOCX hash.
- V1 baseline preservation: 540 manifested V1 files checked; no baseline files missing after safe restoration of 23 manifest-listed Master Lab mirrors omitted by the source ZIP; no canonical changes; no unexpected changes.
- Server boundary: no .mcp.json and no mcpServers manifest entry.
- Marketplace assets: composer icon and logo are valid square PNG files.

## Scope and residual risk

The deterministic tools, package structure, schemas, and behavioral contracts were executed locally. The 130 behavioral cases are structured evaluation specifications rather than 130 live model runs against external companies. Live research quality still depends on source availability and on the executing model following the mandatory browsing, provenance, and audit instructions.
