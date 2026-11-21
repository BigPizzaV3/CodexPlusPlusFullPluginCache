# Guidejar plugin

A private plugin package for the existing Guidejar MCP server. It adds a
Guidejar workflow skill and connects directly to `https://mcp.guidejar.com/mcp`
using Streamable HTTP and the server's existing OAuth flow. No server deployment
or embedded credentials are needed.

## Connect

Open the created plugin in the host, install/connect it, and complete Guidejar
sign-in and consent if requested. The host discovers authorization metadata from
the MCP server. Workspace membership and MCP controls govern available actions.

Try: “Find guides about onboarding in my Guidejar workspace.”

For a safe connection check, ask for your Guidejar teams, then list a small
number of guides. Creating or editing documents should be tested only as part
of a user-requested content task.

## Package contents

- `plugin.json`: Agent Plugins 1.0 manifest and listing details.
- `mcp.json`: Remote MCP endpoint, with no stored credentials.
- `skills/guidejar/`: Workflow instructions and tool reference.
- `assets/icon.png`: Existing Guidejar brand icon from this repository.

Official setup documentation:
https://www.guidejar.com/blog/create-sops-with-codex-and-guidejar

The source currently implements 11 tools. The existing connected app exposed
10 tools during preparation; `get_team_folders` was not exposed there. The skill
therefore checks live tool availability. Saving the package does not by itself
verify the newly installed plugin or deploy local server changes.
