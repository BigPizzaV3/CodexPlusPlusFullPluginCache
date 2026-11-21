# 3DJ Studio plugin

3DJ Studio connects an AI assistant to [3DJ](https://www.3dj.app), the browser-based parametric CAD workbench by Neural Deep Network Ltd. With it the assistant can fetch verified parametric starters, build and measure a Replicad/OpenCascade script in 3DJ's isolated kernel, export the result as a binary STL, an ISO 10303 STEP file or a GLB with one named part per node (ready for Blender, FreeCAD, Fusion 360 and web viewers), save editable parts to your 3DJ gallery, compile and measure OpenSCAD, compose a render brief for SketchMonkey Design Studio, and, where enabled, prepare and accept operator print-quote reviews.

The same folder works as a Claude plugin, as an Agent Plugins 1.0 package and as an OpenAI (ChatGPT / Codex) plugin:

- `.claude-plugin/plugin.json` and `.mcp.json` are read by Claude Code, Claude.ai and Cowork.
- `plugin.json` (Agent Plugins schema with `extensions.com.openai`) and `mcp.json` are read by ChatGPT and Codex; `.codex-plugin/plugin.json` is the compatibility overlay for older Codex clients.
- `skills/` holds the two skills every host loads: `create-model` and `print-production`.

## Install

Claude Code:

```
/plugin marketplace add NeuralDEEPnet/3dj
/plugin install 3dj-studio@neuraldeep-plugins
```

Claude.ai / Cowork: Customize ▸ Plugins ▸ Add ▸ add the marketplace `NeuralDEEPnet/3dj`, or upload a zip of this folder. Then connect the 3DJ server from the plugin's Connectors tab and sign in.

Codex:

```
codex plugin marketplace add NeuralDEEPnet/3dj
```

## What it sends and where

Every tool call goes to the 3DJ MCP server at `https://www.3dj.app/api/mcp` over HTTPS. Nine public tools (starters for both CAD kernels, script validation, rendered views, assembly checks, revision comparison, the evidence schema, the design brief and configurator inspection) need no account. Account tools authenticate with OAuth 2.1 + PKCE (dynamic client registration) or a per-user API key minted at https://www.3dj.app/agents; the plugin never stores or asks for credentials in chat. What travels: CAD script source, parameter values, model names and metadata, and the resulting measurements and download URLs. Do not submit personal, medical, biometric or payment data; the server refuses it.

Quote tools record review requests and acceptances only. Nothing in this plugin charges a card, books a printer or ships anything.

## Related

- Connector guide: https://www.3dj.app/connector.md
- Blender 4.2+ add-on (pulls and pushes parts through the same server): `integrations/blender` in the repository.
- SketchMonkey Design Studio: https://www.sketchmonkey.design
