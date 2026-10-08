# CSC workbench UI port

This directory contains the shared presentation and interaction modules ported
from `chatgpt/web/src/codex-security` at
`6bfb775837eba4ca38c5e5d0d48ae0d69563ab53`.

The port covers the workbench frame and navigation, overview dashboard,
findings collection and details, scans collection and details, repository
overview and nested repository views, and new-scan setup. The top-level page
modules keep data loading and mutations close to the Codex Security Cloud MCP
operations; this directory holds the reusable workbench UI.

## Plugin adaptations

- Codex Security Cloud MCP operations replace the web application's data signals.
- Routes are relative to the plugin router, and external links use the host
  bridge.
- Controls and icons come from the bundled platform UI kit and `@oai/icons`.
  OpenAI Sans fonts are bundled as assets; no Codex application code is imported.
- A viewport subscription replaces the host responsive signal.
- Overview follows the summary, pipeline, Needs attention, and paired-chart
  order in the design. The eight-row preview reuses finding table primitives.
  Chart geometry comes from dashboard aggregates; shared controls and theme
  tokens remain in use. Exact chart values remain available to screen readers
  without additional disclosure controls. No host chart runtime is required.
- New Scan uses the plugin's existing operations for both modes: Commit
  changes creates continuous monitoring, while Repository launches a one-time
  full-repository workflow.
- Scan details request findings with `scan_id`; the backend filters and paginates
  the results for that workflow or commit execution.

No web application runtime, browser credentials, or new host API is included.
The build declares the shared controls' dependencies explicitly. See
`../../docs/design/figma-alignment.md` for the design references, custom
composition, and intentional data-driven differences.

## Local validation

Sync the maintained source into the build package before running its checks:

```sh
rsync -a --delete --exclude '.gitignore' --exclude 'BUILD.bazel' \
  chatgpt/oai-maintained-plugins/plugins/defense-factory/.internal/defense-factory-ui/ \
  api/sheep/packs/defense_factory/defense-factory-ui/plugin/
```

Then run the package TypeScript check, Vite production build, and resource
test from `api/sheep/packs/defense_factory/defense-factory-ui`.
