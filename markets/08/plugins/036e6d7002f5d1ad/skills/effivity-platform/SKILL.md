---
name: effivity-platform
description: Interact with the Effivity compliance platform using its MCP tools. Use when users ask about Effivity form data, workflow masters, workflow-related forms, FAQ information, or support tickets.
---

# Effivity Platform

Use the Effivity MCP tools only for operations supported by the Effivity platform.

## Scope

This skill is limited to capabilities exposed by the Effivity MCP server. Do not infer capabilities that are not exposed by the available tools.

## Tool Selection

- `list_form_data` — retrieve existing form data.
- `get_workflow_master` — retrieve workflow master information.
- `list_workflow_masters` — list workflow master records.
- `ask_faq` — answer questions using internal FAQ knowledge.
- `get_workflow_forms` — retrieve workflow-related forms.
- `create_support_ticket` — create a new support ticket.

## Behavioral Rules

- Use read-only tools only for retrieval and inspection.
- Do not claim that a tool can create, update, or delete data unless its defined behavior explicitly supports that operation.
- Do not claim that these tools provide arbitrary internet or external-system access.
- Creating a support ticket is a write operation but is not destructive because it adds a new record rather than deleting or irreversibly altering existing data.
- Do not claim that an existing ticket or record was modified unless the underlying tool actually performs that operation.

## Detailed References

See [Tool Reference](references/tool-reference.md) for detailed tool behavior.

See [Tool Annotations](references/tool-annotations.md) for the reviewer-oriented annotation justifications.

See [Usage Guidelines](references/usage-guidelines.md) for detailed usage boundaries and expected behavior.
