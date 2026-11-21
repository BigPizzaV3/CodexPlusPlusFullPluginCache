# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-11-16

### Added

- Codex and OpenAI plugin directory support: an Agent Plugins `plugin.json` and `mcp.json`, plus a Codex marketplace in `.agents/plugins/marketplace.json`.
- A Cursor manifest and marketplace in `.cursor-plugin/`, and a Gemini CLI extension in `gemini-extension.json`.
- A Claude Code marketplace in `.claude-plugin/marketplace.json`, which Grok Build also reads.
- Google Antigravity support in `.antigravity-plugin/` and `mcp_config.json`.
- Native Grok Build and Muse Code manifests in `.grok-plugin/` and `.muse-plugin/`.
- Directory listing fields in `.claude-plugin/plugin.json`: display name, icon, and documentation, support, and terms URLs.

## [1.2.0] - 2026-11-12

### Changed

- `edit-site` now chats with the Flint agent through `start_chat`, `wait_for_reply` and `send_message`, so Flint can ask questions and follow-ups keep their context. It no longer uses the deprecated `run_background_agent` and `check_background_agent_status` tools.

## [1.0.0] - 2026-03-24

### Added

- Initial release of the Flint plugin for Claude Code
- `edit-site` skill for modifying Flint websites via background AI agents
- MCP server integration with OAuth authentication
- Site listing, background agent execution, and publishing capabilities
