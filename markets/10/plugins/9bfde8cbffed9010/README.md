# ohmyho.st plugin package

This package combines the ohmyho.st Skills with its remote MCP connection. The client connects
through managed OAuth. Current account membership, roles and explicit token restrictions determine
which actions are available. Existing authenticated connections retain their OAuth identity; a
cached tool catalog or Skill may require a refresh or new chat, not a new OAuth connection.

The server advertises WorkOS Connect authorization metadata and standard OIDC scopes
(`openid`, `profile`, `email`, `offline_access`). A workspace must exist before project work.
Secret input and GitHub connection use their own protected handoffs. This package contains no
API keys, device tokens, runtime credentials, hooks or local server dependency.

Use the included get-started and deploy Skills to continue the same project across chats.
Keep the existing local CLI/device-login workflow for a local checkout, and the GitHub Skill
for a project that already uses GitHub or a customer who explicitly selects it.

Plugin package version 0.1.54 carries the 0.1.52 client workflows and allowlisted Native Auth password guidance. The October 8 review
recording in the manifest is historical and does not demonstrate this update.

## Package contents

The package contains ten Skills and their supporting files, an OpenAI compatibility manifest at
`.codex-plugin/plugin.json`, and its remote connector configuration in `.mcp.json`. Its Skills
retain the reviewed workflows with the 0.1.52 Auth guidance update; the get-started and troubleshooting Skills add a
ChatGPT-specific fallback when remote feedback tools are unavailable. The package has no hooks,
registered-app references or bundled credentials.

## Native testing and publication

This repository package is prepared for testing, not evidence of a public directory listing or
a completed native-client acceptance run. First verify the deployed HTTPS server and OAuth
discovery, then install the package in the chosen client's private/local testing source. In
Claude, add/connect the bundled connector from the plugin's Connectors tab; installing the
Skills alone does not authenticate the user. In ChatGPT, test the custom remote MCP connection
and the complete installed package through the supported plugin testing flow.

Exercise a new app, a resumed app, a competing edit, a denied project and a private secret-input
handoff. Check a verified preview and an explicitly approved publication of the exact commit.
Public review, reviewer access, listings and publication remain separate authorized steps;
never bundle reviewer credentials or fabricate a registered connector ID.

Official packaging references:

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [OpenAI connection testing](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [OpenAI submission](https://developers.openai.com/plugins/deploy/submission)
- [Claude manifest reference](https://code.claude.com/docs/en/plugins-reference)
- [Claude plugins and bundled connectors](https://claude.com/docs/plugins/overview)
