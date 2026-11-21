---
name: setup
description: Connect a PageLantern workspace and verify read access after installing the plugin or when the user asks to get started, reconnect, or troubleshoot authorization. Use monitoring for a concrete monitor task once connected.
---

# Set up PageLantern

Explain that PageLantern can inspect monitors, settings/history/uptime, graphs and monitoring locations; read existing client reports; and—with additional authorization—run HTTP checks, create HTTP uptime monitors, and pause or resume scheduled monitoring.

1. Check whether the `pagelantern` tools are available. If they are, call `list_monitors` with `page: 0, size: 5` to verify read access. This is a connection check, not a fresh website check. If the user has already requested a concrete action, continue with the monitoring skill after connecting.
2. If no connection exists or authentication fails, guide the user through the host's connection flow and PageLantern sign-in/workspace authorization. Account credentials stay in that flow. Never request credentials or tokens in the conversation.
3. Hosted ChatGPT starts with `monitors:read reports:read`. Native Codex uses its registered `pagelantern-codex` client and may offer the server's broader scopes; use the explicit read-only login instructions in the [package guide](../../README.md) when needed. Older grants do not gain `reports:read` automatically and may need renewed consent. Do not claim installation alone completed OAuth or verified a live deployment.
4. Confirm only what the tool proves: access to the connected workspace, the returned count/page, and available monitor names/status. If the workspace has no monitors, offer to create one when the user supplies an authorized public URL. Do not create, run, pause, or resume a monitor merely because setup was invoked.
5. When the requested task concerns reports, verify `list_report_packs` separately; a successful monitor list does not prove report permission. Empty report results are valid and do not authorize generation or delivery. Members/viewers see approved reports only.

For `403` or `insufficient_scope`, explain which scope is missing and that mutations also require Owner/Admin. Reconnect or approve expanded scopes when supported by the host; otherwise follow the guide for a deliberately elevated connection. Do not repeatedly retry unchanged permissions. For expired access, reconnect. For service failures, report that verification is incomplete without claiming the workspace is empty.

Finish with one useful next action based on the user's request, such as viewing recorded health or inspecting a chosen monitor. The release may still require deployment and host acceptance; follow the package status rather than assuming marketplace availability.
