# ReMCP OpenAI Plugins review and authorization

The registered ReMCP App identifier is `app-6aaaba1295a4819195a4987e18e43428`. This package updates its skills and descriptive metadata; it is **not a new App**. The configured, authorized MCP server endpoint is `https://remcp.site/mcp`. Do not switch to an unavailable `/mcp-review` route or invent an MCP API key.

## OAuth and MCP key

The Plugins panel may show **Authentication: Authorized** and **MCP key: Not specified**. A separate static MCP key is not required for an OAuth-connected MCP server. Keep the existing authorized MCP configuration. Reauthorize only if the platform actually reports an auth failure. Never include a credential or secret in the ZIP.

## Tool selection and PDF inspection

- Use only the MCP tools advertised in the current connection. A standalone deployment can advertise approximately 173 individually named tools; compact connections use fewer grouped definitions. Exact counts can evolve.
- `pdf_info`: read-only inspection of a permitted local PDF path on an explicitly paired computer. With local `pdfinfo`, reads metadata/properties including page count/title/author where present; otherwise reports bytes and annotation count. It does not edit the PDF, extract text or write output.
- `pdf_annotations`: reads existing annotation metadata; it does not add, remove or change annotations.
- Never call missing `render_file_preview`, `render_image_preview`, or `render_terminal_preview` helpers. Use native MCP results instead.

## Reviewer environment

OpenAI may test remote desktop, terminal, file and browser operations. **Use a distinct reviewer identity and a specifically paired disposable test computer**; normal authorized `/mcp` can operate real devices. A clean tool-contract preflight is not platform approval. Check OAuth access, tool descriptions/annotations, and the actual selected machine's capability list.

## Logo and listing

The App's icon, verified publisher, domain and listing details belong to the registered OpenAI App and may not be changed through a skill-only archive. Update/verify them through the existing App's publishing interface; do not create a duplicate App, and do not place real tokens under “MCP key”.
