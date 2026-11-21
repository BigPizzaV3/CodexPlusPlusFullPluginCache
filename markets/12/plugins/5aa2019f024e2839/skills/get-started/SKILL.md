---
name: get-started
description: Connect to Maker and identify the active organization and project when the user starts a Maker website workflow or asks which account is connected.
---

# Get started with Maker

Use the connected Maker MCP tools for the user's requested website workflow.

1. If Maker tools are unavailable, ask the user to connect Maker through the host's plugin or connector settings using their existing account.
2. Call `whoami` to identify the active organization. Resolve a requested existing project with `list_projects`; use returned identifiers rather than guessing them. If several projects match, ask the user to select one.
3. Follow the current tool schemas and returned confirmation steps for the requested operation. A project preview and a published website are different states: describe the state the tools actually report.

Example: “Show my Maker projects” needs the connected account and project list. It does not authorize creating, editing, or publishing a project.
