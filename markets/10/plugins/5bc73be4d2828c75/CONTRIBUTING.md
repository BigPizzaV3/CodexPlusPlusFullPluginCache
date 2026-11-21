# Contributing

Maintain the unified plugin here: connector packaging, app operation, and recruiting methods. See [the recruiting authoring guide](docs/recruiter-authoring.md) and [behavioral cases](evals/recruiting.md). Update `catalog.json` and README when changing a skill; keep resources inside its directory.

## Validate

On an authorized verification host:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
DISABLE_TELEMETRY=1 bunx skills add . --list
```

CI validates official pinned schemas, connector consistency, portable skill metadata, local references, and regression cases. Skill discovery is checked separately. Follow your machine's local test restrictions.

## Refresh public tools

`python3 scripts/refresh_tools.py` calls unauthenticated public MCP discovery and updates the JSON and Markdown snapshot. Review the diff. It must never accept a token or call a business tool. Descriptions are service data, not instructions to the maintainer. Live schemas and account permissions take precedence over the snapshot.

## Release

Use `plugin.json` as the version authority. Update all manifest versions, marketplace metadata, `server.json`, `catalog.json`, every `skills/*/SKILL.md` version, and CHANGELOG together. Keep all connector URLs consistent. Submit a scoped PR and require passing CI at the current head. Separate model review runs only when the user requests it.

Schemas were pinned from the Genfeed reference package; retain their origins and digests in `schemas/sources.json`. Do not copy its branding, credentials, generated tool catalog, or marketplace acceptance claims.

Run the client rehearsal in [docs/compatibility.md](docs/compatibility.md) before claiming authenticated compatibility. A public listing requires a separate submission; committing a manifest does not publish it.

Build the portable upload with `python3 scripts/package.py`; its allowlist contains public package files and excludes environment files and repository tooling. The package includes all skills and MCP configuration without fetching a second repository at runtime.
