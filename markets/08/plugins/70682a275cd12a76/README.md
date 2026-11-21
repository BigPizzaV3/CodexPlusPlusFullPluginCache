# Orpinn for ChatGPT

This is the portable Agent Plugins package for the production Orpinn MCP endpoint.

- `plugin.json` is the portable plugin manifest.
- `mcp.json` registers the public HTTPS MCP endpoint.
- `.codex-plugin/plugin.json` and `.mcp.json` are compatibility files.
- `skills/orpinn-business-insights/SKILL.md` defines the safe read-first workflow.

The package contains no customer credential or OAuth secret. OAuth client registration, OpenAI domain verification, publication status, and the directory URL are deployment-owned values documented in `docs/client-ai/chatgpt-plugin-delivery.md`.

The published package uses the legacy-generated name
`app-6ab7856c3c048191993a0fbcf3b41d65`, not the source folder name. Its display
name remains Orpinn and its MCP server key remains `orpinn`. Preserve the exact
package name, verified individual publisher, prompts, and production MCP URL
when uploading a version to the existing plugin; never create a duplicate app.

Version 1.3.0 declares 91 source tools and six skills: business insights,
catalog updates, menu editing, actual media, paper-menu import and action history.
It adds 57 independently gated tools to the existing 34, including actual image
bytes, catalog lifecycle, complete shared-price previews, verified-source import
comparison and explicit decisions, menu hours/settings and expanded content.
Ten positive and four negative scenarios are provided for external review.
The package declares public OAuth DCR without secrets. An uploaded skill or ZIP
does not deploy backend tools, activate flags, expand grants or prove runtime.

Validate with `python3 scripts/ops/build-orpinn-plugin.py` from the repository.
Build with `--output /absolute/output/directory`; the builder creates the plugin
ZIP, six individual skill ZIPs, a source inventory, default-off tool flags and
SHA256SUMS with reproducible content. Use `--reuse-configured-app` for uploads
to the existing configured app so its established OAuth configuration is reused.

The 1.3.0 backend deployment and honest review handoff are documented in
`docs/client-ai/workspace-release-2026-11-02.md`. Validation is a bundled
source/package check; per-tool live acceptance is left to external review at
the owner's request. Images are never substituted when a real source is
unavailable. Host generation and vision require actual host capabilities and
real file handoff; Orpinn does not pretend to generate images or certify OCR.
Reviewer credentials belong only in the secure review dashboard.
