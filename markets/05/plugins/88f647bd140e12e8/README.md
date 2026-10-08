# vercel

This directory packages the runtime content from [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) version `0.54.0` for the OpenAI plugin directory.

## What is included

- `skills/`: 33 current skills, including their reference files and Codex display metadata
- `.mcp.json`: the Vercel MCP server at `https://mcp.vercel.com`
- `vercel.md`: the Vercel ecosystem reference graph
- `agents/` and `commands/`: upstream workflow reference content
- Plugin icons and assets

## OpenAI packaging

The OpenAI package version is `0.54.1`; the upstream content baseline remains `0.54.0`.

The package uses `.codex-plugin/plugin.json` with the local plugin id `vercel`. Skills are discovered from their `SKILL.md` name, description, and retrieval metadata. The upstream hook runtime is not included.

The runtime skills and supporting references follow upstream, with OpenAI packaging and safety guidance retained. Source-only `overlay.yaml` files and `upstream/` copies are excluded so each skill has one discoverable definition. The shadcn and next-forge skills have been removed from both copies.

The Eve skill uses installed documentation when available and public documentation otherwise. Installing dependencies or scaffolding an Eve project must be part of the user's requested setup.

Deployment examples keep CI credentials away from untrusted PR code and scope protected browser-test authentication to the verified deployment origin. Next.js framework guidance comes from version-matched Next.js documentation and the official Next.js workflow skills instead of bundled Next.js skills.

The Vercel connection is declared as an MCP server rather than an app reference. Connect and authenticate with Vercel through the host's MCP setup before using its tools. MCP supports both reads and writes within your granted permissions. Use `list_deployment_events` for build output. Digital subscriptions, credits, and add-on purchases are unavailable through MCP; domain registration requires a quote and explicit approval.

## Usage

After installing the plugin, invoke a skill such as `ai-sdk`, `build-agents`, or `deployments-cicd`, or describe the task so the host can choose the relevant skill. The `agents/` and `commands/` files preserve upstream workflows as reference material; they do not register separate Codex agents or slash commands.

## Package layout

```text
vercel/
├── .codex-plugin/plugin.json
├── .mcp.json
├── skills/
├── vercel.md
├── agents/
├── commands/
└── assets/
```

For submission, ZIP this plugin's manifest, MCP configuration, runtime skills, references, and assets. Include dotfiles and omit unrelated local website files, authoring templates, app manifests, and hook configurations or scripts. Upload the ZIP to the existing draft to run OpenAI's listing and skill checks again.

## Reporting issues

Report upstream content issues in [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin/issues). Packaging changes belong here in `openai/plugins`.
