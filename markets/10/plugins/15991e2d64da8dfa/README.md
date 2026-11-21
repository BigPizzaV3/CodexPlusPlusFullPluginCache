# StartupSprints workflow package

Public review preparation and remaining requirements are tracked in [the repository submission guide](https://github.com/savelkouls/StartupSprints.com/blob/main/docs/openai-submission.md). Package version 1.0.3 uses Brian's explicitly authorized verified individual publisher identity; StartupSprints remains a product of Roborian, Inc. It contains existing brand icons, verified public policy/support URLs, release notes, country targeting, five positive / three negative review scenarios, and Brian's recorded ChatGPT MCP walkthrough. The recording uses the earlier development tool catalog; that connection has since been refreshed to all 17 deployed tools. The portal accepted all five skills and passed their checks in 1.0.2. Final case execution and portal verification are tracked separately; this package remains a review draft until those checks and developer attestations are complete.

This portable Agent Plugins 1.0.0 source package contains five founder workflow skills and the existing StartupSprints Streamable HTTP connection at `https://startupsprints.com/api/mcp`. The goal is useful progress toward the founder's mission: read saved context, select the right action, produce concrete work, preserve it when authorized, and review real evidence.

The strategy coordinator provides a general entry point across the library. Customer discovery includes the detailed `problem-interviews` pilot. Other workflows follow live execution briefs and field schemas; this release does not contain a detailed procedure for every strategy.

Each `skills/<name>/` directory is self-contained. The copies of `references/mcp-workflow.md` and `references/prompt-examples.md` must remain identical across skills. No skill depends on a sibling directory. The same source files can be packaged or exposed for MCP skill import; a scan imports a snapshot rather than live-loading future edits.

Installing skills does not grant LinkedIn, Reddit, Chrome, email, or calendar access. The assistant discovers optional capabilities at runtime, confirms each intended authenticated identity, and reuses explicit bounded action approvals. Account confirmation alone never authorizes sending or publishing.

Use the intended client's supported private/local package flow to install and enable this package, then authenticate the StartupSprints MCP connection through the host's consent flow. No tokens belong in these files. Adding only the MCP URL does not by itself install persistent skills. Saving a package, installation, OAuth success, a Scan Tools import, and public directory approval are separate checks; this source package alone does not establish any of them.

Format references: [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json), [MCP schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json), and [OpenAI package guidance](https://developers.openai.com/plugins/build/plugins).

## Local installation

1. Open this repository as a trusted local project in a supported desktop client. Its `.agents/plugins/marketplace.json` points to `./integrations/openai/startupsprints`; keep that relative layout intact.
2. Restart the desktop client. Find **StartupSprints** in its local plugin marketplace, install it, and enable it. The catalog's `AVAILABLE` policy makes installation optional.
3. If your client supports project plugin configuration, enable `startupsprints@startupsprints-local` using its supported settings. For Codex, the equivalent project `.codex/config.toml` entry is shown below; merge it with existing settings rather than replacing the file.
4. Authenticate the remote MCP connection using the host's consent flow. Choose the intended eligible Director startup and only the required scopes. Confirm the returned startup with `list_startups` and `get_startup_profile` before substantive work.

```toml
[plugins."startupsprints@startupsprints-local"]
enabled = true
```

For a client that needs explicit marketplace registration, run `codex plugin marketplace add .` from the repository root. `codex plugin marketplace list` shows resolved catalog roots. These instructions follow [OpenAI's local package flow](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually); host availability and workspace policy determine the actual install surface.

The manifest connects to the production URL. To test another reachable deployment, use an isolated package copy and change its `mcp.json` URL. A cloud host cannot reach your computer's localhost endpoint without a separately configured supported route. Reload local packages after edits; never edit a host's generated plugin cache.

## MCP import and updates

For a ChatGPT development connection with an outdated tool list, open the existing plugin's **Manage** page and select **Refresh tools**. Check that all 17 tools are visible, including `get_action_workspace`, `save_action_work`, `save_asset_content`, and `record_action_result`, then start a fresh chat. Refreshing the catalog does not grant additional OAuth scopes; saving assets and recording results still require their respective consent. `record_action_result` ends an already-started attempt with an explicit completed/failed verdict; saving findings or drafts does not complete an action.

For an OpenAI MCP skill import, first deploy the updated server and connect it with the intended test account. Run **Scan Tools** in the plugin development flow, inspect the five imported skills and their supporting files, review the imported snapshot, and submit a new plugin version through that flow. Repeat the scan/version process after changing served skills. Refreshing the MCP connection alone does not update installed snapshots. See [OpenAI's MCP skills import contract](https://developers.openai.com/plugins/build/mcp-server#import-skills-from-the-mcp-server).

## Verification

Run these checks from the repository root:

```text
npm run typecheck
node --import tsx --test tests/assistant-workflows.test.ts tests/mcp-assistant.test.ts tests/mcp-discovery.test.ts
npm test
npm run build
```

The actual-route tests check initialization guidance, six prompts with optional context, startup isolation, authorization, paginated skill discovery, exact resource bytes and SHA-256 digests, invalid parameters, and URI alias rejection. Inspect `.next/server/app/api/mcp/route.js.nft.json` and `.next/standalone/integrations/openai/startupsprints/skills/` to ensure every declared supporting file reaches the deployed server.

In an installed client, verify all five skills are available, then request the customer-discovery workflow for a confirmed startup. Check that it reads the current brief and work, qualifies actual evidence, and produces an interview kit. Exercise these additional cases: absent Chrome with public research available; an unconfirmed service account; a save conflict requiring reread and merge; reused bounded outreach approval; and an ambiguous “wrap up” that leaves the attempt open pending an explicit outcome verdict.

Protocol tests and simulated skill evaluations do not establish live account access, installation, OAuth completion, Scan Tools acceptance, or a public release. Record those external checks separately when performed.
