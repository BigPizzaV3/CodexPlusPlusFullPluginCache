# Proxyman Plugin

Official Proxyman workflows for ChatGPT and Codex. This skills-only plugin helps users install and configure Proxyman, capture and inspect HTTP/HTTPS/WebSocket traffic, use debugging tools, manage certificates and settings, connect the local MCP bridge, automate with `proxyman-cli`, and handle licenses safely.

## Runtime model

- The plugin itself contains skills and static references only.
- Proxyman remains a separately installed desktop application.
- Operational MCP workflows use the stdio bridge bundled with the user's local Proxyman installation.
- The package does not contain the Proxyman application, a license, credentials, captured traffic, or a hosted MCP server.

## Included skills

- `proxyman-download-setup`
- `proxyman-app-settings`
- `proxyman-certificates-recovery`
- `proxyman-mcp-setup`
- `proxyman-traffic-debugging`
- `proxyman-debugging-tools`
- `proxyman-license-management`
- `proxyman-cli`
- `proxyman-https-capture`

The source skill bundle is maintained at `../../skills/`. Keep the packaged `skills/` tree byte-for-byte synchronized with it before publishing a new version.

## Privacy and safety

Captured traffic can contain credentials and personal data. The skills keep Proxyman MCP redaction enabled by default, require explicit approval for sensitive exports and destructive changes, and never ask users to paste license keys or certificate passwords into agent tool calls.

See the repository's `SUBMISSION.md` for marketplace listing copy, reviewer tests, release notes, and the remaining portal steps.
