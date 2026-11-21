# 9to5 Coverage plugin

This directory is a portable plugin package for ChatGPT and Codex. It bundles the existing
`improve-coverage-with-9to5` skill and connects to the production read-only MCP
server. It contains no credentials and requires no local server or new dependencies.

## Install locally

Add the following entry to `plugins` in this repository's
`.agents/plugins/marketplace.json` (create the catalog if it does not exist):

```json
{
  "name": "9to5-local",
  "interface": {"displayName": "9to5 local plugins"},
  "plugins": [
    {
      "name": "9to5-coverage",
      "source": {"source": "local", "path": "./integrations"},
      "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
      "category": "Developer Tools"
    }
  ]
}
```

Paths resolve from the repository root. Preserve any other catalog entries.
Restart Codex, open the Plugins directory, select **9to5 local plugins**, and
install **9to5 Coverage**. Complete OAuth authorization when prompted and review
the `coverage:read` permission. A manually configured `9to5_coverage` MCP server
is an alternative connection; avoid enabling both copies.

The GitHub App must already be installed for the repository, and CI must have
uploaded coverage. In a new chat with that repository's checkout, ask:

> Use 9to5 Coverage to inspect OWNER/REPO PR NUMBER, identify uncovered changed
> lines, and add focused tests. Report the tested SHA and what remains unverified
> until CI uploads coverage for the new commit.

Verify repository discovery, PR coverage, and uncovered changed lines after
sign-in. The plugin reads coverage metadata; source inspection, edits, and tests
use the authorized local checkout. Fresh hosted coverage is required to confirm
improvement.

## Package and publish

From the repository root:

```sh
cd integrations
zip -r /tmp/9to5-coverage-plugin.zip plugin.json mcp.json skills assets README.md
```

This package has not been installed, authenticated, or submitted to the public
directory by creating these files. Public distribution requires submission and
review of the HTTPS MCP integration, authentication, and plugin metadata.

The portal verifies domain ownership at
`https://coverage.9to5.software/.well-known/openai-apps-challenge`.
Set `OPENAI_APPS_CHALLENGE` in the production environment to the exact token from
the portal; the endpoint returns only that token as plain text, or 404 when
unset. Preserve an existing challenge used by another plugin.

## Interactive report

In hosts supporting MCP Apps, `show_pr_coverage` displays the authenticated PR
report as a card. Refresh loads the latest run; pagination and file details keep
the displayed commit, run ID, version, and format. File details include unchanged
lines; use `get_uncovered_changed_lines` for changed-line test targets.

The HTML resource is served by the production MCP server, not bundled in this
ZIP. Deploy the server before validating the uploaded plugin. Run its UI check:

```sh
node --test --experimental-test-coverage --test-coverage-include='priv/mcp/pr-coverage.mjs' --test-coverage-lines=100 priv/mcp/pr-coverage.test.mjs
```

See the [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins)
and [submission guide](https://developers.openai.com/plugins/deploy/submission).
