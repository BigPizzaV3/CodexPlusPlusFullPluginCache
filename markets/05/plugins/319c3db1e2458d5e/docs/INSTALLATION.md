# Installation and Cloud Use

Documentation checked on 2026-09-07. Availability depends on account and workspace policy. No account installation is included in this source package.

## Cloud distribution

The core is a skills-only native plugin. Use a supported workspace publishing or plugin-directory route; do not assume that uploading a ZIP into an ordinary chat installs a plugin.

For an administered workspace, an admin can distribute a local plugin to the workspace or import a GitHub marketplace. For GitHub distribution, use a repository you choose to publish to, package this plugin under its `plugins/research-plugin/` directory, and generate a marketplace through Plugin Creator. No repository or account is chosen by this package. The admin imports that repository through Admin > Plugins > Add > Import marketplace and reviews access. See [workspace plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management).

For public distribution, follow the [plugin submission workflow](https://developers.openai.com/plugins/deploy/submission). Confirm publisher identity, redistribution rights, required listing assets, and any provider requirements before submitting. This project is not represented as approved or published.

If your account has neither workspace publishing nor another supported private-plugin installation route, this package cannot grant that capability. As a manual fallback, the bundled skills and references can be supplied as instructions/material in a cloud conversation, explicitly asking ChatGPT to apply them; that is not an installed plugin or guaranteed automatic skill selection.

## Mobile acceptance check

After cloud distribution and installation in the same workspace, open a fresh cloud ChatGPT conversation on the phone, select the plugin, and run a representative research request in your preferred language. Confirm references are accessible, retrieval works, and the response language matches. Repeat with the desktop computer turned off to verify there is no local runtime dependency. Supported plugin surfaces are documented in [ChatGPT Plugins](https://learn.chatgpt.com/docs/plugins).

## Optional MCP connections

The core has no mandatory connectors. The remote-MCP archive includes `.mcp.json` for hosts that load bundled HTTP MCP definitions. Do not assume this registers cloud connections automatically.

For cloud environments that require registered connections, follow [Connect and test](https://developers.openai.com/plugins/deploy/connect-chatgpt): enable Developer mode when permitted, add each desired endpoint in ChatGPT Plugins, inspect its discovered tools, and test it. Use the actual registered connection IDs with Plugin Creator if packaging those connections into `.app.json`. Never invent connection IDs or embed account secrets. If unavailable, retain the core package and its web/file fallback.

The package does not change your personal marketplace or install anything into Cursor/Codex. Local testing and cloud distribution have distinct state and must be verified separately.
