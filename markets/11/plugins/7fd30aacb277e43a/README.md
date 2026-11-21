# Amboro for ChatGPT

Ask ChatGPT to build and run **applets** for your Amboro account. Applets are small, single-file tools that live beside
your chart in the Amboro workspace.

ChatGPT reaches Amboro through the Amboro MCP server. It signs in to your account through Amboro's own login and
consent page, sees only your applets, and can ask for your permission before it creates or deploys one. It cannot read
your sessions, your trades or your account details. There is no token to copy.

## Add Amboro as a custom connector

ChatGPT connects to a remote MCP server as a *custom connector*. OpenAI documents the steps in
[Developer mode and MCP apps in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt).
In short:

1. A workspace admin turns on developer mode and custom MCP connectors in the workspace settings.
2. Create a connector, paste the Amboro MCP address (it ends in `/mcp`) and choose **OAuth**.
3. Sign in to Amboro and approve *Read your applets* and *Create and deploy applets you own*.
4. Scan the tools. The Amboro applet tools appear in the connector.

## Try it

- *Build me an applet that shows a checklist for the current symbol.*
- *Make an applet that calculates position size from my risk and stop distance.*
- *List my applets and archive the ones I no longer use.*

## The authoring skill

[`skills/amboro-applets`](skills/amboro-applets) is the guide a model follows to write an applet that passes
validation, written in provider-neutral language. The connector also offers the same guide through its
`get_applet_authoring_guide` tool, so ChatGPT works without installing the skill separately.

## Disconnect

Sign in to Amboro and open **Connected apps** (`/connect/connected-apps` on your Amboro address), then choose
*Disconnect* beside ChatGPT. Access ends within 15 minutes.

## Listing in ChatGPT

This folder is the package uploaded to OpenAI's plugin portal: the manifest (`.codex-plugin/plugin.json`), the Amboro
MCP server it connects to (`.mcp.json`, `https://mcp.amboro.app/mcp`, OAuth with dynamic client registration), the
authoring skill and the icons in `assets/`. A listing requires OpenAI's review; nothing here claims Amboro is listed.

Questions or problems: open an issue in this repository.
