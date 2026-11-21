---
name: onboarding
description: Connect VoxStudio Cloud, open its cloud session library, or troubleshoot its remote MCP authentication and tools.
---

This skill uses the VoxStudio Cloud plugin and its `voxstudio_cloud` MCP server at `https://voxstudio.me/cloud/mcp`. Discover tools from that server using their live schemas, including deferred tools. In OpenAI hosts, use only tool identifiers beginning with `mcp__voxstudio_cloud__`; the separate `mcp__voxstudio__` namespace belongs to the local Mac app. Keep every Cloud request on the Cloud connection. If Cloud tools are unavailable, inspect and report the actual connection or tool exposure error. Request OAuth reconnection only when authentication is required, expired or rejected; missing tools alone do not establish an OAuth failure. Do not substitute local tools or treat local sessions as the Cloud catalog.

VoxStudio Cloud uses one remote HTTP MCP connection for knowledge evidence and media processing. Users authorize their own VoxStudio account through the browser. Never request a password or paste access tokens into chat or configuration.

Use the endpoint and installation instructions in the user's VoxStudio Settings → MCP. After installing or enabling the plugin, start a new chat. Avoid creating duplicate connections to the same endpoint under different server names. If the host omits plugin tools because of its plugin tool budget, an ordinary MCP configuration named `voxstudio_cloud` for the same endpoint can provide the effective connection while retaining the plugin skills and existing OAuth. Inspect the host's effective configuration to confirm which connection is active.

Knowledge tools read only authorized sources; the host model composes answers. Media tools can create sessions and queue processing jobs. Explain the actual requested permissions when reconnecting. An old media-only authorization may require a new cloud connection; refresh cannot add knowledge permission.

Call `mcp__voxstudio_cloud__voxstudio_workspace` with `{}` to open the shared Cloud session and evidence reader when MCP Apps are supported. Claude uses inline cards and the host's fullscreen mode; OpenAI may provide a workspace panel. Navigation, original text and evidence selection stay inside the reader. Claude connector behavior is defined by public server instructions and tool descriptions, so it does not depend on these OpenAI plugin skills.

For a connection failure, inspect the current MCP error. An authentication error requires OAuth reconnection; a connection or tool exposure error requires resolving that reported failure. Successful OAuth does not prove that Cloud tools were loaded into the current chat. For an expired package download, use Settings → MCP to obtain a fresh download link. Do not claim a tool or processing job succeeded without its returned result.
