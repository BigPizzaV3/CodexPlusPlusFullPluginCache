# SwedishExpat ChatGPT package

This directory is the portable Agent Plugins package for SwedishExpat's public, read-only relocation-guide service. It is intentionally separate from the MCP implementation so the submission package can be reviewed without repository code, credentials or user data.

## Included files

- `plugin.json` is the portable Agent Plugins manifest and OpenAI presentation metadata.
- `mcp.json` configures one public, unauthenticated Streamable HTTP MCP server at `https://swedish-expats.com/mcp`.
- `assets/icon.png` is the 512 × 512 branded package icon derived from the public site favicon.
- `skills/source-cited-relocation-research/SKILL.md` directs source-cited, boundary-aware use of the two tools.

The server exposes two read-only tools:

- `search({ query })` searches the nine published Article guides and returns only public records: `id`, `title` and canonical `url`.
- `fetch({ id })` returns one allowlisted public guide with its full published `text`, canonical `url`, `metadata.primarySourceURLs`, explicit `metadata.contentReviewedAt`, and `metadata.limitations`.

`fetch` does not accept URLs. The service cannot read accounts, progress, uploads, private documents or local files, and has no write tools. It does not make official, legal or immigration eligibility decisions. `contentReviewedAt: null` means that the published guide has no guide-level review date available; it is not a fresh official-source check.

## Test-connection evidence

The public [review page](https://swedish-expats.com/integrations/chatgpt/review-1.0.0.html) hosts an actual ChatGPT custom MCP test recording. The recording demonstrates a live public-MCP connection using `search` and `fetch`, including canonical links, primary-source URLs and explicit null-review semantics. It is edited only to shorten waiting gaps and crop account-navigation areas.

Public Chrome playback was verified on 21 October 2026: the recording advanced beyond 41 seconds with readyState 4 and no media error. The manifest's `demo_recording_url` points to that reviewer page. This is evidence of a custom test connection and selected tool interaction; directory installation, submission, approval and listing remain separate outcomes.

## Local package checks

Run the dependency-free structural gate from the repository root:

```sh
node scripts/check-chatgpt-package.mjs --draft
```

This checks the package's local structure and fields, no-auth MCP configuration, strict allowlist, icon dimensions, review coverage and absence of credential-like configuration. It does not perform full remote JSON Schema validation or claim that ChatGPT has installed, approved or invoked the plugin.

After deployment, run:

```sh
node scripts/check-chatgpt-package.mjs --live
```

The live check requires expected publisher-page HTML and the MCP endpoint's JSON HTTP 405 response to GET. It does not test the MCP protocol. Use the production MCP client checks and the reviewer cases to test live tool behavior.

## Build the upload archive

```sh
node scripts/package-chatgpt.mjs
```

The script runs the draft gate, creates an explicitly allowlisted ZIP under the ignored `test-results/chatgpt-integration/` directory, and prints its SHA-256. It never archives the repository wholesale. The archive contains only:

```text
plugin.json
mcp.json
README.md
assets/icon.png
skills/source-cited-relocation-research/SKILL.md
```

## Submission sequence

1. Confirm the recording plays publicly, then add a `demo_recording_url` only if the current publisher flow requests one.
2. Run every positive and negative case against the live MCP server and retain the real outputs.
3. Follow the current ChatGPT publisher flow for any requested domain verification. Publish only the exact public challenge at the provider-specified path; never invent a challenge or include private credentials.
4. Upload the generated ZIP through the current ChatGPT plugin submission flow. Submission, approval and directory listing are separate outcomes and are not implied by the package or the custom test connection.
