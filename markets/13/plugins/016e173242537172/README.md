# Himalayas for ChatGPT and Codex

This folder is the plugin package for OpenAI's plugin directory (Agent Plugins
format). It connects to `https://mcp.himalayas.app/mcp/chatgpt`, a route of the
Himalayas MCP server built for this directory, and bundles the nine Himalayas
skills.

## How it differs from the canonical plugin

The skills are copies of the ones in `../skills`, edited for OpenAI's plugin
guidelines:

- Provider-neutral wording ("the assistant").
- No plan prices, no payment or billing flows, and no tools the
  `/mcp/chatgpt` route leaves out. Where a feature needs a Himalayas Plus plan,
  the skills say so in one sentence and carry on with the free path.
- `skills/himalayas-basics/references/tools.md` lists exactly the tools on
  `/mcp/chatgpt`. Regenerate it with `scripts/chatgpt-tools-md.py`.

There are no commands, hooks or other client-specific settings. When a
canonical skill changes, make the same change here, keeping the edits above.

## Build

From the repository root:

```bash
scripts/package-chatgpt.sh
```

It validates the manifests, checks listing limits, test cases and banned
terms, and writes `dist/himalayas-chatgpt.zip` with this folder as its only
top-level directory. Upload that ZIP on the OpenAI plugins dashboard.
