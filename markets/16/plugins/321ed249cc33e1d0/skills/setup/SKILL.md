---
name: setup
description: Connect a PBJConnect account to this plugin, check authorized organizations, change shared organizations, or disconnect access.
---

Use the PBJConnect MCP tools provided by this plugin. Tool prefixes vary by host; locate tools by their documented names. Never use another service or an arbitrary URL as a substitute.

1. If the host prompts for access, use the Connect control in the plugin. Sign in on PBJConnect, select organizations, and approve. Credentials belong on PBJConnect. The user approves access.
2. Call `connection_status` after connecting. Report the available organizations and offer useful examples without reconnecting.
3. If the user wants to revoke access or change which organizations they share, call `connect_account` for the management link. To choose a different set, disconnect and reconnect through the host.
4. After the user completes the page, call `connection_status` again. Only claim connection when it reports `connected: true`.
5. Use the returned organization IDs for later requests. A user with several organizations can choose among their explicitly shared organizations. Do not infer membership from an email address or company name.

These tools read facility-level and organization-level aggregates. They do not run SQL, refresh connectors, return resident/employee records, change submissions, or submit to CMS. Existing PBJConnect permissions still apply. The account link expires after 90 days and can be revoked at the returned management URL. A password reset or removed membership can require reconnection.

If tools are not available, explain that the plugin must be installed and connected in the current ChatGPT or Codex session. Do not invent results or claim a background connection exists.

After connecting, suggest a relevant question such as: “Compare staffing and census trends across my facilities,” “Review last quarter's reporting gaps,” or “Compare PCC census with CMS census.” Do not run a broad data analysis unless requested.
