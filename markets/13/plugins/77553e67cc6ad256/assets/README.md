# OpenAI plugin assets

Status: Gil approved the icon set on 2026-10-20. `logo.png` and `composer-icon.png` in this folder are copies of the approved tiles from `artifacts/connector-assets/png/` and match the icons that the MCP server serves.

Source: `/Users/gilmillasseau/Personal/formasnap/artifacts/connector-assets/png/`

| Copy from | Copy to (in the ZIP) | Referenced by | Size | Format |
|---|---|---|---|---|
| `tile-square-512.png` | `assets/logo.png` | `interface.logo` | 512 x 512 px, 5.4 KB | PNG, full-bleed square |
| `tile-square-128.png` | `assets/composer-icon.png` | `interface.composerIcon` | 128 x 128 px, 1.6 KB | PNG, full-bleed square |

Rules from the [submission reference](https://developers.openai.com/plugins/deploy/submission), read 2026-10-20: PNG, JPEG, WebP or SVG. Square. At least 48 x 48 px. At most 4096 px a side. At most 5 MiB each. Paths start with `./`.

Not used: `logoDark`, `composerIconDark`, `screenshots`. The plugin has no UI, so no screenshots are needed.

Build the ZIP:

```bash
cd docs/store/openai-plugin
mkdir -p assets
cp /Users/gilmillasseau/Personal/formasnap/artifacts/connector-assets/png/tile-square-512.png assets/logo.png
cp /Users/gilmillasseau/Personal/formasnap/artifacts/connector-assets/png/tile-square-128.png assets/composer-icon.png
```

Before zipping:

1. Replace `demo_recording_url` in `plugin.json` with the unlisted video URL.
2. Check that `developerName` (`Gil Millasseau`, individual verification) equals the name that OpenAI verification shows.
3. Zip the files with `plugin.json` and `mcp.json` at the ZIP root, not inside a folder: `zip -r ../bystep-plugin.zip plugin.json mcp.json assets -x assets/README.md`.
4. Do not add `test_credentials` or `reviewer_instructions`. OpenAI rejects the ZIP. Enter credentials in the portal Review details form.

Validation, 2026-10-20: both JSON files pass the schemas at `https://agent-plugins.org/schemas/1.0.0/` (`bunx ajv-cli@5 validate --spec=draft2020`).
