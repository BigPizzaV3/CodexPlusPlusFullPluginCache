# Nervus preview plugin

This optional portable Agent Plugins 1.0.0 package bundles 6 guided workflows and one remote OAuth MCP connection. It contains no credentials, app bindings, connection identifiers, reviewer credentials, or local user data. The direct MCP connection works without installing these skills.

For OpenAI clients, listing, review and publication metadata lives in `plugin.json` under `extensions.com.openai`, its packaged listing images live under `assets/`, and the OAuth declaration lives in `mcp.json` under `mcpServers.nervus.extensions["com.openai"].auth`. The portable core of both documents is validated against the canonical Agent Plugins 1.0.0 schemas. Agent Plugins 1.0.0 defines no portable OAuth fields, so a strict generic client that rejects unknown server-entry members may treat this top-level `mcp.json` as invalid; the direct remote MCP connection to https://app.nervus.chat/mcp remains available in that case.

Import the ZIP only where your client exposes a supported plugin archive import. Workspace upload can require administrator permission. If full installation is unavailable, report it as blocked on this host. Direct MCP at https://app.nervus.chat/mcp is a separate diagnostic, not proof of package installation. Downloading or importing the ZIP does not connect your Nervus account; complete OAuth separately.

Reading is the default. Staging files and saving confirmed results require separate consent; existing grants gain no authority.

After connecting, run nervus-setup, then test Inbox, your complete active Tasks, cited project context and Thread briefs with exact titles and source links. Refresh the host connection metadata after server updates. Installation, skill activation, web/mobile availability and updates require separate host verification; this ZIP does not guarantee synchronization or automatic updates. No Git, marketplace or public directory submission is required. Uploading or submitting this package to a directory is an authorized external action outside this archive.
