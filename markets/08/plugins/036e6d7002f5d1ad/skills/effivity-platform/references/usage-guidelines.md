# Effivity MCP Usage Guidelines

## General
Only use capabilities exposed by the MCP server. Do not infer unsupported API capabilities.

## Read Operations
The following tools are read-only:
- `list_form_data`
- `get_workflow_master`
- `list_workflow_masters`
- `get_workflow_forms`

Use these tools to retrieve or inspect existing platform information.

## FAQ
Use `ask_faq` for questions that can be answered from the platform FAQ knowledge. Do not represent it as general-purpose web search.

## Support Tickets
Use `create_support_ticket` when the user requests creation of a support ticket. Creating a ticket creates a new application record. Do not claim an existing record was modified unless the underlying tool explicitly performs such an operation.

## Scope
All tools are constrained to their defined Effivity application scope. Do not claim that they can access arbitrary websites, unrelated external systems, or unsupported platform data.
