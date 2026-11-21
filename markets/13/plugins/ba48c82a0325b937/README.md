# Booklee for ChatGPT and Codex

Booklee's plugin connects to the hosted Booklee MCP server and includes account connection, appointment, and business workflows. Public discovery is anonymous; protected actions use Booklee OAuth and your selected access.

Install the package and complete the OAuth connection when ChatGPT prompts you. The package declares Booklee as an OAuth MCP server and uses the ChatGPT adapter, so installation can open Booklee sign-in and consent before the first conversation. Finish both Booklee sign-in and the `/mcp/authorize` consent screen by choosing the capabilities and business or location targets and clicking **Allow**. The connection is complete only after ChatGPT returns to the chat and `get_access_context` succeeds. The setup workflow remains available for an explicit manual connection check, but it is not registered as an automatic onboarding action; installation must not ask the user to select a Booklee environment.

For a Local or SSH/VPS Codex session, select that host before starting the chat. Plugin installation and MCP enablement are host-specific; installing on Local does not enable Booklee on the VPS, and an already-open chat will not gain a newly installed server. If Booklee is visible in the plugin but the chat says the MCP server is not loaded, open the plugin's **Manage/Settings** for the selected host, enable the `booklee` MCP server, reconnect it, and create another new chat before using `@Booklee`. The compatibility manifest is host-neutral and does not launch a cloud setup chat. The bundled MCP entry uses the Codex-compatible HTTP shape; OAuth is discovered from Booklee's protected-resource metadata when the first protected tool runs. No cloud environment is required.

This source package points to **production** at `https://booklee.app/api/mcp/chatgpt`. Production MCP activation and public directory review are separate release steps. A package existing in this repository does not mean its production endpoint is enabled or the plugin is listed in a provider directory.

For staging acceptance, build the explicitly named staging package with the repository's `plugins:package` command. Do not connect a staging account to a production endpoint or reuse a token across environments.

Disconnect access at https://booklee.app/mcp/connections or from Booklee account settings. Remove the installed plugin separately in the client if you no longer want its skills.

Publisher: Booklee. Support: https://booklee.app/contact. Privacy: https://booklee.app/privacy. Terms: https://booklee.app/terms.

The package uses Booklee's existing icon. No open-source license is assigned by this packaging change. Provider names identify compatibility; this package does not claim endorsement by OpenAI or Anthropic.
