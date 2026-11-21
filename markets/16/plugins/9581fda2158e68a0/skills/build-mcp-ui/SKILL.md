---
name: build-mcp-ui
description: Build a usable interactive MCP Apps UI with ui:// resources, host bridge, real tool interactions, accessible states and a useful text-only fallback.
---
# Interactive MCP Apps UI

1. Check target host supports MCP Apps and the UI actually improves selection, browsing, editing or confirmation. Otherwise deliver tool-only MCP.
2. Use `@modelcontextprotocol/ext-apps` helpers (`registerAppTool`, `registerAppResource`, `RESOURCE_MIME_TYPE`) with the **current** installed MCP SDK version. Read the official ext-apps quickstart; do not mix v1 imports with v2 samples.
3. Register the UI resource with `ui://...` URI and `text/html;profile=mcp-app`, and link the tool using `_meta.ui.resourceUri` in its registration. Ensure a real resource response is returned.
4. Use the official MCP Apps bridge and capability negotiation. Do not reach into the host's parent DOM, assume arbitrary network access, or trust client-side authority.
5. Create an original design system appropriate for the host surface. Read `../../references/design-references.md`, `../../references/design-quality.md`. Focus on hierarchy, proportion, readable type and restrained motion; avoid generic dashboard filler.
6. Implement real loading, empty, error, permission, success and retry states and meaningful keyboard/focus behavior. Don't draw fake buttons or charts with fabricated data.
7. Restrict CSP `connectDomains` and `resourceDomains` to actual needs; app-visible tool calls must still pass server authorization.
8. Render in a compatible client or test harness, inspect visually, and test action-to-tool calls and fallback when possible. Report unverified host support accurately.

Useful starting point: https://github.com/modelcontextprotocol/ext-apps/blob/main/docs/quickstart.md
