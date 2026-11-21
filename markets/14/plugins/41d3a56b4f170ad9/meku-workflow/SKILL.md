---
name: meku-workflow
description: Use when the user wants to access their Meku account, list workspaces or projects, inspect a project, or create and update projects through the connected Meku MCP server.
---

# Meku workflow

Use the connected Meku MCP server for actions involving the user's Meku account and projects. Do not assume the user has access to any workspace or project until you retrieve it from the connected tools.

## Workflow

1. For account or workspace questions, retrieve the signed-in user's profile or workspaces using the available Meku tools.
2. For project lookup, search/list projects in the appropriate workspace before reading project details or files.
3. For a new project, gather the user's goal from their prompt and use the create-project workflow. If several workspaces are available and the tool needs a choice, ask the user to choose one.
4. For project changes, inspect relevant project state or files first, then make a scoped change aligned with the request.
5. For deployments, analytics, databases, or connectors, use the matching supported tools and confirm any consequential action where the tool's workflow requires it.
6. Report tool results accurately. Do not claim an action succeeded until the tool confirms it.

## Authentication and safety

Use the MCP server's supported OAuth sign-in and consent flow. Never ask the user to paste passwords, OAuth tokens, or secrets into chat or plugin files. Do not assume endpoint capabilities, scopes, or project permissions beyond what the connected server advertises.
