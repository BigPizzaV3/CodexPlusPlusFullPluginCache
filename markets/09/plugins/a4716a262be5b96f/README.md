# PDFHost MCP plugin

PDFHost is a PDF hosting platform for permanent shareable links, website embeds,
QR codes, and document analytics. This package connects the hosted PDFHost MCP
server to ChatGPT and Codex.

Server URL: `https://pdfhost.se/mcp`

The server uses OAuth 2.1 with PKCE and exposes read-only document search,
document details, embed code, and aggregate analytics. It is also compatible
with Manus through its Custom MCP Servers integration.

## Local testing

1. Enable ChatGPT Developer mode.
2. Add `https://pdfhost.se/mcp` as an MCP server.
3. Complete PDFHost sign-in and consent with an active Pro or Studio account.
4. Test all five positive and three negative cases in `plugin.json`.

## Manus

In Manus, open Settings, Integrations, Custom MCP Servers, add the server URL,
and complete the OAuth sign-in flow.
