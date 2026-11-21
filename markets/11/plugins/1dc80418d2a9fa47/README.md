# Accessibility Checks & Fixes

By **Inkable Docs LLC** · package version **1.1.0**

Check PDF, Word (DOCX), and PowerPoint (PPTX) accessibility. Fix supported Word and PowerPoint issues and download separate updated files. Findings support WCAG and PDF/UA review workflows; automated results do not certify conformance. PDF remediation is unsupported.

## Tools

| Task                     | Start                          | Retrieve                  |
| ------------------------ | ------------------------------ | ------------------------- |
| Check PDF, DOCX, or PPTX | `check_document_accessibility` | `get_accessibility_check` |
| Fix DOCX                 | `remediate_docx_accessibility` | `get_docx_remediation`    |
| Fix PPTX                 | `remediate_pptx_accessibility` | `get_pptx_remediation`    |

The original attachment is preserved. Jobs can be queued or running before completion. Reports and remediation results retain warnings and remaining/deferred checks; completion does not mean every issue was fixed.

## Packaged skills

- **Check accessibility** (`check-document-accessibility`): submit supported original attachments, retrieve reports, and explain findings without overstating WCAG or PDF/UA coverage.
- **Fix Word & PowerPoint** (`fix-office-accessibility`): select the dedicated format-specific tools, track asynchronous remediation, and deliver the returned Office file with remaining issues.

## Connection and files

- MCP endpoint: `https://inkabledocs.com/mcp`.
- OAuth 2.0 Authorization Code with PKCE; authorization server: `https://clerk.inkabledocs.com`.
- Existing public OAuth client and scopes `checks:run`, `reports:read` are preserved.
- ChatGPT inputs use the original `openai/fileParams` attachment contract, including `download_url` and `file_id`.
- Completed DOCX/PPTX retrieval returns an embedded binary MCP resource. This package does not use Claude's staged uploads or signed-link output.

## Package layout

- `plugin.json`: canonical portable manifest with OpenAI listing, review cases, and release notes.
- `.codex-plugin/plugin.json`: matching compatibility manifest, with the same identity, version, publisher, listing, and review metadata.
- `mcp.json` and `.mcp.json`: matching production MCP and public OAuth configuration.
- `skills/`: two workflows, each declaring its MCP dependency.
- `assets/icons/`: original Inkable pen geometry on an opaque white tile. Both themes use the black pen on white, at 256px for the composer and 512px for the listing. The SVG source is included.

No client secret, API key, private test credentials, environment file, or deployment credential is included.
