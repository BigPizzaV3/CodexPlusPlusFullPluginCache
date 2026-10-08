# ProductNow OpenAI Plugin Package

This folder packages the hosted ProductNow MCP server for OpenAI plugin submission.

## Contents

- `plugin.json` - portable Agent Plugins manifest used for OpenAI upload.
- `mcp.json` - portable MCP server declaration for `https://api.productnow-prod.com/mcp`.
- `.codex-plugin/plugin.json` - Codex compatibility manifest for local plugin tooling.
- `.mcp.json` - Codex-compatible MCP server declaration.
- `assets/icon.png` - ProductNow listing and composer icon.
- `build.sh` - builds the uploadable ZIP from the nested source directory.

## Submission Package

From the repository root, run:

```bash
./marketplace/openai/build.sh
```

The script keeps the plugin source nested in `marketplace/openai`, while building
`productnow.zip` at the repository root with `plugin.json` at the root of the
archive. It includes only the manifests and referenced assets, and excludes
macOS metadata.

To write the archive somewhere else, pass an output path:

```bash
./marketplace/openai/build.sh /tmp/productnow-plugin-1.0.0.zip
```

Upload the generated ZIP in the OpenAI Plugins dashboard.

## Before Review

The manifest imports listing metadata, MCP server configuration, five positive review cases, and three negative review cases. Before submitting for review, complete the dashboard-only items:

- Enter dedicated reviewer credentials in Review details.
- Verify that the `demo_recording_url` from `plugin.json` was imported into
  Review details and that the Loom recording is accessible to reviewers. The
  manifest manages this field, so a separate dashboard URL is not required;
  update `plugin.json` and upload a new ZIP if it changes.
- Seed the reviewer test workspace with a `Plugin Review` folder containing a
  `Plugin Review Seed` document and a writable `Plugin Review Editable Seed`
  document. Give the reviewer account permission to create documents in that
  folder and edit the editable seed.
- Confirm the domain verification challenge at `https://api.productnow-prod.com/.well-known/openai-apps-challenge`.

If the reviewer seed data changes, update the review cases in `plugin.json`. The `.codex-plugin/plugin.json` file is only a local compatibility fallback and intentionally omits newer submission-only review fields.
