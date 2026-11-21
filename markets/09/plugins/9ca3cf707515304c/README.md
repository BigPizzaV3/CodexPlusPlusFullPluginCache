# Eclincher

Plugin identifier: eclincher. Display name: Eclincher.
Remote MCP endpoint: https://app.eclincher.com/mcp
Authentication: OAuth, handled by the MCP host. No credentials or invented connection IDs are included.

## Test in ChatGPT
Enable Developer mode, add a new custom MCP connection with the endpoint above, select OAuth, and authorize an Eclincher test account. Test in a new chat using the current server tools. This does not require public submission or approval.

## Test with a personal marketplace
Copy this plugin folder to ~/plugins/eclincher. Add the entry below to the plugins array of ~/.agents/plugins/marketplace.json, preserving existing entries. For a new marketplace, use the full object below. Restart the ChatGPT desktop app, choose the Personal marketplace and install Eclincher. Local support varies by client; direct MCP developer-mode testing is the ChatGPT alternative.

```json
{"name":"personal","interface":{"displayName":"Personal"},"plugins":[{"name":"eclincher","source":{"source":"local","path":"./plugins/eclincher"},"policy":{"installation":"AVAILABLE","authentication":"ON_INSTALL"},"category":"Productivity"}]}
```

## Submit
Upload this ZIP in the OpenAI Plugins dashboard under your verified Eclincher developer identity. Under MCPs, connect https://app.eclincher.com/mcp with OAuth, complete the portal domain-verification challenge and scan the current tools. Resolve findings and supply reviewer credentials, five tested positive cases, three negative cases, a video walkthrough and release notes. Submit for review; publish after approval.

The ZIP declares the remote MCP endpoint; OpenAI creates any required registered connection identity during setup. Do not invent a plugin_asdk_app ID or include .app.json in a public submission.

## Validation scope
Package structure and local manifest validation were checked. An authenticated OAuth flow and tool execution were not tested. Server tool names are discovered dynamically rather than embedded in this package.

## Version 1.0.6 review-case correction
This package declares exactly five positive and three negative review cases. Brand/profile discovery and scheduled-post create/edit are consolidated workflows so coverage is retained without exceeding the portal count. See REVIEW-PREPARATION.md for validation scope and remaining authenticated checks.
