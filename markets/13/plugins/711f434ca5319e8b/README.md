# Maktkartan ChatGPT package

This directory is the portable, read-only Agent Plugins package for Maktkartan. It is intentionally separate from the MCP implementation so a reviewer can inspect exactly what will be submitted.

## Contents

- `plugin.json` is the OpenAI-facing portable plugin manifest.
- `mcp.json` points to the one public, unauthenticated Streamable HTTP endpoint: `https://maktkartan.se/mcp`.
- `assets/icon.png` is the package icon.

The package describes five read-only tools:

- `search({ query })` searches the bilingual public guide and government-status index and returns at most ten standard MCP search results (`id`, `title`, `url`).
- `fetch({ id })` returns an allowlisted public guide or government-status document with text, link and provenance metadata.
- `get_parliament_members({ party?, constituency?, limit?, offset? })` returns public parliamentary-member data. `limit` is capped at 50.
- `get_state_budget({ area_number? })` returns published state-budget information; `area_number` is restricted to 1 through 27.
- `get_government_status({})` returns the published government-status record.

Guide fetches preserve publication/edit dates and primary sources. Government status preserves recorded check/review dates. Member and budget results preserve snapshot/file mode and read dates; budget results also state units and reporting period. Article edits are not fresh source checks. Fetched documents and data responses carry their own limitations; search returns only standard document identifiers, titles and canonical URLs. The MCP server does not accept arbitrary URLs, private material, political-quiz responses, tracking preferences or any write operation.

## Local package checks

Run the dependency-free structural gate from the repository root:

```sh
node scripts/check-chatgpt-package.mjs --draft
```

The manifest includes a `demo_recording_url` for the actual ChatGPT test walkthrough. The command confirms package contents, portable manifest fields, the single unauthenticated HTTPS MCP server, icon format, review coverage, local walkthrough assets and absence of secret configuration. The recording is an ordered sequence of actual screenshots, not a continuous screen capture.

After the public policy pages are verified, this optional network check confirms their availability:

```sh
node scripts/check-chatgpt-package.mjs --live
```

It does not claim that the MCP endpoint works or that ChatGPT has approved the package. Test the actual endpoint with a compatible MCP client before submitting it.

## Build the upload archive

```sh
node scripts/package-chatgpt-plugin.mjs
```

The script runs the draft gate, creates `dist/maktkartan-chatgpt-plugin-<version>.zip` with the explicit package allowlist (never a broad `zip -r` of the repository), and prints its SHA-256. `dist/` is ignored by Git. The archive contains only:

```text
plugin.json
mcp.json
assets/icon.png
README.md
```

## Submission sequence

1. Test all five tools against the live MCP endpoint and record real outputs for the review cases.
2. Verify ownership of `maktkartan.se` in the publisher flow. Follow the current domain-verification instructions. Publish only the exact public challenge at the provider-specified path; never invent a challenge or include private credentials.
3. Upload the generated ZIP in the current ChatGPT developer or marketplace publisher flow and confirm the declared `demo_recording_url` plays in a public browser before submitting.
4. Submit for review after the live tool behaviour matches the manifest. Marketplace approval and directory listing are separate outcomes and are not implied by this package.

Maktkartan is independently run by Adrian Martén. Public site, support, privacy and terms pages are declared in `plugin.json`.
